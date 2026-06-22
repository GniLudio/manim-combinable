from typing import Any

from manim import Animation, AnimationGroup
from manim.utils import rate_functions
from manim.utils.rate_functions import RateFunction


class ApplyRate(AnimationGroup):
    def __init__(
        self,
        animation: Animation,
        rate_func: RateFunction,
        **kwargs: Any,
    ) -> None:
        super().__init__(animation, rate_func=rate_func, **kwargs)


class Linear(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.linear, **kwargs)


class Reverse(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, lambda t: 1 - t, **kwargs)


class Smooth(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.smooth, **kwargs)


class SmoothStep(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.smoothstep, **kwargs)


class SmootherStep(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.smootherstep, **kwargs)


class SmoothererStep(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.smoothererstep, **kwargs)


class RushInto(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.rush_into, **kwargs)


class RushFrom(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.rush_from, **kwargs)


class SlowInto(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.slow_into, **kwargs)


class DoubleSmooth(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.double_smooth, **kwargs)


class RunningStart(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.running_start, **kwargs)


class Lingering(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.lingering, **kwargs)


class ExponentialDecay(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.exponential_decay, **kwargs)


class EaseInSine(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.ease_in_sine, **kwargs)


class EaseOutSine(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.ease_out_sine, **kwargs)


class EaseInOutSine(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.ease_in_out_sine, **kwargs)


class EaseInQuad(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.ease_in_quad, **kwargs)


class EaseOutQuad(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.ease_out_quad, **kwargs)


class EaseInOutQuad(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.ease_in_out_quad, **kwargs)


class EaseInCubic(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.ease_in_cubic, **kwargs)


class EaseOutCubic(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.ease_out_cubic, **kwargs)


class EaseInOutCubic(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.ease_in_out_cubic, **kwargs)


class EaseInQuart(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.ease_in_quart, **kwargs)


class EaseOutQuart(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.ease_out_quart, **kwargs)


class EaseInOutQuart(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.ease_in_out_quart, **kwargs)


class EaseInQuint(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.ease_in_quint, **kwargs)


class EaseOutQuint(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.ease_out_quint, **kwargs)


class EaseInOutQuint(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.ease_in_out_quint, **kwargs)


class EaseOnExpo(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.ease_in_expo, **kwargs)


class EaseOutExpo(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.ease_out_expo, **kwargs)


class EaseInOutExpo(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.ease_in_out_expo, **kwargs)


class EaseInCirc(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.ease_in_circ, **kwargs)


class EaseOutCirc(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.ease_out_circ, **kwargs)


class EaseInOutCirc(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.ease_in_out_circ, **kwargs)


class EaseInBack(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.ease_in_back, **kwargs)


class EaseOutBack(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.ease_out_back, **kwargs)


class EaseInOutBack(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.ease_in_out_back, **kwargs)


class EaseInElastic(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.ease_in_elastic, **kwargs)


class EaseOutElastic(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.ease_out_elastic, **kwargs)


class EaseInOutElastic(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.ease_in_out_elastic, **kwargs)


class EaseInBounce(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.ease_in_bounce, **kwargs)


class EaseOutBounce(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.ease_out_bounce, **kwargs)


class EaseInOutBounce(ApplyRate):
    def __init__(self, animation: Animation, **kwargs: Any) -> None:
        super().__init__(animation, rate_functions.ease_in_out_bounce, **kwargs)
