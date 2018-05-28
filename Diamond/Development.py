#
#   Copyright (c) 2018 Amit Green.  All rights reserved.
#
@gem('Diamond.Development')
def gem():
    require_gem('Diamond.Chore')
    require_gem('Diamond.Core')
    require_gem('Diamond.Counter')
    require_gem('Diamond.Interval')
    require_gem('Diamond.Shared')
    require_gem('Diamond.Thread')


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
            use_right     = (7   if thread_number & 1 else   0)

            while counter.number < 10:
                priority = t.shared.ATOMIC_INCREMENT__priority()
                chore    = create_DiamondChore(t, priority, counter)

                if use_right:
                    if shared.left is none:
                        previous = shared.COMPARE_AND_SWAP__chore(none, chore)

                        success = (7   if previous is none else   0)
                    else:
                        success = 0

                    if success is 0:
                        assert shared.right_status == STATUS_ACTIVE
                        assert shared.right        is none

                        shared.right_status = STATUS_USING__1
                        shared.right        = chore
                else:
                    if shared.right is none:
                        previous = shared.COMPARE_AND_SWAP__chore(none, chore)

                        success = (7   if previous is none else   0)
                    else:
                        success = 0

                    if success is 0:
                        assert shared.left_status == STATUS_ACTIVE
                        assert shared.left        is none

                        shared.left_status = STATUS_USING__1
                        shared.left        = chore

                sleep(0.00001)

                chore.chore()

                previous = shared.COMPARE_AND_SWAP__chore(chore, none)

                if previous is not chore:
                    raise_runtime_error('run#3: previous is %s', previous)


    @share
    def command_development():
        line('check_interval is %d', fetch_check_interval())

        counter = create_Counter()
        shared  = create_DiamondShared()

        line('shared: %s', shared)

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
