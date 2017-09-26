#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.Absent')
def gem():
    class Absent(Object):
        __slots__ = (())


        many = left = kt3 = kt2 = kq4 = kq3 = kq2 = kd2 = end = comment = c = begin = b = a = none


        @static_method
        def __bool__():
            return false


        @static_method
        def __str__():
            return 'absent'


        if is_python_2:
            __nonzero__ = __bool__


    absent = Absent()


    built_in(
        'absent',   absent,
    )
