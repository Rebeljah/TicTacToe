##

import game_board as game
import observer as ref
import cpu_opponent as cpu


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

    turn = ''
    winner = ''
    while not winner:
        turn = ref.get_next_turn(turn)

        if game_mode == 'PVP' or turn == '1':
            board = game.player_make_move(board, p1_char, p2_char, turn)
        elif game_mode == 'PVE' and turn == '2':
            board = cpu.choose_move(board, p2_char)

        game.refresh_display(board)

        winner = ref.get_winner(board, p1_char, p2_char)

    return winner


def main():
    play_again = True
    while play_again:
        board, game_mode, p1_char, p2_char = game.get_new_game()

        winner = game_loop(board, game_mode, p1_char, p2_char)
        print(winner, 'WINS!')

        play_again = ask_play_again()


main()
