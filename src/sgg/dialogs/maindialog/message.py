from .dialog import Dialog

__all__ = ["Message"]


class Message(Dialog):
    command = "tk_messageBox"
