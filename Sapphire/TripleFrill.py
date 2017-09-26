#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.TripleFrill')
def gem():
    class TripleFrill(Object):
        __slots__ = ((
            'a',                        #   SapphireToken+
            'b',                        #   SapphireToken+
            'c',                        #   SapphireToken+
        ))


        frill_estimate = 3


        def __init__(t, a, b, c):
            t.a = a
            t.b = b
            t.c = c


        def __repr__(t):
            return arrange('<%s %r %r %r>', t.__class__.__name__, t.a, t.b, t.c)


        def count_newlines(t):
            return t.a.count_newlines() + t.b.count_newlines() + t.c.count_newlines()


        def display_token(t):
            return arrange('<triple-frill %s %s %s>', t.a.display_token(), t.b.display_token(), t.c.display_token())


    TripleFrill.kt1 = TripleFrill.a
    TripleFrill.kt2 = TripleFrill.b
    TripleFrill.kt3 = TripleFrill.c


    triple_frill_cache = {}

    conjure_triple_frill = produce_triple_cache_functions('triple_frill', TripleFrill, triple_frill_cache)


    @share
    def dump_triple_frill_cache():
        dump_cache('triple_frill_cache', triple_frill_cache)


    share(
        'conjure_triple_frill',     conjure_triple_frill,
    )
