from manim import *





class Eqq(Scene):
    def construct(self):
       # eq_taylor[8].set_color(YELLOW)
        ## FIRST FRAME
        eq2 = MathTex(r"e^{i\pi}+1=0", substrings_to_isolate=["e",r'^{i\pi}'],font_size=120)
        eq2.set_color_by_tex('e',RED)
        eq2.set_color_by_tex(r'^{i\pi}',YELLOW)
        
        text_apresent = MarkupText(f'Provando a identidade de <span fgcolor="{RED}">Euler</span>:',color=WHITE).to_edge(UP)
        
        author = MarkupText(f"By <span fgcolor='{RED}'>@gpftc_</span>, in <span fgcolor='{BLUE}'>python3</span><span fgcolor='{PURPLE}'>/manim</span>",color=WHITE,font_size=20).to_edge(DOWN)
        # author[1].set_color(RED)
        # author[3].set_color(BLUE)
        # author[4].set_color(PURPLE)
        
        self.play(Write(text_apresent))
        self.wait(.5)
        self.play(Write(eq2),Write(author))
        

        self.wait(2)
      
        self.play(FadeOut(eq2))
        
        
        
        
        ## SECOND FRAME
        text_apresent_taylor = MarkupText(f'Pela série de <span fgcolor="{RED}">Taylor</span>, temos',color=WHITE).to_edge(UP)
        
        self.play(TransformMatchingShapes(text_apresent,text_apresent_taylor))
        self.wait(0.5)
        
        
        eq_taylor = MathTex(r"{{f(x)}} = f(a) + f'(a)({{x}}-a) +  \frac{f''(a)}{2!}({{x}}-a)^{2} + \dots + \frac{f^n(a)}{n!} ({{x}}-a)^n + \dots",font_size=40)
        eq_taylor[0].set_color(RED)
        eq_taylor[0][2].set_color(YELLOW)
        eq_taylor[2].set_color(YELLOW)
        eq_taylor[4].set_color(YELLOW)
        eq_taylor[6].set_color(YELLOW)
        
        self.play(Write(eq_taylor))
        self.wait()
        
        
        tex_a = Tex("com $a=0$, temos").to_edge(UP)
        
        self.play(ReplacementTransform(text_apresent_taylor,tex_a))
        self.wait()
        
        
        eq_mac = MathTex(r"{{f(x)}} = f(0) + f'(0)({{x}}) +  \frac{f''(0)}{2!}({{x}})^{2} + \dots + \frac{f^n(0)}{n!} ({{x}})^n + \dots",font_size=40)
        eq_mac[0].set_color(RED)
        eq_mac[0][2].set_color(YELLOW)
        eq_mac[2].set_color(YELLOW)
        eq_mac[4].set_color(YELLOW)
        eq_mac[6].set_color(YELLOW)
        
        self.play(ReplacementTransform(eq_taylor,eq_mac))
        self.wait(2)
        
        
        tex_sen = Tex("aplicando em {{$sen(x)$}}, fica").to_edge(UP)
        tex_sen[1].set_color(GREEN)
        tex_sen[1][4].set_color(YELLOW)
        
        self.play(ReplacementTransform(tex_a,tex_sen))
        self.wait()
        
        
        eq_sin = MathTex(r"{{sen(x)}} = sen(0) + sen'(0){{x}} + \frac{sen''(0)}{2!}{{x}}^2 + \dots + \frac{sen^n(0)}{n!}{{x}}^n+ \dots",font_size=40)
        eq_sin[0].set_color(GREEN)
        eq_sin[0][4].set_color(YELLOW)
        eq_sin[2].set_color(YELLOW)
        eq_sin[4].set_color(YELLOW)
        eq_sin[6].set_color(YELLOW)
        
        self.play(ReplacementTransform(eq_mac,eq_sin))
        self.wait(2)
        
        
        eq_sin_1 = MathTex(r"{{sen(x)}} = sen(0) + cos(0){{x}} - \frac{sen(0)}{2!}{{x}}^{2} - \frac{cos(0)}{3!}{{x}}^{3} + \frac{sen(0)}{4!}{{x}}^{4}  +\frac{cos(0)}{5!}{{x}}^{5} + \dots",font_size=35)
        eq_sin_1[0].set_color(GREEN)
        eq_sin_1[0][4].set_color(YELLOW)
        eq_sin_1[2].set_color(YELLOW)
        eq_sin_1[4].set_color(YELLOW)
        eq_sin_1[6].set_color(YELLOW)
        eq_sin_1[8].set_color(YELLOW)
        eq_sin_1[10].set_color(YELLOW)
        
        self.play(ReplacementTransform(eq_sin,eq_sin_1))
        self.wait(2)
        
        
        eq_sin_2 = MathTex(r"{{sen(x)}} = 0 + {{x}} - \frac{1}{3!}{{x}}^{3} + 0 + \frac{1}{5!}{{x}}^{5} + \dots",font_size=45)
        eq_sin_2[0].set_color(GREEN)
        eq_sin_2[0][4].set_color(YELLOW)
        eq_sin_2[2].set_color(YELLOW)
        eq_sin_2[4].set_color(YELLOW)
        eq_sin_2[6].set_color(YELLOW)
        
        self.play(ReplacementTransform(eq_sin_1,eq_sin_2))
        self.wait(2)
        
        
        eq_sin_3 = MathTex(r"{{sen(x)}} =  {{x}} - \frac{1}{3!}{{x}}^3 + \frac{1}{5!}{{x}}^{5} - \frac{1}{7!}{{x}}^7 + \frac{1}{9!}{{x}}^9 - \dots + \frac{(-1)^{n}}{(2n+1)!}{{x}}^{2n+1}+\dots",font_size=35)
        eq_sin_3[0].set_color(GREEN)
        eq_sin_3[0][4].set_color(YELLOW)
        eq_sin_3[2].set_color(YELLOW)
        eq_sin_3[4].set_color(YELLOW)
        eq_sin_3[6].set_color(YELLOW)
        eq_sin_3[8].set_color(YELLOW)
        eq_sin_3[10].set_color(YELLOW)
        eq_sin_3[12].set_color(YELLOW)
        
        self.play(ReplacementTransform(eq_sin_2,eq_sin_3))
        self.wait(2)
        
        tex_mem_sen = Tex("Memorize isso na sua mente!").to_edge(UP)
        tex_mem_sen.set_color(YELLOW)
         
        self.play(ReplacementTransform(tex_sen,tex_mem_sen))
        self.wait(2)
        
        
        
        
        
        # THIRD FRAME 
        tex_cos = Tex("Agora, aplicando a série de {{Taylor}} com $a=0$ em {{$cos(x)$}}").to_edge(UP)
        tex_cos[1].set_color(RED)
        tex_cos[3].set_color(ORANGE)
        
        self.play(ReplacementTransform(tex_mem_sen,tex_cos))
        self.wait(2)
        
        
        eq_cos = MathTex(r"{{cos(x)}} = cos(0) + cos'(0){{x}} + \frac{cos''(0)}{2!}{{x}}^{2} + \dots + \frac{cos^{n}(0)}{n!}{{x}}^{n} + \dots",font_size=40)
        eq_cos[0].set_color(ORANGE)
        eq_cos[0][4].set_color(YELLOW)
        eq_cos[2].set_color(YELLOW)
        eq_cos[4].set_color(YELLOW)
        eq_cos[6].set_color(YELLOW)
        
        self.play(ReplacementTransform(eq_sin_3,eq_cos))
        self.wait(2)
        
        
        eq_cos_1 = MathTex(r"{{cos(x)}} = cos(0) - sen(0){{x}} - \frac{cos(0)}{2!}{{x}}^{2} + \frac{sen(0)}{3!}{{x}}^{3} + \frac{cos(0)}{4!}{{x}}^{4} -\dots",font_size=40)
        eq_cos_1[0].set_color(ORANGE)
        eq_cos_1[0][4].set_color(YELLOW)
        eq_cos_1[2].set_color(YELLOW)
        eq_cos_1[4].set_color(YELLOW)
        eq_cos_1[6].set_color(YELLOW)
        eq_cos_1[8].set_color(YELLOW)
        
        self.play(ReplacementTransform(eq_cos,eq_cos_1))
        self.wait(2)
        
        
        eq_cos_2 = MathTex(r"{{cos(x)}} = 1 - 0 - \frac{1}{2!}{{x}}^{2} + 0 + \frac{1}{4!}{{x}}^{4} - \dots")
        eq_cos_2[0].set_color(ORANGE)
        eq_cos_2[0][4].set_color(YELLOW)
        eq_cos_2[2].set_color(YELLOW)
        eq_cos_2[4].set_color(YELLOW)
        
        self.play(ReplacementTransform(eq_cos_1,eq_cos_2))
        self.wait(2)
        
        
        eq_cos_3 = MathTex(r"{{cos(x)}} = 1 - \frac{1}{2!}{{x}}^{2} + \frac{1}{4!}{{x}}^{4} - \frac{1}{6!}{{x}}^{6} + \frac{1}{8!}{{x}}^{8} - \dots + \frac{(-1)^{n}}{(2n)!}{{x}}^{2n} + \dots",font_size=35)
        eq_cos_3[0].set_color(ORANGE)
        eq_cos_3[0][4].set_color(YELLOW)
        eq_cos_3[2].set_color(YELLOW)
        eq_cos_3[4].set_color(YELLOW)
        eq_cos_3[6].set_color(YELLOW)
        eq_cos_3[8].set_color(YELLOW)
        eq_cos_3[10].set_color(YELLOW)
        
        self.play(ReplacementTransform(eq_cos_2,eq_cos_3))
        self.wait(2)
        
        tex_mem_cos = Tex("Memorize isso na sua mente!").to_edge(UP)
        tex_mem_cos.set_color(YELLOW)
        self.play(ReplacementTransform(tex_cos,tex_mem_cos))
        self.wait(2)
        
        
        
        
        
        #  FOURTH FRAME
        tex_euler = Tex("Agora, em {{$exp(x)$}}").to_edge(UP)
        tex_euler[1].set_color(RED)
        tex_euler[1][4].set_color(YELLOW)
        self.play(ReplacementTransform(tex_mem_cos,tex_euler))
        
        
        eq_euler = MathTex(r"{{exp(x)}} = exp(0) + exp'(0){{x}} + \frac{exp''(0)}{2!}{{x}}^{2}+\frac{exp'''(0)}{3!}{{x}}^{3} + \dots + \frac{exp^n(0)}{n!}{{x}}^{n} + \dots",font_size=30)
        eq_euler[0].set_color(RED)
        eq_euler[0][4].set_color(YELLOW)
        eq_euler[2].set_color(YELLOW)
        eq_euler[6].set_color(YELLOW)
        eq_euler[8].set_color(YELLOW)
        #eq_euler[10].set_color(YELLOW)
        
        self.play(ReplacementTransform(eq_cos_3,eq_euler))
        self.wait(2)
        
        
        eq_euler1 = MathTex(r"{{exp(x)}} = exp(0) + exp(0){{x}} + \frac{exp(0)}{2!}{{x}}^{2}+\frac{exp(0)}{3!}{{x}}^{3} + \dots + \frac{exp(0)}{n!}{{x}}^{n} + \dots",font_size=35)
        eq_euler1[0].set_color(RED)
        eq_euler1[0][4].set_color(YELLOW)
        eq_euler1[2].set_color(YELLOW)
        eq_euler1[6].set_color(YELLOW)
        eq_euler1[8].set_color(YELLOW)
        
        self.play(ReplacementTransform(eq_euler,eq_euler1))
        self.wait(2)
        
        
        eq_euler2 = MathTex(r"{{exp(x)}} = 1 + {{x}} + \frac{1}{2!}{{x}}^{2}+\frac{1}{3!}{{x}}^{3} + \dots + \frac{1}{n!}{{x}}^{n} + \dots",font_size=35)
        eq_euler2[0].set_color(RED)
        eq_euler2[0][4].set_color(YELLOW)
        eq_euler2[2].set_color(YELLOW)
        eq_euler2[6].set_color(YELLOW)
        
        self.play(ReplacementTransform(eq_euler1,eq_euler2))
        self.wait(2)
        
        
        tex_mem_euler = Tex("Memorize isso na sua mente!").to_edge(UP)
        tex_mem_euler.set_color(YELLOW)
        self.play(ReplacementTransform(tex_euler,tex_mem_euler))
        self.wait(2)
        
        
        
        
        ## LAST FRAME
        self.play(FadeOut(eq_euler2))
        tex_i = Tex(r"com isso tudo, podemos afirmar que {{exp(xi)}} é").to_edge(UP)
        tex_i[1].set_color(RED)
        tex_i[1][4:6].set_color(YELLOW)
        
        
        eq_ix = MathTex(r"{{e}}^{ {{ix}} }= 1 + {{ix}} + \frac{1}{2!}({{xi}})^{2} + \frac{1}{3!}({{xi}})^{3} + \frac{1}{4!}({{xi}})^{4} + \frac{1}{5!}({{xi}})^{5} + \frac{1}{6!}({{xi}})^{6} + \frac{1}{7!}({{xi}})^{7} + \dots",font_size=30)
        eq_ix[0].set_color(RED)
        eq_ix[2].set_color(YELLOW)
        eq_ix[4].set_color(YELLOW)
        eq_ix[6].set_color(YELLOW)
        eq_ix[8].set_color(YELLOW)
        eq_ix[10].set_color(YELLOW)
        eq_ix[12].set_color(YELLOW)
        eq_ix[14].set_color(YELLOW)
        eq_ix[16].set_color(YELLOW)
        
        self.play(ReplacementTransform(tex_mem_euler,tex_i))
        self.play(Write(eq_ix))
        self.wait(2)
        
        
        eq_ix1 = MathTex(r"{{e}}^{ {{ix}} }= 1 + {{ix}} - \frac{1}{2!}{{x}}^{2} - \frac{1}{3!}{{x}}^{3}{{i}} + \frac{1}{4!}{{x}}^{4} + \frac{1}{5!}{{x}}^{5}{{i}} - \frac{1}{6!}{{x}}^{6} - \frac{1}{7!}{{x}}^{7}{{i}} + \dots",font_size=30)
        eq_ix1[0].set_color(RED)
        eq_ix1[2].set_color(YELLOW)
        eq_ix1[4].set_color(YELLOW)
        eq_ix1[6].set_color(YELLOW)
        eq_ix1[8].set_color(YELLOW)
        eq_ix1[10].set_color(YELLOW)
        eq_ix1[12].set_color(YELLOW)
        eq_ix1[14].set_color(YELLOW)
        eq_ix1[16].set_color(YELLOW)
        eq_ix1[18].set_color(YELLOW)
        eq_ix1[20].set_color(YELLOW)
        eq_ix1[22].set_color(YELLOW)
        
        self.play(TransformMatchingShapes(eq_ix,eq_ix1))
        self.wait(2)
        
        
        eq_ix2 = MathTex(r"{{e}}^{ {{ix}} } =  \left( 1 - \frac{1}{2!}{{x}}^{2} + \frac{1}{4!}{{x}}^{4} - \frac{1}{6!}{{x}}^{6}+\dots\right) + {{i}} \left( {{x}} - \frac{1}{3!}{{x}}^{3} + \frac{1}{5!}{{x}}^{5} - \frac{1}{7!}{{x}}^{7} + \dots \right)",font_size=30)
        eq_ix2[0].set_color(RED)
        eq_ix2[2].set_color(YELLOW)
        eq_ix2[4].set_color(YELLOW)
        eq_ix2[6].set_color(YELLOW)
        eq_ix2[8].set_color(YELLOW)
        eq_ix2[10].set_color(YELLOW)
        eq_ix2[12].set_color(YELLOW)
        eq_ix2[14].set_color(YELLOW)
        eq_ix2[16].set_color(YELLOW)
        eq_ix2[18].set_color(YELLOW)
        
        self.play(TransformMatchingShapes(eq_ix1,eq_ix2))
        self.wait(2)
        
        eq_ix3 = MathTex(r"{{e}}^{ {{ix}} } =  {{\left( 1 - \frac{1}{2!}x^{2} + \frac{1}{4!}x^{4} - \frac{1}{6!}x^{6}+\dots\right)}} + {{i}} {{\left( x - \frac{1}{3!}x^{3} + \frac{1}{5!}x^{5} - \frac{1}{7!}x^{7} + \dots \right)}}",font_size=30)
        eq_ix3[0].set_color(RED)
        eq_ix3[2].set_color(YELLOW)
        eq_ix3[4].set_color(ORANGE)
        eq_ix3[6].set_color(YELLOW)
        eq_ix3[8].set_color(GREEN)
        
        self.play(TransformMatchingShapes(eq_ix2,eq_ix3))
        self.wait(2)
        
        
        eq_ix4 = MathTex(r"{{e}}^{ {{ix}} } =  {{cos(x)}} + {{i}}{{sen(x)}}",font_size=40)
        eq_ix4[0].set_color(RED)
        eq_ix4[2].set_color(YELLOW)
        eq_ix4[4].set_color(ORANGE)
        eq_ix4[4][4].set_color(YELLOW)
        eq_ix4[6].set_color(YELLOW)
        eq_ix4[7].set_color(GREEN)
        eq_ix4[7][4].set_color(YELLOW) 
        self.play(ReplacementTransform(eq_ix3,eq_ix4))
        self.wait(2)
        
        
        
        
        
        ##  END FRAME
        tex_end = Tex("E colocando {{$x=\pi$}}, temos").to_edge(UP)
        tex_end[1].set_color(YELLOW)
        
        self.play(ReplacementTransform(tex_i,tex_end))
        
        
        eq_e = MathTex(r"{{e}}^{ {{i\pi}} } =  {{cos(\pi)}} + {{i}}{{sen(\pi)}}",font_size=40)
        eq_e[0].set_color(RED)
        eq_e[2].set_color(YELLOW)
        eq_e[4].set_color(ORANGE)
        eq_e[4][4].set_color(YELLOW)
        eq_e[6].set_color(YELLOW)
        eq_e[7].set_color(GREEN)
        eq_e[7][4].set_color(YELLOW)

        self.play(TransformMatchingShapes(eq_ix4,eq_e))
        self.wait(2)
        
        
        eq_e1 = MathTex(r"{{e}}^{ {{i\pi}} } =  {{(-1)}} + {{i}}*{{(0)}}",font_size=40)
        eq_e1[0].set_color(RED)
        eq_e1[2].set_color(YELLOW)
        eq_e1[4].set_color(ORANGE)
        eq_e1[6].set_color(YELLOW)
        eq_e1[8].set_color(GREEN)

        self.play(TransformMatchingShapes(eq_e,eq_e1))
        self.wait(2)
        
        
        eq_e2 = MathTex(r"{{e}}^{ {{i\pi}} } +  {{1}} = {{0}}",font_size=40)
        eq_e2[0].set_color(RED)
        eq_e2[2].set_color(YELLOW)
        eq_e2[4].set_color(ORANGE)
        eq_e2[6].set_color(GREEN)

        self.play(TransformMatchingShapes(eq_e1,eq_e2))
        self.wait(2)
        
        
        tex_end_ = Tex("Et Voilà!!").to_edge(UP)
        self.play(ReplacementTransform(tex_end,tex_end_))
        self.wait(2)
        
        self.play(FadeOut(tex_end_))
        self.wait()
        self.play(FadeOut(eq_e2))