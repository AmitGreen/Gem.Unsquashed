#
#   Copyright (c) 2018 Amit Green.  All rights reserved.
#
@gem('Crystal.Game')
def gem():
    require_gem('Crystal.Core')
    require_gem('Crystal.Chess')
    require_gem('Crystal.Player')


    @share
    def command_game():
        assert initial_enemy_chess_king.mirror is initial_ally_chess_king
        assert initial_ally_chess_king .mirror is initial_enemy_chess_king

        line('initial_ally_chess_king:  %s',  initial_ally_chess_king)
        line('initial_enemy_chess_king:  %s', initial_enemy_chess_king)
