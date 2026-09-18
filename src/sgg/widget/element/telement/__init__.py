from re import fullmatch

import numpy as np

from sgg.widget.element import Element

__all__ = ["TElement"]


class TElement(Element):
    def _padding(self, args):
        args = np.array(args)
        if args.ndim == 1 and args.shape[0] <= 4:
            return args.tolist()
        else:
            raise ValueError

    def _unit_change(self, val):
        if self._is_real(val):
            return self._to_real(val)
        elif isinstance(val, np.str_):
            return self._unit_point(str(val))
        elif isinstance(val, str):
            return fullmatch(r"^\d+[icmp]$", val)
        raise ValueError
