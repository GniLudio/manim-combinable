from typing import Any

from manim import OUT, PI, Mobject
from manim.opengl import OpenGLMobject
from manim.typing import Point3DLike, Vector3DLike

from manim_combinable.helper import RelativeUpdater


class Rotate(RelativeUpdater[Mobject | OpenGLMobject, float]):
    """Replaces :class:`manim.Rotate`"""

    def __init__(
        self,
        mobject: Mobject,
        angle: float = PI,
        axis: Vector3DLike = OUT,
        about_point: Point3DLike | None = None,
        about_edge: Vector3DLike | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(
            mobject,
            setter=lambda change: self.mobject.rotate(
                angle=change,
                axis=self.axis,
                about_point=self.about_point,
                about_edge=self.about_edge,
            ),
            getter=lambda a: a * self.angle,
            **kwargs,
        )
        self.angle = angle
        self.axis = axis
        self.about_point = about_point
        self.about_edge = about_edge
