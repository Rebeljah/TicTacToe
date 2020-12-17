'''
cpu_opponent.py
Makes a move by finding a possible winning scenario and then making the
first move from that winning line.

-copy the game board

-alternate turns starting with 2(CPU), then to 1(simulated_player). On each
turn, the CPU or sim_player will make a random move to an empty box.

--keep track of the order in which 2(CPU) makes moves (tuples / dicts?)

--After each move, check is 2(CPU) has won.
---if the CPU wins, check to see which character in the winning line was placed
   first. Make this move onto the live game board
---if 1(sim_player) wins or the copied board runs out of empty boxes, make
   a new copy of the board and begin the process of placing chars again.
'''
import random
import copy
import game_board as game
import observer as ref


def choose_move(board, player_char, cpu_char):
    while True:
        sim_board = copy.deepcopy(board)

        move = \
            simulate_game(sim_board, player_char, cpu_char)

        if move:
            board = place_char(board, cpu_char, move)
            return board


def simulate_game(sim_board, player_char, cpu_char):
    turn = 1
    move = 0
    mem = {}
    winner = ''

    while not winner:
        turn = game.get_next_turn(turn)
        char = game.get_current_char(player_char, cpu_char, turn)

        index = get_random_index(sim_board)
        if index:
            char = game.get_current_char(player_char, cpu_char, turn)
            sim_board = place_char(sim_board, char, index)

            if turn == 2:
                move += 1
                mem.update({move: index})
        else:
            return None

        winner, row = ref.get_winner(sim_board, player_char, cpu_char)

    return get_first_move(winner, row, mem)


def get_random_index(sim_board):
    size = len(sim_board)
    empty_boxes = ref.find_empty_indices(sim_board)
    row, col = '', ''

    if empty_boxes:
        while (row, col) not in empty_boxes:
            row = random.randrange(size)
            col = random.randrange(size)
    else:
        return False
    return (row, col)


def get_first_move(winner, winning_row, mem):
    if winner == 1:
        return None

    actual_mem = {}
    winning_indices = [element[0] for element in winning_row]

    for move_number, index in mem.items():
        if index in winning_indices:
            actual_mem.update({move_number: index})

    mem = actual_mem
    if mem:
        return mem[min(mem.keys())]
    else:
        return False


def place_char(board, char, index):
    row, col = index

    board[row][col] = char

    return board
