'''observer.py'''

def get_winner(board, p1_char, p2_char):
    '''Returns winner (1 or 2) if a winning row is found

       Get each possible winning line from the board, then check each for a win.

       '''
    board_size = len(board)

    hoz_lines = get_hoz_rows(board)
    vert_lines = get_vert_rows(board)
    diag_lines = get_diag_rows(board)

    for line_type in (hoz_lines, vert_lines, diag_lines):
        for line in line_type:
            is_win = True  # True as default then test for lose conditions
            if line[0] == ' ':
                is_win = False
            else:
                for idx in range(1, board_size):
                    if line[idx] != line[0]:
                        is_win = False

            if is_win:  # if no lose conditions were found in the line
                if line[0] == p1_char:
                    winner = '1'
                else:
                    winner = '2'
                return winner
            else:
                winner = False  # set winner to False then continue to next line
    return winner


def get_hoz_rows(board):
    '''Simply copies the board (each element represents a hoz row already)'''
    hoz_rows = board.copy()

    return hoz_rows


def get_vert_rows(board):
    '''For each column in the board, get the elements in that column.

      Make a list for each vertical row, appending each list to 'diag_rows'
       '''
    board_size = len(board)

    vert_rows = []

    for col in range(board_size):
        vert_row = [board[row][col] for row in range(board_size)]
        vert_rows.append(vert_row)

    return vert_rows


def get_diag_rows(board):
    '''Returns a list of the diagonal rows in the board

       In the first diagonal, increase both the row and col index by one
       on each iteration.
       For the second diagonal, the row increases by one on each iteration, the
       col is equal to -i-1.'''
    size = len(board)

    diagonal = [board[i][i] for i in range(size)]
    anti_diagonal = [board[i][-i-1] for i in range(size)]

    diag_rows = [diagonal, anti_diagonal]

    return diag_rows
