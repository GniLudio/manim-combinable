from abc import ABC
from collections.abc import Callable
from typing import Any, Generic, TypeVar, cast

from manim import Animation, Mobject, Scene
from manim.opengl import OpenGLMobject

M = TypeVar("M", bound=Mobject | OpenGLMobject)
V = TypeVar("V")


class SetterGetter(Animation, ABC, Generic[M, V]):
    """Animates a mobject using a setter and getter.

    Parameters
    ----------
    mobject
        The mobject.
    setter(value)
        A function that applies the value to the mobject.
    getter
        A function that retruns the target value.
    """

    def __init__(
        self,
        mobject: M,
        setter: Callable[[V], Any],
        getter: V | Callable[[float], V],
        **kwargs: Any,
    ) -> None:
        super().__init__(mobject, **kwargs)
        self.setter = setter
        self.getter = getter

    def interpolate(self, alpha: float) -> None:
        value = _to_value(self.getter, self.get_rate_func()(alpha))
        self.setter(value)


class InterpolatedSetterGetter(SetterGetter[M, V]):
    """Animates a mobject using a setter and start/end values.

    Parameters
    ----------
    mobject
        The mobject.
    start
        The start value.
    end
        The end value.
    setter(value)
        A function that applies the value to the mobject.
    interpolator(start, end, alpha)
        A function that interpolates between the start and end value.
    """

    def __init__(
        self,
        mobject: M,
        start: V | Callable[[], V],
        end: V | Callable[[], V],
        setter: Callable[[V], Any],
        interpolator: Callable[[V, V, float], V] = lambda start, end, a: start + a * (end - start),
        **kwargs: Any,
    ) -> None:
        super().__init__(
            mobject=mobject,
            setter=setter,
            getter=lambda a: self.interpolator(self._start_value, _to_value(self.end), a),
            **kwargs,
        )
        self.start = start
        self.end = end
        self.interpolator = interpolator

    def _setup_scene(self, scene: Scene) -> None:
        self._start_value = _to_value(self.start)
        super()._setup_scene(scene)


class RelativeUpdater(Animation, ABC, Generic[M, V]):
    """Animates a mobject by applying relative changes.
    Parameters
    ----------
    mobject
        The mobject.
    setter(change)
        The function that applies the change.
    getter(alpha)
        The function that returns the target value.
    subtractor(current_value, previous_value)
        The subtractor function.
    """

    def __init__(
        self,
        mobject: M,
        setter: Callable[[V], Any],
        getter: Callable[[float], V],
        subtractor: Callable[[V, V], V] = lambda current, previous: current - previous,
        **kwargs: Any,
    ) -> None:

        super().__init__(mobject, **kwargs)
        self.getter = getter
        self.subtractor = subtractor
        self.setter = setter

    def _setup_scene(self, scene: Scene) -> None:
        self._previous_value = self.getter(self.get_rate_func()(0))
        super()._setup_scene(scene)

    def interpolate(self, alpha: float) -> None:
        current_value = self.getter(self.get_rate_func()(alpha))
        change = self.subtractor(current_value, self._previous_value)
        self.setter(change)
        self._previous_value = current_value


def _to_value(value_or_getter: V | Callable[..., V], *args: Any, **kwargs: Any) -> V:
    if not callable(value_or_getter):
        return value_or_getter
    return cast("V", value_or_getter(*args, **kwargs))
