"""Methodology slides."""

from manim import *
from manim_slides import Slide


class Methodology(Slide):
    """Methodology and approach."""
    
    def construct(self):
        title = Text("Methodology", font_size=48, weight=BOLD)
        title.to_edge(UP)
        
        # Methodology components
        components = VGroup(
            Text("1. Environment Setup", font_size=32, weight=BOLD),
            Text("   • Physics simulation (PyBullet/Gymnasium)", font_size=28),
            Text("   • State and action space definition", font_size=28),
            Text("   • Reward function design", font_size=28),
            Text(""),
            Text("2. RL Algorithm", font_size=32, weight=BOLD),
            Text("   • PPO / SAC / TD3 (choose your algorithm)", font_size=28),
            Text("   • Neural network architecture", font_size=28),
            Text("   • Hyperparameter tuning", font_size=28),
            Text(""),
            Text("3. Training & Evaluation", font_size=32, weight=BOLD),
            Text("   • Training procedure", font_size=28),
            Text("   • Performance metrics", font_size=28),
            Text("   • Comparison with baseline controllers", font_size=28),
        )
        components.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        components.next_to(title, DOWN, buff=0.5)
        components.scale(0.9)
        
        self.play(Write(title))
        self.next_slide()
        
        # Animate in groups
        for i in range(0, len(components), 4):
            group = components[i:i+4]
            self.play(Write(group))
            self.next_slide()

