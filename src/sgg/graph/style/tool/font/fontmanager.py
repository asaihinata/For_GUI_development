from matplotlib.font_manager import FontEntry, findSystemFonts, fontManager

__all__ = ["Fontmanager", "Fontentry"]


class Fontmanager:
    fontmanager = fontManager.ttflist

    def __iter__(self):
        return iter(self.fontmanager)

    def __len__(self):
        return len(self.fontmanager)

    def __contains__(self, item):
        return item in self.fontmanager

    def __getitem__(self, val):
        if not isinstance(val, int | slice):
            return None
        return self.fontmanager[val]

    def __reversed__(self):
        return reversed(self.fontmanager)

    @classmethod
    def fname(cls):
        return [i.fname for i in cls.fontmanager]

    @classmethod
    def name(cls):
        return [i.name for i in cls.fontmanager]

    @classmethod
    def style(cls):
        return [i.style for i in cls.fontmanager]

    @classmethod
    def variant(cls):
        return [i.variant for i in cls.fontmanager]

    @classmethod
    def weight(cls):
        return [i.weight for i in cls.fontmanager]

    @classmethod
    def stretch(cls):
        return [i.stretch for i in cls.fontmanager]

    @classmethod
    def size(cls):
        return [i.size for i in cls.fontmanager]

    def sysfont(self):
        return findSystemFonts()

    @staticmethod
    def sysfont():
        return findSystemFonts()


class Fontentry:
    def __init__(self, fontentry):
        if isinstance(fontentry, FontEntry):
            self.fontentry = fontentry
        else:
            raise TypeError("fontentryの型が違います")

    def fname(self):
        return self.fontentry.fname

    def name(self):
        return self.fontentry.name

    def style(self):
        return self.fontentry.style

    def variant(self):
        return self.fontentry.variant

    def weight(self):
        return self.fontentry.weight

    def stretch(self):
        return self.fontentry.stretch

    def size(self):
        return self.fontentry.size
