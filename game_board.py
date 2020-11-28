

def get_new_game():
    board = get_blank_board()

    # get game mode
    game_mode = ask_game_mode()

    # get player characters
    p1_char = ''
    while p1_char not in ('X', 'O'):
        print('-' * 58)
        p1_char = input('Player 1, Choose X or O\n'
                        'Choice (x or o): ').upper()

    p2_char = get_opposite_char(p1_char)

    return board, game_mode, p1_char, p2_char


def get_blank_board():
    # create a 2d "board".
    # row and column count correspond to board size

    board_size = 3
    board = []
    for row in range(board_size):
        board.append([' '] * board_size)

    return board


def ask_game_mode():
    mode = ''
    while mode not in [1, 2]:
        print('-' * 58 + '\n',
              'Select an option:\n'
              '# 1 - PLAYER V. PLAYER\n'
              '# 2 - PLAYER VS. CPU', sep='')
        mode = int(input('Choice (enter a number): '))

    if mode == 1:
        mode = 'PVP'
    else:
        mode = 'PVE'

    return mode


def get_opposite_char(char):
    if char == 'X':
        opposite_char = 'O'
    else:
        opposite_char = 'X'
    return opposite_char


def player_make_move(board, p1_char, p2_char, turn):
    board_size = len(board)
    player_char = get_current_char(p1_char, p2_char, turn)

    possible_choices = board_size**2
    box_choice = ''
    while box_choice not in range(1, possible_choices + 1):
        print('-' * 58 + '\n',
              turn, ', choose a box to place an ', player_char, ' in it.',
              sep='')
        box_choice = int(input('Box #: '))

    # match the player selection to a box on the board
    box_num = 0
    for row in range(board_size):
        for col in range(board_size):
            box_num += 1
            if box_num == box_choice:
                board[row][col] = player_char

    return board


def get_current_char(p1_char, p2_char, turn):  # TODO - this can be done w/ dictionaries
    if turn == 1:
        return p1_char
    else:
        return p2_char


def find_empty_boxes(board):
    empty_boxes = []
    box_num = 0
    for row in board:
        for col in row:
            box_num += 1
            if col == ' ':
                empty_boxes.append(box_num)

    return empty_boxes


def refresh_display(board):
    print('-' * 58)
    for row in board:
        print(row)
