#
#   Copyright (c) 2017-2018 Amit Green.  All rights reserved.
#
@gem('Diamond.Development')
def gem():
    require_gem('Diamond.Core')


    import sys


    check_interval        = sys.getcheckinterval
    change_check_interval = sys.setcheckinterval


    LARGE_CHECK_INTERVAL  = Method(change_check_interval, 7777777)
    NORMAL_CHECK_INTERVAL = Method(change_check_interval, 100)


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
