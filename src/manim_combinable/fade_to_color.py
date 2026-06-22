from typing import Any

from manim import Animation, AnimationGroup, Mobject, ParsableManimColor
from manim.opengl import OpenGLMobject

from manim_combinable.color import SetColor
from manim_combinable.flatten import Flatten


class FadeToColor(AnimationGroup):
    """Replaces :class:`manim.FadeToColor`"""

    def __init__(
        self,
        mobject: Mobject | OpenGLMobject,
        color: ParsableManimColor | None = None,
        start_color: ParsableManimColor | None = None,
        flatten: bool = True,
        **kwargs: Any,
    ) -> None:
        animations: list[Animation]
        if not flatten:
            animations = [SetColor(mobject=mobject, color=color, start_color=start_color)]
        else:
            animations = [Flatten(mobject, lambda leaf: SetColor(mobject=leaf, color=color, start_color=start_color))]
        super().__init__(*animations, **kwargs)
