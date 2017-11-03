#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Marble.Core')
def gem():
    require_gem('Gem.DelayedFileOutput')


    from Gem import create_DelayedFileOutput


    share(
        #
        #   Imported functions
        #
        'create_DelayedFileOutput',     create_DelayedFileOutput,
    )
