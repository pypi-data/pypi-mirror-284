import html
from typing import Optional

from stfu_tg.doc import Element, EscapedStr, SupportsStr


class StyleStr(Element):
    prefix: str
    postfix: str
    text: str

    def __str__(self) -> str:
        return self.text

    def __init__(self, item: Element | SupportsStr):
        item = EscapedStr.if_needed(item)
        self.text = f'{self.prefix}{item}{self.postfix}'


class Bold(StyleStr):
    prefix = '<b>'
    postfix = '</b>'


class Italic(StyleStr):
    prefix = '<i>'
    postfix = '</i>'


class Code(StyleStr):
    prefix = '<code>'
    postfix = '</code>'


class Strikethrough(StyleStr):
    prefix = '<s>'
    postfix = '</s>'


class Underline(StyleStr):
    prefix = '<u>'
    postfix = '</u>'


class Spoiler(StyleStr):
    prefix = '<tg-spoiler>'
    postfix = '</tg-spoiler>'


class Pre(StyleStr):
    prefix: str
    postfix = '</pre>'

    def __init__(self, item: Element | SupportsStr, language: Optional[str] = None):
        if language:
            self.prefix = f'<pre><code class="language-{language}">'
        else:
            self.prefix = '<pre>'

        super().__init__(item)


class Url(StyleStr):
    prefix: str
    postfix = '</a>'

    def __init__(self, item: Element | SupportsStr, link: str):
        # We escape it manually because we need to escape quotes as well
        self.prefix = f'<a href="{html.escape(link)}">'
        super().__init__(item)


class BlockQuote(StyleStr):
    prefix: str
    postfix = '</blockquote>'

    def __init__(self, item: Element | SupportsStr, expandable: bool = False):
        self.prefix = '<blockquote expandable>' if expandable else '<blockquote>'
        super().__init__(item)
