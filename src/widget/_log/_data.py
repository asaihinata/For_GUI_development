NOTSET,DEBUG,INFO,WARNING,ERROR,CRITICAL=0,10,20,30,40,50
LevelName={CRITICAL:'CRITICAL',ERROR:'ERROR',WARNING:'WARNING',INFO:'INFO',DEBUG:'DEBUG',NOTSET:'NOTSET'}
NameLevel={'CRITICAL':CRITICAL,'ERROR':ERROR,'WARNING':WARNING,'INFO':INFO,'DEBUG':DEBUG,'NOTSET':NOTSET}
COLORS={DEBUG:'\033[36m',INFO:'\033[32m',WARNING:'\033[33m',ERROR:'\033[31m',CRITICAL:'\033[41m\033[97m'}
RESET='\033[0m'
formats_list=['name','levelno','levelname','pathname','filename','module','lineno','funcName','created','asctime','msecs','relativeCreated','thread','threadName','taskName','process','processName','message']
formats_dict={'name':'%(name)s','levelno':'%(levelno)s','levelname':'%(levelname)s','pathname':'%(pathname)s','filename':'%(filename)s','module':'%(module)s','lineno':'%(lineno)d','funcName':'%(funcName)s','created':'%(created)f','asctime':'%(asctime)s','msecs':'%(msecs)d','relativeCreated':'%(relativeCreated)d','thread':'%(thread)d','threadName':'%(threadName)s','taskName':'%(taskName)s','process':'%(process)d','processName':'%(processName)s','message':'%(message)s'}
log_clear={
'none':['none',None,'',' '],# 何もしない
'once':['once'],# 読み込み時一度だけ消す
'do':['do']# 毎回消す
}