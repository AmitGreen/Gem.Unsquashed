#
#   Copyright (c) 2018 Amit Green.  All rights reserved.
#
@gem('Crystal.Square')
def gem():
    #require_gem('Crystal.Core')


    class Square(Object):
        __slot__ = ((
            'name',                 #   String+
            'column',               #   Integer
            'row',                  #   Integer
        ))


        def __init__(t, name, column, row):
            t.name   = name
            t.column = column
            t.row    = row


        def __repr__(t):
            return arrange('<Square %s>', t.name)


    square_a2 = Square('a2', 2, 1)
    square_b2 = Square('b2', 2, 2)
    square_c2 = Square('c2', 2, 3)
    square_d2 = Square('d2', 2, 4)
    square_e2 = Square('e2', 2, 5)

    square_a1 = Square('a1', 1, 1)
    square_b1 = Square('b1', 1, 2)
    square_c1 = Square('c1', 1, 3)
    square_d1 = Square('d1', 1, 4)
    square_e1 = Square('e1', 1, 5)



    class EmptySquare(Object):
        ally         = false
        enemy        = false
        empty_square = true


        @static_method
        def __repr__():
            return '<Empty-Square>'


        def mirror(t):
            return t


        @static_method
        def portray_abbreviation():
            return 'Empty'


        @static_method
        def portray_numbers():
            return ''


    empty_square = EmptySquare()


    share(
        'empty_square',      empty_square,

        'square_a1',         square_a1,
        'square_a2',         square_a2,
        'square_b1',         square_b1,
        'square_b2',         square_b2,
        'square_c1',         square_c1,
        'square_c2',         square_c2,
        'square_d1',         square_d1,
        'square_d2',         square_d2,
        'square_e1',         square_e1,
        'square_e2',         square_e2,
    )
