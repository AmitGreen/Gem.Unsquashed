#
#   Copyright (c) 2018 Amit Green.  All rights reserved.
#
@gem('Crystal.ChessPawn')
def gem():
    #require_gem('Crystal.Core')


    @export
    class ChessPawn(Object):
        is_empty_square = false


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
                t.square.empty

            t.current_health = health
            return t


        def mirror(t):
            t.ally = not t.ally

            return t


        def portray_abbreviation(t):
            if t.ally:
                return 'WP'

            return 'BP'


        def portray_numbers(t):
            if t.maximum_health == ChessKing.initial_health:
                return arrange('%d/%d', t.current_attack, t.current_health)

            return arrange('%d/%d(%d)', t.current_attack, t.current_health, t.maximum_health)

            
    @export
    def create_ally_chess_pawn(int health):
        return ChessPawn(true, 1, health, health)k
