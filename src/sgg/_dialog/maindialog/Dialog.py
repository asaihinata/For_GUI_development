from tkinter import _destroy_temp_root, _get_temp_root

__all__ = ["Dialog"]


class Dialog:
    command = None

    def __init__(self, master=None, **options):
        if master == None:
            master = options.get("parent")
        self.master, self.options = master, options

    def _fixoptions(self):
        pass

    def _fixresult(self, widget, result):
        return result

    def show(self, **options):
        for k, v in options.items():
            self.options[k] = v
        self._fixoptions()
        master = self.master
        if master == None:
            master = _get_temp_root()
        try:
            self._test_callback(master)
            s = self._fixresult(
                master, master.tk.call(self.command, *master._options(self.options))
            )
        finally:
            _destroy_temp_root(master)
        return s

    def _test_callback(self, master):
        pass
