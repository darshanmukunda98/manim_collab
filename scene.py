from manim import *
class MovingFrameBox(Scene):
    def construct(self):
        title = MathTex(
            "Security \\",  "Basics", color=BLUE
        )

        second_line = MathTex(
            "A \\ short \\ series,"
        )

        third_line = MathTex(
            "To \\ deliver \\ intuition"
        )

        fourth_line = MathTex(
            "Gives \\ you \\ a \\ little \\ understanding \\ on" )

        how_part = MathTex("How \\")
        identity = MathTex("Internet~Security \\",color=RED)
        end_part = MathTex("works")

        how_part.next_to(identity, LEFT)
        end_part.next_to(identity, RIGHT)
        self.wait(1)

        for blob in [title, second_line, third_line, fourth_line]:
            self.play(Write(blob))
            self.wait(1)
            self.remove(blob)

        self.play(Write(how_part))
        self.play(Write(identity))
        self.play(Write(end_part))

        framebox1 = SurroundingRectangle(how_part, buff = .1)
        framebox2 = SurroundingRectangle(identity, buff = .1)
        framebox3 = SurroundingRectangle(end_part, buff = .1)

        self.play(
            ShowCreation(framebox1),
        )
        self.wait()
        self.play(
            ReplacementTransform(framebox1,framebox2),
        )
        self.wait()
        self.play(
             ReplacementTransform(framebox2,framebox3),
        )
        self.wait()

