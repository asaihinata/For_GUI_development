from numpy._core import umath as um

__all__ = ["NDArrayOperatorsMixin"]


def _disables_array_ufunc(obj):
    try:
        return obj.__array_ufunc__ is None
    except AttributeError:
        return False


def _binary_method(ufunc, name):
    def func(self, other):
        if _disables_array_ufunc(other):
            return NotImplemented
        return ufunc(self, other)

    func.__name__ = f"__{name}__"
    return func


def _reflected_binary_method(ufunc, name):
    def func(self, other):
        if _disables_array_ufunc(other):
            return NotImplemented
        return ufunc(other, self)

    func.__name__ = f"__r{name}__"
    return func


def _inplace_binary_method(ufunc, name):
    def func(self, other):
        return ufunc(self, other, out=(self,))

    func.__name__ = f"__i{name}__"
    return func


def _unary_method(ufunc, name):
    def func(self):
        return ufunc(self)

    func.__name__ = f"__{name}__"
    return func


class NDArrayOperatorsMixin:
    __lt__ = _binary_method(um.less, "lt")
    __le__ = _binary_method(um.less_equal, "le")
    __eq__ = _binary_method(um.equal, "eq")
    __ne__ = _binary_method(um.not_equal, "ne")
    __gt__ = _binary_method(um.greater, "gt")
    __ge__ = _binary_method(um.greater_equal, "ge")
    __add__ = _binary_method(um.add, "add")
    __radd__ = _reflected_binary_method(um.add, "add")
    __iadd__ = _inplace_binary_method(um.add, "add")
    __sub__ = _binary_method(um.subtract, "sub")
    __rsub__ = _reflected_binary_method(um.subtract, "sub")
    __isub__ = _inplace_binary_method(um.subtract, "sub")
    __mul__ = _binary_method(um.multiply, "mul")
    __rmul__ = _reflected_binary_method(um.multiply, "mul")
    __imul__ = _inplace_binary_method(um.multiply, "mul")
    __matmul__ = _binary_method(um.matmul, "matmul")
    __rmatmul__ = _reflected_binary_method(um.matmul, "matmul")
    __imatmul__ = _inplace_binary_method(um.matmul, "matmul")
    __truediv__ = _binary_method(um.true_divide, "truediv")
    __rtruediv__ = _reflected_binary_method(um.true_divide, "truediv")
    __itruediv__ = _inplace_binary_method(um.true_divide, "truediv")
    __floordiv__ = _binary_method(um.floor_divide, "floordiv")
    __rfloordiv__ = _reflected_binary_method(um.floor_divide, "floordiv")
    __ifloordiv__ = _inplace_binary_method(um.floor_divide, "floordiv")
    __mod__ = _binary_method(um.remainder, "mod")
    __rmod__ = _reflected_binary_method(um.remainder, "mod")
    __imod__ = _inplace_binary_method(um.remainder, "mod")
    __pow__ = _binary_method(um.power, "pow")
    __rpow__ = _reflected_binary_method(um.power, "pow")
    __ipow__ = _inplace_binary_method(um.power, "pow")
    __lshift__ = _binary_method(um.left_shift, "lshift")
    __rlshift__ = _reflected_binary_method(um.left_shift, "lshift")
    __ilshift__ = _inplace_binary_method(um.left_shift, "lshift")
    __rshift__ = _binary_method(um.right_shift, "rshift")
    __rrshift__ = _reflected_binary_method(um.right_shift, "rshift")
    __irshift__ = _inplace_binary_method(um.right_shift, "rshift")
    __and__ = _binary_method(um.bitwise_and, "and")
    __rand__ = _reflected_binary_method(um.bitwise_and, "and")
    __iand__ = _inplace_binary_method(um.bitwise_and, "and")
    __xor__ = _binary_method(um.bitwise_xor, "xor")
    __rxor__ = _reflected_binary_method(um.bitwise_xor, "xor")
    __ixor__ = _inplace_binary_method(um.bitwise_xor, "xor")
    __or__ = _binary_method(um.bitwise_or, "or")
    __ror__ = _reflected_binary_method(um.bitwise_or, "or")
    __ior__ = _inplace_binary_method(um.bitwise_or, "or")
    __divmod__ = _binary_method(um.divmod, "divmod")
    __rdivmod__ = _reflected_binary_method(um.divmod, "divmod")
    __neg__ = _unary_method(um.negative, "neg")
    __pos__ = _unary_method(um.positive, "pos")
    __abs__ = _unary_method(um.absolute, "abs")
    __invert__ = _unary_method(um.invert, "invert")
