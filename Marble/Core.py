#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Marble.Core')
def gem():
    require_gem('Gem.DelayedFileOutput')
    require_gem('Gem.Path')


    from Gem import create_DelayedFileOutput, path_join


    share(
        #
        #   Imported functions
        #
        'create_DelayedFileOutput',     create_DelayedFileOutput,
        'path_join',                    path_join,
    )
