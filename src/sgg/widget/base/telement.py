import numpy as np

from .element import Element

__all__ = ["TElement"]


class TElement(Element):
    def _padding(self, args):
        args = np.array(args)
        if args.ndim == 1 and args.shape[0] <= 4:
            return args.tolist()
        else:
            raise ValueError
