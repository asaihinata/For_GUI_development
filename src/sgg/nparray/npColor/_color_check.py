from re import compile, findall

from numpy import array, fromiter, uint8

__all__ = ["check"]
HEX6_RE = compile(r"^#[0-9a-f]{6}$")
HEX3_RE = compile(r"^#[0-9a-f]{3}$")
RGB_RE = compile(r"^rgb\((\d+),(\d+),(\d+)\)$")
HSV_RE = compile(r"^hsv\((\d+),(\d+),(\d+)\)$")


def chagehex6(val):
    val = val[0][1:]
    return fromiter(
        (int(val[i : i + 2], 16) for i in range(0, len(val), 2)), dtype=uint8
    )


def chage(val):
    return array(val[0], dtype=uint8)


def check(name):
    if name[0] == "#":
        if HEX6_RE.match(name):
            return chagehex6(findall(HEX6_RE, name))
        if HEX3_RE.match(name):

            def sets(t):
                return f"{t}{t}"

            val = findall(HEX3_RE, name)[0][1:]
            return fromiter(
                (int(sets(val[i : i + 1]), 16) for i in range(0, len(val))), dtype=uint8
            )
    if RGB_RE.match(name):
        return chage(findall(RGB_RE, name))
    if HSV_RE.match(name):
        return chage(findall(HSV_RE, name))
