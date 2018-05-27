#
#   Copyright (c) 2018 Amit Green.  All rights reserved.
#
@gem('Gem.Thread')
def gem():
    PythonThread = __import__('thread')


    export(
        'allocate_lock',        PythonThread.allocate_lock,
        'start_new_thread',     PythonThread.start_new_thread,
        'thread_identifier',    PythonThread.get_ident,
    )
