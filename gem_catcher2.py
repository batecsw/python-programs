# Write your code here :-)
import random

WIDTH = 800
HEIGHT = 600
score = 0
game_over = False

ship = Actor('playership1_red')
ship.x = 570
ship.y = 450

gem = Actor('alien')
gem.x = gem.x = random.randint(20, 780)
gem.y = 0

def update():
    global score, game_over

    if keyboard.left:
        ship.x = ship.x - 5
    if keyboard.right:
        ship.x = ship.x + 5

    gem.y = gem.y + 3 + score/5
    if gem.y > HEIGHT:
        game_over = True
    if gem.colliderect(ship):
        gem.x = random.randint(20, 780)
        gem.y = 0
        score = score + 1


def draw():
    screen.fill((80,0,70))

    if game_over:
        screen.draw.text('Game Over' , (360, 300) , color=(255,255,255), fontsize = 30)
        screen.draw.text('Final Score: ' + str(score) , (360, 350), color=(255,255,255), fontsize = 30)
    else:
        ship.draw()
        gem.draw()
        screen.draw.text('Score: ' + str(score) , (15,10), color=(255,255,255), fontsize = 30)
