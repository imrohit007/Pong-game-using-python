import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Set up the game clock
clock = pygame.time.Clock()

# Set up the paddles
paddle_width = 10
paddle_height = 100
paddle_speed = 5
player1_paddle = pygame.Rect(50, (screen_height / 2) - (paddle_height / 2), paddle_width, paddle_height)
player2_paddle = pygame.Rect(screen_width - 50 - paddle_width, (screen_height / 2) - (paddle_height / 2), paddle_width, paddle_height)

# Set up the ball
ball_width = 10
ball_speed = 5
ball_direction = random.choice([(1, 1), (-1, 1), (1, -1), (-1, -1)])
ball = pygame.Rect((screen_width / 2) - (ball_width / 2), (screen_height / 2) - (ball_width / 2), ball_width, ball_width)

# Set up the score
score_font = pygame.font.Font(None, 50)
player1_score = 0
player2_score = 0

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1_paddle.move_ip(0, -paddle_speed)
    if keys[pygame.K_s]:
        player1_paddle.move_ip(0, paddle_speed)
    if keys[pygame.K_UP]:
        player2_paddle.move_ip(0, -paddle_speed)
    if keys[pygame.K_DOWN]:
        player2_paddle.move_ip(0, paddle_speed)

    # Move the ball
    ball.move_ip(ball_speed * ball_direction[0], ball_speed * ball_direction[1])

    # Check for collision with walls
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_direction = (ball_direction[0], -ball_direction[1])

    # Check for collision with paddles
    if ball.colliderect(player1_paddle) or ball.colliderect(player2_paddle):
        ball_direction = (-ball_direction[0], ball_direction[1])

    # Check for out of bounds
    if ball.left <= 0:
        player2_score += 1
        ball_direction = random.choice([(1, 1), (-1, 1), (1, -1), (-1, -1)])
        ball.center = (screen_width / 2, screen_height / 2)
    if ball.right >= screen_width:
        player1_score += 1
        ball_direction = random.choice([(1, 1), (-1, 1), (1, -1), (-1, -1)])
        ball.center = (screen_width / 2, screen_height / 2)

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the paddles
    pygame.draw.rect(screen, (255, 255, 255), player1_paddle)
    pygame.draw.rect(screen, (255, 255, 255), player2_paddle)

    # Draw the ball
    pygame.draw.rect(screen, (255, 255, 255), ball)

    # Draw the score
    player1_score_text = score_font.render(str(player1_score), True, (255, 255, 255))
    player2_score_text = score_font.render(str(player2_score), True, (255, 255, 255))
    screen.blit(player1_score_text, (screen_width / 4, 10))
    screen.blit(player2_score_text, (3 * screen_width / 4, 10))

    # Update the screen
    pygame.display.update()

    # Check for game over
    if player1_score == 10 or player2_score == 10:
        game_over_font = pygame.font.Font(None, 100)
        if player1_score == 10:
            game_over_text = game_over_font.render("Player 1 wins!", True, (255, 255, 255))
        else:
            game_over_text = game_over_font.render("Player 2 wins!", True, (255, 255, 255))
        screen.blit(game_over_text, ((screen_width / 2) - (game_over_text.get_width() / 2), (screen_height / 2) - (game_over_text.get_height() / 2)))
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.quit()
        quit()

    # Limit the frame rate
    clock.tick(60)

