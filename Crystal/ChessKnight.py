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
            t.square.load_north(board).attacked(board, t.current_attack)


    @export
    def create_ally_chess_Knight(square):
        return ChessKnight(square, true, ChessKnight.initial_attack, ChessKnight.initial_health, ChessKnight.initial_health)
