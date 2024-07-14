import re
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class State:
    tag: Optional[str] = None
    is_closing: Optional[bool] = None
    text: Optional[str] = None


def parse(text: str):
    position = 0
    for match in re.finditer(r"(<<|>>)|<(/?)([a-z\-]+)>", text):
        escape, is_closing, tag = match.groups()
        start_position, end_position = match.span()

        yield State(tag=None, is_closing=None, text=text[position:start_position])

        if escape:
            yield State(tag=None, is_closing=None, text=escape[0])
        else:
            yield State(tag=tag, is_closing=bool(is_closing), text=None)

        position = end_position

    if position < len(text):
        yield State(tag=None, is_closing=None, text=text[position:])
