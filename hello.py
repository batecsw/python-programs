from random import randint

WIDTH = 800
HEIGHT = 600

ship = Actor('playership1_red')
ship.x = 370
ship.y = 550

gem = Actor('gemgreen')
gem.x = randint(20, 780)
gem.y = 0

lives = 3
score = 0
high_score = 0
game_over = False

def on_mouse_move(pos, rel, buttons):
    ship.x = pos[0]

def update():
    global score, high_score, high_name, lives, game_over

    if keyboard.left:
        ship.x = ship.x - 10
    if keyboard.right:
        ship.x = ship.x + 10
    if ship.x < 0:
        ship.x = 800
    if ship.x > 800:
        ship.x = 0

    gem.y = gem.y + 4 + score / 5
    if gem.y > 600:
        new_gem()
        lives = lives - 1
    if lives < 1:
        game_over = True
    if gem.colliderect(ship):
        new_gem()
        score = score + 1
    if (game_over and keyboard.y):
        if score > high_score:
            high_score = score
        score = 0
        lives = 3
        game_over = False

def new_gem():
    gem.x = randint(20, 780)
    gem.y = 0

def draw():
    screen.fill((80,0,70))
    if game_over:
        screen.draw.text('Game Over', (100, 100), color=(255,255,255), fontsize=50)
        screen.draw.text('Score: ' + str(score), (100, 150), color=(255,255,255), fontsize=50)
        screen.draw.text('Press "Y" key to play again', (100, 300), color=(255,255,255), fontsize=40)
        if score > high_score:
            screen.draw.text("Congratulations! You've beaten the high score!", (100, 200), color=(255,255,255), fontsize=40)

    else:
        gem.draw()
        ship.draw()
        screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)
        screen.draw.text('Lives: ' + str(lives), (670,10), color=(255,255,255), fontsize=30)
        screen.draw.text('High Score: ' + str(high_score), (330,10), color=(255,255,255), fontsize=30)
