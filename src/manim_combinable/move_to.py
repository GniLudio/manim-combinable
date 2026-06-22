from typing import Any

from manim import ORIGIN, Mobject
from manim.opengl import OpenGLMobject
from manim.typing import Point3D, Point3DLike, Vector3DLike

from manim_combinable.helper import InterpolatedSetterGetter


class MoveTo(InterpolatedSetterGetter[Mobject | OpenGLMobject, Point3D]):
    def __init__(
        self,
        mobject: Mobject | OpenGLMobject,
        point_or_mobject: Point3DLike | Mobject | OpenGLMobject,
        aligned_edge: Vector3DLike = ORIGIN,
        coor_mask: Vector3DLike = (1, 1, 1),
        **kwargs: Any,
    ) -> None:
        super().__init__(
            mobject=mobject,
            start=lambda: self.mobject.get_center(),
            end=self._get_end,
            setter=lambda v: self.mobject.move_to(v),
            **kwargs,
        )
        self.point_or_mobject = point_or_mobject
        self.aligned_edge = aligned_edge
        self.coor_mask = coor_mask

    def _get_end(self) -> Point3D:
        return (
            self.mobject.copy()
            .move_to(
                point_or_mobject=self.point_or_mobject,
                aligned_edge=self.aligned_edge,
                coor_mask=self.coor_mask,
            )
            .get_center()
        )
