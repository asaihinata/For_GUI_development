from os.path import join
from pathlib import Path
import numpy as np
from polars import read_csv
__all__:list[str]=['getcsv']
def getcsv()->np.ndarray[np.str_,np.str_]:
 path=join(Path(__file__).parent,'color.csv')
 get_csv=read_csv(path,encoding='utf-8-sig',has_header=False)
 get_csv=get_csv.to_numpy(use_pyarrow=True)
 return get_csv