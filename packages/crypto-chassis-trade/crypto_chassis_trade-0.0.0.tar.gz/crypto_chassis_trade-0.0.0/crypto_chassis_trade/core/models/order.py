from dataclasses import dataclass
from decimal import Decimal
from typing import Optional
from typing import Dict
from typing import Tuple
from typing import Any
from functools import cached_property
from crypto_chassis_trade.core.models.model_base import ModelBase
from enum import IntEnum

class OrderStatus(IntEnum):

    CREATE_SENT = 1
    CANCEL_SENT = 2
    CREATE_ACKNOWLEDGED = 3
    CANCEL_ACKNOWLEDGED = 4
    UNTRIGGERED = 5
    NEW = 6
    PARTIALLY_FILLED = 7
    FILLED = 8
    CANCELED = 9
    EXPIRED = 10
    REJECTED = 11

@dataclass(frozen=True,kw_only=False)
class Order(ModelBase):

    order_id: Optional[str] = None
    client_order_id: Optional[str] = None
    is_buy: Optional[bool] = None
    limit_price: Optional[str] = None
    quantity: Optional[str] = None


    is_post_only: Optional[bool] = False
    is_fok: Optional[bool] = False
    is_ioc: Optional[bool] = False
    is_reduce_only: Optional[bool] = False

    extra_params: Optional[Dict[str, Any]] = None

    cumulative_filled_quantity: Optional[str] = None
    cumulative_filled_quote_quantity: Optional[str] = None

    exchange_create_time_point: Optional[Tuple[int, int]] = None
    status: Optional[str] = None


    @cached_property
    def limit_price_as_float(self):
        return float(self.limit_price) if self.limit_price else None

    @cached_property
    def limit_price_as_decimal(self):
        return Decimal(self.limit_price) if self.limit_price else None


    @cached_property
    def quantity_as_float(self):
        return float(self.quantity) if self.quantity else None

    @cached_property
    def quantity_as_decimal(self):
        return Decimal(self.quantity) if self.quantity else None



    @cached_property
    def cumulative_filled_quantity_as_float(self):
        return float(self.cumulative_filled_quantity) if self.cumulative_filled_quantity else None

    @cached_property
    def cumulative_filled_quantity_as_decimal(self):
        return Decimal(self.cumulative_filled_quantity) if self.cumulative_filled_quantity else None

    @cached_property
    def cumulative_filled_quote_quantity_as_float(self):
        return float(self.cumulative_filled_quote_quantity) if self.cumulative_filled_quote_quantity else None

    @cached_property
    def cumulative_filled_quote_quantity_as_decimal(self):
        return Decimal(self.cumulative_filled_quote_quantity) if self.cumulative_filled_quote_quantity else None

    @property
    def is_sent(self):
        return self.status <= OrderStatus.CANCEL_SENT

    @property
    def is_open(self):
        return self.status >= CREATE_ACKNOWLEDGED and self.status <= PARTIALLY_FILLED

    @property
    def is_closed(self):
        return self.status >= OrderStatus.FILLED
