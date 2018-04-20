#
#   Copyright (c) 2018 Amit Green.  All rights reserved.
#
@gem('Crystal.ChessRook')
def gem():
    require_gem('Crystal.CardRoot')


    @export
    class ChessRoot(CardRoot):
        ally_abbreviation  = 'WR'
        enemy_abbreviation = 'BR'
        initial_attack     = 2
        initial_health     = 5


        __slots__ = (())


        def action(t, board):
            north = t.square.load_north(board)

            if north_ww.is_card:
                north_ww.attacked(board, t)
                return

            board.a2.attacked_ignore_shield(board, t)


        def prepare(t, board):
            line('Rook.prepare: incomplete')


    @export
    def create_ally_chess_rook(square, special = false):
        health = ChessRook.initial_health + (1   if special else   0)

        return ChessRook(square, true, ChessRook.initial_attack, health, health)
