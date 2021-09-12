from uuid import uuid4

from pynvim.api.nvim import Nvim

from ...registry import rpc
from ...shared.repeat import sanitize
from ..edit import edit
from ..nvim.completions import UserData
from ..runtime import Stack
from ..state import state


@rpc(blocking=True)
def repeat(nvim: Nvim, stack: Stack) -> None:
    s = state()
    sanitized = sanitize(s.last_edit)
    data = UserData(
        uid=uuid4(),
        instance=uuid4(),
        sort_by="",
        change_uid=uuid4(),
        primary_edit=sanitized,
        secondary_edits=(),
        doc=None,
        extern=None,
    )
    edit(nvim, stack=stack, state=s, data=data, synthetic=True)
