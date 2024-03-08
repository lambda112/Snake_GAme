import turtle as t
from time import sleep


class Snake:
    def __init__(self) -> None:
        self.starting_positions = [(0,0), (-20,0), (-40, 0)]
        self.segments = [] 

        # Create Snake
        for position in self.starting_positions:
            new_segment = t.Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def get_postion(self):
        # Get position of all segements
        segment_positions = []
        for seg in self.segments:
            segment_positions.append(seg.pos())
        
        return segment_positions

    def move(self):
        # Animate Snake
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(20)