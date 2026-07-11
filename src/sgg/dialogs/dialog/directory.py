from typing import ClassVar

from sgg.dialogs.maindialog import Dialog

__all__ = ["askdirectory","Directory",]


class Directory(Dialog):
    command: ClassVar[str] = "tk_chooseDirectory"

    def _fixresult(self, widget, result):
        if result:
            try:
                result = result.string
            except:
                pass
            self.options["initialdir"] = result
        self.directory = result
        return result


def askdirectory(**options):
    return Directory(**options).show()
