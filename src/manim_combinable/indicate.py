from typing import Any

from manim import PURE_YELLOW, Animation, AnimationGroup, Mobject, ParsableManimColor, there_and_back

from manim_combinable.color import SetColor
from manim_combinable.scale import Scale


class Indicate(AnimationGroup):
    """Replaces :class:`manim.Indicate`"""

    def __init__(
        self,
        mobject: Mobject,
        scale_factor: float = 1.2,
        color: ParsableManimColor = PURE_YELLOW,
        **kwargs: Any,
    ) -> None:
        animations: list[Animation] = []
        if scale_factor is not None:
            animations.append(Scale(mobject=mobject, scale_factor=scale_factor, rate_func=there_and_back))
        if color is not None:
            animations.append(SetColor(mobject=mobject, color=color, rate_func=there_and_back))
        super().__init__(
            *animations,
            **kwargs,
        )
