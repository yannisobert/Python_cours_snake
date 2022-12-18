import random
import pygame

from data.SnakeClass import Snake

pygame.init()

# Variables
width = 600
height = 600
display = pygame.display.set_mode((width, height))
block = 10
snake_speed = 15
time = pygame.time.Clock()
best_score = 0

# Images
apple = pygame.transform.scale(pygame.image.load('images/apple.png').convert_alpha(), (10, 10))
snakeHead = pygame.transform.scale(pygame.image.load('images/snake.png').convert_alpha(), (10, 10))
fire = pygame.transform.scale(pygame.image.load('images/fire.png').convert_alpha(), (10, 10))
dead_head = pygame.transform.scale(pygame.image.load('images/dead_head.png').convert_alpha(), (200, 200))

def loose_msg():
    display.blit(pygame.font.Font('font/Grand9K Pixel.ttf', 50).render('You loose.', True, (255, 0, 0)), [160, 100])
    display.blit(dead_head, [200, 300])

class Score :
    def your_score(score):
        display.blit(
            pygame.font.Font('font/Grand9K Pixel.ttf', 20).render("Your score: " + str(score), True, (255, 255, 255)),[0, 0])
    def your_best_score(best_score):
        display.blit(pygame.font.Font('font/Grand9K Pixel.ttf', 20).render("Your best score: " + str(best_score), True, (255, 255, 255)), [0, 50])

snake = Snake()

def gameLoop(best_score):
    game_over = False
    game_close = False
    x1 = 300
    y1 = 300
    x1_change = 0
    y1_change = 0
    snake_size = []
    length_of_snake = 1
    # Random apple
    x_apple = round(random.randrange(0, width) / 10.0) * 10.0
    y_apple = round(random.randrange(10, height) / 10.0) * 10.0
    # Random fire
    x_fire = round(random.randrange(0, width) / 10.0) * 10.0
    y_fire = round(random.randrange(0, height) / 10.0) * 10.0
    while not game_over:
        while game_close == True:
            display.fill((0, 0, 0))
            loose_msg()
            Score.your_score(length_of_snake - 1)

            if best_score < length_of_snake - 1:
                Score.your_best_score(length_of_snake - 1)
            else:
                Score.your_best_score(best_score)
            pygame.display.update()
            for event in pygame.event.get():
                if best_score < length_of_snake - 1:
                    best_score = length_of_snake - 1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameLoop(best_score)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                # left
                if event.key == pygame.K_LEFT and x1_change != snake.y_positive:
                    x1_change = snake.moveLeft()
                    y1_change = 0
                # right
                if event.key == pygame.K_RIGHT and x1_change != snake.y_negative:
                    x1_change = snake.moveRight()
                    y1_change = 0
                # up
                if event.key == pygame.K_UP and y1_change != snake.y_positive:
                    y1_change = snake.moveUp()
                    x1_change = 0
                # down
                if event.key == pygame.K_DOWN and y1_change != -snake.y_negative:
                    y1_change = snake.moveDown()
                    x1_change = 0
        # borders
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        display.fill((0, 0, 0))
        display.blit(apple, [x_apple, y_apple, block, block])
        display.blit(fire, [x_fire, y_fire, block, block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_size.append(snake_Head)
        if len(snake_size) > length_of_snake:
            del snake_size[0]
        # if snake touch him
        for x in snake_size[:-1]:
            if x == snake_Head:
                game_close = True
        for x in snake_size:
            display.blit(snakeHead, [x[0], x[1], block, block])

        Score.your_score(length_of_snake - 1)

        if best_score < length_of_snake - 1:
            Score.your_best_score(length_of_snake - 1)
        else:
            Score.your_best_score(best_score)
        pygame.display.update()
        pygame.display.update()
        # If the coordonates of the head of the snake is on the apple
        if x1 == x_apple and y1 == y_apple:
            x_apple = round(random.randrange(0, width) / 10.0) * 10.0
            y_apple = round(random.randrange(0, height) / 10.0) * 10.0
            length_of_snake += 1
            x_fire = round(random.randrange(0, width) / 10.0) * 10.0
            y_fire = round(random.randrange(0, height) / 10.0) * 10.0
        # If the coordonates of the head of the snake is on the block
        if x1 == x_fire and y1 == y_fire:
            x_fire = round(random.randrange(0, width) / 10.0) * 10.0
            y_fire = round(random.randrange(0, height) / 10.0) * 10.0
            game_close = True
        time.tick(snake_speed)
    pygame.quit()
    quit()

gameLoop(best_score)