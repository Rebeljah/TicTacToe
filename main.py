
import game_board as game
import observer as ref
import cpu_opponent as cpu


def main():
    play_again = True

    while play_again:
        board, game_mode, p1_char, p2_char = game.get_new_game()

        winner = game_loop(board, game_mode, p1_char, p2_char)
        print(winner, 'WINS!')

        play_again = ask_play_again()


def game_loop(board, game_mode, p1_char, p2_char):
    '''Keep letting p1 and p2/cpu make moves until one side WINS
       The game loops consists of 4 steps. First, the current turn is decided;
       it will be either 1 or 2. Second, either the current player or cpu makes
       a move. Third, the board is checked for a winner. If a win is found, the
       winning player / cpu is indicated by the return value, either 1 or 2.
       -1 will always be p1, 2 can be either p2 or a opponent'''
    game.refresh_display(board)
    turn = ''
    winner = ''

    while not winner:
        turn = game.get_next_turn(turn)

        if game_mode == 'PVP' or turn == 1:
            board = game.player_make_move(board, p1_char, p2_char, turn)
        elif game_mode == 'PVE' and turn == 2:
            board = cpu.choose_move(board, p1_char, p2_char)

        winner, row = ref.get_winner(board, p1_char, p2_char)

        game.refresh_display(board)
    return winner


def ask_play_again():
    response = ''
    while response not in ['y', 'n']:
        response = input('Insert another coin? (y/n): ').lower()

    if response == 'y':
        return True
    else:
        return False


main()
