#
#   Copyright (c) 2017-2018 Amit Green.  All rights reserved.
#
@gem('Diamond.Development')
def gem():
    require_gem('Diamond.Core')
    require_gem('Diamond.Thread')


    import sys


    check_interval        = sys.getcheckinterval
    change_check_interval = sys.setcheckinterval


    LARGE_CHECK_INTERVAL  = Method(change_check_interval, 7777777)
    NORMAL_CHECK_INTERVAL = Method(change_check_interval, 100)

    
    import time


    sleep = time.sleep


    class Shared(Object):
        __slots__ = ((
            'number',                   #   Integer
        ))


        def __init__(t):
            t.number = 0


        def ATOMIC_ADD(t, thread_number, v):
            LARGE_CHECK_INTERVAL()

            number = t.number

            t.number += v

            NORMAL_CHECK_INTERVAL()

            return number


    def create_Shared():
        return Shared()


    class DevelopmentThread(BaseThread):
        __slots__ = ((
            'shared',                   #   Shared
        ))


        def __init__(t, thread_number, lock, shared):
            BaseThread.__init__(t, thread_number, lock)

            t.shared = shared


        def run(t):
            line('Now running: %s', t)

            shared        = t.shared
            thread_number = t.thread_number

            while shared.number < 10:
                number = shared.ATOMIC_ADD(thread_number, 1)

                line('Thread %s says: %d', t, number)


    @share
    def command_development():  
        shared = create_Shared()

        thread_many = []

        append_thread = thread_many.append

        for thread_number in iterate_range(2):
            thread = create_Thread(DevelopmentThread, thread_number, shared)

            append_thread(thread)

            thread.start()

        for v in thread_many:
            line("Waiting for %s to exit ...", v)
            v.wait()
            line("... done waiting for %s to exit", v) 

        line('check_interval is %d', check_interval())
