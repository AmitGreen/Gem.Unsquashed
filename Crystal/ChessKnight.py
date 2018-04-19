#
#   Copyright (c) 2018 Amit Green.  All rights reserved.
#
@gem('Crystal.ChessKnight')
def gem():
    require_gem('Crystal.CardRoot')


    @export
    class ChessKnight(CardRoot):
        ally_abbreviation  = 'WN'
        enemy_abbreviation = 'BN'
        initial_attack     = 3
        initial_health     = 4


        __slots__ = (())


        def action(t, board):
            north_ww = t.square.load_north_ww(board)

            if north_ww.is_card:
                north_ww.attacked(board, t)
                return

            north_ee = t.square.load_north_ee(board)

            if north_ee.is_card:
                north_ee.attacked(board, t)
                return

            board.a2.attacked(board, t)


    @export
    def create_ally_chess_knight(square, special = false):
        health = ChessKnight.initial_health + (1   if special else   0)

        return ChessKnight(square, true, ChessKnight.initial_attack, health, health)
