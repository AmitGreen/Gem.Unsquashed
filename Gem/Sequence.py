#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.Sequence')
def gem():
    #
    #   Sequence:
    #
    #       Basically a tuple
    #


    tuple__length = Tuple.__len__


    empty_iterator = iterate( (()) )


    class Sequence_0(Object):
        __slots__ = (())
        total     = 0


        @static_method
        def __repr__():
            return '{,}'


        @static_method
        def __iter__():
            return empty_iterator


    class Sequence_1(Object):
        __slots__ = ((
            'a',                        #   Any excluding Absent
        ))


        total = 1


        def __iter__(t):
            yield t.a


        def __repr__(t):
            return arrange('{%s}', portray(t.a))


    class Sequence_2(Object):
        __slots__ = ((
            'a',                        #   Any excluding Absent
            'b',                        #   Any excluding Absent
        ))


        total = 2


        def __iter__(t):
            yield t.a
            yield t.b


        def __repr__(t):
            return arrange('{%s, %s}', portray(t.a), portray(t.b))


    class Sequence_3(Object):
        __slots__ = ((
            'a',                        #   Any excluding Absent
            'b',                        #   Any excluding Absent
            'c',                        #   Any excluding Absent
        ))


        total = 3


        def __iter__(t):
            yield t.a
            yield t.b
            yield t.c


        def __repr__(t):
            return arrange('{%s, %s, %s}', portray(t.a), portray(t.b), portray(t.c))


    class Sequence_4(Object):
        __slots__ = ((
            'a',                        #   Any excluding Absent
            'b',                        #   Any excluding Absent
            'c',                        #   Any excluding Absent
            'd',                        #   Any excluding Absent
        ))


        total = 4


        def __iter__(t):
            yield t.a
            yield t.b
            yield t.c
            yield t.d


        def __repr__(t):
            return arrange('{%s, %s, %s, %s}', portray(t.a), portray(t.b), portray(t.c), portray(t.d))


    class Sequence_Many(Tuple):
        __slots__ = (())


        def __repr__(t):
            return arrange('{%s}', ', '.join(portray(v)   for v in t))


        @property
        def total(t):
            return tuple__length(t)


    new_Sequence_1    = Method(Object.__new__, Sequence_1)
    new_Sequence_2    = Method(Object.__new__, Sequence_2)
    new_Sequence_3    = Method(Object.__new__, Sequence_3)
    new_Sequence_4    = Method(Object.__new__, Sequence_4)
    new_Sequence_Many = Method(Tuple .__new__, Sequence_Many)


    @export
    def create_sequence_1(a):
        t = new_Sequence_1()

        t.a = a

        return t


    @export
    def create_sequence_2(a, b):
        t = new_Sequence_2()

        t.a = a
        t.b = b

        return t


    @export
    def create_sequence_3(a, b, c):
        t = new_Sequence_3()

        t.a = a
        t.b = b
        t.c = c

        return t


    @export
    def create_sequence_4(a, b, c, d):
        t = new_Sequence_4()

        t.a = a
        t.b = b
        t.c = c
        t.d = d

        return t


    create_sequence_many = new_Sequence_Many

    sequence_0 = Sequence_0()


    export(
        'create_sequence_many',     create_sequence_many,
        'sequence_0',               sequence_0,
    )
