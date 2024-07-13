from dataclasses import dataclass
from decimal import Decimal
from typing import Optional
from functools import cached_property
from crypto_chassis_trade.core.models.model_base import ModelBase

@dataclass(frozen=True,kw_only=False)
class Fill(ModelBase):

    order_id: Optional[str] = None
    client_order_id: Optional[str] = None
    trade_id: Optional[int] = None
    is_buy: Optional[bool] = None
    price: Optional[str] = None
    quantity: Optional[str] = None


    fee_asset: Optional[str] = None
    fee_quantity: Optional[str] = None



    @cached_property
    def price_as_float(self):
        return float(self.price) if self.price else None

    @cached_property
    def price_as_decimal(self):
        return Decimal(self.price) if self.price else None

    @cached_property
    def quantity_as_float(self):
        return float(self.quantity) if self.quantity else None

    @cached_property
    def quantity_as_decimal(self):
        return Decimal(self.quantity) if self.quantity else None

    @cached_property
    def fee_quantity_as_float(self):
        return float(self.fee_quantity) if self.fee_quantity else None

    @cached_property
    def fee_quantity_as_decimal(self):
        return Decimal(self.fee_quantity) if self.fee_quantity else None
