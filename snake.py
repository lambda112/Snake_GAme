import turtle as t
from time import sleep

MOVE_DISTANCE = 10

class Snake:
    def __init__(self) -> None:
        self.starting_positions = [(0,0), (-20,0), (-40, 0)]
        self.new_cord_value = -40
        self.new_pos = (-60, 0)
        self.segments = [] 
        self.reset_snake()

    def reset_snake(self):
        # Create Snake
        for position in self.starting_positions:
            new_segment = self.create_segment(position)
            self.segments.append(new_segment)

    def create_segment(self, position):
        new_segment = t.Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        return new_segment
        
    def get_position(self):
        # Get position of all segements
        segment_positions = []
        for seg in self.segments:
            segment_positions.append(seg.pos())
        
        return segment_positions
    
    def check_collision(self):
        for pos in self.get_position()[1:]:
            if self.segments[0].distance(pos) < 0.5:
                print("Game Over")
                return True
            
        return False

    def move(self):
        # Animate Snake
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)

    def upward(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
            self.new_pos = (self.segments[-1].xcor(), self.new_cord_value + 20)
            
    def downward(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
            self.new_pos = (self.segments[-1].xcor(), abs(self.new_cord_value) + 20)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
            self.new_pos = (self.new_cord_value - 20, self.segments[-1].ycor())

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
            self.new_pos = (abs(self.new_cord_value) + 20, self.segments[-1].ycor())

    
        