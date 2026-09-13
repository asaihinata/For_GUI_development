import numpy as np

from sgg.dev import _is_real

from .element import Element

__all__ = ["TElement"]


class TElement(Element):
    def _padding(self, args):
        args = np.array(args)
        if args.ndim == 1 and args.shape[0] <= 4:
            return args.tolist()
        else:
            raise ValueError

    def _unit_change(self, val):
        if _is_real(val):
            return val
        elif isinstance(val, np.str_):
            return self._unit_point(str(val))
        elif isinstance(val, str):
            if val[len(val) - 1] in ["c", "m", "i", "p"]:
                return val
            else:
                try:
                    float(val)
                except:
                    raise ValueError
                else:
                    return val
        raise ValueError
