import json
from os.path import isfile
from threading import Lock
import requests.exceptions
from google.protobuf.json_format import MessageToJson
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter,_create_exp_backoff_generator,encode_spans,sleep
from opentelemetry.exporter.otlp.proto.http.trace_exporter import _logger as otel_logger
from opentelemetry.sdk.trace.export import SpanExporter,SpanExportResult
from detail.client.logs import get_detail_logger
logger=get_detail_logger(__name__)
class OTLPJsonHttpExporter(OTLPSpanExporter):
	def __init__(A,*B,**C):super().__init__(*B,**C);A.lock=Lock();A._session.headers.update({'content-type':'application/json'});A._MAX_RETRY_TIMEOUT=30
	def export(B,spans):
		if B._shutdown:otel_logger.warning('Exporter already shutdown, ignoring batch');return SpanExportResult.FAILURE
		D=MessageToJson(encode_spans(spans),use_integers_for_enums=True)
		for C in _create_exp_backoff_generator(max_value=B._MAX_RETRY_TIMEOUT):
			if C==B._MAX_RETRY_TIMEOUT:otel_logger.error('Failed to export batch after hitting max retries');return SpanExportResult.FAILURE
			with B.lock:
				try:A=B._export(D)
				except requests.exceptions.ConnectionError:otel_logger.info('Connection error, retrying in %ss.',C);sleep(C);continue
			if A.ok:return SpanExportResult.SUCCESS
			elif A.status_code!=500 and B._retryable(A):otel_logger.warning('Transient status code %s encountered while exporting span batch, retrying in %ss.',A.status_code,C);sleep(C);continue
			else:
				if'spans_api_key_span_id_key'not in A.text:otel_logger.error('Failed to export batch code: %s, response: %r',A.status_code,A.text)
				return SpanExportResult.FAILURE
		return SpanExportResult.FAILURE
class JsonLSpanExporter(SpanExporter):
	def __init__(A,output_path):
		super().__init__();A.output_path=output_path;A.lock=Lock()
		if isfile(A.output_path):raise RuntimeError(f"{A.output_path} must be empty to be used as an export file")
	def export(C,spans):
		H='resource';G='kind';F='context';D=[]
		for B in spans:A=json.loads(B.to_json());A['traceId']=A[F]['trace_id'];A['parentId']=A['parent_id'];A['id']=A[F]['span_id'];A['kind_str']=A[G];A[G]=B.kind.value;A['timestamp']=int(B._start_time/1000);A['duration']=(B._end_time-B._start_time)/1000;A[H]['_attributes']=A[H].pop('attributes');D.append(A)
		with C.lock:
			with open(C.output_path,'a')as E:
				for B in D:json.dump(B,E);E.write('\n')
		return SpanExportResult.SUCCESS