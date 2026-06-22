from typing import Any

from manim import VMobject
from manim.opengl import OpenGLVMobject

from manim_combinable.helper import InterpolatedSetterGetter


class SetStrokeOpacity(InterpolatedSetterGetter[VMobject | OpenGLVMobject, float]):
    def __init__(
        self,
        mobject: VMobject | OpenGLVMobject,
        opacity: float | None = None,
        start_opacity: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(
            mobject=mobject,
            start=start_opacity if start_opacity is not None else lambda: self.mobject.get_stroke_opacity(),
            end=opacity if opacity is not None else mobject.get_stroke_opacity(),
            setter=lambda v: self.mobject.set_stroke(opacity=v),
            **kwargs,
        )
        self.opacity = opacity
        self.start_opacity = start_opacity
