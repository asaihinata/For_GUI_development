import time
from collections.abc import Callable
def measurement_time(func,do=1000):
 if not isinstance(func,Callable):
  raise TypeError("funcには関数型を指定してください")
 start_time=time.perf_counter()
 for _ in range(do):func()
 end_time=time.perf_counter()
 timesmath=end_time-start_time
 return timesmath