#
#   Copyright (c) 2018 Amit Green.  All rights reserved.
#
@gem('Diamond.Chore')
def gem():
    require_gem('Diamond.Core')
    require_gem('Diamond.Status')


    class DiamondChore(Object):
        __slots__ = ((
            'status',                   #   Integer
            'done',                     #   Integer
            'priority',                 #   Integer
            'thread',                   #   BaseThread+
            'ephemeral',                #   FibonacciEphemeral
            'atom',                     #   FibonacciAtom
        ))


        def __init__(t, priority, thread, ephemeral):
            t.status    = STATUS_ACTIVE__2
            t.done      = 0
            t.priority  = priority
            t.thread    = thread
            t.ephemeral = ephemeral
            t.atom      = none


        def ATOMIC_DOUBLE_DECREMENT__status(t):
            LARGE_CHECK_INTERVAL()

            status = t.status - 2

            t.status = status

            NORMAL_CHECK_INTERVAL()

            return status


        #
        #   Step 1: t.atom        = ephemeral.atom      [CAS]
        #   Step 2: epemeral.atom = t.atom.next_atom()  [CAS]
        #   Step 3: t.done        = 7                   [OVERWRITE]
        #
        def chore(t):
            thread_number = t.thread.thread_number
            ephemeral     = t.ephemeral
            atom          = t.atom

            if atom is none:
                atom = ephemeral.atom

                previous = t.COMPARE_AND_SWAP__atom(none, atom)                 #   ATTEMPT: Step #1 [CAS]

                if previous is none:                                            #   SUCCESS: Step #1 [CAS]
                    line('#%d: step #1 done ... %s ...', thread_number, t)

                    after = atom.next_atom() 

                    previous = ephemeral.COMPARE_AND_SWAP__atom(atom, after)    #   ATTEMPT: Step #2 [CAS]

                    t.done = 7                                                  #   STEP #3 [OVERWRITE]

                    if previous is atom:                                        #   SUCCESS: Step #2 [CAS]
                        line('#%d: step #2 done ... %s', thread_number, t)
                    else:                                                       #   FAILED: Step #2 [CAS]
                        line('#%d: attempted to do step #2 ... BUT already done ... %s', thread_number, t)

                    #
                    #   PRIMARY PATH:
                    #       We did Step #1
                    #       Attempted to do Step #2 (Either we did it or someone else did it)
                    #       We did Step #3
                    #
                    return

                #
                #   We TRIED to do step #1; but someone else did it instead ...
                #
                if t.done is 7:
                    line('#%d: attempted to do step #1 ... BUT steps #1, #2 & #3 already done ... %s',
                         thread_number, t)

                    return

                line('#%d: attempted to do step #1 ... BUT step #1 already done (step #3 NOT done) ... %s ...',
                     thread_number, t)

                t.atom = previous
            else:                                                               #   Step #1 already done
                if t.done is 7:                                                 #   Step #1, #2 & #3 already done
                    line('#%d: steps #1, #2, & #3 already done ... %s', thread_number, t)
                    return

                line('#%d: step #1 already done ... %s ...', thread_number, t)

            #
            #   SECONDARY path:
            #       1.  Someone else did step #1:
            #               o   We may have attempted to do step #1 & failed; OR
            #               o   Step #1 was already done before we started.
            #       2.  We did not check if they did Step #2
            #       3.  They did NOT do step #3.
            #
            #       So we need to check if Step #2 needs to be done
            #
            if atom is not ephemeral.atom:                                      #   Step #2 already done
                t.done = 7                                      
                line('#%d: step #2 already done ... %s', thread_number, t)
                return

            previous = ephemeral.COMPARE_AND_SWAP__atom(atom, after)            #   Step #2 [CAS]

            t.done = 7                                                          #   Step #3 [OVERWRITE]

            if previous is atom:                                                #   SUCCESS: Step #2 [CAS]
                line('#%d: step #2 done ... %s', thread_number, t)
            else:                                                               #   FAILED: Step #2 [CAS]
                line('#%d: attempted to do step #2 ... BUT already done ... %s', thread_number, t)


        def COMPARE_AND_SWAP__atom(t, before, after):
            LARGE_CHECK_INTERVAL()

            r = t.atom

            if r is before:
                t.atom = after

            NORMAL_CHECK_INTERVAL()

            return r


        def COMPARE_AND_SWAP__status(t, before, after):
            LARGE_CHECK_INTERVAL()

            r = t.status

            if r is before:
                t.status = after

            NORMAL_CHECK_INTERVAL()

            return r


        def __repr__(t):
            status    = t.status
            done      = t.done
            priority  = t.priority
            thread    = t.thread
            ephemeral = t.ephemeral
            atom      = t.atom

            status_name = status_map[status & STATUS_MASK]
            count       = status & COUNT_MASK

            return arrange('<DiamondChore %s %s %d; %d #%d; %s>',
                           status_name, ('done'   if done else   'ready'), count,
                           priority, thread.thread_number,
                           ('none'   if atom is none else   atom))


    @share
    def create_DiamondChore(priority, thread, ephemeral):
        return DiamondChore(priority, thread, ephemeral)
