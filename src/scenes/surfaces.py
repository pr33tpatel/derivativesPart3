import numpy as np
from manim import *


class SurfaceIntro(ThreeDScene):
    def construct(self):
        title = Text("From curves to surfaces", font_size=36)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))

        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-1, 4, 1],
            x_length=6,
            y_length=6,
            z_length=4,
        )

        labels = axes.get_axis_labels(Tex("x"), Tex("y"), Tex("z"))

        surface = Surface(
            lambda u, v: axes.c2p(u, v, 0.25 * (u**2 + v**2)),
            u_range=[-2.5, 2.5],
            v_range=[-2.5, 2.5],
            resolution=(24, 24),
            fill_opacity=0.8,
            checkerboard_colors=[BLUE_D, BLUE_E],
        )

        self.set_camera_orientation(phi=65 * DEGREES, theta=-45 * DEGREES)

        self.play(Create(axes), FadeIn(labels))
        self.play(Create(surface), run_time=2)
        self.begin_ambient_camera_rotation(rate=0.08)

        point_coords = np.array([1.2, 0.8])
        z_val = 0.25 * (point_coords[0] ** 2 + point_coords[1] ** 2)

        point = Dot3D(axes.c2p(point_coords[0], point_coords[1], z_val), color=YELLOW)
        vertical = DashedLine(axes.c2p(point_coords[0], point_coords[1], 0), axes.c2p(point_coords[0], point_coords[1], z_val), color=GRAY)

        question = Tex(r"What does slope mean here?", font_size=34)
        question.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(question)

        arrow_x = Arrow3D(
            start=axes.c2p(point_coords[0], point_coords[1], z_val), end=axes.c2p(point_coords[0] + 0.9, point_coords[1], z_val), color=RED
        )

        arrow_y = Arrow3D(
            start=axes.c2p(point_coords[0], point_coords[1], z_val), end=axes.c2p(point_coords[0], point_coords[1] + 0.9, z_val), color=GREEN
        )

        self.play(FadeIn(point), Create(vertical))
        self.play(Write(question))
        self.play(Create(arrow_x), Create(arrow_y))
        self.wait(2)
