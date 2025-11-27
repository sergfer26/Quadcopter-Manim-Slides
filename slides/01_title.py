"""Title slide for the dissertation presentation."""

from manim import *
from manim_slides import Slide


class TitleSlide(Slide):
    """Title slide with dissertation title and author information."""
    
    def construct(self):
        # Title
        title = Text(
            "Quadcopter Control using\nDeep Reinforcement Learning",
            font_size=48,
            weight=BOLD
        )
        title.to_edge(UP, buff=1)
        
        # Subtitle or author
        subtitle = Text(
            "Dissertation Presentation",
            font_size=32,
            color=GRAY
        )
        subtitle.next_to(title, DOWN, buff=0.5)
        
        # Author name
        author = Text(
            "Your Name",
            font_size=24,
            color=WHITE
        )
        author.to_edge(DOWN, buff=1)
        
        # Date
        date = Text(
            "2024",
            font_size=20,
            color=GRAY
        )
        date.next_to(author, DOWN, buff=0.3)
        
        # Animate
        self.play(Write(title))
        self.next_slide()
        self.play(Write(subtitle))
        self.next_slide()
        self.play(Write(author), Write(date))
        self.wait()

