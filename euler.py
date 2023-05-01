from manim import *





class Eqq(Scene):
    def construct(self):
        eq_taylor = MathTex(r"f(x) = f(a) + f(a)(x-a) + f(a) \frac{(x-a)^{2}}{2!} + \cdots + f^n(a) \frac{(x-a)^n}{n!} + \cdots",font_size=40)
        eq_taylor[1].set_color(YELLOW)
        ## FIRST FRAME
        eq2 = MathTex(r"e^{i\pi}+1=0", substrings_to_isolate=["e",r'^{i\pi}'],font_size=120)
        eq2.set_color_by_tex('e',RED)
        eq2.set_color_by_tex(r'^{i\pi}',YELLOW)
        
        text_apresent = MarkupText(f'Provando a identidade de <span fgcolor="{RED}">Euler</span>:',color=WHITE).to_edge(UP)
        
        self.play(Write(text_apresent))
        self.wait(.5)
        self.play(Write(eq2))

        self.wait(2)
      
        self.play(FadeOut(eq2))
        
        
        
        ## SECOND FRAME
        text_apresent_taylor = MarkupText(f'Pela série de <span fgcolor="{RED}">Taylor</span>, temos',color=WHITE).to_edge(UP)
        self.play(TransformMatchingShapes(text_apresent,text_apresent_taylor))
        self.wait(0.5)
        
    
        
        self.play(Write(eq_taylor))
        self.wait()
        tex_a = Tex("com $a=0$, temos").to_edge(UP)
        self.play(TransformMatchingShapes(text_apresent_taylor,tex_a))
        self.wait()
        
        eq_mac = MathTex(r"f(x)=f(0)+f'(0)(x)+f''(0)\frac{(x)^{2}}{2!}+\dots+f^n(0)\frac{(x)^n}{n!}+\dots",font_size=40)
    
        self.play(ReplacementTransform(eq_taylor,eq_mac))
        self.wait()
        self.play(FadeOut(tex_a))
        self.wait()
        
        

 
        
        
        
       
        
        


