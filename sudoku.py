from cell import *
from Board import *
from sudoku_generator import *
import copy
def main():
    import pygame, sys
    pygame.init()
    screen = pygame.display.set_mode((600,670))
    pygame.display.set_caption("Sudoku")
    screen.fill((255,255,255))
    pygame.font.init()
    welcome = pygame.font.SysFont('Arial', 70)
    welcome_screen = welcome.render('Welcome To Sudoku', False, (0, 0, 0))
    screen.blit(welcome_screen, (40,100))
    mode = pygame.font.SysFont('Arial', 50)
    mode_screen = mode.render('Select Mode', False, (0, 0, 0))
    screen.blit(mode_screen, (188,300))
    hard = pygame.font.SysFont('Arial', 40)
    hard_screen = hard.render('Hard', False, (0, 0, 0))
    screen.blit(hard_screen, (150,400))
    medium = pygame.font.SysFont('Arial', 40)
    medium_screen = medium.render('Medium', False, (0, 0, 0))
    screen.blit(medium_screen, (240,400))
    easy = pygame.font.SysFont('Arial', 40)
    easy_screen = easy.render('Easy', False, (0, 0, 0))
    screen.blit(easy_screen, (370,400))

    count = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and count == 0:
                count += 1
                x,y = event.pos
                if 400<y<450 and 143<=x<=230:
                    mode = "hard"
                    removed_cells = 50
                elif 400<y<450 and 231<=x<=364:
                    mode = "medium"
                    removed_cells = 40
                elif 400<y<450 and 365<=x<=454:
                    mode = "easy"
                    removed_cells = 30
                screen.fill((255, 255, 255))
                board = Board(600,600,screen,mode)
                board.draw()
                number_board = SudokuGenerator(9, removed_cells)
                number_board.fill_values()
                full_board = number_board.get_board()
                final = []
                for i in range(len(full_board)):
                    lst = []
                    for j in range(len(full_board)):
                        lst.append(full_board[i][j])
                    final.append(lst)
                number_board.remove_cells()
                nboard = number_board.get_board()
                og_board = []
                for i in range(len(full_board)):
                    lst = []
                    for j in range(len(full_board)):
                        lst.append(full_board[i][j])
                    og_board.append(lst)
                boardo = og_board[:]
                board.set(nboard)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                col = int((x//66.66) + 1)
                row = int((y//66.66) + 1)
                if y>600 and x<200:
                    screen.fill((255, 255, 255))
                    board1 = Board(600,600,screen,mode)
                    board1.draw()
                    print(boardo)
                    board1.set(boardo)
                    number_board.board = boardo
                elif y>600 and 200<=x<400:
                    main()
                elif y>600 and 400<=x<=600:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    num = 1
                elif event.key == pygame.K_2:
                    num = 2
                elif event.key == pygame.K_3:
                    num = 3
                elif event.key == pygame.K_4:
                    num = 4
                elif event.key == pygame.K_5:
                    num = 5
                elif event.key == pygame.K_6:
                    num = 6
                elif event.key == pygame.K_7:
                    num = 7
                elif event.key == pygame.K_8:
                    num = 8
                elif event.key == pygame.K_9:
                    num = 9
                else:
                    pass
                if number_board.get_board()[row-1][col-1] != 0:
                    pass
                elif final[row-1][col-1] == num:
                    number_board.get_board()[row-1][col-1] = num
                    count = 0
                    for i in range(len(number_board.get_board())):
                        for j in range(len(number_board.get_board())):
                            if number_board.get_board()[i][j] != 0:
                                count+=1

                    if count != 81:
                        placer = Cell1(num,row,col,screen)
                        placer.draw((128,128,128))
                    else:
                        screen.fill((255, 255, 255))
                        if number_board.get_board() == final:
                            gamewon = pygame.font.SysFont('Arial', 70)
                            gamewon_screen = gamewon.render('GAME WON!', False, (0, 0, 0))
                            screen.blit(gamewon_screen, (130, 250))
                        else:
                            gameover = pygame.font.SysFont('Arial', 70)
                            gameover_screen = gameover.render('GAME OVER', False, (0, 0, 0))
                            screen.blit(gameover_screen, (130, 250))

                else:
                    number_board.get_board()[row - 1][col - 1] = num
                    count = 0
                    for i in range(len(number_board.get_board())):
                        for j in range(len(number_board.get_board())):
                            if number_board.get_board()[i][j] != 0:
                                count += 1
                    if count != 81:
                        placer = Cell1(num, row, col, screen)
                        placer.draw((255, 0, 0))
                    else:
                        screen.fill((255, 255, 255))
                        if number_board.get_board() == final:
                            gamewon = pygame.font.SysFont('Arial', 70)
                            gamewon_screen = gamewon.render('GAME WON!', False, (0, 0, 0))
                            screen.blit(gamewon_screen, (130, 250))
                        else:
                            gameover = pygame.font.SysFont('Arial', 70)
                            gameover_screen = gameover.render('GAME OVER', False, (0, 0, 0))
                            screen.blit(gameover_screen, (130, 250))
        pygame.display.update()
if __name__ == "__main__":
    main()