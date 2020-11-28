

import random as rand
import observer as ref
import game_board as game


def choose_move(board, cpu_char):
    board_copy = copy_board(board)
    cpu2_char = game.get_opposite_char(cpu_char)
    turn = ''

    winner = ''
    while not winner:
        turn = ref.get_next_turn(turn)

        # reset the board state if no more boxes are available 
        if find_empty_boxes(board_copy) == []:
            board_copy = copy_board(board)

        board_copy = simulate_move(board_copy, cpu_char, cpu2_char, turn)
        winner = ref.get_winner(board_copy, cpu_char, cpu2_char)


def simulate_move(board, cpu_char, cpu2_char, turn):
    # choose the char to use
    if turn == '1':
        game_char = cpu2_char
    else:
        game_char = cpu2_char

    board_size = len(board)
    num_boxes = board_size**2
    empty_boxes = find_empty_boxes(board)

    # choose a random box from the avaiable empty boxes
    box_choice = ''
    while box_choice not in empty_boxes:
        box_choice = rand.randint(1, num_boxes)

    board = place_game_char(board, game_char, box_choice)

    return board


def find_empty_boxes(board):
    empty_boxes = []
    box_num = 0
    for row in board:
        for col in row:
            box_num += 1
            if col == ' ':
                empty_boxes.append(box_num)

    return empty_boxes


def place_game_char(board, game_char, box_choice):
    box_num = 0
    for row in board:
        for col in row:
            box_num += 1
            if box_num == box_choice:
                board[row][col] = game_char

    return board


def copy_board(board):
    copy = [] + board

    return copy
