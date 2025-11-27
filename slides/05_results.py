"""Results and evaluation slides."""

from manim import *
from manim_slides import Slide


class Results(Slide):
    """Results and evaluation."""
    
    def construct(self):
        title = Text("Results", font_size=48, weight=BOLD)
        title.to_edge(UP)
        
        # Results summary
        results_text = Text(
            "Key Findings:",
            font_size=36,
            weight=BOLD
        )
        results_text.next_to(title, DOWN, buff=1)
        
        findings = VGroup(
            Text("• RL controller achieves stable hover", font_size=32),
            Text("• Successful trajectory tracking", font_size=32),
            Text("• Robust to disturbances", font_size=32),
            Text("• Comparable or better than PID baseline", font_size=32),
        )
        findings.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        findings.next_to(results_text, DOWN, buff=0.8)
        
        # Note: You can add actual plots/graphs here
        # For example, using Manim's plotting capabilities
        
        self.play(Write(title))
        self.next_slide()
        self.play(Write(results_text))
        self.next_slide()
        
        for finding in findings:
            self.play(Write(finding))
            self.next_slide()
        
        # Placeholder for plots
        plot_note = Text(
            "[Add performance plots here]",
            font_size=24,
            color=GRAY,
            italic=True
        )
        plot_note.to_edge(DOWN, buff=1)
        self.play(Write(plot_note))
        self.wait()

