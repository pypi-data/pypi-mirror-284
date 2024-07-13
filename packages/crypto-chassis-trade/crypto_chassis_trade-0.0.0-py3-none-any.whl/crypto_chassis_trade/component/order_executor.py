class OrderExecutor:

    def __init__(self, *, is_buy, target_quantity=None,target_quote_quantity = None,order_quantity_randomization_max=0.1,worst_slippage=0.005,worst_price=None,refresh_interval_seconds=0.5,time_soft_limit_seconds=5,time_hard_limit_seconds=10):
        self._is_buy = is_buy
        self._target_quantity = target_quantity
        self._target_quote_quantity = target_quote_quantity
        self._order_quantity_randomization_max = order_quantity_randomization_max
        self._worst_slippage = worst_slippage
        self._worst_price = worst_price
        self._refresh_interval_seconds = refresh_interval_seconds
        self._time_soft_limit_seconds = time_soft_limit_seconds
        self._time_hard_limit_seconds = time_hard_limit_seconds
        # STYLE: prefer maker, prefer taker, both_maker_and_taker

    @property
    def is_buy(self):
        return self._is_buy

    @is_buy.setter
    def is_buy(self, is_buy):
        self._is_buy = is_buy
        self.refresh()

    @property
    def target_quantity(self):
        return self._target_quantity

    @target_quantity.setter
    def target_quantity(self, target_quantity):
        self._target_quantity = target_quantity
        self._target_quote_quantity = None
        self.refresh()
