from manim import *

if True:
    from manim_combinable import *


class DefaultAddScene(Scene):
    def construct(self) -> None:
        text_1 = Text("I was added with Add!")
        text_2 = Text("Me too!")
        text_3 = Text("And me!")
        texts = VGroup(text_1, text_2, text_3).arrange(DOWN)
        rect = SurroundingRectangle(texts, buff=0.5)

        self.play(
            Create(rect, run_time=3.0),
            Succession(
                Wait(1.0),
                # You can Add a Mobject in the middle of an animation...
                Add(text_1),
                Wait(1.0),
                # ...or multiple Mobjects at once!
                Add(text_2, text_3),
            ),
        )
        self.wait()


class BlinkingExample(Scene):
    def construct(self) -> None:
        text = Text("Blinking").scale(1.5)
        self.add(text)
        self.play(Blink(text, blinks=3))


class ChangeDecimalToValueExample(Scene):
    def construct(self) -> None:
        number = DecimalNumber(0)
        self.add(number)
        self.play(ChangeDecimalToValue(number, 10, run_time=3))
        self.wait()


class SpeedModifierExample(Scene):
    def construct(self) -> None:
        a = Dot().shift(LEFT * 4)
        b = Dot().shift(RIGHT * 4)
        self.add(a, b)
        self.play(
            ChangeSpeed(
                AnimationGroup(
                    a.animate(run_time=1).shift(RIGHT * 8),
                    b.animate(run_time=1).shift(LEFT * 8),
                ),
                speedinfo={0.3: 1, 0.4: 0.1, 0.6: 0.1, 1: 1},
                rate_func=linear,
            )
        )


class SpeedModifierUpdaterExample(Scene):
    def construct(self) -> None:
        a = Dot().shift(LEFT * 4)
        self.add(a)

        ChangeSpeed.add_updater(a, lambda x, dt: x.shift(RIGHT * 4 * dt))
        self.play(
            ChangeSpeed(
                Wait(2),
                speedinfo={0.4: 1, 0.5: 0.2, 0.8: 0.2, 1: 1},
                affects_speed_updaters=True,
            )
        )


class SpeedModifierUpdaterExample2(Scene):
    def construct(self) -> None:
        a = Dot().shift(LEFT * 4)
        self.add(a)

        ChangeSpeed.add_updater(a, lambda x, dt: x.shift(RIGHT * 4 * dt))
        self.wait()
        self.play(
            ChangeSpeed(
                Wait(),
                speedinfo={1: 0},
                affects_speed_updaters=True,
            )
        )


class ChangingDecimalExample(Scene):
    def construct(self) -> None:
        number = DecimalNumber(0)
        self.add(number)
        self.play(ChangingDecimal(number, lambda a: 5 * a, run_time=3))
        self.wait()


class UsingCircumscribe(Scene):
    def construct(self) -> None:
        lbl = Tex(r"Circum-\\scribe").scale(2)
        self.add(lbl)
        self.play(Circumscribe(lbl))
        self.play(Circumscribe(lbl, Circle))
        self.play(Circumscribe(lbl, fade_out=True))
        self.play(Circumscribe(lbl, time_width=2))
        self.play(Circumscribe(lbl, Circle, True))


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


class UsingFlash(Scene):
    def construct(self) -> None:
        dot = Dot(color=PURE_YELLOW).shift(DOWN)
        self.add(Tex("Flash the dot below:"), dot)
        self.play(Flash(dot))
        self.wait()


class FlashOnCircle(Scene):
    def construct(self) -> None:
        radius = 2
        circle = Circle(radius)
        self.add(circle)
        self.play(
            Flash(
                circle,
                line_length=1,
                num_lines=30,
                color=RED,
                flash_radius=radius + SMALL_BUFF,
                time_width=0.3,
                run_time=2,
                rate_func=rush_from,
            )
        )


class UsingFocusOn(Scene):
    def construct(self) -> None:
        dot = Dot(color=PURE_YELLOW).shift(DOWN)
        self.add(Tex("Focusing on the dot below:"), dot)
        self.play(FocusOn(dot))
        self.wait()


class UsingIndicate(Scene):
    def construct(self) -> None:
        tex = Tex("Indicate").scale(3)
        self.play(Indicate(tex))
        self.wait()


class LaggedStartExample(Scene):
    def construct(self) -> None:
        title = Text("lag_ratio = 0.25").to_edge(UP)

        dot1 = Dot(point=LEFT * 2 + UP, radius=0.16)
        dot2 = Dot(point=LEFT * 2, radius=0.16)
        dot3 = Dot(point=LEFT * 2 + DOWN, radius=0.16)
        line_25 = DashedLine(start=LEFT + UP * 2, end=LEFT + DOWN * 2, color=RED)
        label = Text("25%", font_size=24).next_to(line_25, UP)
        self.add(title, dot1, dot2, dot3, line_25, label)

        self.play(
            LaggedStart(
                dot1.animate.shift(RIGHT * 4),
                dot2.animate.shift(RIGHT * 4),
                dot3.animate.shift(RIGHT * 4),
                lag_ratio=0.25,
                run_time=4,
            )
        )


class LaggedStartMapExample(Scene):
    def construct(self) -> None:
        title = Tex("LaggedStartMap").to_edge(UP, buff=LARGE_BUFF)
        dots = VGroup(*[Dot(radius=0.16) for _ in range(35)]).arrange_in_grid(rows=5, cols=7, buff=MED_LARGE_BUFF)
        self.add(dots, title)

        # Animate yellow ripple effect
        for mob in dots, title:
            self.play(
                LaggedStartMap(
                    ApplyMethod,
                    mob,
                    lambda m: (m.set_color, YELLOW),
                    lag_ratio=0.1,
                    rate_func=there_and_back,
                    run_time=2,
                )
            )


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


class TimeWidthValues(Scene):
    def construct(self) -> None:
        p = RegularPolygon(5, color=DARK_GRAY, stroke_width=6).scale(3)
        lbl = VMobject()
        self.add(p, lbl)
        p = p.copy().set_color(BLUE)
        for time_width in [0.2, 0.5, 1, 2]:
            lbl.become(Tex(rf"\texttt{{time\_width={{{{{time_width:.1f}}}}}}}"))
            self.play(ShowPassingFlash(p.copy().set_color(BLUE), run_time=2, time_width=time_width))


class ShrinkToCenterExample(Scene):
    def construct(self) -> None:
        self.play(ShrinkToCenter(Text("Hello World!")))


class SuccessionExample(Scene):
    def construct(self) -> None:
        dot1 = Dot(point=LEFT * 2 + UP * 2, radius=0.16, color=BLUE)
        dot2 = Dot(point=LEFT * 2 + DOWN * 2, radius=0.16, color=MAROON)
        dot3 = Dot(point=RIGHT * 2 + DOWN * 2, radius=0.16, color=GREEN)
        dot4 = Dot(point=RIGHT * 2 + UP * 2, radius=0.16, color=YELLOW)
        self.add(dot1, dot2, dot3, dot4)

        self.play(
            Succession(
                dot1.animate.move_to(dot2),
                dot2.animate.move_to(dot3),
                dot3.animate.move_to(dot4),
                dot4.animate.move_to(dot1),
            )
        )
