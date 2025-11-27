"""Introduction and background slides."""

from manim import *
from manim_slides import Slide


class Introduction(Slide):
    """Introduction slide with overview of the topic."""
    
    def construct(self):
        title = Text("Introduction", font_size=48, weight=BOLD)
        title.to_edge(UP)
        
        # Key points
        points = VGroup(
            Text("• Quadcopters require precise control for stable flight", font_size=32),
            Text("• Traditional control methods have limitations", font_size=32),
            Text("• Deep Reinforcement Learning offers adaptive solutions", font_size=32),
            Text("• This work explores RL-based control strategies", font_size=32),
        )
        points.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        points.next_to(title, DOWN, buff=1)
        
        self.play(Write(title))
        self.next_slide()
        
        for point in points:
            self.play(Write(point))
            self.next_slide()

