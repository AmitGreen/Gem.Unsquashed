#
#   Copyright (c) 2018 Amit Green.  All rights reserved.
#
@gem('Crystal.EmptySquare')
def gem():
    require_gem('Crystal.Square')


    class EmptySquare(Object):
        ally            = false
        enemy           = false
        is_empty_square = true


        __slots__ = ((
            'square',                   #   Square
        ))


        def __init__(t, square):
            t.square = square


        def __repr__(t):
            return arrange('<EmptySquare %s>', t.square)


        def mirror(t, square):
            return square.empty


        def portray_abbreviation(t):
            return arrange('%s: empty', t.square.name)


        @static_method
        def portray_numbers():
            return ''


    def produce_empty_square(square):
        r            = EmptySquare(square)
        square.empty = r

        return r


    empty_square_a2 = produce_empty_square(square_a2)
    empty_square_b2 = produce_empty_square(square_b2)
    empty_square_c2 = produce_empty_square(square_c2)
    empty_square_d2 = produce_empty_square(square_d2)
    empty_square_e2 = produce_empty_square(square_e2)

    empty_square_a1 = produce_empty_square(square_a1)
    empty_square_b1 = produce_empty_square(square_b1)
    empty_square_c1 = produce_empty_square(square_c1)
    empty_square_d1 = produce_empty_square(square_d1)
    empty_square_e1 = produce_empty_square(square_e1)


    del EmptySquare.__init__


    share(
        'empty_square_a2',  empty_square_a2,
        'empty_square_b2',  empty_square_b2,
        'empty_square_c2',  empty_square_c2,
        'empty_square_d2',  empty_square_d2,
        'empty_square_e2',  empty_square_e2,

        'empty_square_a1',  empty_square_a1,
        'empty_square_b1',  empty_square_b1,
        'empty_square_c1',  empty_square_c1,
        'empty_square_d1',  empty_square_d1,
        'empty_square_e1',  empty_square_e1,
    )
