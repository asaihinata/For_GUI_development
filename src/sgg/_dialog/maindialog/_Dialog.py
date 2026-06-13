from os.path import split

from .dialog import Dialog

__all__ = ["_Dialog"]


class _Dialog(Dialog):
    def _fixoptions(self):
        try:
            self.options["filetypes"] = tuple(self.options["filetypes"])
        except:
            pass

    def _fixresult(self, widget, result):
        if result:
            try:
                result = result.string
            except:
                pass
            path, file = split(result)
            self.options["initialdir"] = path
            self.options["initialfile"] = file
        self.filename = result
        return result
