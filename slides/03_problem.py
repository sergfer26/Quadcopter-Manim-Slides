"""Problem statement slide."""

from manim import *
from manim_slides import Slide


class ProblemStatement(Slide):
    """Problem statement and motivation."""
    
    def construct(self):
        title = Text("Problem Statement", font_size=48, weight=BOLD)
        title.to_edge(UP)
        
        problem_text = Text(
            "How can we design an effective deep reinforcement learning\n"
            "controller for quadcopter stabilization and trajectory tracking?",
            font_size=36,
            line_spacing=1.2
        )
        problem_text.next_to(title, DOWN, buff=1)
        
        challenges = VGroup(
            Text("Challenges:", font_size=32, weight=BOLD),
            Text("• High-dimensional state and action spaces", font_size=28),
            Text("• Real-time control requirements", font_size=28),
            Text("• Safety and stability constraints", font_size=28),
            Text("• Sim-to-real transfer", font_size=28),
        )
        challenges.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        challenges.next_to(problem_text, DOWN, buff=1)
        
        self.play(Write(title))
        self.next_slide()
        self.play(Write(problem_text))
        self.next_slide()
        self.play(Write(challenges))
        self.wait()

