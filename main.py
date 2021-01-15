import pygame
import random
import sys

fps = 30
clock = pygame.time.Clock()
draw = False
position = [0, 0]
list_balls = []

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color('black'))
    pygame.display.set_caption('Шарики')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                r = random.randrange(0, 255)
                g = random.randrange(0, 255)
                b = random.randrange(0, 255)
                R = random.randrange(5, 50)
                v = [random.randrange(-4, 7), random.randrange(-4, 7)]
                while v[0] == 0 and v[1] == 0:
                    v = [random.randrange(-4, 7), random.randrange(-4, 7)]

                pygame.draw.circle(screen, pygame.Color(r, g, b), event.pos, R, 4)
                list_balls.append([list(event.pos), [v[0], v[1]], (r, g, b), R])
        screen.fill(pygame.Color('black'))
        for i in list_balls:
            if i[0][0] - i[3] < 0:
                i[1][0] = -i[1][0]
            elif i[0][0] + i[3] > width:
                i[1][0] = -i[1][0]
            if i[0][1] - i[3] < 0:
                i[1][1] = -i[1][1]
            elif i[0][1] + i[3] > height:
                i[1][1] = -i[1][1]

            i[0][0] += i[1][0]
            i[0][1] += i[1][1]
            pygame.draw.circle(screen, (i[2]), i[0], i[3], 4)

        clock.tick(fps)
        pygame.display.flip()
    sys.exit()
