#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.DualFrill')
def gem():
    class DualFrill(Object):
        __slots__ = ((
            'a',                        #   SapphireToken+
            'b',                        #   SapphireToken+
        ))


        frill_estimate = 2


        def __init__(t, a, b):
            t.a = a
            t.b = b


        def __repr__(t):
            return arrange('<%s %r %r>', t.__class__.__name__, t.a, t.b)


        def count_newlines(t):
            return t.a.count_newlines() + t.b.count_newlines()


        def display_token(t):
            return arrange('<dual-frill %s %s>', t.a.display_token(), t.b.display_token())

 
    DualFrill.kd1 = DualFrill.a
    DualFrill.kd2 = DualFrill.b


    dual_frill_cache = {}

    conjure_dual_frill = produce_dual_cache('dual_frill', DualFrill, dual_frill_cache)


    @share
    def dump_dual_frill_cache():
        dump_cache('dual_frill_cache', dual_frill_cache)


    share(
        'conjure_dual_frill',   conjure_dual_frill,
    )
