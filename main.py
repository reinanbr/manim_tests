from manim import *

class ShowWrite(Scene):
    def construct(self):
        text1 = Text("Hello", font_size=144)
        self.play(Write(text1))
        self.wait()
        self.play(FadeOut(text1))
        self.play(Write( MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots"
        )
))
        self.wait()
        
        
        

class Eqq(Scene):
    def construct(self):
        eq2 = MathTex("{{a}}^2", "+", "{{b}}^2", "=", "{{c}}^2")
        eq3 = MathTex("{{a}}^2", "=", "{{c}}^2", "-", "{{b}}^2")

        self.add(eq2)
        self.wait(0.5)
        self.wait(0.5)
        self.play(TransformMatching(eq2, eq3))
        self.wait(0.5)



class Eq(Scene):
    def construct(self):
        equation_1 = MathTex("w", "\\times","v", "=", "1")
        equation_1.shift(UP*2).scale(2)
        equation_2 = MathTex("v", "=", "w^{-1}")
        equation_2.scale(2)
        equation_3 = MathTex("w", "\\times","w^{-1}", "=", "1")
        equation_3.shift(UP*2).scale(2)

        self.play(Write(equation_1), Write(equation_2))
        self.wait(2)
        self.play(FadeOut(equation_1[2]))

        self.play(
            TransformMatchingShapes(
                VGroup(equation_1[0:2], equation_1[3:], equation_2[2].copy()),
                equation_3,
            )
        )