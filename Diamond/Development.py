#
#   Copyright (c) 2018 Amit Green.  All rights reserved.
#
@gem('Diamond.Development')
def gem():
    require_gem('Diamond.Core')
    require_gem('Diamond.Counter')
    require_gem('Diamond.Interval')
    require_gem('Diamond.Shared')
    require_gem('Diamond.Thread')
    require_gem('Diamond.Work')


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
        shared  = create_DiamondShared()

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
