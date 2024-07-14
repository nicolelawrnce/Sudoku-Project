import pygame, sys
from cell import *
pygame.init()
class Board:
    def __init__(self,width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
    def draw(self):
        # reset button
        reset = pygame.font.SysFont('Arial', 30)
        reset_screen = reset.render('Reset', False, (0, 0, 0))
        self.screen.blit(reset_screen, (55, 620))

        # restart button
        restart = pygame.font.SysFont('Arial', 30)
        restart_screen = restart.render('Restart', False, (0, 0, 0))
        self.screen.blit(restart_screen, (250, 620))

        # exit button
        exit = pygame.font.SysFont('Arial', 30)
        exit_screen = exit.render('Exit', False, (0, 0, 0))
        self.screen.blit(exit_screen, (475, 620))

        # horizontal line:
        for i in range(0, 4):
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * 200), (600, i * 200), 4)
        # vertical line:
        for i in range(0, 4):
            pygame.draw.line(self.screen, (0, 0, 0), (i * 200, 0), (i * 200, 600), 4)
        # smaller horizontal lines:
        for i in range(1, 9):
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * 600 / 9), (600, i * 600 / 9), 2)
        # smaller vertical lines:
        for i in range(1, 9):
            pygame.draw.line(self.screen, (0, 0, 0), (i * 600 / 9, 0), (i * 600 / 9, 600), 2)
    def set(self,board):
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != 0:
                    placer = Cell1(board[i][j], i + 1, j + 1, self.screen)
                    placer.draw((0, 0, 0))
                else:
                    x_exact = ((i + 1) * (600 / 9)) - 600 / 18 - 9
                    y_exact = ((j + 1) * (600 / 9)) - 600 / 18 - 20
                    pygame.draw.circle(self.screen, (255, 255, 255), (x_exact, y_exact), 10)