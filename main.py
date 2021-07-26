import pygame
import sys
import snake
import fruit
from pygame.locals import *
from config import *
from util import intersect

# Initialise pygame
pygame.init()


def main():

    looping = True
    yummy = False
    score = 0

    player = snake.Snake(SNAKE_POSITION, 3, SNAKE_SIZE)
    curr_fruit = fruit.Fruit(FRUIT_SIZE)

    while looping:
        command = None
        # Input
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and (event.key == K_d or event.key == K_RIGHT) and command is None:
                command = True
            if event.type == pygame.KEYDOWN and (event.key == K_a or event.key == K_LEFT) and command is None:
                command = False

        # Processing
        player.order(command)
        if yummy:
            yummy = False
            player.grow()
        player.creep()
        player.overscreen()

        if intersect(curr_fruit, player):
            curr_fruit = fruit.Fruit(FRUIT_SIZE)
            score += 1
            yummy = True

        # Defining forms

        snake_shape = []
        for chunk in player.body:
            snake_shape.append(pygame.Rect(chunk.position[0], chunk.position[1], chunk.width, chunk.height))
        fruit_shape = pygame.Rect(curr_fruit.position[0], curr_fruit.position[1], FRUIT_SIZE, FRUIT_SIZE)

        score_text = BASIC_FONT.render('score:' + str(score), False, WHITE)

        # Rendering

        if player.die():
            looping = False
            player.color = RED

        WINDOW.fill(BLACK)
        pygame.draw.rect(WINDOW, curr_fruit.color, fruit_shape)
        for shape in snake_shape:
            pygame.draw.rect(WINDOW, player.color, shape)
        WINDOW.blit(score_text, (0, 0))
        pygame.display.update()

        player.speed += 0.01
        fpsClock.tick(int(player.speed))

    restart = True

    while restart:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                main()

        # Display 'Game over' interface
        game_over = BIG_FONT.render('GAME OVER', False, WHITE)
        any_key = BASIC_FONT.render('press any key to restart', False, WHITE)
        WINDOW.blit(game_over, (WINDOW_WIDTH/2 - 120, WINDOW_HEIGHT/2 - 22))
        WINDOW.blit(any_key, (0, WINDOW_HEIGHT - 22))
        pygame.display.update()


main()
