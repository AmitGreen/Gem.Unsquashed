#
#   Copyright (c) 2018 Amit Green.  All rights reserved.
#
@gem('Diamond.Development')
def gem():
    require_gem('Diamond.Chore')
    require_gem('Diamond.Core')
    require_gem('Diamond.Fibonacci')
    require_gem('Diamond.Interval')
    require_gem('Diamond.Shared')
    require_gem('Diamond.Thread')


    class DevelopmentThread(BaseThread):
        __slots__ = ((
            'ephemeral',                #   FibonacciEphemeral
            'shared',                   #   Shared
        ))


        def __init__(t, thread_number, lock, ephemeral, shared):
            BaseThread.__init__(t, thread_number, lock)

            t.ephemeral = ephemeral
            t.shared    = shared


        def run(t):
            line('Now running: %s', t)

            ephemeral     = t.ephemeral
            shared        = t.shared
            thread_number = t.thread_number
            use_right     = (7   if thread_number & 1 else   0)

            while ephemeral.atom.second < 100:
                priority = t.shared.ATOMIC_INCREMENT__priority()
                my_chore = create_DiamondChore(priority, t, ephemeral)

                line('#%d: created %s', thread_number, my_chore)

                if use_right:
                    if shared.left is none:
                        previous = shared.COMPARE_AND_SWAP__chore(none, my_chore)

                        success = (7   if previous is none else   0)
                    else:
                        success = 0

                    if success is 0:
                        assert shared.right_status == STATUS_ACTIVE
                        assert shared.right        is none

                        shared.right_status = STATUS_USING__1
                        shared.right        = my_chore
                else:
                    if shared.right is none:
                        previous = shared.COMPARE_AND_SWAP__chore(none, my_chore)

                        success = (7   if previous is none else   0)
                    else:
                        success = 0

                    if success is 0:
                        assert shared.left_status == STATUS_ACTIVE
                        assert shared.left        is none

                        shared.left_status = STATUS_USING__1
                        shared.left        = my_chore

                sleep(0.00001)

                while 7 is 7:
                    chore = shared.chore

                    if my_chore.done is 7:
                        break

                    if my_chore is not chore:
                        raise_runtime_error('run#3: my_chore%s is not chore%s', my_chore, chore)

                    chore.chore()

                    previous = shared.COMPARE_AND_SWAP__chore(chore, none)

                    if previous is not chore:
                        raise_runtime_error('run#3: previous is %s', previous)

                    if 0 and chore is my_chore:
                        status = my_chore.ATOMIC_DOUBLE_DECREMENT__status()

                        if status == STATUS_ACTIVE:
                            previous = my_chore.COMPARE_AND_SWAP__status(status, STATUS_REMOVING__1)

                            if status != previous:
                                line('#%d: attempted to remove %s; ...',
                                     thread_number, my_chore)


    @share
    def command_development():
        line('check_interval is %d', fetch_check_interval())

        ephemeral = create_Fibonacci()
        shared    = create_DiamondShared()

        line('shared: %s', shared)

        thread_many = []

        append_thread = thread_many.append

        for thread_number in iterate_range(1):
            thread = create_Thread(DevelopmentThread, thread_number, ephemeral, shared)

            append_thread(thread)

            thread.start()

        for v in thread_many:
            line("Waiting for %s to exit ...", v)
            v.wait()
            line("... done waiting for %s to exit", v)
