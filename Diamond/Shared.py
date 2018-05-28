#
#   Copyright (c) 2018 Amit Green.  All rights reserved.
#
@gem('Diamond.Shared')
def gem():
    require_gem('Diamond.Core')
    require_gem('Diamond.Interval')


    class Shared(Object):
        __slots__ = ((
            'work',                     #   Work | None
        ))


        def __init__(t):
            t.work = none


        def COMPARE_AND_SWAP__work(t, before, after):
            LARGE_CHECK_INTERVAL()

            r = t.work

            if r is before:
                t.work = after

            NORMAL_CHECK_INTERVAL()

            return r
                


    @share
    def create_Shared():
        return Shared()
