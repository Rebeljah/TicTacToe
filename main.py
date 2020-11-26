##

import game_board as game
import observer as ref


def ask_play_again():
    response = ''
    while response not in ['y', 'n']:
        response = input('Insert another coin? (y/n): ').lower()

    if response == 'y':
        return True
    else:
        return False


def game_loop(board, game_mode, p1_char, p2_char):
    game.refresh_display(board)
    turn = 'p1'

    while True:
        # get the first move then swap turns
        board = game.player_make_move(board, p1_char, p2_char, turn)
        game.refresh_display(board)

        winner = ref.get_winner(board, p1_char, p2_char)
        if winner:
            return winner
        else:
            turn = ref.get_next_turn(turn)

        # get second move from player if in 2p mode or cpu in 1p mode
        if game_mode == 'PVP':
            board = game.player_make_move(board, p1_char, p2_char, turn)
        elif game_mode == 'PVE':
            board = cpu.make_move(board, p2_char)
        game.refresh_display(board)

        winner = ref.get_winner(board, p1_char, p2_char)
        if winner:
            return winner
        else:
            turn = ref.get_next_turn(turn)  # swap turns


def main():
    play_again = True
    while play_again:
        board, game_mode, p1_char, p2_char = game.get_new_game()

        winner = game_loop(board, game_mode, p1_char, p2_char)
        print(winner, 'WINS!')

        play_again = ask_play_again()


main()
