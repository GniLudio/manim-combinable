from typing import Any

from manim import Mobject
from manim.opengl import OpenGLMobject

from manim_combinable.scale import Scale


class ScaleInPlace(Scale):
    """Replaces :class:`manim.ScaleInPlace`"""

    def __init__(
        self,
        mobject: Mobject | OpenGLMobject,
        scale_factor: float,
        **kwargs: Any,
    ) -> None:
        super().__init__(
            mobject=mobject,
            scale_factor=scale_factor,
            **kwargs,
        )
