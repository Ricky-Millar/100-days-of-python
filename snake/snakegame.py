import time
from turtle import Turtle, Screen


class Snake:
    '''creates and controls the snake in the game'''

    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor('black')
        self.screen.title('Lange Schlange')
        self.snake_body = []
        self.prev_body_part_pos = (0, 0)
        self.body_pos_list = []
        self.screen.tracer(0)
        self.movement = True

    def build_snake(self, initial_length):
        '''creates a snakyboi with a defined length, if its longer than the screen its gunna poop'''
        for body_part in range(initial_length):
            snake_body_part = Turtle(shape='square')
            snake_body_part.speed('fastest')
            snake_body_part.penup()
            self.snake_body.append(snake_body_part)
            self.snake_body[body_part].color('white')
            self.snake_body[body_part].goto(-20 * body_part, 0)
            self.body_pos_list.append(self.snake_body[body_part].pos())
            self.screen.update()

    def alt_snake_movement(self):
        '''Creates list of snakes body part positions then cycles the positions through the list, adding a new head position each time'''
        self.snake_body[0].forward(20)  # Move snake head
        self.body_pos_list.insert(0,
                                  self.snake_body[0].pos())  # Appends new head position to list of body part positions
        del self.body_pos_list[
            len(self.body_pos_list) - 1]  # removes the last position from the list so the new list is shifted forwars by one
        for body_part in range(1, len(self.snake_body)):
            self.snake_body[body_part].setpos(self.body_pos_list[body_part])
        self.screen.update()
        time.sleep(0.1)

    def listen_for_turns(self):
        '''listens for WASD key strokes then changes snake heading aproprietly'''
        self.screen.listen()
        self.screen.onkey(key='space', fun=self.grow_snake)
        self.screen.onkey(key='w', fun=self.up)
        self.screen.onkey(key='a', fun=self.turn_right)
        self.screen.onkey(key='s', fun=self.down)
        self.screen.onkey(key='d', fun=self.turn_left)

    def turn_left(self):
        if self.snake_body[0].heading() == 180:
            return
        else:
            self.snake_body[0].setheading(0)

    def turn_right(self):
        if not self.snake_body[0].heading() != 0:
            return
        else:
            self.snake_body[0].setheading(180)

    def up(self):
        if not self.snake_body[0].heading() != 270:
            return
        else:
            self.snake_body[0].setheading(90)

    def down(self):
        if not self.snake_body[0].heading() != 90:
            return
        else:
            self.snake_body[0].setheading(270)

    def grow_snake(self):
        '''adds a length onto snakyboi'''
        self.body_pos_list.append(self.snake_body[len(self.snake_body) - 1].pos())
        self.snake_body.append(Turtle(shape='square'))
        self.snake_body[len(self.snake_body) - 1].color('white')
        self.snake_body[len(self.snake_body) - 1].penup()


    def end_game(self):
        '''Clears the snake from the screen'''
        self.screen.clear()
