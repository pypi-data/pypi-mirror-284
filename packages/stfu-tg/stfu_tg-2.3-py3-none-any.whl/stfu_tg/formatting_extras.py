from .doc import Element, EscapedStr, SupportsStr
from .formatting import Bold


class Title(Element):
    item: Element
    prefix: Element
    postfix: Element
    bold: bool

    def __init__(
            self,
            item: Element | SupportsStr,
            prefix: Element | SupportsStr = '[',
            postfix: Element | SupportsStr = ']',
            bold: bool = True
    ):
        self.item = EscapedStr.if_needed(item)
        self.prefix = EscapedStr.if_needed(prefix)
        self.postfix = EscapedStr.if_needed(postfix)
        self.bold = bold

    def __str__(self) -> str:
        text = f"{self.prefix}{self.item}{self.postfix}"

        if self.bold:
            text = str(Bold(text))

        return text


class Template(Element):
    item: Element
    placeholders: dict[str, Element]

    def __init__(
            self,
            item: Element | SupportsStr,
            **kwargs: Element | SupportsStr
    ):
        self.item = EscapedStr.if_needed(item)
        self.placeholders = {k: EscapedStr.if_needed(v) for k, v in kwargs.items()}

    def __str__(self) -> str:
        text = str(self.item)

        for k, v in self.placeholders.items():
            text = text.replace(f'{{{k}}}', str(v))

        return text
