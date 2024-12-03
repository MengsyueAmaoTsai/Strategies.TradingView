class OrderSizeAdjustmentService:
    def __init__(
        self,
        initial_capital: int,
        acceptable_drawdown_ratio: float = 0.2,
        drawdown_multiplier: float = 2,
    ) -> None:
        self._initial_capital = initial_capital
        self._single_strategy_drawdown_limit = acceptable_drawdown_ratio
        self._drawdown_multiplier = drawdown_multiplier

    def adjust_order_size(
        self, backtest_drawdown: float, backtest_order_size: int
    ) -> int:
        max_drawdown = (
            self._single_strategy_drawdown_limit
            / self._drawdown_multiplier
            * self._initial_capital
        )
        size = backtest_order_size * (max_drawdown / backtest_drawdown)

        return int(size)


service = OrderSizeAdjustmentService(initial_capital=1000)

order_size = service.adjust_order_size(
    backtest_drawdown=16464.13, backtest_order_size=30000
)

print(f"We should set the order size to: {order_size}")