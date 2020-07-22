from typing import Optional, Set

from .da import or_else
from .types import State


def initial() -> State:
    return State(char_inserted=False, sources=set())


def forward(
    state: State,
    *,
    char_inserted: Optional[bool] = None,
    sources: Optional[Set[str]] = None
) -> State:
    new_state = State(
        char_inserted=or_else(char_inserted, state.char_inserted),
        sources=or_else(sources, state.sources),
    )
    return new_state
