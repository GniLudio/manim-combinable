from typing import Any

from manim import ManimColor, ParsableManimColor, VMobject
from manim.opengl import OpenGLVMobject

from manim_combinable.helper import InterpolatedSetterGetter


class SetStrokeColor(InterpolatedSetterGetter[VMobject | OpenGLVMobject, ManimColor]):
    def __init__(
        self,
        mobject: VMobject | OpenGLVMobject,
        color: ParsableManimColor | None = None,
        start_color: ParsableManimColor | None = None,
        **kwargs: Any,
    ) -> None:
        assert color is None or start_color is None
        super().__init__(
            mobject,
            start=(
                ManimColor.parse(start_color)
                if start_color is not None
                else (lambda: ManimColor.parse(self.mobject.get_stroke_color()))
            ),
            end=ManimColor.parse(color) if color is not None else ManimColor.parse(self.mobject.get_stroke_color()),
            setter=lambda v: self.mobject.set_stroke(color=v),
            interpolator=ManimColor.interpolate,
            **kwargs,
        )
