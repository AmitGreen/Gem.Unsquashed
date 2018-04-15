#
#   Copyright (c) 2018 Amit Green.  All rights reserved.
#
@gem('Crystal.ChessKing')
def gem():
    #require_gem('Crystal.Core')


    @export
    class ChessKing(Object):
        empty_square   = false
        initial_attack = 1
        initial_health = 20


        __slots__ = ((
            'ally',                     #   Boolean
            'current_attack',           #   Integer
            'current_health',           #   Integer
            'maximum_health',           #   Integer
        ))


        def __init__(t, ally, current_attack, current_health, maximum_health):
            t.ally           = ally
            t.current_attack = current_attack
            t.current_health = current_health
            t.maximum_health = maximum_health


        @property
        def enemy(t):
            return not t.ally


        def action(t, board, square):
            assert square is square_a1

            board.a2 = board.a2.attacked(t.current_attack)


        def attacked(t, attack):
            health = t.current_health - attack

            if health < 0:
                t.current_health = 0
                return t


            t.current_health = health
            return t


        def mirror(t):
            t.ally = not t.ally

            return t


        def portray_abbreviation(t):
            if t.ally:
                return 'WK'

            return 'BK'


        def portray_numbers(t):
            if t.maximum_health == ChessKing.initial_health:
                return arrange('%d/%d', t.current_attack, t.current_health)

            return arrange('%d/%d(%d)', t.current_attack, t.current_health, t.maximum_health)
    @export
    def create_ally_chess_king():
        return ChessKing(true, ChessKing.initial_attack, ChessKing.initial_health, ChessKing.initial_health)


    @export
    def create_enemy_chess_king():
        return ChessKing(false, ChessKing.initial_attack, ChessKing.initial_health, ChessKing.initial_health)
