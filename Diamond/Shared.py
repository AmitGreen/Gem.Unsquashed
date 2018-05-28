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
            'status',                   #   Integer
            'chore',                    #   DiamondChore | None
            'priority',                 #   Integer

            'left_status',              #   Integer
            'left',                     #   DiamondChore | None

            'right_status',             #   Integer
            'right',                    #   DiamondChore | None
        ))


        def __init__(t):
            t.status       = STATUS_ACTIVE__1
            t.chore        = none
            t.priority     = 0

            t.left_status = STATUS_ACTIVE
            t.left        = none

            t.right_status = STATUS_ACTIVE
            t.right        = none


        def ATOMIC_INCREMENT__priority(t):
            LARGE_CHECK_INTERVAL()

            priority = t.priority

            t.priority += 1

            NORMAL_CHECK_INTERVAL()

            return priority


        def COMPARE_AND_SWAP__chore(t, before, after):
            LARGE_CHECK_INTERVAL()

            r = t.chore

            if r is before:
                t.chore = after

            NORMAL_CHECK_INTERVAL()

            return r


        def __repr__(t):
            LARGE_CHECK_INTERVAL()

            status       = t.status
            chore        = t.chore
            priority     = t.priority

            left_status  = t.left_status
            left         = t.left

            right_status = t.right_status
            right        = t.right

            NORMAL_CHECK_INTERVAL()

            status_name = status_map[status & STATUS_MASK]
            count       = status & COUNT_MASK

            left_status_name = status_map[left_status & STATUS_MASK]
            left_count       = left_status & COUNT_MASK

            right_status_name = status_map[right_status & STATUS_MASK]
            right_count       = right_status & COUNT_MASK

            return arrange('<DiamondShared %s %d %s; %d; %s %d %s; %s %d %s>',
                           status_name,       count,       chore,
                           priority,
                           left_status_name,  left_count,  left,
                           right_status_name, right_count, right)


    @share
    def create_DiamondShared():
        return DiamondShared()
