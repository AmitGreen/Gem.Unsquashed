#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.Absent')
def gem():
    class Absent(Object):
        __slots__ = (())


        herd_estimate = 0
        is_herd       = false


        @static_method
        def __bool__():
            return false


        @static_method
        def __str__():
            return 'absent'


        @static_method
        def __repr__():
            return '<absent>'


        display_token = __str__


        if is_python_2:
            __nonzero__ = __bool__


    absent = Absent()


    Absent.k4 = Absent.k3 = Absent.k2 = Absent.k1 = absent


    built_in(
        'absent',   absent,
    )
