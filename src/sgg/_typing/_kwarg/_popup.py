from typing import Literal, TypedDict


# popup
class Dict_P_Information(TypedDict):
    title: str = "Information"
    message: str = "Information message"
    icon: Literal["info", "warning", "error", "question"] = "info"


class Dict_P_Warning(TypedDict):
    title: str = "Warning"
    message: str = "Warning message"
    icon: Literal["info", "warning", "error", "question"] = "warning"


class Dict_P_Error(TypedDict):
    title: str = "Error"
    message: str = "Error message"
    icon: Literal["info", "warning", "error", "question"] = "error"


class Dict_P_Question(TypedDict):
    title: str = "Question"
    message: str = "Question message"
    icon: Literal["info", "warning", "error", "question"] = "question"
