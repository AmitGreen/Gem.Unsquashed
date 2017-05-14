#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Pearl.Core')
def gem():
    require_gem('Gem.Absent')
    require_gem('Gem.Exception')


    from Gem import stop_iteration


    share(
        #
        #   Values
        #
        'stop_iteration',               stop_iteration,
    )
