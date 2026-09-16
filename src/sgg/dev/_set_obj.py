import numpy as np

__all__ = ["_SET_OBJ"]


class _SET_OBJ:
    def _to_str(self, s):
        if isinstance(s, str):
            return s
        if isinstance(s, np.str_):
            return str(s)

    def _is_str(self, s):
        if isinstance(s, str) or (
            isinstance(s, np.generic) and np.issubdtype(s.dtype, np.str_)
        ):
            return True
        return False

    def _to_number(self, val):
        if isinstance(val, int | np.integer):
            return int(val)
        elif isinstance(val, float | np.floating):
            return float(val)
        elif isinstance(val, complex | np.complexfloating):
            return complex(val)

    def _is_number(self, val):
        if isinstance(val, int | float | complex) or (
            isinstance(val, np.generic) and np.issubdtype(val.dtype, np.number)
        ):
            return True
        return False

    def _is_real(self, val):
        if isinstance(val, int | float) or (
            isinstance(val, np.generic)
            and np.issubdtype(val.dtype, np.integer | np.floating)
        ):
            return True
        return False

    def _to_real(self, val):
        if isinstance(val, int | float):
            return val
        elif isinstance(val, np.generic):
            if np.issubdtype(val.dtype, np.integer):
                return int(val)
            elif np.issubdtype(val.dtype, np.floating):
                return float(val)

    def _is_int(self, val):
        if isinstance(val, int) or (
            isinstance(val, np.generic) and np.issubdtype(val.dtype, np.integer)
        ):
            return True
        return False

    def _to_str_flat_list(self, array):
        if isinstance(array, list | tuple):
            return self._flatten(array)
        elif isinstance(array, range):
            return list(array)
        elif isinstance(array, np.ndarray) and array.dtype.kind == "U":
            return array.ravel().tolist()
        elif isinstance(array, str):
            return [array]
        elif isinstance(array, np.str_):
            return [str(array)]
        raise TypeError(f"{array}には文字列のみが入った配列を指定してください")

    def _to_flat_list(self, array):
        if np.isscalar(array):
            return [array]
        elif isinstance(array, list | tuple):
            return self._flatten(array)
        elif isinstance(array, range):
            return list(array)
        elif isinstance(array, np.ndarray):
            return array.ravel().tolist()

    def _flatten(self, lst):
        result = []
        for item in lst:
            if isinstance(item, list | tuple):
                result.extend(self._flatten(item))
            else:
                result.append(item)
        return result
