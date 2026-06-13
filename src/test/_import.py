from os.path import abspath, dirname, join
from sys import path
import numpy as np

path.append(abspath(join(dirname(__file__), "..")))
from sgg import *
