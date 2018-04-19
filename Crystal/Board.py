#
#   Copyright (c) 1018 Amit Green.  All rights reserved.
#
@gem('Crystal.Board')
def gem():
    require_gem('Crystal.BlankSquare')


    @share
    class GameBoard(Object):
        __slots__ = ((
            'turn_number',              #   Integer
            'player',                   #   Player

            'v0',                       #   VoidSquare

            'a2',                       #   BlankSquare | Card+
            'b2',                       #   BlankSquare | Card+
            'c2',                       #   BlankSquare | Card+
            'd2',                       #   BlankSquare | Card+
            'e2',                       #   BlankSquare | Card+

            'a1',                       #   BlankSquare | Card+
            'b1',                       #   BlankSquare | Card+
            'c1',                       #   BlankSquare | Card+
            'd1',                       #   BlankSquare | Card+
            'e1',                       #   BlankSquare | Card+
        ))


        def __init__(t, turn_number, player, a2, a1):
            t.turn_number = turn_number
            t.player      = player

            t.v0 = void_square

            t.a2 = a2
            t.b2 = blank_square_b2
            t.c2 = blank_square_c2
            t.d2 = blank_square_d2
            t.e2 = blank_square_e2

            t.a1 = a1
            t.b1 = blank_square_b1
            t.c1 = blank_square_c1
            t.d1 = blank_square_d1
            t.e1 = blank_square_e1


        def add_normal_x1(t, create):
            if t.b1 is blank_square_b1:
                t.b1 = create(square_b1)
                line("%s created %s", t.player.name, t.b1.portray())
                return true

            if t.c1 is blank_square_c1:
                t.c1 = create(square_c1)
                line("%s created %s", t.player.name, t.c1.portray())
                return true

            if t.d1 is blank_square_d1:
                t.d1 = create(square_d1)
                line("%s created %s", t.player.name, t.d1.portray())
                return true

            if t.e1 is blank_square_e1:
                t.e1 = create(square_e1)
                line("%s created %s", t.player.name, t.e1.portray())
                return true

            return false


        def add_special_x1(t, create):
            if t.b1 is blank_square_b1:
                t.b1 = create(square_b1, true)
                line("%s created %s", t.player.name, t.b1.portray())
                return true

            if t.c1 is blank_square_c1:
                t.c1 = create(square_c1, true)
                line("%s created %s", t.player.name, t.c1.portray())
                return true

            if t.d1 is blank_square_d1:
                t.d1 = create(square_d1, true)
                line("%s created %s", t.player.name, t.d1.portray())
                return true

            if t.e1 is blank_square_e1:
                t.e1 = create(square_e1, true)
                line("%s created %s", t.player.name, t.e1.portray())
                return true

            return false

        
        def lookup_square_x1(t):
            if t.b1 is blank_square_b1:     return square_b1
            if t.c1 is blank_square_c1:     return square_c1
            if t.d1 is blank_square_d1:     return square_d1
            if t.e1 is blank_square_e1:     return square_e1

            return 0


        def actions(t):
            prepare = t.a1.prepare

            if prepare is not 0:
                prepare(t)

            prepare = t.b1.prepare

            if prepare is not 0:
                prepare(t)

            prepare = t.c1.prepare

            if prepare is not 0:
                prepare(t)

            prepare = t.d1.prepare

            if prepare is not 0:
                prepare(t)

            prepare = t.e1.prepare

            if prepare is not 0:
                prepare(t)

            if t.a1 is not blank_square_a1:    t.a1.action(t)
            if t.b1 is not blank_square_b1:    t.b1.action(t)
            if t.c1 is not blank_square_c1:    t.c1.action(t)
            if t.d1 is not blank_square_d1:    t.d1.action(t)
            if t.e1 is not blank_square_e1:    t.e1.action(t)

            if t.player is alice:
                t.player = bob
            else:
                t.player = alice
                t.turn_number += 1

            t.mirror()


        def dump_abbreviation(t):
            line('Turn: #%d; Player: %s', t.turn_number, t.player.name)

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
            a2 = t.a1.mirror(square_a2)
            b2 = t.b1.mirror(square_b2)
            c2 = t.c1.mirror(square_c2)
            d2 = t.d1.mirror(square_d2)
            e2 = t.e1.mirror(square_e2)

            a1 = t.a2.mirror(square_a1)
            b1 = t.b2.mirror(square_b1)
            c1 = t.c2.mirror(square_c1)
            d1 = t.d2.mirror(square_d1)
            e1 = t.e2.mirror(square_e1)

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


    v0 = GameBoard.v0

    a2 = GameBoard.a2
    b2 = GameBoard.b2
    c2 = GameBoard.c2
    d2 = GameBoard.d2
    e2 = GameBoard.e2

    a1 = GameBoard.a1
    b1 = GameBoard.b1
    c1 = GameBoard.c1
    d1 = GameBoard.d1
    e1 = GameBoard.e1


    load_v0 = v0.__get__
 
    load_a2 = a2.__get__
    load_b2 = b2.__get__
    load_c2 = c2.__get__
    load_d2 = d2.__get__
    load_e2 = e2.__get__

    load_a1 = a1.__get__
    load_b1 = b1.__get__
    load_c1 = c1.__get__
    load_d1 = d1.__get__
    load_e1 = e1.__get__


    store_v0 = v0.__set__
 
    store_a2 = a2.__set__
    store_b2 = b2.__set__
    store_c2 = c2.__set__
    store_d2 = d2.__set__
    store_e2 = e2.__set__

    store_a1 = a1.__set__
    store_b1 = b1.__set__
    store_c1 = c1.__set__
    store_d1 = d1.__set__
    store_e1 = e1.__set__


    load = ((
            load_v0,

            load_a2, load_b2, load_c2, load_d2, load_e2,
            load_a1, load_b1, load_c1, load_d1, load_e1,
        ))


    store = ((
            store_v0,

            store_a2, store_b2, store_c2, store_d2, store_e2,
            store_a1, store_b1, store_c1, store_d1, store_e1,
        ))


    def fix_square(square, center, north_ww = 0, north_west = 0, north = 0, north_east = 0, north_ee = 0):
        square.load_center     = load[center]
        square.load_north_ww   = load[north_ww]
        square.load_north_west = load[north_west]
        square.load_north      = load[north]
        square.load_north_east = load[north_east]
        square.load_north_ee   = load[north_ee]

        square.store_center     = store[center]
        square.store_north_ww   = store[north_ww]
        square.store_north_west = store[north_west]
        square.store_north      = store[north]
        square.store_north_east = store[north_east]
        square.store_north_ee   = store[north_ee]


    fix_square(square_a2,  1)
    fix_square(square_b2,  2)
    fix_square(square_c2,  3)
    fix_square(square_d2,  4)
    fix_square(square_e2,  5)

    fix_square(square_a1,  6,                               north = 1, north_east = 2, north_ee = 3)
    fix_square(square_b1,  7,               north_west = 1, north = 2, north_east = 3, north_ee = 4)
    fix_square(square_c1,  8, north_ww = 1, north_west = 2, north = 3, north_east = 4, north_ee = 5)
    fix_square(square_d1,  9, north_ww = 2, north_west = 3, north = 4, north_east = 5)
    fix_square(square_e1, 10, north_ww = 3, north_west = 4, north = 5)


    share(
        'load_v0',      load_v0,

        'load_a2',      load_a2,
        'load_b2',      load_b2,
        'load_c2',      load_c2,
        'load_d2',      load_d2,
        'load_e2',      load_e2,

        'load_a1',      load_a1,
        'load_b1',      load_b1,
        'load_c1',      load_c1,
        'load_d1',      load_d1,
        'load_e1',      load_e1,


        'store_v0',     store_v0,

        'store_a2',     store_a2,
        'store_b2',     store_b2,
        'store_c2',     store_c2,
        'store_d2',     store_d2,
        'store_e2',     store_e2,

        'store_a1',     store_a1,
        'store_b1',     store_b1,
        'store_c1',     store_c1,
        'store_d1',     store_d1,
        'store_e1',     store_e1,
    )
