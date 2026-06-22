from typing import Any

from manim import Mobject, VMobject
from manim.opengl import OpenGLMobject
from manim.typing import Point3D

from manim_combinable.helper import SetterGetter


class MoveAlongPath(SetterGetter[Mobject | OpenGLMobject, Point3D]):
    """Replaces :class:`manim.MoveAlongPath`"""

    def __init__(
        self,
        mobject: Mobject,
        path: VMobject,
        **kwargs: Any,
    ) -> None:
        kwargs.setdefault("suspend_mobject_updating", False)
        super().__init__(
            mobject,
            setter=lambda v: self.mobject.move_to(v),
            getter=self._get_value,
            **kwargs,
        )
        self.path = path

    def _get_value(self, alpha: float) -> Point3D:
        return self.path.point_from_proportion(self.get_rate_func()(alpha))
