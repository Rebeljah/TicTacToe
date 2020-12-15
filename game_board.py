'''game_board.py'''


def get_new_game():
    board = get_blank_board()

    # get game mode
    game_mode = ask_game_mode()

    # get player characters
    p1_char = ask_p1_char()

    p2_char = get_opposite_char(p1_char)

    return board, game_mode, p1_char, p2_char


def get_blank_board():
    '''Returns a square array with each element set to ' ' '''
    board_size = 3
    blank_row = [' '] * board_size

    board = [blank_row[:] for row in range(board_size)]

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


def ask_p1_char():
    p1_char = ''
    while p1_char not in ('X', 'O'):
        print('-' * 58)
        p1_char = input('Player 1, Choose X or O\n'
                        'Choice (x or o): ').upper()

    return p1_char


def get_opposite_char(char):
    if char == 'X':
        opposite_char = 'O'
    else:
        opposite_char = 'X'
    return opposite_char


def player_make_move(board, p1_char, p2_char, turn):
    '''Let the player decide which box number to place his/her character in
       Return the board after the player has made a move.'''
    board_size = len(board)
    player_char = get_current_char(p1_char, p2_char, turn)

    possible_choices = board_size**2
    box_choice = None
    while box_choice not in range(1, possible_choices + 1):
        print('-' * 58 + '\n',
              turn, ', choose a box to place an ', player_char, ' in it.',
              sep='')
        box_choice = int(input('Box #: '))

    # match the player selection to a box on the board
    box_num = 0
    for r_idx in range(board_size):
        for c_idx in range(board_size):
            box_num += 1
            if box_num == box_choice:
                board[r_idx][c_idx] = player_char

    return board


def get_current_char(p1_char, p2_char, turn):
    if turn == 1:
        return p1_char
    return p2_char


def find_empty_boxes(board):
    '''Return a list of index pairs for each empty element in the board'''
    empty_boxes = []
    for r_idx, row in enumerate(board):
        for c_idx, col in enumerate(row):
            if col == ' ':
                empty_boxes.append((r_idx, c_idx))

    return empty_boxes


def refresh_display(board):
    '''display the board to the terminal'''
    print('-' * 58)
    for row in board:
        print(row)


def get_next_turn(current_turn):
    '''Takes either 1 or 2 as input and returns the opposite number'''

    if current_turn in ('', 2):
        return 1
    return 2
