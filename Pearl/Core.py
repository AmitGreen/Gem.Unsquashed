#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Pearl.Core')
def gem():
    require_gem('Gem.Absent')
    require_gem('Gem.Cache')
    require_gem('Gem.Exception')
    require_gem('Gem.Global')
    require_gem('Gem.System')


    from Gem import gem_global, produce_cache_functions, python_frame, stop_iteration


    share(
        #
        #   Functions
        #
        'produce_cache_functions',      produce_cache_functions,
        'python_frame',                 python_frame,


        #
        #   Values
        #
        'gem_global',                   gem_global,
        'stop_iteration',               stop_iteration,
    )
