'''observer.py'''


def get_winner(board, p1_char, p2_char):
    board_size = len(board)

    hoz_rows = get_hoz_rows(board)
    vert_rows = get_vert_rows(board)
    diag_rows = get_diag_rows(board)

    for type in (hoz_rows, vert_rows, diag_rows):
        for row in type:
            is_win = True  # True as default then test for lose conditions
            if row[0][1] == ' ':
                is_win = False
            else:
                for idx in range(1, board_size):
                    if row[idx][1] != row[0][1]:
                        is_win = False

            if is_win:  # if no lose conditions were found in the row
                if row[0][1] == p1_char:
                    winner = 1
                else:
                    winner = 2
                return winner, row
    return None, None  # no winning line found


def get_hoz_rows(board):
    size = len(board)
    rows = []

    for row in range(size):
        rows.append([((row, col), board[row][col]) for col in range(size)])

    return rows


def get_vert_rows(board):
    size = len(board)
    rows = []

    for col in range(size):
        rows.append([((row, col), board[row][col]) for row in range(size)])

    return rows


def get_diag_rows(board):
    size = len(board)

    rows = [[], []]
    for i in range(size):
        rows[0].append(((i, i), board[i][i]))
        rows[1].append(((i, -i - 1), board[i][-i - 1]))

    return rows


def find_empty_indices(board):
    '''Return a list of index pairs for each empty element in the board'''
    empty_indices = []
    for r_idx, row in enumerate(board):
        for c_idx, col in enumerate(row):
            if col == ' ':
                empty_indices.append((r_idx, c_idx))

    return empty_indices
