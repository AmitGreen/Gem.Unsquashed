#
#   Copyright (c) 2018 Amit Green.  All rights reserved.
#
@gem('Diamond.Work')
def gem():
    require_gem('Diamond.Core')


    class Work(Object):
        __slots__ = ((
            'counter',                  #   Shared
        ))


        def __init__(t, counter):
            t.counter = counter


        def work(t, thread_number):
            number = t.counter.ATOMIC_ADD__number(thread_number, 1)

            line('#%d: %d', thread_number, number)


    @share
    def create_Work(counter):
        return Work(counter)
