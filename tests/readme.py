from manim import *

from manim_combinable import *


class ScaleRotateAndFadeToColor(Scene):
    def construct(self) -> None:
        text = Text("Hello", font_size=92)
        self.play(
            ScaleInPlace(text, 3, rate_func=there_and_back),
            Rotate(text, 2 * PI, rate_func=there_and_back),
            Succession(
                FadeToColor(text, RED),
                FadeToColor(text, GREEN),
                FadeOut(text, shift=4 * UP),
            ),
            run_time=10,
        )


class FlattenExample(Scene):
    def construct(self) -> None:
        tex_1 = Tex("Hello", font_size=128).set_color_by_gradient(RED, GREEN, BLUE)
        tex_2 = tex_1.copy()
        self.add(VGroup(tex_1, tex_2).arrange(DOWN))
        self.wait()

        self.play(
            SetColor(tex_1, GREY),
            Flatten(tex_2, lambda l: SetColor(l, GREY)),
        )
