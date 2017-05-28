#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.Configuration')
def gem():
    class Gem_Configuration(Object):
        __slots__ = ((
            'testing',                  #   Boolean
        ))

        
        def __init__(t):
            t.testing = false


    gem_configuration = Gem_Configuration()


    del Gem_Configuration.__init__


    export(
        'gem_configuration',    gem_configuration,
    )
