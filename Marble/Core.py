#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Marble.Core')
def gem():
    require_gem('Gem.ContextManager')
    require_gem('Gem.DelayedFileOutput')
    require_gem('Gem.Path')


    from Gem import create_DelayedFileOutput, empty_context_manager, path_join


    share(
        #
        #   Imported functions
        #
        'create_DelayedFileOutput',     create_DelayedFileOutput,
        'empty_context_manager',        empty_context_manager,
        'path_join',                    path_join,
    )
