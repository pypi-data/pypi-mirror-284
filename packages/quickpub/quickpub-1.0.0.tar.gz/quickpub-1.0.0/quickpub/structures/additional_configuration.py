from dataclasses import dataclass
from typing import Optional, List
from ..runnables import Runnable
from ..managers import PythonManager


@dataclass(frozen=True)
class AdditionalConfiguration:
    python_manager: Optional[PythonManager] = None
    runners: Optional[List[Runnable]] = None


__all__ = [
    'AdditionalConfiguration',
]
