#
#   Copyright (c) 2018 Amit Green.  All rights reserved.
#
@gem('Diamond.Counter')
def gem():
    require_gem('Diamond.Core')
    require_gem('Diamond.Interval')


    class Counter(Object):
        __slots__ = ((
            'number',                   #   Integer
        ))


        def __init__(t):
            t.number = 0


        def ATOMIC_ADD__number(t, thread_number, v):
            LARGE_CHECK_INTERVAL()

            number = t.number

            t.number += v

            NORMAL_CHECK_INTERVAL()

            return number


    @share
    def create_Counter():
        return Counter()
