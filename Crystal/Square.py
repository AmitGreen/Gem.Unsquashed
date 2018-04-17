#
#   Copyright (c) 2018 Amit Green.  All rights reserved.
#
@gem('Crystal.Square')
def gem():
    #require_gem('Crystal.Core')


    class Square(Object):
        __slots__ = ((
            'name',                 #   String+
            'column',               #   Integer
            'row',                  #   Integer
            'empty',                #   Vacant | EmptySquare
        ))


        def __init__(t, name, column, row):
            t.name   = name
            t.column = column
            t.row    = row
           #t.empty  = empty        #   Done in produce_empty_square


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


    del Square.__init__


    share(
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
