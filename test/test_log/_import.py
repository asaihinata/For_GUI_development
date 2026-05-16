from pathlib import Path
from sys import path
path.append(str(Path(__file__).parent.resolve().parent.parent))
from src.sgg import *
clear()