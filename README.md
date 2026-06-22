# Manim-Combinable

Makes manim animations combinable. 
* [Progress Tracker](./docs/progress_tracker.md)
* [Examples](./docs/examples.md)

## Usage
```py
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
```

https://github.com/user-attachments/assets/5feba7c7-13e6-46e2-b470-fcf77995ce37

## How it works

The animations are combinable due to the following behavior restrictions:
* Only necessary properties are changed.
* The changes behave like updaters.

## API Changes

* All animation constructors are drop-in-replacements.
    * if not: please create an issue
    * see [Comparisons](./docs/comparisons.md)
* Fields and method can differ to Manim's non-combinable animations.

## Nested Mobjects

When working with nested mobjects, it is sometimes necessary to use the `Flatten` utility:
```py
class FlattenExample(Scene):
    def construct(self):
        tex_1 = Tex("Hello", font_size=128).set_color_by_gradient(RED, GREEN, BLUE)
        tex_2 = tex_1.copy()
        self.add(VGroup(tex_1, tex_2).arrange(DOWN))
        self.wait()

        self.play(
            SetColor(tex_1, GREY),
            Flatten(tex_2, lambda l: SetColor(l, GREY)),
        )
```
https://github.com/user-attachments/assets/6b2ceae8-91ae-4c4b-b57c-317c8e0c5db4

## Stuttering Movement

When you transform a mobject while translating it, the movement sometimes stutters. That stems from the fact that (most) translations rely on the objects center, which is influenced by the objects bounding box.


One way to circumvent this is adding a wrapper (e.g. a circle or square) around the object, on which you then apply the translation.
