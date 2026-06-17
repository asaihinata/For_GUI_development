from collections.abc import Sequence
from typing import Any, Literal

from matplotlib.lines import Line2D
from matplotlib.patches import Circle, Polygon, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections.polar import PolarAxes
from matplotlib.spines import Spine
from matplotlib.text import Text
from numpy import float64
from numpy.typing import NDArray

__all__ = ["radar_factory", "RadarTransform", "RadarAxes"]

def radar_factory(
    num_vars: int, frame: Literal["circle", "polygon"] = "circle"
) -> NDArray[float64]: ...

class RadarTransform(PolarAxes.PolarTransform):
    def transform_path_non_affine(self, path: Path) -> Path: ...

class RadarAxes(PolarAxes):
    name: str = "radar"
    PolarTransform: RadarTransform
    def __init__(self, *args: tuple, **kwargs: dict) -> None: ...
    def fill(
        self, *args: tuple, closed: bool = True, **kwargs: dict
    ) -> list[Polygon]: ...
    def plot(self, *args: tuple, **kwargs: dict) -> Line2D: ...
    def set_varlabels(self, labels: Sequence[str | Text] | None = None) -> None: ...
    def _gen_axes_patch(self) -> Circle | RegularPolygon: ...
    def _gen_axes_spines(self) -> Any | dict[str, Spine]: ...
