from .doc import Doc, Element, EscapedStr, SupportsStr
from .formatting import Bold, Underline


class Section(Doc):
    title_element: Element
    title_postfix: Element
    title_underline: bool
    title_bold: bool
    indent: int
    indent_text: str

    def __init__(
            self,
            *items: Element | SupportsStr,
            title: Element | SupportsStr = '',
            title_underline=True,
            title_bold=False,
            indent=1,
            indent_text='  ',
            title_postfix: Element | SupportsStr = ':'
    ):
        self.title_element = EscapedStr.if_needed(title)
        self.indent = indent
        self.title_underline = title_underline
        self.title_bold = title_bold
        self.indent_text = indent_text
        self.title_postfix = EscapedStr.if_needed(title_postfix)

        super().__init__(*items)

    @property
    def title(self) -> str:
        if not self.title_element:
            return ''

        title = Underline(self.title_element) if self.title_underline else self.title_element
        title = Bold(title) if self.title_bold else title
        return f'{title}{self.title_postfix}'

    def to_str(self, additional_indent: int = 0) -> str:
        text = ''
        text += self.title
        for item in self:
            text += '\n'

            if type(item) is Section:
                text += self.indent_text * (self.indent + additional_indent)
                text += item.to_str(additional_indent=additional_indent + self.indent)
            elif type(item) is VList:
                text += item.to_str(additional_indent=(additional_indent + self.indent) * 2)
            else:
                text += self.indent_text * (self.indent + additional_indent)
                text += str(item)

        return text

    def __str__(self) -> str:
        return self.to_str()


class VList(Doc):
    def __init__(
            self,
            *items: Element | SupportsStr,
            indent: int = 0,
            prefix: Element | SupportsStr = '- '
    ):
        super().__init__(*items)

        self.prefix = EscapedStr.if_needed(prefix)
        self.indent = indent

    def to_str(self, additional_indent: int = 0) -> str:
        indent = self.indent + additional_indent
        space = ' ' * indent if indent else ' '
        text = ''
        for idx, item in enumerate(self):
            if idx > 0:
                text += '\n'
            text += f'{space}{self.prefix}{item}'

        return text

    def __str__(self) -> str:
        return self.to_str()
