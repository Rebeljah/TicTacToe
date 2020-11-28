

def get_winner(board, p1_char, p2_char):

    hoz_lines = get_hoz_rows(board)
    vert_lines = get_vert_rows(board)
    diag_lines = get_diag_rows(board)
    board_size = len(board)

    winner = ''
    for line_type in [hoz_lines, vert_lines, diag_lines]:
        for line in line_type:
            is_win = True  # switches to False if not a winning line
            for idx in range(board_size):
                if line[idx] != line[0] or line[0] == ' ':
                    is_win = False

            if is_win:
                if line[0] == p1_char:
                    winner = 1
                else:
                    winner = 2

    return winner


def get_hoz_rows(board):
    hoz_rows = []
    for hoz_row in board:
        hoz_rows.append(hoz_row)
    return hoz_rows


def get_vert_rows(board):
    vert_rows = []
    for column in range(len(board)):
        vert_row = []
        for hoz_row in board:
            vert_row.append(hoz_row[column])
        vert_rows.append(vert_row)
    return vert_rows


def get_diag_rows(board):
    diag_length = len(board)
    max_index = diag_length - 1

    diag_rows = []
    for diag_row_num in range(2):
        if diag_row_num == 0:
            row_idx, col_idx = 0, 0  # start point of downwards line
            row_shift, col_shift = 1, 1
        elif diag_row_num == 1:
            row_idx, col_idx, = max_index, 0  # start point of upwards line
            row_shift, col_shift = -1, 1

        diag_row = []
        for box in range(diag_length):
            diag_row.append(board[row_idx][col_idx])
            row_idx += row_shift
            col_idx += col_shift
        diag_rows.append(diag_row)
    return diag_rows


def get_next_turn(turn):
    if turn == '' or turn == 2:
        return 1
    else:
        return 2
