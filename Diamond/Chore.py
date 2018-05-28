#
#   Copyright (c) 2018 Amit Green.  All rights reserved.
#
@gem('Diamond.Chore')
def gem():
    require_gem('Diamond.Core')


    class DiamondChore(Object):
        __slots__ = ((
            'thread',                   #   BaseThread+
            'priority',                 #   Integer
            'counter',                  #   Shared
        ))


        def __init__(t, thread, priority, counter):
            t.thread   = thread
            t.priority = priority
            t.counter  = counter


        def chore(t):
            thread_number = t.thread.thread_number

            number = t.counter.ATOMIC_ADD__number(thread_number, 1)

            line('#%d: %d, %d', thread_number, t.priority, number)


    @share
    def create_DiamondChore(thread, priority, counter):
        return DiamondChore(thread, priority, counter)
