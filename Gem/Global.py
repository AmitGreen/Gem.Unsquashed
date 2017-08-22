#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.Global')
def gem():
    class Gem_Global(Object):
        __slots__ = (())


        if is_python_2:
            __slots__ += ((
                'context',              #   None | Exception
            ))


        __slots__ += ((
            'testing',                  #   Boolean
        ))


        def __init__(t):
            if is_python_2:
                t.context = none

            t.testing = false


    gem_global = Gem_Global()


    del Gem_Global.__init__


    export(
        'gem_global',    gem_global,
    )
