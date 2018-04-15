#
#   Copyright (c) 2018 Amit Green.  All rights reserved.
#
@gem('Crystal.Game')
def gem():
    require_gem('Crystal.Core')
    require_gem('Crystal.Board')
    require_gem('Crystal.Chess')
    require_gem('Crystal.Player')
    require_gem('Crystal.Square')


    def command_test():
        assert initial_enemy_chess_king.mirror is initial_ally_chess_king
        assert initial_ally_chess_king .mirror is initial_enemy_chess_king


    def command_dump():
        line('initial_ally_chess_king:  %s',  initial_ally_chess_king)
        line('initial_enemy_chess_king:  %s', initial_enemy_chess_king)
        line('empty_square:  %s', empty_square)


    @share
    def command_game():
        command_test()
        command_dump()

        board = GameBoard(1, alice, initial_enemy_chess_king, initial_ally_chess_king)

        board.dump_abbreviation()

        board.actions()
        line('---')
        board.dump_abbreviation()
