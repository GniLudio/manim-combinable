from typing import Any

import numpy as np
from manim import Animation, AnimationGroup, Group, Mobject, VGroup, VMobject
from manim.typing import Point3DLike, Vector3DLike

from manim_combinable.apply_rate import Reverse
from manim_combinable.flatten import Flatten
from manim_combinable.move_to import MoveTo
from manim_combinable.opacity import SetOpacity
from manim_combinable.scale import Scale
from manim_combinable.shift import Shift


class FadeIn(AnimationGroup):
    """Replaces :class:`manim.FadeIn`"""

    def __init__(
        self,
        *mobjects: Mobject,
        opacity: float | tuple[float | None, float | None] | None = None,
        start_opacity: float | tuple[float | None, float | None] | None = 0,
        shift: Vector3DLike | None = None,
        target_position: Point3DLike | Mobject | None = None,
        scale: float | None = None,
        flatten_fade: bool = True,
        **kwargs: Any,
    ) -> None:
        assert len(mobjects) > 0
        mobject: Mobject
        if len(mobjects) == 1:
            mobject = mobjects[0]
        elif isinstance(mobjects[0], VMobject):
            mobject = VGroup(*mobjects)
        else:
            mobject = Group(*mobjects)

        animations: list[Animation] = [
            SetOpacity(mobject=mobject, opacity=opacity, start_opacity=start_opacity)
            if not flatten_fade
            else Flatten(mobject, lambda leaf: SetOpacity(mobject=leaf, opacity=opacity, start_opacity=start_opacity))
        ]
        if shift is not None:
            animations.append(Reverse(Shift(mobject=mobject, shift=-np.asarray(shift))))
        if target_position is not None:
            animations.append(Reverse(MoveTo(mobject=mobject, point_or_mobject=target_position)))
        if scale is not None:
            animations.append(Reverse(Scale(mobject=mobject, scale_factor=scale)))
        super().__init__(*animations, **kwargs)
