from manimlib.imports import *

class D55P9(Scene):
    def construct(self):
        author = TextMobject("Made By Stanley Jian")
        self.play(Write(author))
        self.wait()
             
        manim = TextMobject("With Manim")
        manim.shift(np.array((0,-1/3,0))).scale(0.75)
        author.generate_target().shift(np.array((0,1/3,0)))
        self.play(MoveToTarget(author),Write(manim))
        self.wait()
            
        title = TextMobject("Day 55 Problem 9",background_stroke_width=0)
        self.play(ReplacementTransform(VGroup(author,manim),title))
        self.wait()
               
        titleT = title.generate_target()
        titleT.scale(0.85)
        titleT.to_edge(UP,MED_SMALL_BUFF)
        self.play(MoveToTarget(title))
        self.wait()
           
        plane = NumberPlane()
        self.bring_to_back(plane)
        self.play(ShowCreation(plane))
        self.wait()
             
        v50 = Vector(np.array((5,0,0)))
        v50L = TexMobject("\\vec{u}")
        v50L.next_to(v50,direction=DOWN)
        self.play(GrowArrow(v50))
        self.wait()
         
        v50B = Brace(v50,DOWN)
        self.play(GrowFromCenter(v50B))
        self.wait()
         
        v50BL = TexMobject("5")
        v50BL.next_to(v50B,direction=DOWN)
        self.play(Write(v50BL))
        self.wait()
         
        self.play(FadeOut(VGroup(v50B,v50BL)))
        self.wait()
         
        self.play(Write(v50L))
        self.wait()
              
        v50r = v50.deepcopy()
        v50r.set_color("#FFD868")
        self.play(GrowArrow(v50r))
        self.wait()
              
        v50rT = v50r.generate_target()
        v50rT.rotate_about_origin(1/5*np.pi)
        angle = Arc(angle=1/5*np.pi)
        angleL = TexMobject("36\\si{\\degree}").scale(0.7)
        angleL.next_to(angle,direction=RIGHT)
        angleL.shift(np.array((0,0.15,0)))
        self.play(MoveToTarget(v50r))
        self.wait()
          
        self.play(GrowFromCenter(angle),Write(angleL))
        self.wait()
          
        v50rL = TexMobject("\\vec{v}").set_color("#FFD868")
        v50rL.move_to(np.array((2.5*np.cos(1/5*np.pi)-0.5,2.5*np.sin(1/5*np.pi)+0.5,0)))
        self.play(Write(v50rL))
        self.wait()
          
        self.play(FadeOut(VGroup(v50rL,v50L)))
        self.wait()
             
        circle = Circle(radius=5)
        self.play(ShowCreation(circle,run_time=2))
        self.wait()
        
        self.play(ApplyMethod(circle.scale_about_point,0.2,ORIGIN,run_time=2.5),
                  ApplyMethod(v50r.scale_about_point,0.2,ORIGIN,run_time=2.5))
        self.wait()
        
        unit = DashedLine(start=ORIGIN,end=np.array((np.cos(2/3*np.pi),np.sin(2/3*np.pi),0)))
        unitB = Brace(Line(start=ORIGIN,end=np.array((1,0,0))),direction=UP,buff=0).rotate_about_origin(2/3*np.pi)
        unitBL = TexMobject("1").move_to(np.array((np.cos(2/3*np.pi)/2-0.45,np.sin(2/3*np.pi)/2-0.2,0))).scale(0.5)
        
        self.play(ShowCreation(unit))
        self.wait()
        self.play(ShowCreation(unitB),Write(unitBL))
        self.wait()
        self.play(FadeOut(VGroup(unit,unitB,unitBL)))
         
        self.play(ApplyMethod(circle.scale_about_point,5.0,ORIGIN,run_time=2.5),
                  ApplyMethod(v50r.scale_about_point,5.0,ORIGIN,run_time=2.5))
        self.wait()
                  
        altitude = DashedLine(start=np.array((5*np.cos(1/5*np.pi),5*np.sin(1/5*np.pi),0)),end=np.array((5*np.cos(1/5*np.pi),0,0)))
        projection = Line(start=ORIGIN,end=np.array((5*np.cos(1/5*np.pi),0,0)))
        perpendicular = VGroup(Line(start=np.array((5*np.cos(1/5*np.pi)-0.25,0,0)),end=np.array((5*np.cos(1/5*np.pi)-0.25,0.25,0))),Line(start=np.array((5*np.cos(1/5*np.pi)-0.25,0.25,0)),end=np.array((5*np.cos(1/5*np.pi),0.25,0))))
        self.play(ShowCreation(altitude),FadeIn(perpendicular))
        self.wait()
            
        altitudeC = Line(start=np.array((5*np.cos(1/5*np.pi),5*np.sin(1/5*np.pi),0)),end=np.array((5*np.cos(1/5*np.pi),0,0))).set_color("#FFFF00")
        projectionC = projection.deepcopy().set_color("#FFFF00")
        braceV = Brace(altitude,RIGHT)
        braceH = Brace(projection,DOWN)
        braceVL = TexMobject("5sin(36\\si{\\degree})").scale(0.8)
        braceHL = TexMobject("5cos(36\\si{\\degree})").scale(0.8)
        braceVL.next_to(braceV,direction=RIGHT)
        braceHL.next_to(braceH,direction=DOWN)
        self.play(ShowPassingFlash(altitudeC,time_width=0.4))
        self.wait()
        self.play(GrowFromCenter(braceV),Write(braceVL))
        self.wait()
        self.play(ShowPassingFlash(projectionC,time_width=0.4))
        self.wait()
        self.play(GrowFromCenter(braceH),Write(braceHL))
        self.wait()
              
        v50form = TexMobject("\\vec{u}=[5,0]")
        varrow = TexMobject("\\Rightarrow")
        v50rform0 = TexMobject("\\vec{v}=[5cos(36\\si{\\degree}),5sin(36\\si{\\degree})]")
        v50rform1 = TexMobject("=5\\times[cos(36\\si{\\degree}),sin(36\\si{\\degree})]")
        v50rform1.next_to(v50rform0,RIGHT)
        varrow.rotate(3/2*np.pi)
        varrow.next_to(v50form,DOWN)
        v50rform0.next_to(varrow,DOWN)
        VGroup(v50form,varrow,v50rform0).move_to(ORIGIN)
        self.play(FadeOut(VGroup(angle,angleL,plane,v50,v50r,circle,altitude,braceH,braceV,perpendicular)),ReplacementTransform(VGroup(braceVL,braceHL),v50rform0),Write(VGroup(v50form,varrow)))
        self.wait()
          
        v50rform0.generate_target().move_to(ORIGIN)
        self.play(FadeOut(VGroup(varrow,v50form)),MoveToTarget(v50rform0))
        self.wait()
          
        v50rform0.generate_target().shift(np.array((-v50rform1.get_width()/2,0,0)))
        self.play(MoveToTarget(v50rform0))
        self.wait()
          
        v50rform1.shift(np.array((-v50rform1.get_width()/2,0,0)))
        self.play(Write(v50rform1))
        self.wait()
          
        self.play(FadeOutAndShift(VGroup(v50rform0,v50rform1)))
        self.wait()
          
        generalized1 = TexMobject("Rot(\\vec{u},\\theta)=\\vec{u}_{x}\\times[cos(\\theta),sin(\\theta)]")
        generalized2 = TexMobject("(\\vec{u}_{x}\\in\\mathbb{R},\\vec{u}_{y}=0)").next_to(generalized1,direction=DOWN)
        group = VGroup(generalized1,generalized2).move_to(ORIGIN)
        self.play(Write(group))
        self.wait()
        generalizedR = SurroundingRectangle(group)
        self.play(ShowCreationThenDestruction(generalizedR))
        self.wait()
          
        self.play(FadeOutAndShift(group))
        self.wait()
         
        self.bring_to_back(plane)
        self.play(ShowCreation(plane))
        self.wait()
         
        exampleVU = Vector(np.array((2.5,0,0))).set_color("#BAF1A1")
        exampleVV = exampleVU.deepcopy().set_color("#FA744F")
        exampleVUL = TexMobject("\\vec{u}")
        exampleVVL = TexMobject("\\vec{v}")
        exampleVUL.next_to(exampleVU,direction=DOWN).set_color("#BAF1A1")
        exampleVVL.next_to(exampleVV,direction=DOWN).set_color("#FA744F")
        self.play(GrowArrow(exampleVU),Write(exampleVUL))
        self.wait()
        self.play(exampleVUL.to_edge,UP+LEFT)
        self.wait()
        self.play(GrowArrow(exampleVV),Write(exampleVVL))
        self.wait()
        exampleVVL.generate_target().align_to(exampleVUL).next_to(exampleVUL,direction=DOWN)
        self.play(MoveToTarget(exampleVVL))
        self.wait()
         
        varTheta = 0
        varX = 2.5
        varSin = 0
        varCos = 2.5
         
        def getThetaDegFromCoord():
            return lambda f : exampleVV.get_angle()*180/np.pi if exampleVV.get_angle()*180/np.pi>0 else 360+exampleVV.get_angle()*180/np.pi
        def getXComponent():
            return lambda f : exampleVU.get_vector()[0]
        def getCos():
            return lambda f : exampleVU.get_vector()[0]*np.cos(exampleVV.get_angle() if exampleVV.get_angle()>0 else np.pi*2+exampleVV.get_angle())
        def getSin():
            return lambda f : exampleVU.get_vector()[0]*np.sin(exampleVV.get_angle() if exampleVV.get_angle()>0 else np.pi*2+exampleVV.get_angle())
         
        exampleVULV1 = TexMobject("=[").next_to(exampleVUL)
        exampleVULV2 = DecimalNumber(varX).next_to(exampleVULV1,buff=0.05)
        exampleVULV3 = TexMobject(",0]").next_to(exampleVULV2,buff=0.05)
        VGroup(exampleVULV1,exampleVULV2,exampleVULV3).set_color("#BAF1A1")
         
        exampleTheta1 = TexMobject("\\theta\\si{\\degree}=").next_to(exampleVUL,direction=DOWN).align_to(exampleVUL,LEFT)
        exampleTheta2 = DecimalNumber(varTheta).next_to(exampleTheta1)
        VGroup(exampleTheta1,exampleTheta2).set_color("#FEB72B")
         
        exampleVVLV1 = TexMobject("=\\vec{u}_{x}\\times[cos(\\theta),sin(\\theta)]").next_to(exampleTheta1,direction=DOWN).align_to(exampleVULV1,LEFT)
        exampleVVLV2 = TexMobject("=[").next_to(exampleVVLV1,direction=DOWN).align_to(exampleVVLV1,LEFT)
        exampleVVLV3 = DecimalNumber(varCos).next_to(exampleVVLV2)
        exampleVVLV4 = TexMobject(",").next_to(exampleVVLV3,buff=0.5)
        exampleVVLV5 = DecimalNumber(varSin).next_to(exampleVVLV4)
        exampleVVLV6 = TexMobject("]").next_to(exampleVVLV5,buff=0.5)
        VGroup(exampleVVLV1,exampleVVLV2,exampleVVLV3,exampleVVLV4,exampleVVLV5,exampleVVLV6).set_color("#FA744F")
         
        self.play(exampleVVL.shift,np.array((0,-DEFAULT_MOBJECT_TO_MOBJECT_BUFFER-exampleTheta1.get_height(),0)))
        self.wait()
         
        self.play(Write(VGroup(exampleVULV1,exampleVULV2,exampleVULV3)),
                  Write(VGroup(exampleTheta1,exampleTheta2)),
                  Write(VGroup(exampleVVLV1,exampleVVLV2,exampleVVLV3,exampleVVLV4,exampleVVLV5,exampleVVLV6)))
        self.wait()
         
        self.play(Rotating(exampleVV,run_time=5,rate_func=smooth,radians=2/3*np.pi,about_point=ORIGIN),
                  ChangingDecimal(exampleTheta2,getThetaDegFromCoord()),
                  ChangingDecimal(exampleVVLV3,getCos()),
                  ChangingDecimal(exampleVVLV5,getSin()))
        self.wait()
        self.play(Rotating(exampleVV,run_time=12,rate_func=smooth,radians=7/6*np.pi,about_point=ORIGIN),
                  ChangingDecimal(exampleTheta2,getThetaDegFromCoord()),
                  ChangingDecimal(exampleVVLV3,getCos()),
                  ChangingDecimal(exampleVVLV5,getSin()))
        self.wait()
        self.play(ApplyMethod(exampleVV.scale_about_point,0.6,ORIGIN,run_time=2.5),
                  ApplyMethod(exampleVU.scale_about_point,0.6,ORIGIN,run_time=2.5),
                  ChangingDecimal(exampleVULV2,getXComponent()),
                  ChangingDecimal(exampleVVLV3,getCos()),
                  ChangingDecimal(exampleVVLV5,getSin()))
        self.wait()
        self.play(Rotating(exampleVV,run_time=5,rate_func=smooth,radians=-2/3*np.pi,about_point=ORIGIN),
                  ChangingDecimal(exampleTheta2,getThetaDegFromCoord()),
                  ChangingDecimal(exampleVVLV3,getCos()),
                  ChangingDecimal(exampleVVLV5,getSin()))
        self.wait()
        self.play(ApplyMethod(exampleVV.scale_about_point,8/3,ORIGIN,run_time=6),
                  ApplyMethod(exampleVU.scale_about_point,8/3,ORIGIN,run_time=6),
                  ChangingDecimal(exampleVULV2,getXComponent()),
                  ChangingDecimal(exampleVVLV3,getCos()),
                  ChangingDecimal(exampleVVLV5,getSin()))
        self.wait()
        self.play(ApplyMethod(exampleVV.scale_about_point,5/8,ORIGIN,run_time=2.5),
                  ApplyMethod(exampleVU.scale_about_point,5/8,ORIGIN,run_time=2.5),
                  ChangingDecimal(exampleVULV2,getXComponent()),
                  ChangingDecimal(exampleVVLV3,getCos()),
                  ChangingDecimal(exampleVVLV5,getSin()))
        self.wait()
        self.play(Rotating(exampleVV,run_time=12,rate_func=smooth,radians=-7/6*np.pi,about_point=ORIGIN),
                  ChangingDecimal(exampleTheta2,getThetaDegFromCoord()),
                  ChangingDecimal(exampleVVLV3,getCos()),
                  ChangingDecimal(exampleVVLV5,getSin()))
        self.wait()
         
        self.play(FadeOutAndShift(plane,run_time=2),FadeOut(VGroup(exampleVU,exampleVV,exampleVUL,exampleVVL,exampleTheta1,exampleTheta2,exampleVULV1,exampleVULV2,exampleVULV3,exampleVVLV1,exampleVVLV2,exampleVVLV3,exampleVVLV4,exampleVVLV5,exampleVVLV6),run_time=2))
        self.wait()
        
        intro = TextMobject("Before we end:")
        vector = TexMobject("\\vec{u}=[5cos(\\theta),5sin(\\theta)]").next_to(intro,direction=DOWN)
        vectorQuestion = TexMobject("\\left|\\vec{u}\\right|=?").next_to(vector,direction=DOWN)
        VGroup(intro,vector,vectorQuestion).move_to(ORIGIN)
        self.play(Write(intro))
        self.wait()
        
        self.play(Write(VGroup(vector,vectorQuestion)))
        self.wait()
        
        self.play(FadeOut(VGroup(intro,vector)),
                  ApplyMethod(vectorQuestion.move_to,ORIGIN))
        self.wait()
        
        answer1 = TexMobject("\\left|\\vec{u}\\right|")
        self.play(ReplacementTransform(vectorQuestion,answer1))
        self.wait()
        
        answer2 = TexMobject("=(5cos\\theta)^{2}+(5sin\\theta)^{2}")
        
        self.play(ApplyMethod(answer1.shift,np.array((-answer2.get_width()/2,0,0))))
        self.wait()
        
        answer2.next_to(answer1)
        answer3 = TexMobject("=25cos^{2}(\\theta)+25sin^{2}(\\theta)").next_to(answer2,direction=DOWN).align_to(answer2,direction=LEFT)
        answer4 = TexMobject("=25[cos^{2}(\\theta)+sin^{2}(\\theta)]").next_to(answer3,direction=DOWN).align_to(answer3,direction=LEFT)
        answer5 = TexMobject("=25").next_to(answer4,direction=DOWN).align_to(answer4,direction=LEFT)
        
        self.play(Write(answer2))
        self.wait()
        
        self.play(Write(answer3))
        self.wait()
        
        self.play(Write(answer4))
        self.wait()
        
        self.play(Write(answer5))
        self.wait()
        
        self.play(ApplyMethod(VGroup(answer1,answer2,answer3,answer4,answer5).move_to,ORIGIN))
        self.wait()
        
        self.play(FadeOutAndShift(VGroup(answer1,answer2,answer3,answer4,answer5,title),run_time=2))
        self.wait()
         
        conclusion = TextMobject("Thanks for watching!")
        self.play(Write(conclusion))
        self.wait()
          
        box = SurroundingRectangle(conclusion)
        self.play(ShowCreationThenDestruction(box))
        self.wait()
         
        self.play(FadeOutAndShift(conclusion))
        self.wait()
        
