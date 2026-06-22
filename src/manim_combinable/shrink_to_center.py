from typing import Any

from manim import Mobject
from manim.opengl import OpenGLMobject

from manim_combinable.scale import Scale


class ShrinkToCenter(Scale):
    """Replaces :class:`manim.ShrinkToCenter`"""

    def __init__(
        self,
        mobject: Mobject | OpenGLMobject,
        scale_factor: float = 0,
        **kwargs: Any,
    ) -> None:
        super().__init__(mobject, scale_factor=scale_factor, **kwargs)
