from typing import Any

import numpy as np
from manim import Mobject
from manim.opengl import OpenGLMobject
from manim.typing import Vector3D, Vector3DLike

from manim_combinable.helper import RelativeUpdater


class Shift(RelativeUpdater[Mobject | OpenGLMobject, Vector3D]):
    def __init__(
        self,
        mobject: Mobject | OpenGLMobject,
        shift: Vector3DLike,
        **kwargs: Any,
    ) -> None:
        super().__init__(
            mobject=mobject,
            setter=lambda change: self.mobject.shift(change),
            getter=lambda a: a * np.asarray(self.shift),
            **kwargs,
        )
        self.shift = shift
