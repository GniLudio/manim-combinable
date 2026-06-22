from typing import Any

from manim import AnimationGroup, Mobject, VMobject
from manim.opengl import OpenGLMobject, OpenGLVMobject

from manim_combinable.fill_opacity import SetFillOpacity
from manim_combinable.helper import InterpolatedSetterGetter
from manim_combinable.stroke_opacity import SetStrokeOpacity


class _SetOpacity(InterpolatedSetterGetter[Mobject | OpenGLMobject, float]):
    def __init__(
        self,
        mobject: Mobject | OpenGLMobject,
        opacity: float | None = None,
        start_opacity: float | None = None,
        **kwargs: Any,
    ) -> None:
        assert opacity is not None or start_opacity is not None
        super().__init__(
            mobject=mobject,
            start=start_opacity if start_opacity is not None else lambda: self.mobject.get_opacity(),
            end=opacity if opacity is not None else mobject.get_opacity(),
            setter=lambda v: self.mobject.set_opacity(v),
            **kwargs,
        )


class SetOpacity(AnimationGroup):
    def __init__(
        self,
        mobject: Mobject | OpenGLMobject,
        opacity: float | tuple[float | None, float | None] | None = None,
        start_opacity: float | tuple[float | None, float | None] | None = None,
        **kwargs: Any,
    ) -> None:
        assert opacity is not None or start_opacity is not None
        if isinstance(mobject, VMobject | OpenGLVMobject):
            animations = [
                SetFillOpacity(
                    mobject=mobject,
                    opacity=opacity if not isinstance(opacity, tuple) else opacity[0],
                    start_opacity=start_opacity if not isinstance(start_opacity, tuple) else start_opacity[0],
                    **kwargs,
                ),
                SetStrokeOpacity(
                    mobject=mobject,
                    opacity=opacity if not isinstance(opacity, tuple) else opacity[1],
                    start_opacity=start_opacity if not isinstance(start_opacity, tuple) else start_opacity[1],
                    **kwargs,
                ),
            ]
        else:
            assert not isinstance(opacity, tuple) and not isinstance(start_opacity, tuple)
            animations = [
                _SetOpacity(
                    mobject=mobject,
                    opacity=opacity,
                    start_opacity=start_opacity,
                )
            ]
        super().__init__(*animations, **kwargs)
