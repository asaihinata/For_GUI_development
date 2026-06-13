from os.path import abspath, dirname, join
from pathlib import Path
from sys import path
import numpy as np

path.append(abspath(join(dirname(__file__), "..")))
path.append(str(Path(__file__).parent.resolve().parent.parent.parent))
from sgg import *
