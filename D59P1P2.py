from manimlib.imports import *

class D59P1(Scene):
    def construct(self):
        author = TextMobject("Made By Stanley Jian")
        self.play(Write(author))
        self.wait()
             
        manim = TextMobject("With Manim")
        manim.shift(np.array((0,-1/3,0))).scale(0.75)
        author.generate_target().shift(np.array((0,1/3,0)))
        self.play(MoveToTarget(author),Write(manim))
        self.wait()
            
        title = TextMobject("Day 59 Problem 1",background_stroke_width=0)
        self.play(ReplacementTransform(VGroup(author,manim),title))
        self.wait()
               
        title.generate_target().scale(0.85).to_edge(UP,MED_SMALL_BUFF)
        self.play(MoveToTarget(title))
        self.wait()
        
        wheel = Circle(radius=2).set_color(WHITE)
        framework = VGroup(Line(start=ORIGIN,end=np.array((0,-12/5,0))),
                           Line(start=np.array((-1,-12/5,0)),end=np.array((1,-12/5,0))),
                           Line(start=np.array((-1,-12/5,0)),end=np.array((0,-2,0))),
                           Line(start=np.array((1,-12/5,0)),end=np.array((0,-2,0))))
        VGroup(wheel,framework).shift(np.array((0,1/5,0)))
        self.play(ShowCreation(VGroup(wheel,framework)))
        self.wait()
        
        player = Dot(point=np.array((0,-9/5,0)))
        self.play(ShowCreation(player))
        self.wait()
        
        self.play(FocusOn(player))
        self.wait()
        
        self.play(Rotate(player,angle=7/3*np.pi,about_point=np.array((0,1/5,0)),run_time=5))
        self.wait()
        
        player2 = player.deepcopy().set_color("#F40552")
        self.play(ShowCreation(player2))
        self.wait()
        
        playerL = TextMobject("Player").scale(0.7).to_edge(UP+LEFT).set_color("#F40552")
        player3 = player2.deepcopy()
        self.add(player3)
        self.play(ApplyMethod(player3.next_to,playerL))
        self.wait()
        
        self.play(Write(playerL))
        self.wait()
        
        lowest = Line(start=np.array((0,-2,0)),end=np.array((0,-12/5,0))).set_color("#BAF1A1").shift(np.array((0,1/5,0)))
        self.play(ShowCreation(lowest))
        self.wait()
        
        lowestL = TextMobject("1m").set_color("#BAF1A1").next_to(playerL,direction=DOWN).align_to(playerL,direction=LEFT).scale(0.7)
        lowest2 = lowest.deepcopy()
        self.add(lowest2)
        lowest2.generate_target().rotate(np.pi/2,about_point=np.array((0,-2,0))).next_to(lowestL)
        self.play(MoveToTarget(lowest2))
        self.wait()
        
        self.play(Write(lowestL))
        self.wait()
        
        radius = DashedLine(start=np.array((0,1/5,0)),end=player.get_arc_center())
        radiusL = TextMobject("5m").scale(0.7).next_to(lowestL,direction=DOWN).align_to(lowestL,direction=LEFT).set_color("#FA744F")
        radius2 = radius.deepcopy().set_color("#FA744F")
        radius3 = radius2.deepcopy()
        self.play(ShowCreation(radius))
        self.wait()
        
        self.play(ShowCreation(radius2))
        self.wait()
        
        self.add(radius3)
        radius3.generate_target().rotate(1/6*np.pi,about_point=np.array((0,1/5,0))).next_to(radiusL)
        self.play(MoveToTarget(radius3))
        
        self.play(Write(radiusL))
        self.wait()
        
        center = Arc(start_angle=3/2*np.pi,angle=1/3*np.pi,radius=1/3,arc_center=np.array((0,1/5,0)))
        self.play(GrowFromCenter(center))
        self.wait()
        
        center2 = center.deepcopy().set_color("#FFE277")
        self.play(GrowFromCenter(center2))
        self.wait()
        
        centerL = TexMobject("t\\si{\\degree}").scale(0.7).next_to(radiusL,direction=DOWN).align_to(radiusL,direction=LEFT).set_color("#FFE277")
        centerT = TexMobject("(V_{Rot}=1\\si{\\degree}\\slash s,T_{Rot}=ts)").scale(0.5).next_to(centerL,direction=DOWN).align_to(centerL,direction=LEFT).set_color("#F8E1F4")
        center3 = center2.deepcopy()
        center3.generate_target().rotate(5/6*np.pi,about_point=np.array((0,1/5,0))).next_to(centerL)
        self.play(MoveToTarget(center3))
        self.wait()
        
        self.play(Write(centerL))
        self.wait()
        
        self.play(Write(centerT))
        
        altitude = DashedLine(start=player.get_arc_center(),end=np.array((0,-4/5,0)))
        perpendicular = VGroup(Line(start=np.array((0,-3/5,0)),end=np.array((1/5,-3/5,0))),
                               Line(start=np.array((1/5,-3/5,0)),end=np.array((1/5,-4/5,0))))
        self.play(ShowCreation(altitude))
        self.wait()
        
        self.play(FadeIn(perpendicular))
        self.wait()
        
        projection = Line(start=np.array((0,1/5,0)),end=np.array((0,-4/5,0))).set_color("#0779E4")
        self.play(ShowCreation(projection))
        self.wait()
        
        projectionL = TexMobject("5cos(t\\si{\\degree})m").set_color("#0779E4").scale(0.7).next_to(centerT,direction=DOWN).align_to(centerT,direction=LEFT)
        projection2 = projection.deepcopy()
        self.add(projection2)
        projection2.generate_target().rotate(1/2*np.pi,about_point=np.array((0,1/5,0))).next_to(projectionL)
        self.play(MoveToTarget(projection2))
        self.wait()
        
        self.play(Write(projectionL))
        self.wait()
        
        dist = Line(start=np.array((0,-4/5,0)),end=np.array((0,-11/5,0))).set_color("#EFA8E4")
        self.play(ShowCreation(dist))
        self.wait()
        
        self.remove(radius)
        radius4 = radius2.deepcopy()
        self.add(radius4)
        self.play(Rotate(radius4,angle=-1/3*np.pi,about_point=np.array((0,1/5,0)),run_time=2))
        self.wait()
        
        self.play(Rotate(radius4,angle=1/3*np.pi,about_point=np.array((0,1/5,0)),run_time=2))
        self.wait()
        
        plus = TexMobject("+").set_opacity(0)
        minus = TexMobject("-").set_opacity(0)
        equal = TexMobject("=").set_opacity(0)
        plus2 = plus.deepcopy().set_opacity(0)
        minus2 = minus.deepcopy().set_opacity(0)
        equal2 = equal.deepcopy().set_opacity(0)
        distL = TexMobject("[6-5cos(t\\si{\\degree})]m").set_color("#EFA8E4").set_opacity(0).scale(0.7)
        
        group1 = VGroup(lowest2,plus,radius3,minus,projection2,equal,dist)
        group2 = VGroup(lowestL,plus2,radiusL,minus2,projectionL,equal2,distL)
        self.play(*[ApplyMethod(segment.rotate_in_place,1/2*np.pi) for segment in [lowest2,radius3,projection2]],
                  FadeOutAndShiftDown(VGroup(lowest,radius4,wheel,framework,playerL,player2,player3,centerL,centerT,center2,center3,center,altitude,perpendicular,player,radius2,projection)))
        self.play(ApplyMethod(group1.arrange,RIGHT,True,np.array((0,(minus.get_height()*16+DEFAULT_MOBJECT_TO_MOBJECT_BUFFER)/2,0))),
                  ApplyMethod(group2.arrange,RIGHT,True,np.array((0,-(2.5+DEFAULT_MOBJECT_TO_MOBJECT_BUFFER)/2,0))))
        self.wait()
        
        group3 = VGroup(*[item.deepcopy().set_opacity(1) for item in [plus,minus,equal,plus2,minus2,equal2]])
        self.play(*[Write(symbol) for symbol in group3])
        self.wait()
        
        distL2 = distL.deepcopy().set_opacity(1)
        self.play(Write(distL2))
        self.wait()
        
        box = SurroundingRectangle(distL2)
        self.play(ShowCreationThenDestruction(box))
        self.wait()
        
        self.play(FadeOutAndShift(VGroup(group1,group2,group3,distL2)))
        self.wait()
        
        title.generate_target().scale(20/17).center()
        self.play(MoveToTarget(title))
        self.wait()
        
        newtitle = TextMobject("Day 59 Problem 2",background_stroke_width=0)
        self.play(ReplacementTransform(title,newtitle))
        self.wait()
        
        newtitle.generate_target().scale(0.85).to_edge(UP,MED_SMALL_BUFF)
        self.play(MoveToTarget(newtitle))
        self.wait()
        
