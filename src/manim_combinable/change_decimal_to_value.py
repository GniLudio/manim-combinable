from typing import Any

import manim

from manim_combinable.helper import InterpolatedSetterGetter


class ChangeDecimalToValue(InterpolatedSetterGetter[manim.DecimalNumber, float]):
    """Replaces :class:`manim.ChangeDecimalToValue`"""

    def __init__(
        self,
        decimal_mob: manim.DecimalNumber,
        target_number: float | None = None,
        start_value: float | None = None,
        **kwargs: Any,
    ) -> None:
        assert target_number is not None or start_value is not None
        super().__init__(
            decimal_mob,
            start=start_value if start_value is not None else (lambda: self.mobject.get_value()),
            end=target_number if target_number is not None else decimal_mob.get_value(),
            setter=lambda v: self.mobject.set_value(v),
            **kwargs,
        )
