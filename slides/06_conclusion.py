"""Conclusion and future work slides."""

from manim import *
from manim_slides import Slide


class Conclusion(Slide):
    """Conclusion and future work."""
    
    def construct(self):
        title = Text("Conclusion", font_size=48, weight=BOLD)
        title.to_edge(UP)
        
        conclusions = VGroup(
            Text("• Deep RL successfully applied to quadcopter control", font_size=32),
            Text("• Demonstrated stable flight and trajectory tracking", font_size=32),
            Text("• Potential for real-world deployment", font_size=32),
        )
        conclusions.arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        conclusions.next_to(title, DOWN, buff=1)
        
        future_work_title = Text(
            "Future Work:",
            font_size=36,
            weight=BOLD
        )
        future_work_title.next_to(conclusions, DOWN, buff=1)
        
        future_work = VGroup(
            Text("• Real-world testing and validation", font_size=28),
            Text("• Multi-quadcopter coordination", font_size=28),
            Text("• Advanced maneuvers and acrobatics", font_size=28),
        )
        future_work.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        future_work.next_to(future_work_title, DOWN, buff=0.5)
        
        self.play(Write(title))
        self.next_slide()
        
        for conclusion in conclusions:
            self.play(Write(conclusion))
            self.next_slide()
        
        self.play(Write(future_work_title))
        self.next_slide()
        self.play(Write(future_work))
        self.wait()