class D59P2(GraphScene):
    CONFIG = {
        "x_max" : 34,
        "x_min" : 0,
        "x_axis_width": 12,
        "x_tick_frequency" : 2*np.pi,
        "x_axis_label" : "t",
        "y_max" : 20,
        "y_min" : 0,
        "y_axis_height": 6,
        "y_tick_frequency" : 2,
        "y_axis_label" : "f(t)",
        "axes_color" : WHITE,
        "graph_origin": 3 * DOWN + 6 * LEFT,
        "area_opacity": 0.8
    }
    
    def construct(self):
        title = TextMobject("Day 59 Problem 2",background_stroke_width=0).scale(0.85).to_edge(UP,MED_SMALL_BUFF)
        self.add(title)
        
        def defaultFunc1():
            return lambda x : 6-5*np.cos(x)
        def defaultFunc2():
            return lambda x : 6+5*np.cos(x)
        
        GraphScene.setup_axes(self)
        self.x_axis.label_direction = DOWN
        self.y_axis.label_direction = LEFT
        xLabelPos = range(2,12,2)
        xLabel = [str(num)+"\\pi" for num in xLabelPos]
        for p,l in zip(xLabelPos,xLabel):
            self.x_axis.add(TexMobject(l).scale(0.7).next_to(self.coords_to_point(p*np.pi,0),DOWN))
        for num in range(2,22,2):
            self.y_axis.add(TexMobject(str(num)).scale(0.7).next_to(self.coords_to_point(0,num),LEFT))
        self.x_axis_label_mob.shift(np.array((1.1,-0.35,0))).scale(0.7)
        self.y_axis_label_mob.shift(np.array((-0.5,0.2,0))).scale(0.7)
        self.play(Write(self.x_axis,run_time=4),Write(self.y_axis,run_time=3))
        self.wait()
        
        graph = self.get_graph(defaultFunc1(),color="#FF862F")
        graphT = TexMobject("f(t)=6-5cos(t)").next_to(graph,direction=UP).shift(np.array((0,0.5,0))).scale(0.7)
        self.play(Write(graphT),ShowCreation(graph,run_time=5))
        self.wait()
        
        dot = Dot(self.coords_to_point(0,1))
        lineV = Line(start=self.coords_to_point(0,1),end=self.coords_to_point(0,0),stroke_width=2)
        lineH = Line(start=self.coords_to_point(0,1),end=self.coords_to_point(0,1.001),stroke_width=2)
        dotY = Dot(self.coords_to_point(0,1)).set_color("#F2ED6F")
        dotY2 = Dot().set_color("#F2ED6F").next_to(graphT,buff=LARGE_BUFF*1.5).shift(np.array((-1.75,0,0)))
        dotYT = TexMobject("=").next_to(dotY2).scale(0.75)
        dotN = DecimalNumber(1).next_to(dotYT).scale(0.75)
        
        self.play(ShowCreation(VGroup(dot,lineV,lineH)))
        self.wait()
        
        self.play(ApplyMethod(graphT.shift,np.array((-1.75,0,0))),ShowCreation(VGroup(dotY,dotY2)))
        self.wait()
        
        self.play(Write(VGroup(dotYT,dotN)))
        self.wait()
        
        def updateH():
            return lambda m : m.put_start_and_end_on(dot.get_arc_center(),self.coords_to_point(0,self.point_to_coords(dot.get_arc_center())[1]))
        def updateV():
            return lambda m : m.put_start_and_end_on(dot.get_arc_center(),self.coords_to_point(self.point_to_coords(dot.get_arc_center())[0],0))
        def updateY():
            return lambda m : m.move_arc_center_to(self.coords_to_point(0,self.point_to_coords(dot.get_arc_center())[1]))
        def updateN():
            return lambda n : self.point_to_coords(dot.get_arc_center())[1]
        
        self.play(MoveAlongPath(dot,graph,run_time=15),
                  UpdateFromFunc(lineH,updateH()),
                  UpdateFromFunc(lineV,updateV()),
                  UpdateFromFunc(dotY,updateY()),
                  ChangingDecimal(dotN,updateN()))
        self.wait()

        newGraphT = TexMobject("f(t)=6+5cos(t)").scale(0.7).move_to(graphT)
        newGraph = self.get_graph(defaultFunc2(),color="#BAF1A1")
        self.play(ReplacementTransform(graph,newGraph,run_time=3),
                  ReplacementTransform(graphT,newGraphT,run_time=3),
                  ApplyMethod(dot.move_to,self.coords_to_point(0,11.001),run_time=3),
                  UpdateFromFunc(lineH,updateH()),
                  UpdateFromFunc(lineV,updateV()),
                  UpdateFromFunc(dotY,updateY()),
                  ChangingDecimal(dotN,updateN()))
        self.wait()
        self.bring_to_back(newGraph)

        self.play(MoveAlongPath(dot,graph,run_time=15),
                  UpdateFromFunc(lineH,updateH()),
                  UpdateFromFunc(lineV,updateV()),
                  UpdateFromFunc(dotY,updateY()),
                  ChangingDecimal(dotN,updateN()))
        self.wait()

        self.play(FadeOutAndShift(VGroup(dot,newGraph,newGraphT,dotY,dotY2,dotYT,dotN,lineH,lineV,self.x_axis,self.y_axis)))
        self.wait()
        
        conclusion1 = TextMobject("f(t)=6-5cos(t) is a ride starting at the bottom.").scale(0.6)
        conclusion2 = TextMobject("f(t)=6+5cos(t) is a ride starting at the top.").scale(0.6)
        conclusion2.next_to(conclusion1,direction=DOWN)
        VGroup(conclusion1,conclusion2).center()
        self.play(Write(conclusion1))
        self.wait()
        self.play(Write(conclusion2))
        self.wait()

        box = SurroundingRectangle(VGroup(conclusion1,conclusion2))
        self.play(ShowCreationThenDestruction(box))
        self.wait()
        
        self.play(FadeOutAndShift(VGroup(conclusion1,conclusion2)))
        self.wait()
        
        ending = TextMobject("Thanks for watching!")
        self.play(Write(ending))
        self.wait()
          
        box = SurroundingRectangle(ending)
        self.play(ShowCreationThenDestruction(box))
        self.wait()
         
        self.play(FadeOutAndShift(VGroup(ending,title)))
        self.wait()
