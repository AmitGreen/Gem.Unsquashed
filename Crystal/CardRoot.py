#
#   Copyright (c) 2018 Amit Green.  All rights reserved.
#
@gem('Crystal.CardRoot')
def gem():
    @export
    class CardRoot(Object):
        prepare         = 0
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


        def attacked(t, board, attack):
            health = t.current_health - attack

            if health <= 0:
                square = t.square
                square.store_center(board, square.blank)

                return

            t.current_health = health


        attacked_ignore_shield = attacked

            
        def heal_1(t):
            if t.current_health < t.maximum_health:
                t.current_health += 1
                return


        def mirror(t, square):
            t.square = square
            t.ally   = not t.ally

            return t


        def portray_abbreviation(t):
            return arrange('%s: %s', t.square.name, (t.ally_abbreviation   if t.ally else   t.enemy_abbreviation))


        def portray_numbers(t):
            if t.maximum_health == ChessKing.initial_health:
                return arrange('%d/%d', t.current_attack, t.current_health)

            return arrange('%d/%d(%d)', t.current_attack, t.current_health, t.maximum_health)
