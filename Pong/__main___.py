import pygame

pygame.init()

window = pygame.display.set_mode([1280, 720])
window_title = pygame.display.set_caption("Futeball Pong")

win = pygame.image.load("assets/win.png")

score1 = 0
score1_image = pygame.image.load("assets/score/" + str(score1) + ".png")
score2 = 0
score2_image = pygame.image.load("assets/score/" + str(score2) + ".png")

field = pygame.image.load("assets/field.png")

player1 = pygame.image.load("assets/player1.png")
player1_y = 287
player1_move_up = False
player1_move_down = False

player2 = pygame.image.load("assets/player2.png")
player2_y = 287

ball = pygame.image.load("assets/ball.png")
ball_x = 617
ball_y = 337
ball_dir_x = -6
ball_dir_y = -2

ball_speed_x = -6
ball_speed_y = 1

loop = True

def draw():

    if score1 or score2 < 9:
        window.blit(field, (0, 0))
        window.blit(player1, (50, player1_y))
        window.blit(player2, (1150, player2_y))
        window.blit(ball, (ball_x, ball_y))
        window.blit(score1_image, (500, 50))
        window.blit(score2_image, (710, 50))

        move_ball()
        move_player()

    else:
        window.blit(win, (300, 300))

def move_ball():
    global ball_x
    global ball_y
    global ball_dir_x
    global ball_dir_y
    global score1
    global score2
    global score1_image
    global score2_image

    ball_x += ball_dir_x
    ball_y += ball_dir_y

    if ball_x < 128 and player1_y < ball_y + 23 < player1_y + 146:
        ball_dir_x *= -1
        ball_dir_x += 1
        ball_dir_y += 1

    if ball_x > 1100 and player2_y < ball_y + 23 < player2_y + 146:
        ball_dir_x *= -1
        ball_dir_x -= 1
        ball_dir_y += 1

    if ball_y < 0:
        ball_dir_y *= -1
    elif ball_y > 680:
        ball_dir_y *= -1

    if ball_x < 0:
        score2 += 1
        ball_x = 617
        ball_y = 337
        ball_dir_x *= -1
        ball_dir_y *= -1
        score2_image = pygame.image.load("assets/score/" + str(score2) + ".png")
        ball_dir_x = ball_speed_x
        ball_dir_y = ball_speed_y

    elif ball_x > 1280:
        score1 += 1
        ball_x = 617
        ball_y = 337
        ball_dir_x *= -1
        ball_dir_y *= -1
        score1_image = pygame.image.load("assets/score/" + str(score1) + ".png")
        ball_dir_x = ball_speed_x
        ball_dir_y = ball_speed_y

def move_player():
    global player1_y
    global player2_y

    if player1_move_up:
        player1_y -= 5
    if player1_move_down:
        player1_y += 5

    if player1_y < 0:
        player1_y = 0
    elif player1_y > 575:
        player1_y = 575

    player2_y = ball_y

while loop:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            loop = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1_move_up = True
            if event.key == pygame.K_s:
                player1_move_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player1_move_up = False
            if event.key == pygame.K_s:
                player1_move_down = False

    draw()

    pygame.display.update()