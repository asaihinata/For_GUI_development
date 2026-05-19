from ..maindialog._Dialog import _Dialog
class SaveAs(_Dialog):command='tk_getSaveFile'
def asksaveasfilename(**options):return SaveAs(**options).show()