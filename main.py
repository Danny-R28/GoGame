import pygame
from sys import exit
import numpy as np
import time

# קצב עידכון המסך 60 פעמים בשנייה
FRAME_RATE = 60

# גובה המסך
HIGHT = 800
# אורך המסך
WIDTH = 800

BG_COLOR = 'burlywood2'




class Board(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        self.step_size = int(400 / self.size)

    def draw(self, screen):
        xs = np.linspace(100, 700, self.size)
        ys = np.linspace(100, 700, self.size)

        for i in range(self.size):
            pygame.draw.line(screen, 'black', start_pos=(xs[i], ys[0]), end_pos=(xs[i], ys[-1]))

        for i in range(self.size):
            pygame.draw.line(screen, 'black', start_pos=(xs[0], ys[i]), end_pos=(xs[-1], ys[i]))

        for x_i in [3, self.size // 2, -4]:
            for y_i in [3, self.size // 2, -4]:
                pygame.draw.circle(screen, 'black', (xs[x_i], ys[y_i]), 5)


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HIGHT))

    # כותרת
    pygame.display.set_caption('משחק גו של בן')
    clock = pygame.time.Clock()

    print('hello world')
    board = Board(pos=(50, 50), size=19)

    cells = [[None for _ in range(19)] for _ in range(19)]

    turn = 'black'

    while True:
        screen.fill(BG_COLOR)
        board.draw(screen)

        for i in range(19):
            for j in range(19):
                val = cells[i][j]
                if val is not None:
                    pygame.draw.circle(screen, val, (i * 33.3 + 100, j * 33.3 + 100), 10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if event.button == 1:
                    print(f'button 1 pressed, pos : {(x, y)}')
                if event.button == 2:
                    print(f'button 2 pressed, pos : {(x, y)}')
                if event.button == 3:
                    print(f'button 3 pressed, pos : {(x, y)}')
                    i = int((x - 100 + 33.3 / 2 ) // 33.3)
                    j = int((y - 100 + 33.3 / 2 ) // 33.3)
                    cells[i][j] = turn
                    turn = 'white' if turn == 'black' else 'black'

            #     elif event.key == pygame.K_d:
            #         board.deal()
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 1:
            #         pos = pygame.mouse.get_pos()
            #         board.press(pos)


        # תעדכן את התמונה על המסך
        pygame.display.update()
        # תחכה שייעבור זמן לעידכון נוסף
        clock.tick(FRAME_RATE)

if __name__ == '__main__':
    main()
