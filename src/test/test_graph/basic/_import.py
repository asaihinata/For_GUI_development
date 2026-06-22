from os.path import abspath, dirname, join
from pathlib import Path
from sys import path
import numpy as np

path.append(abspath(join(dirname(__file__), "..")))
path.append(str(Path(__file__).parent.resolve().parent.parent.parent))
from sgg import *

rng = np.random.default_rng(seed=42)


def randrange(min=0, max=1, size=None):
    return rng.random(size) * (max - min) + min


def randsint(low=1, high=None, lenght=1, hierarchy=None):
    if isinstance(hierarchy, int) and 2 <= hierarchy:
        return rng.integers(low=low, high=high, size=(hierarchy, lenght))
    else:
        return rng.integers(low=low, high=high, size=lenght)


xlabel = "x軸のラベル"
ylabel = "y軸のラベル"
zlabel = "z軸のラベル"
linex = np.arange(1, 4, 1)
liney1 = rng.integers(50, 80, size=3)
liney2 = rng.integers(50, 80, size=(4, 3))
stemx1 = rng.integers(50, 80, size=3)
stemx2 = rng.integers(50, 80, size=(2, 3))
stemy = np.arange(1, 4, 1)
piedata = rng.integers(30, 50, size=5)
pielabel = ["1月", "2月", "3月", "4月", "5月"]
bargraphx1 = ["1月", "2月", "3月", "4月", "5月"]
bargraphy1 = rng.integers(30, 60, size=5)
bargraphx2 = ["1月", "2月", "3月"]
bargraphy2 = rng.integers(30, 60, size=(2, 3))
scatterx1 = ["1月", "2月", "3月", "4月", "5月"]
scattery1 = rng.integers(0, 10, size=5)
scatterx2 = np.arange(1, 4, 1)
scattery2 = rng.integers(100, 400, size=(2, 3))
waterfallx = ["1月", "2月", "3月", "4月", "5月", "6月"]
waterfally = [30, -10, 10, 5, 10, -80]
stackx = np.arange(1, 4, 1)
stacky = rng.integers(50, 80, size=(2, 3))
errorbarx = np.arange(2, 12, 2)
errorbary = rng.integers(0, 3, 5)
err = rng.integers(3, size=5)
xerr = rng.integers(3, size=5)
yerr = rng.integers(3, size=5)
dscatterx = np.arange(0, 4, 1)
dscattery = [3, 4, 9, 10]
dscatterz = [10, 20, 30, 40]
stepdata = rng.integers(1, 10, size=5)
histdata = rng.normal(10, 50, size=1000)
boxdata1 = rng.normal(10, 100, size=100)
boxdata2 = rng.normal(20, 90, size=(2, 150))
eventdata = rng.gamma(4, size=(3, 50))
ecdfdata = 4 + rng.normal(0, 1.5, size=100)
stackeddata = rng.integers(1, 10, (3, 3)) + 2
stackeddataname = ["dataname1", "dataname2", "dataname3"]
violindata = rng.normal((3, 5, 4), (0.75, 1.00, 0.75), (200, 3))
hexbinx1 = rng.standard_normal((1, 5000))
hexbiny1 = 1.2 * hexbinx1 + rng.standard_normal((1, 5000)) / 3
hexbinx2 = 2 + rng.random((1, 5000))
hexbiny2 = 2 + 1.2 * hexbinx2 + rng.standard_normal((1, 5000)) / 3
hist2dx = rng.standard_normal(5000)
hist2dy = 1.2 * hist2dx + rng.standard_normal(5000) / 3
linefillx = np.linspace(0, 8, 16)
linefillymax = 3 + 4 * linefillx / 8 + rng.uniform(0.0, 0.5, len(linefillx))
linefillymin = 1 + 2 * linefillx / 8 + rng.uniform(0.0, 0.5, len(linefillx))
funnedata = rng.integers(10, 50, size=3)
hatplotx = rng.integers(20, 30, size=5, endpoint=True)
hatplotdata = hatplotx + 3
radarplotdata = rng.integers(10, 15, size=5)
radarfilldata1 = rng.integers(50, 100, size=5)
radarfilldata2 = rng.integers(50, 100, size=(3, 5))
barpolarx = np.linspace(0, np.pi * 2, 5)
barpolary = rng.integers(30, 60, size=5)
barpolardata = rng.integers(30, 60, size=5)
errorpolarx = np.arange(2, 12, 2)
errorpolary = rng.integers(0, 3, 5)
polarerr = rng.integers(2, size=5) + 0.5
polarxerr = rng.integers(2, size=5) + 0.5
polaryerr = rng.integers(2, size=5) + 0.5
linepolarx = np.arange(1, 4, 1)
linepolary = rng.integers(50, 80, size=3)
linepolardata = np.arange(1, 4, 1)
scatterpolarx = rng.integers(0, 10, size=5)
scatterpolary = rng.integers(0, 10, size=5)
scatterpolardata = rng.integers(0, 10, size=5)
stempolarx = rng.integers(50, 80, size=3)
stempolary = np.arange(1, 4, 1)
stempolardata = rng.integers(50, 80, size=3)
