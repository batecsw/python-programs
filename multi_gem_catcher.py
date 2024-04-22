# Write your code here :-)
import random

WIDTH = 800
HEIGHT = 600

def on_mouse_move(pos, rel, buttons):
    ship.x = pos[0]

def spawn_gem():
    items = ["gemred" , "gemyellow" , "gemgreen" , "gemblue"]
    gem = Actor(items[random.randint(0, 3)])
    gem.x = random.randint(20, 780)
    gem.y = 0
    return gem

ship = Actor("playership1_red")
ship.x = 370
ship.y = 550

score = 0
lives = 3
game_over = False
high_score = 0
best_player = ""
gems = [spawn_gem()]
counter = 0

def update():
    global score, high_score, best_player, lives, game_over, counter
    if not game_over:
        if keyboard.left:
            ship.x = ship.x - 5
        if keyboard.right:
            ship.x = ship.x + 5

        if ship.x < 0:
            ship.x = WIDTH
        if ship.x > WIDTH:
            ship.x = 0

        if counter > (70 - score):
            gems.append(spawn_gem())
            counter  = 0
        else:
            counter += 1

        if lives == 0:
            game_over = True

        for gem in gems:
            gem.y = gem.y + 5 + score / 20

            if gem.y > 600:
                gems.remove(gem)
                lives = lives - 1

            if gem.colliderect(ship):
                gems.remove(gem)
                score = score + 1

    else:
        if keyboard.y:
            if score > high_score:
                high_score = score
                best_player = input("Please enter your name")
            score = 0
            lives = 3
            game_over = False

def draw():
    screen.fill((80, 0, 70))
    if game_over:
        screen.draw.text("Game Over", (100, 100), color=(255, 255, 255), fontsize=60)
        screen.draw.text("Score: " + str(score), (100, 150), color=(255, 255, 255), fontsize=60)
        if score > high_score:
            screen.draw.text("Well done, you have beaten the high score!", (100, 200), color=(255, 0, 0), fontsize=45)
        screen.draw.text('Press "y" key to play again', (100, 250), color=(255, 255, 255), fontsize=45)
    else:
        for gem in gems:
            gem.draw()
        ship.draw()
        screen.draw.text("Score: " + str(score), (15, 10), color=(255, 255, 255), fontsize=30)
        screen.draw.text("High Score: " + str(high_score) + "      Champion:" + best_player, (150, 10), color=(255, 255, 255), fontsize=30)
        screen.draw.text("Lives: " + str(lives), (650, 10), color=(255, 255, 255), fontsize=30)
