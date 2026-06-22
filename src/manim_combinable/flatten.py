from collections.abc import Callable
from typing import Any

from manim import Animation, AnimationGroup, Mobject
from manim.opengl import OpenGLMobject


class Flatten(AnimationGroup):
    def __init__(
        self,
        mobject: Mobject | OpenGLMobject,
        animation: Callable[[Mobject], Animation],
        max_depth: int | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(
            *(animation(leaf) for leaf in _get_leaves(mobject=mobject, max_depth=max_depth)),
            **kwargs,
        )


def _get_leaves(mobject: Mobject | OpenGLMobject, max_depth: int | None = None) -> set[Mobject | OpenGLMobject]:
    leaves: set[Mobject | OpenGLMobject] = set()
    seen: set[Mobject | OpenGLMobject] = {mobject}
    current_depth: set[Mobject | OpenGLMobject] = {mobject}

    while len(current_depth) > 0 and (max_depth is None or max_depth >= 0):
        next_depth: set[Mobject | OpenGLMobject] = set()
        for node in current_depth:
            if len(node.submobjects) == 0 or max_depth == 0:
                leaves.add(node)
            else:
                next_depth.update(node.submobjects)
        next_depth -= seen
        seen |= next_depth

        current_depth = next_depth
        max_depth = max_depth - 1 if max_depth is not None else None

    return leaves
