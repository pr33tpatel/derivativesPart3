import numpy as np
from manim import *


class RecapCalc1(Scene):
    def construct(self):
        title = Text("Quick recap: derivatives in 2D", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))

        ax = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 5, 1],
            x_length=8,
            y_length=5,
            axis_config={"include_numbers": False},
        )
        labels = ax.get_axis_labels(Tex("x"), Tex("y"))

        graph = ax.plot(lambda x: 0.25 * (x - 2) ** 2 + 1, x_range=[0, 4.5], color=BLUE)
        graph_label = ax.get_graph_label(graph, MathTex("y=f(x)"), x_val=4, direction=UR)

        self.play(Create(ax), Write(labels))
        self.play(Create(graph), FadeIn(graph_label))

        x0 = 1.8
        h_tracker = ValueTracker(1.4)

        def f(x):
            return 0.25 * (x - 2) ** 2 + 1

        p1 = always_redraw(lambda: Dot(ax.c2p(x0, f(x0)), color=YELLOW))
        p2 = always_redraw(lambda: Dot(ax.c2p(x0 + h_tracker.get_value(), f(x0 + h_tracker.get_value())), color=BLUE))

        secant = always_redraw(
            lambda: ax.get_secant_slope_group(
                x=x0,
                graph=graph,
                dx=h_tracker.get_value(),
                dx_line_color=GRAY,
                dy_line_color=GRAY,
                secant_line_color=BLUE,
                secant_line_length=4,
            )
        )

        tangent = ax.get_secant_slope_group(
            x=x0,
            graph=graph,
            dx=0.001,
            dx_line_color=GRAY,
            dy_line_color=GRAY,
            secant_line_color=PURPLE,
            secant_line_length=4,
        )

        point_label = MathTex("A").next_to(p1, DOWN)
        h_label = always_redraw(
            lambda: (
                MathTex("h")
                .scale(0.8)
                .next_to(Line(ax.c2p(x0, f(x0)), ax.c2p(x0 + h_tracker.get_value(), f(x0 + h_tracker.get_value()))).get_center(), DOWN)
            )
        )

        recap_text = Tex(r"Derivative = slope at a point", font_size=34)
        recap_text.to_edge(DOWN)

        self.play(FadeIn(p1), Write(point_label))
        self.play(Write(recap_text))

        self.play(FadeIn(p2), Create(secant), FadeIn(h_label))
        self.wait(0.5)

        self.play(h_tracker.animate.set_value(0.5), run_time=2)
        self.play(h_tracker.animate.set_value(0.15), run_time=2)

        tangent_label = Tex(r"As $h \to 0$, secant $\to$ tangent", font_size=32)
        tangent_label.to_edge(DOWN)

        self.play(Transform(secant, tangent), Transform(recap_text, tangent_label), FadeOut(p2), FadeOut(h_label), run_time=2)
        self.wait(1)

        next_text = Tex(r"Now let's ask the same question in 3D.", font_size=34)
        next_text.to_edge(DOWN)
        self.play(Transform(recap_text, next_text))
        self.wait(1.5)
