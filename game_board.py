

def get_new_game():
    board_size = 5
    board = []
    for row in range(board_size):
        board.append([' '] * board_size)

    # get game mode
    game_mode = ''
    while game_mode not in ['1', '2']:
        print('-' * 58)
        game_mode = input('Select an option:\n'
                          '# 1 - PLAYER V. PLAYER\n'
                          '# 2 - PLAYER VS. CPU\n'
                          'Choice (enter a number): ')
    if game_mode == '1':
        game_mode = 'PVP'
    elif game_mode == '2':
        game_mode = 'PVE'

    # get player characters
    p1_char = ''
    while p1_char not in ['X', 'O']:
        print('-' * 58)
        p1_char = input('Player 1, Choose X or O\n'
                        'Choice (x or o): ').upper()
    if p1_char == 'X':
        p2_char = 'O'
    else:
        p2_char = 'X'

    return board, game_mode, p1_char, p2_char


def player_make_move(board, p1_char, p2_char, turn):
    board_size = len(board)
    # choose the char to use
    if turn == 'p1':
        player_char = p1_char
    else:
        player_char = p2_char

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


def refresh_display(board):
    for row in board:
        print(row)
