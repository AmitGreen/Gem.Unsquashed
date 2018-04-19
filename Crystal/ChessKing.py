#
#   Copyright (c) 2018 Amit Green.  All rights reserved.
#
@gem('Crystal.ChessKing')
def gem():
    require_gem('Crystal.CardRoot')


    @export
    class ChessKing(CardRoot):
        ally_abbreviation  = 'WK'
        enemy_abbreviation = 'BK'
        initial_attack     = 1
        initial_health     = 20


        __slots__ = (())


        def action(t, board):
            t.square.load_north(board).attacked(board, t.current_attack)


        def attacked(t, board, attack):
            health = t.current_health - attack

            if health < 0:
                t.current_health = 0
                return

            t.current_health = health


        attacked_ignore_shield = attacked



    @export
    def create_ally_chess_king():
        return ChessKing(square_a1, true, ChessKing.initial_attack, ChessKing.initial_health, ChessKing.initial_health)


    @export
    def create_enemy_chess_king():
        return ChessKing(
                square_b1,
                false,
                ChessKing.initial_attack,
                ChessKing.initial_health,
                ChessKing.initial_health,
            )
