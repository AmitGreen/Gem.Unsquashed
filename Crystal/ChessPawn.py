#
#   Copyright (c) 2018 Amit Green.  All rights reserved.
#
@gem('Crystal.ChessPawn')
def gem():
    require_gem('Crystal.CardRoot')


    @export
    class ChessPawn(CardRoot):
        ally_abbreviation  = 'WP'
        enemy_abbreviation = 'BP'
        initial_attack     = 1
        initial_health     = 1


        __slots__ = (())


        def action(t, board):
            north_east = t.square.load_north_east(board)

            if north_east.is_card:
                north_east.attacked(board, t.current_attack)
                return

            north_west = t.square.load_north_west(board)

            if north_west.is_card:
                north_west.attacked(board, t.current_attack)
                return

            board.a2.attacked_ignore_shield(board, t.current_attack)


    @export
    def create_ally_chess_pawn(square, health):
        return ChessPawn(square, true, ChessPawn.initial_attack, health, health)
