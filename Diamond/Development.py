#
#   Copyright (c) 2017-2018 Amit Green.  All rights reserved.
#
@gem('Diamond.Development')
def gem():
    require_gem('Diamond.Core')
    require_gem('Diamond.Counter')
    require_gem('Diamond.Interval')
    require_gem('Diamond.Thread')


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
                


    def create_Shared():
        return Shared()



    class Work(Object):
        __slots__ = ((
            'counter',                  #   Shared
        ))


        def __init__(t, counter):
            t.counter = counter


        def work(t, thread_number):
            number = t.counter.ATOMIC_ADD__number(thread_number, 1)

            line('#%d: %d', thread_number, number)


    def create_Work(counter):
        return Work(counter)



    class DevelopmentThread(BaseThread):
        __slots__ = ((
            'counter',                  #   Counter
            'shared',                   #   Shared
        ))


        def __init__(t, thread_number, lock, counter, shared):
            BaseThread.__init__(t, thread_number, lock)

            t.counter = counter
            t.shared   = shared


        def run(t):
            line('Now running: %s', t)

            counter       = t.counter
            shared        = t.shared
            thread_number = t.thread_number

            while counter.number < 10:
                work     = create_Work(counter)
                previous = shared.COMPARE_AND_SWAP__work(none, work)

                sleep(0.00001)

                if previous is not none:
                    raise_runtime_error('run: previous is %s', previous)

                work.work(thread_number)

                previous = shared.COMPARE_AND_SWAP__work(work, none)

                if previous is not work:
                    raise_runtime_error('work.work: previous is %s', previous)


    @share
    def command_development():
        line('check_interval is %d', fetch_check_interval())

        counter = create_Counter()
        shared  = create_Shared()

        thread_many = []

        append_thread = thread_many.append

        for thread_number in iterate_range(1):
            thread = create_Thread(DevelopmentThread, thread_number, counter, shared)

            append_thread(thread)

            thread.start()

        for v in thread_many:
            line("Waiting for %s to exit ...", v)
            v.wait()
            line("... done waiting for %s to exit", v)
