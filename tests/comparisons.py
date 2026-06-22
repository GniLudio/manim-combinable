from manim import *

if True:
    from manim_combinable import *


class ChangeDecimalToValueExample(Scene):
    def construct(self) -> None:
        number = DecimalNumber(0)
        self.add(number)
        self.play(ChangeDecimalToValue(number, 10, run_time=3))
        self.wait()


class ChangingDecimalExample(Scene):
    def construct(self) -> None:
        number = DecimalNumber(0)
        self.add(number)
        self.play(ChangingDecimal(number, lambda a: 5 * a, run_time=3))
        self.wait()


class FadeInExample(Scene):
    def construct(self) -> None:
        dot = Dot(UP * 2 + LEFT)
        self.add(dot)
        tex = Tex("FadeIn with ", "shift ", r" or target\_position", " and scale").scale(1)
        animations = [
            FadeIn(tex[0]),
            FadeIn(tex[1], shift=DOWN),
            FadeIn(tex[2], target_position=dot),
            FadeIn(tex[3], scale=1.5),
        ]
        self.play(AnimationGroup(*animations, lag_ratio=0.5))


class FadeOutExample(Scene):
    def construct(self) -> None:
        dot = Dot(UP * 2 + LEFT)
        self.add(dot)
        tex = Tex("FadeOut with ", "shift ", r" or target\_position", " and scale").scale(1)
        animations = [
            FadeOut(tex[0]),
            FadeOut(tex[1], shift=DOWN),
            FadeOut(tex[2], target_position=dot),
            FadeOut(tex[3], scale=0.5),
        ]
        self.play(AnimationGroup(*animations, lag_ratio=0.5))


class FadeToColorExample(Scene):
    def construct(self) -> None:
        self.play(FadeToColor(Text("Hello World!"), color=RED))


class UsingIndicate(Scene):
    def construct(self) -> None:
        tex = Tex("Indicate").scale(3)
        self.play(Indicate(tex))
        self.wait()


class MoveAlongPathExample(Scene):
    def construct(self) -> None:
        d1 = Dot().set_color(ORANGE)
        l1 = Line(LEFT, RIGHT)
        l2 = VMobject()
        self.add(d1, l1, l2)
        l2.add_updater(lambda x: x.become(Line(LEFT, d1.get_center()).set_color(ORANGE)))
        self.play(MoveAlongPath(d1, l1), rate_func=linear)


class UsingRotate(Scene):
    def construct(self) -> None:
        self.play(
            Rotate(
                Square(side_length=0.5).shift(UP * 2),
                angle=2 * PI,
                about_point=ORIGIN,
                rate_func=linear,
            ),
            Rotate(Square(side_length=0.5), angle=2 * PI, rate_func=linear),
        )


class ScaleInPlaceExample(Scene):
    def construct(self) -> None:
        self.play(ScaleInPlace(Text("Hello World!"), 2))


class ShrinkToCenterExample(Scene):
    def construct(self) -> None:
        self.play(ShrinkToCenter(Text("Hello World!")))
