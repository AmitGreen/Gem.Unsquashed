#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Marble.Core')
def gem():
    require_gem('Gem.ContextManager')
    require_gem('Gem.Exception')
    require_gem('Gem.DelayedFileOutput')
    require_gem('Gem.Path')
    require_gem('Gem.System')


    from Gem import create_DelayedFileOutput, empty_context_manager, execute
    from Gem import path_join, print_exception_chain, program_exit, slice_all


    share(
        #
        #   Imported functions
        #
        'create_DelayedFileOutput',     create_DelayedFileOutput,
        'empty_context_manager',        empty_context_manager,
        'execute',                      execute,
        'path_join',                    path_join,
        'print_exception_chain',        print_exception_chain,
        'program_exit',                 program_exit,


        #
        #   Improted values
        #
        'slice_all',                    slice_all,
    )
