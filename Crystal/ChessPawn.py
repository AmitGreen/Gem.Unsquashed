#
#   Copyright (c) 2018 Amit Green.  All rights reserved.
#
@gem('Crystal.ChessPawn')
def gem():
    #require_gem('Crystal.Core')


    @export
    class ChessPawn(Object):
        is_blank_square = false
        is_card         = true


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
            north_east = t.square.load_north_east(board)

            if north_east.is_card:
                north_east.attacked(board, t.current_attack)
                return

            north_west = t.square.load_north_west(board)

            if north_west.is_card:
                north_west.attacked(board, t.current_attack)
                return

            board.a2.attacked_ignore_shield(board, t.current_attack)


        def attacked(t, attack):
            health = t.current_health - attack

            if health < 0:
                t.square.empty

            t.current_health = health
            return t


        def mirror(t, square):
            t.square = square
            t.ally   = not t.ally

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
    def create_ally_chess_pawn(square, health):
        return ChessPawn(square, true, 1, health, health)
