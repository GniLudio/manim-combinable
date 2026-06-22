from collections.abc import Callable
from typing import Any

from manim import DecimalNumber

from manim_combinable.helper import SetterGetter


class ChangingDecimal(SetterGetter[DecimalNumber, float]):
    """Replaces :class:`manim.ChangingDecimal`"""

    def __init__(
        self,
        decimal_mob: DecimalNumber,
        number_update_func: Callable[[float], float],
        suspend_mobject_updating: bool = False,
        **kwargs: Any,
    ) -> None:
        super().__init__(
            mobject=decimal_mob,
            setter=lambda v: self.mobject.set_value(v),
            getter=number_update_func,
            suspend_mobject_updating=suspend_mobject_updating,
            **kwargs,
        )
