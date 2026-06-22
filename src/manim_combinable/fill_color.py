from typing import Any

from manim import ManimColor, ParsableManimColor, VMobject
from manim.opengl import OpenGLVMobject

from manim_combinable.helper import InterpolatedSetterGetter


class SetFillColor(InterpolatedSetterGetter[VMobject | OpenGLVMobject, ManimColor]):
    def __init__(
        self,
        mobject: VMobject | OpenGLVMobject,
        color: ParsableManimColor | None = None,
        start_color: ParsableManimColor | None = None,
        **kwargs: Any,
    ) -> None:
        assert color is not None or start_color is not None
        super().__init__(
            mobject,
            start=ManimColor.parse(start_color) if start_color is not None else (lambda: mobject.get_fill_color()),
            end=ManimColor.parse(color) if color is not None else mobject.get_fill_color(),
            setter=lambda v: self.mobject.set_fill(color=v),
            interpolator=ManimColor.interpolate,
            **kwargs,
        )
