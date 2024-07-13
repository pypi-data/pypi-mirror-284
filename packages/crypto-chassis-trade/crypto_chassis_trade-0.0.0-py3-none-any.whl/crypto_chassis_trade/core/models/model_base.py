from typing import Tuple
from typing import Optional
from dataclasses import dataclass

@dataclass(frozen=True,kw_only=False)
class ModelBase:
    api_method: Optional[str] = None
    symbol: Optional[str] = None
    exchange_update_time_point: Optional[Tuple[int, int]] = None
