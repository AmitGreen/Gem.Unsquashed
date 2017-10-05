#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.DualFrill')
def gem():
    dual_frill_cache  = {}
    lookup_dual_frill = dual_frill_cache.get
    store_dual_frill  = dual_frill_cache.__setitem__


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


    class IndentedToken_X_Frill(DualFrill):
        __slots__ = (())

        comment        = 0
        indented_token = DualFrill.a
        x              = DualFrill.b


    #DualFrill.k1 = DualFrill.a
    DualFrill.k2 = DualFrill.b


    conjure_dual_frill = produce_conjure_dual(
                             'dual-frill',
                             DualFrill,
                             dual_frill_cache,
                             lookup_dual_frill,
                             store_dual_frill
                         )


    conjure__indented_token__x__frill = produce_conjure_dual(
                             'indented-token--x--frill',
                             IndentedToken_X_Frill,
                             dual_frill_cache,
                             lookup_dual_frill,
                             store_dual_frill
                         )


    append_cache('dual-frill', dual_frill_cache)


    share(
        'conjure_dual_frill',                   conjure_dual_frill,
        'conjure__indented_token__x__frill',    conjure__indented_token__x__frill,
    )
