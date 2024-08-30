from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING, Awaitable, Optional

if TYPE_CHECKING:
    __all__ = ["AsyncioEvent"]

class AsyncioEvent(asyncio.Event):
    """Same as asyncio.Event but adds a `wait` with timeout.
    """
    async def wait(self, timeout: Optional[float] = None) -> Awaitable[bool]:
        try:
            await asyncio.wait_for(super().wait(), timeout=timeout)
            return True
        except asyncio.TimeoutError:
            return False
