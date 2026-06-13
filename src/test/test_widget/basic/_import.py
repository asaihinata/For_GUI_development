from pathlib import Path
from sys import path
import numpy as np

path.append(str(Path(__file__).parent.resolve().parent.parent.parent))
from sgg import *
