import pgzrun
import random

WIDTH = 800
HEIGHT = 600

ship = Actor('playership1_red')
ship.x = 370
ship.y = 550

gem = Actor('gemgreen')
gem.x = random.randint(20, 780)
gem.y = 0

score = 0
lives = 3
game_over = False
high_score = 0

def on_mouse_move(pos, rel, buttons):
    ship.x = pos[0]

def update():
    global score, high_score, lives, game_over
    if not game_over:
        if keyboard.left:
            ship.x = ship.x - 5
        if keyboard.right:
            ship.x = ship.x + 5

        if ship.x < 0:
            ship.x = WIDTH
        if ship.x > WIDTH:
            ship.x =0

        gem.y = gem.y + 4 + score / 5

        if gem.y > 600:
            gem.x = random.randint(20, 780)
            gem.y = 0
            lives = lives - 1


        if lives == 0:
            game_over = True

        if gem.colliderect(ship):
            gem.x = random.randint(20, 780)
            gem.y = 0
            score = score + 1

    else:
        if keyboard.y:
            if score > high_score:
                high_score = score
            score = 0
            lives = 3
            game_over = False

def draw():
    screen.fill((80,0,70))
    if game_over:
        screen.draw.text('Game Over', (100, 100), color=(255,255,255), fontsize=60)
        screen.draw.text('Score: ' + str(score), (100, 150), color=(255,255,255), fontsize=60)
        if score > high_score:
            screen.draw.text('Well done, you have beaten the high score!', (100, 200), color=(255,0,0), fontsize=45)
        screen.draw.text('Press "y" key to play again', (100, 250), color=(255,255,255), fontsize=45)
    else:
        gem.draw()
        ship.draw()
        screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)
        screen.draw.text('High Score: ' + str(high_score), (250,10), color=(255,255,255), fontsize=30)
        screen.draw.text('Lives: ' + str(lives), (500,10), color=(255,255,255), fontsize=30)

pgzrun.go() # Must be last line
