from ..maindialog._Dialog import _Dialog
__all__=['_Dialog','asksaveasfilename']
class SaveAs(_Dialog):command='tk_getSaveFile'
def asksaveasfilename(**options):return SaveAs(**options).show()