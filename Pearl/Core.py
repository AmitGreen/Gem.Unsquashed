#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Pearl.Core')
def gem():
    require_gem('Gem.Absent')
    require_gem('Gem.Cache')
    require_gem('Gem.Configuration')
    require_gem('Gem.Exception')


    from Gem import gem_configuration, produce_cache_functions, stop_iteration


    share(
        #
        #   Functions
        #
       'produce_cache_functions',      produce_cache_functions,


        #
        #   Values
        #
        'gem_configuration',            gem_configuration,
        'stop_iteration',               stop_iteration,
    )
