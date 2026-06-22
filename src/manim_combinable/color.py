from typing import Any

from manim import ManimColor, Mobject, ParsableManimColor
from manim.opengl import OpenGLMobject

from manim_combinable.helper import InterpolatedSetterGetter


class SetColor(InterpolatedSetterGetter[Mobject | OpenGLMobject, ManimColor]):
    def __init__(
        self,
        mobject: Mobject | OpenGLMobject,
        color: ParsableManimColor | None = None,
        start_color: ParsableManimColor | None = None,
        **kwargs: Any,
    ) -> None:
        assert color is not None or start_color is not None
        super().__init__(
            mobject,
            start=(
                ManimColor.parse(start_color)
                if start_color is not None
                else (lambda: ManimColor.parse(self.mobject.get_color()))
            ),
            end=ManimColor.parse(color) if color is not None else ManimColor.parse(mobject.get_color()),
            setter=lambda v: self.mobject.set_color(color=v),
            interpolator=ManimColor.interpolate,
            **kwargs,
        )
