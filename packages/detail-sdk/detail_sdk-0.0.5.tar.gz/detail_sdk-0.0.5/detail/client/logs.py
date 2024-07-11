_H='logging.StreamHandler'
_G='formatter'
_F='console_verbose'
_E='format'
_D='withfile'
_C='simple'
_B='handlers'
_A=False
import logging,os
from logging.config import dictConfig
from detail.client.constants import LOCAL_BACKEND_URL,PROD_BACKEND_URL
from detail.client.instrumentation.base import DisableDetail
class VCRStubsFilter(logging.Filter):
	def filter(B,record):
		A=record
		if PROD_BACKEND_URL in A.msg or LOCAL_BACKEND_URL in A.msg:return _A
		if'ingest.sentry.io'in A.msg:return _A
		A.msg=A.msg.replace('not in cassette, sending','being sent');return True
level=os.environ.get('DETAIL_LOG_LEVEL','INFO')
config={'version':1,'disable_existing_loggers':_A,'formatters':{_C:{_E:'%(levelname)s: [%(asctime)s] %(name)s: %(message)s'},_D:{_E:'%(levelname)s: [%(asctime)s] (%(module)s:%(lineno)s): %(message)s'}},_B:{'console_simple':{'class':_H,_G:_C},_F:{'class':_H,_G:_D}},'filters':{'vcr_stubs_filter':{'()':VCRStubsFilter}},'loggers':{'detail':{_B:[_F],'level':level,'propagate':_A}}}
def init():dictConfig(config)
class DetailLogger(logging.Logger):
	def _log(C,*A,**B):
		with DisableDetail():return super()._log(*A,**B,stacklevel=2)
def get_detail_logger(*B,**C):A=logging.Logger.manager;D=A.loggerClass;A.loggerClass=DetailLogger;E=logging.getLogger(*B,**C);A.loggerClass=D;return E