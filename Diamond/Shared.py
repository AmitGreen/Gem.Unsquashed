#
#   Copyright (c) 2018 Amit Green.  All rights reserved.
#
@gem('Diamond.Status')
def gem():
    require_gem('Diamond.Core')
    require_gem('Diamond.Interval')
    require_gem('Diamond.Status')


    class DiamondShared(Object):
        __slots__ = ((
            'status_count',             #   Integer
            'work',                     #   Work | None
        ))


        def __init__(t):
            t.status_count = 1
            t.work         = none


        def COMPARE_AND_SWAP__work(t, before, after):
            LARGE_CHECK_INTERVAL()

            r = t.work

            if r is before:
                t.work = after

            NORMAL_CHECK_INTERVAL()

            return r



        def __repr__(t):
            status_count = t.status_count
            work         = t.work

            status = status_map[status_count & STATUS_MASK]
            count  = status_count & COUNT_MASK

            return arrange('<DiamondShared %s %d; %s>', status, count, work)


    @share
    def create_DiamondShared():
        return DiamondShared()
