import pygame
from checkers import WIDTH, HEIGHT, Board, SQUARE_SIZE, Game, TEAL, WHITE, BROWN, DARK_GREEN
from minimax.algo import *

FPS = 60
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")
game = Game(screen)

is_running = True
clock = pygame.time.Clock()


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


screen.fill(BROWN)
font = pygame.font.Font(None, 36)
font_last = pygame.font.Font(None, 100)
playButton = pygame.Rect(280, 250, 200, 100)
exitButton = pygame.Rect(280, 400, 200, 100)
singleButton = pygame.Rect(280, 250, 200, 100)
twoButton = pygame.Rect(280, 400, 200, 100)
easyButton = pygame.Rect(280, 200, 200, 100)
mediumButton = pygame.Rect(280, 350, 200, 100)
hardButton = pygame.Rect(280, 500, 200, 100)

def game_ai(depth):
    is_running_game = True
    while is_running_game:
        clock.tick(FPS)

        if game.turn == WHITE:
            value, new_board = minimaxab(game.get_board(), depth, WHITE, game)
            game.ai_move(new_board)

        if game.winner() is not None:
            if game.winner() == WHITE:
                won_game("AI")
            else:
                won_game("You")

        if game.turn == WHITE:
            best_valid_moves = {}
            for piece in game.board.get_all_pieces(WHITE):
                valid_moves = game.board.get_valid_moves(piece)
                if valid_moves != {}:
                    best_valid_moves = valid_moves
            if best_valid_moves == {}:
                won_game("You")

        if game.turn == TEAL :
            best_valid_moves = {}
            for piece in game.board.get_all_pieces(TEAL ):
                valid_moves = game.board.get_valid_moves(piece)
                if valid_moves != {}:
                    best_valid_moves = valid_moves
            if best_valid_moves == {}:
                won_game("AI")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running_game = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()

def won_game(type):
    if type == "AI" or type == "Player 2":
        color = WHITE
    else:
        color = TEAL

    run = True
    while run:
        clock.tick(FPS)

        screen.fill(BROWN)
        text = font_last.render(f"{type} WON !!!", True, color)
        text_rect = text.get_rect(center=(400, 350))
        screen.blit(text, text_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    global is_running
    is_running = False
    pygame.quit()


def game_two():
    is_running_game = True
    clock = pygame.time.Clock()
    game = Game(screen)

    while is_running_game:
        clock.tick(FPS)

        if game.winner() is not None:
            if game.winner() == WHITE:
                won_game("Player 2")
            else:
                won_game("Player 1")

        if game.turn == WHITE:
            best_valid_moves = {}
            for piece in game.board.get_all_pieces(WHITE):
                valid_moves = game.board.get_valid_moves(piece)
                if valid_moves != {}:
                    best_valid_moves = valid_moves
            if best_valid_moves == {}:
                won_game("Player 1")

        if game.turn == TEAL:
            best_valid_moves = {}
            for piece in game.board.get_all_pieces(TEAL):
                valid_moves = game.board.get_valid_moves(piece)
                if valid_moves != {}:
                    best_valid_moves = valid_moves
            if best_valid_moves == {}:
                won_game("Player 2")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running_game = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()


while is_running:
    clock.tick(FPS)

    pygame.draw.rect(screen, TEAL, playButton, border_radius=50)
    text = font.render("Play Game", True, (0, 0, 0))
    text_rect = text.get_rect(center=playButton.center)
    screen.blit(text, text_rect)

    pygame.draw.rect(screen, WHITE, exitButton, border_radius=50)
    text = font.render("Exit Game", True, (0, 0, 0))
    text_rect = text.get_rect(center=exitButton.center)
    screen.blit(text, text_rect)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if playButton.collidepoint(pos):
                while is_running:

                    pygame.draw.rect(screen, TEAL, singleButton, border_radius=50)
                    text = font.render("Single Player", True, (0, 0, 0))
                    text_rect = text.get_rect(center=singleButton.center)
                    screen.blit(text, text_rect)

                    pygame.draw.rect(screen, WHITE, twoButton, border_radius=50)
                    text = font.render("Two Player", True, (0, 0, 0))
                    text_rect = text.get_rect(center=twoButton.center)
                    screen.blit(text, text_rect)
                    pygame.display.update()

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            is_running = False

                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pos = pygame.mouse.get_pos()
                            if singleButton.collidepoint(pos):
                                screen.fill(BROWN)
                                while is_running:

                                    pygame.draw.rect(screen, WHITE, easyButton, border_radius=50)
                                    text = font.render("Easy Mode", True, (0, 0, 0))
                                    text_rect = text.get_rect(center=easyButton.center)
                                    screen.blit(text, text_rect)

                                    pygame.draw.rect(screen, TEAL, mediumButton, border_radius=50)
                                    text = font.render("Medium Mode", True, (0, 0, 0))
                                    text_rect = text.get_rect(center=mediumButton.center)
                                    screen.blit(text, text_rect)
                                    pygame.display.update()

                                    pygame.draw.rect(screen, DARK_GREEN, hardButton, border_radius=50)
                                    text = font.render("Hard Mode", True, (0, 0, 0))
                                    text_rect = text.get_rect(center=hardButton.center)
                                    screen.blit(text, text_rect)
                                    pygame.display.update()

                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            is_running = False

                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                            pos = pygame.mouse.get_pos()

                                            if easyButton.collidepoint(pos):
                                                game_ai(1)
                                            elif mediumButton.collidepoint(pos):
                                                game_ai(2)
                                            elif hardButton.collidepoint(pos):
                                                game_ai(4)

                            elif twoButton.collidepoint(pos):
                                game_two()

            elif exitButton.collidepoint(pos):
                is_running = False

pygame.quit()

