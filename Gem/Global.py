#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.Global')
def gem():
    class Gem_Global(Object):
        __slots__ = ((
            'testing',                  #   Boolean
        ))


        def __init__(t):
            t.testing = false


    gem_global = Gem_Global()


    del Gem_Global.__init__


    export(
        'gem_global',    gem_global,
    )
