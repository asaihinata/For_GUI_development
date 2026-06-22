from .message import Message

__all__ = ["_show", "_iconset"]


def _show(title=None, message=None, _icon=None, _type=None, **kw):
    if _icon and "icon" not in kw:
        kw["icon"] = _icon
    if _type and "type" not in kw:
        kw["type"] = _type
    if title:
        kw["title"] = title
    if message:
        kw["message"] = message
    res = Message(**kw).show()
    if isinstance(res, bool):
        return "yes" if res else "no"
    return str(res)


def _iconset(icon, other="info"):
    if icon in ["info", "error", "warning", "question"]:
        return icon
    return other
