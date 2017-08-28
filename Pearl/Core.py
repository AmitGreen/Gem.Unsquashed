#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Pearl.Core')
def gem():
    require_gem('Gem.Absent')
    require_gem('Gem.Cache')
    require_gem('Gem.Cadence')
    require_gem('Gem.Exception')
    require_gem('Gem.Global')
    require_gem('Gem.System')


    from Gem import cadence_constructing, cadence_entered, cadence_exception, cadence_exited, cadence_initialized
    from Gem import Exception, gem_global, maybe_exit_exception, produce_cache_functions, python_frame


    share(
        #
        #   Exception
        #
        'Exception',                    Exception,

        #
        #   Functions
        #
        'maybe_exit_exception',         maybe_exit_exception,
        'produce_cache_functions',      produce_cache_functions,
        'python_frame',                 python_frame,


        #
        #   Values
        #
        'cadence_constructing',         cadence_constructing,
        'cadence_entered',              cadence_entered,
        'cadence_exception',            cadence_exception,
        'cadence_exited',               cadence_exited,
        'cadence_initialized',          cadence_initialized,
        'gem_global',                   gem_global,
    )
