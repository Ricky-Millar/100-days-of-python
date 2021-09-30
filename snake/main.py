from food import Food
from scorebord import ScoreBord
from snakegame import Snake

game = Snake()
score = ScoreBord()
game.screen
game.build_snake(15)
game.listen_for_turns()
game_on = True
food = Food()
while game_on == True:
    game.alt_snake_movement()
    if game.snake_body[0].distance(food) < 15:
        game.grow_snake()
        food.refrest()
        score.add_score()
    for body_part in game.snake_body[1:]:
        if game.snake_body[0].distance(body_part) < 15:
            game_on = False
    if not -280 <= game.snake_body[0].xcor() <= 280 or not -280 <= game.snake_body[0].ycor() <= 280:
        game_on = False

game.end_game()
score.final_score()
game.screen.exitonclick()
