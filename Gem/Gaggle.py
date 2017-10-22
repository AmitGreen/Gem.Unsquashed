#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.Gaggle')
def gem():
    #
    #   Gaggle:
    #
    #       Liquid (modifiable)
    #       Set (Associative Array)
    #       Ordered
    #       Key must not include absent
    #


    class Gaggle_0(Object):
        __slots__ = (())


        total = 0



    class Gaggle_1(Object):
        __slots__ = ((
            'a',                        #   Any
        ))


        total = 1


    empty_gaggle = Gaggle_0()


    new_Gaggle_1 = Method(Object.__new__, Gaggle_1)


    @export
    def create_gaggle_1(a):
        assert a is not absent

        t = new_Gaggle_1()

        t.a = a

        return t


    if __debug__:
        Gaggle_0.add = static_method(rename_function('add__gaggle_0',  create_gaggle_1))
    else:
        Gaggle_0.add = static_method(create_gaggle_1)


    export(
        'empty_gaggle',     empty_gaggle,
    )
