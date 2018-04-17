#
#   Copyright (c) 2018 Amit Green.  All rights reserved.
#
@gem('Crystal.ChessKing')
def gem():
    #require_gem('Crystal.Core')


    @export
    class ChessKing(Object):
        is_blank_square = false
        is_card         = true
        initial_attack  = 1
        initial_health  = 20


        __slots__ = ((
            'square',                   #   Square
            'ally',                     #   Boolean
            'current_attack',           #   Integer
            'current_health',           #   Integer
            'maximum_health',           #   Integer
        ))


        def __init__(t, square, ally, current_attack, current_health, maximum_health):
            t.square         = square
            t.ally           = ally
            t.current_attack = current_attack
            t.current_health = current_health
            t.maximum_health = maximum_health


        @property
        def enemy(t):
            return not t.ally


        def action(t, board):
            t.square.load_north(board).attacked(board, t.current_attack)


        def attacked(t, board, attack):
            health = t.current_health - attack

            if health < 0:
                t.current_health = 0

            t.current_health = health


        attacked_ignore_shield = attacked


        def mirror(t, square):
            t.square = square
            t.ally   = not t.ally

            return t


        def portray_abbreviation(t):
            return arrange('%s: %s', t.square.name, ('WK'   if t.ally else   'BK'))


        def portray_numbers(t):
            if t.maximum_health == ChessKing.initial_health:
                return arrange('%d/%d', t.current_attack, t.current_health)

            return arrange('%d/%d(%d)', t.current_attack, t.current_health, t.maximum_health)


    @export
    def create_ally_chess_king():
        return ChessKing(square_a1, true, ChessKing.initial_attack, ChessKing.initial_health, ChessKing.initial_health)


    @export
    def create_enemy_chess_king():
        return ChessKing(square_b1, false, ChessKing.initial_attack, ChessKing.initial_health, ChessKing.initial_health)
