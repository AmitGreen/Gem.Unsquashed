#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.TripleFrill')
def gem():
    triple_frill_cache  = {}
    lookup_triple_frill = triple_frill_cache.get
    store_triple_frill  = triple_frill_cache.__setitem__


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


    class Commented_IndentedKeyword_X_Frill(TripleFrill):
        __slots__ = (())

        comment          = TripleFrill.a
        indented_keyword = TripleFrill.b
        x                = TripleFrill.c


    class Indented_XY_Frill(TripleFrill):
        __slots__ = (())

        comment     = 0
        indentation = TripleFrill.a
        x           = TripleFrill.b
        y           = TripleFrill.c


    TripleFrill.k1 = TripleFrill.a
    TripleFrill.k2 = TripleFrill.b
    TripleFrill.k3 = TripleFrill.c


    conjure_commented__indented_keyword__x__frill = produce_conjure_triple(
                                                        'commented--indented-keyword--x--frill',
                                                        Commented_IndentedKeyword_X_Frill,
                                                        triple_frill_cache,
                                                        lookup_triple_frill,
                                                        store_triple_frill,
                                                    )

    conjure_indented_xy_frill = produce_conjure_triple(
                                    'indented-xy-frill',
                                    Indented_XY_Frill,
                                    triple_frill_cache,
                                    lookup_triple_frill,
                                    store_triple_frill,
                                )

    conjure_triple_frill = produce_conjure_triple(
                               'triple-frill',
                               TripleFrill,
                               triple_frill_cache,
                               lookup_triple_frill,
                               store_triple_frill,
                           )


    append_cache('triple-frill', triple_frill_cache)


    share(
        'conjure_commented__indented_keyword__x__frill',    conjure_commented__indented_keyword__x__frill,
        'conjure_indented_xy_frill',                        conjure_indented_xy_frill,
        'conjure_triple_frill',                             conjure_triple_frill,
    )
