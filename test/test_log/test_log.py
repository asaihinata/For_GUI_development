import os
from _import import *
if __name__=="__main__":
 logfile=os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),"test_log.log"))
 logger=Logger(
 name=__name__,
 format=["lineno","message","asctime"],
 logfile=True,
 file=logfile
 ).get_logger()
 print(f"\"{logfile}\"ファイルにログを保存する。")
 logger.debug("デバッグログ")
 logger.info("情報ログ")
 logger.warning("警告ログ")
 logger.error("エラーログ")
 logger.critical("重大エラー")