#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.ContextManager')
def gem():
    class EmptyContextManager(Object):
        __slots__ = (())


        def __enter__(t):
            return t


        def __exit__(t, e_type, e, traceback):
            pass


    empty_context_manager = EmptyContextManager()


    export(
        'empty_context_manager',     empty_context_manager,
    )
