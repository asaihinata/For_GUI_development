from ..btn import Btn, Button, asksaveasfilename

__all__ = ["Savebtn"]


class Savebtn(Btn):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.__path = None
        self.text = kw.get("text", "Save file")
        self.title = kw.get("title", "Save file")
        self.defaultextension = kw.get("defaultextension", ".txt")
        self.filetypes = kw.get("filetypes", [("All files", "*.*")])
        self.initialfile = kw.get("initialfile")
        self.initialdir = kw.get("initialdir")
        self.widget = Button(
            master,
            takefocus=self.takefocus,
            anchor=self.anchor,
            padx=self.padx,
            pady=self.pady,
            relief=self.relief,
            wraplength=self.wraplength,
            cursor=self.cursor,
            text=self.text,
            bg=self.bg,
            fg=self.fg,
            font=self.font,
            width=self.width,
            height=self.height,
            command=self._savefile,
            borderwidth=self.borderwidth,
        )

    def __fspath__(self):
        return self.path

    @property
    def path(self):
        return self.__path

    def get_path(self):
        return self.__path

    def _savefile(self):
        self.__path = asksaveasfilename(
            parent=self.master,
            initialfile=self.initialfile,
            initialdir=self.initialdir,
            defaultextension=self.defaultextension,
            filetypes=self.filetypes,
            title=self.title,
        )
        return self.__path
