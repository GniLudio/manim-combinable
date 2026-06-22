from typing import Any

from manim import Mobject
from manim.opengl import OpenGLMobject
from manim.typing import Point3DLike, Vector3DLike

from manim_combinable.helper import RelativeUpdater


class Scale(RelativeUpdater[Mobject | OpenGLMobject, float]):
    def __init__(
        self,
        mobject: Mobject | OpenGLMobject,
        scale_factor: float,
        about_point: Point3DLike | None = None,
        about_edge: Vector3DLike | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(
            mobject=mobject,
            setter=lambda change: self.mobject.scale(
                scale_factor=change,
                about_point=self.about_point,
                about_edge=self.about_edge,
            ),
            getter=lambda a: 1 + a * (self.scale_factor - 1),
            subtractor=lambda c, p: 1 if p == 0 else c / p,
            **kwargs,
        )
        self.scale_factor = scale_factor
        self.about_point = about_point
        self.about_edge = about_edge
