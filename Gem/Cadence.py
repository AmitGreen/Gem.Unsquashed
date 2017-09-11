#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.Cadence')
def gem():
    show = 0


    class Cadence(Object):
        __slots__ = ((
            'name',                                         #   String+
            'is_initialized_exited_or_exception',           #   Boolean
            'is_initialized_exited_exception_or_reuse',     #   Boolean
        ))


        def __init__(t, name, exception = false, exited = false, initialized = false, reuse = false):
            t.name                                     = name
            t.is_initialized_exited_or_exception       = (exception) or (exited) or (initialized)
            t.is_initialized_exited_exception_or_reuse = (exception) or (exited) or (initialized) or (reuse)


    cadence_constructing = Cadence('cadence_constructing')
    cadence_entered      = Cadence('cadence_entered')
    cadence_exception    = Cadence('cadence_exception',   exception   = true)
    cadence_exited       = Cadence('cadence_exited',      exited      = true)
    cadence_initialized  = Cadence('cadence_initialized', initialized = true)
    cadence_reuse        = Cadence('cadence_reuse',       reuse       = true)


    del Cadence.__init__


    export(
        #
        #   Values
        #
        'cadence_constructing', cadence_constructing,
        'cadence_entered',      cadence_entered,
        'cadence_exception',    cadence_exception,
        'cadence_exited',       cadence_exited,
        'cadence_initialized',  cadence_initialized,
        'cadence_reuse',        cadence_reuse,
    )
