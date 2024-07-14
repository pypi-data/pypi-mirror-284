from tml.context import Context
from tml.parser import parse


def markup(text: str) -> str:
    tokens = []

    context = Context()
    for state in parse(text):
        if state.text is not None:
            tokens.append(context.apply(state.text))
        elif state.tag is not None:
            if not state.is_closing:
                context.push(state.tag)
            else:
                context.pop(state.tag)

    return "".join(tokens)
