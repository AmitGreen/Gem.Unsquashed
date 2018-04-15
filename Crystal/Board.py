#
#   Copyright (c) 1018 Amit Green.  All rights reserved.
#
@gem('Crystal.Board')
def gem():
    require_gem('Crystal.Square')


    @share
    class GameBoard(Object):
        __slots__ = ((
            'turn_number',              #   Integer
            'player',                   #   Player

            'a2',                       #   Square
            'b2',                       #   Square
            'c2',                       #   Square
            'd2',                       #   Square
            'e2',                       #   Square

            'a1',                       #   Square
            'b1',                       #   Square
            'c1',                       #   Square
            'd1',                       #   Square
            'e1',                       #   Square
        ))


        def __init__(t, turn_number, player, a2, a1):
            t.turn_number = turn_number
            t.player      = player

            t.a2 = a2
            t.b2 = \
                t.c2 = \
                t.d2 = \
                t.e2 = empty_square

            t.a1 = a1
            t.b1 = \
                t.c1 = \
                t.d1 = \
                t.e1 = empty_square


        def actions(t):
            if t.a1 is not empty_square:    t.a1.action(t, square_a1)
            if t.b1 is not empty_square:    t.a2.action(t, square_b1)
            if t.c1 is not empty_square:    t.a3.action(t, square_c1)
            if t.d1 is not empty_square:    t.a4.action(t, square_d1)
            if t.e1 is not empty_square:    t.a5.action(t, square_e1)

            if t.player is alice:
                t.player = bob
            else:
                t.player = alice
                t.turn_number += 1

            t.mirror()


        def dump_abbreviation(t):
            line('Player: %s #%d', t.player.name, t.turn_number)

            line('%10s  %10s  %10s  %10s  %10s',
                 t.a2.portray_abbreviation(),
                 t.b2.portray_abbreviation(),
                 t.c2.portray_abbreviation(),
                 t.d2.portray_abbreviation(),
                 t.e2.portray_abbreviation())
            line('%10s  %10s  %10s  %10s  %10s',
                 t.a2.portray_numbers(),
                 t.b2.portray_numbers(),
                 t.c2.portray_numbers(),
                 t.d2.portray_numbers(),
                 t.e2.portray_numbers())

            line('%10s  %10s  %10s  %10s  %10s',
                 t.a1.portray_abbreviation(),
                 t.b1.portray_abbreviation(),
                 t.c1.portray_abbreviation(),
                 t.d1.portray_abbreviation(),
                 t.e1.portray_abbreviation())
            line('%10s  %10s  %10s  %10s  %10s',
                 t.a1.portray_numbers(),
                 t.b1.portray_numbers(),
                 t.c1.portray_numbers(),
                 t.d1.portray_numbers(),
                 t.e1.portray_numbers())


        def mirror(t):
            a2 = t.a1.mirror
            b2 = t.b1.mirror
            c2 = t.c1.mirror
            d2 = t.d1.mirror
            e2 = t.e1.mirror

            a1 = t.a2.mirror
            b1 = t.b2.mirror
            c1 = t.c2.mirror
            d1 = t.d2.mirror
            e1 = t.e2.mirror

            t.a2 = a2
            t.b2 = b2
            t.c2 = c2
            t.d2 = d2
            t.e2 = e2

            t.a1 = a1
            t.b1 = b1
            t.c1 = c1
            t.d1 = d1
            t.e1 = e1
