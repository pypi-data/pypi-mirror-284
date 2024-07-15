from .doc import Element, Doc, EscapedStr, SupportsStr
from .formatting import Bold


class KeyValue(Element):
    title: Element
    value: Element
    suffix: Element

    def __init__(
            self,
            title: Element | SupportsStr,
            value: Element | SupportsStr,
            suffix: Element | SupportsStr = ': ',
            title_bold: bool = True
    ):
        self.title = Bold(title) if title_bold else EscapedStr.if_needed(title)
        self.value = EscapedStr.if_needed(value)
        self.suffix = EscapedStr.if_needed(suffix)

    def __str__(self) -> str:
        return f'{self.title}{self.suffix}{self.value}'


class HList(Doc):
    prefix: Element
    divider: Element

    def __init__(
            self,
            *args: Element | SupportsStr,
            prefix: Element | SupportsStr = '',
            divider: Element | SupportsStr = ' '
    ):
        super().__init__(*args)

        self.prefix = EscapedStr.if_needed(prefix)
        self.divider = EscapedStr.if_needed(divider)

    def __str__(self) -> str:
        text = ''
        for idx, item in enumerate(self):
            if idx > 0:
                text += str(self.divider)
            if self.prefix:
                text += str(self.prefix)
            text += str(item)

        return text
