#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.QuadrupleFrill')
def gem():
    quadruple_frill_cache  = {}
    lookup_quadruple_frill = quadruple_frill_cache.get
    store_quadruple_frill  = quadruple_frill_cache.__setitem__


    class QuadrupleFrill(Object):
        __slots__ = ((
            'a',                        #   SapphireToken+
            'b',                        #   SapphireToken+
            'c',                        #   SapphireToken+
            'd',                        #   SapphireToken+
        ))


        frill_estimate = 4


        def __init__(t, a, b, c, d):
            t.a = a
            t.b = b
            t.c = c
            t.d = d


        def __repr__(t):
            return arrange('<%s %r %r %r %r>', t.__class__.__name__, t.a, t.b, t.c, t.d)


        def count_newlines(t):
            return t.a.count_newlines() + t.b.count_newlines() + t.c.count_newlines() + t.d.count_newlines()


        def display_token(t):
            return arrange('<quadruple-frill %s %s %s %s>',
                           t.a.display_token(),
                           t.b.display_token(),
                           t.c.display_token(),
                           t.d.display_token())


    class Commented_XYZ_Frill(QuadrupleFrill):
        __slots__ = (())

        comment = QuadrupleFrill.a
        x       = QuadrupleFrill.b
        y       = QuadrupleFrill.c
        z       = QuadrupleFrill.d


    QuadrupleFrill.k1 = QuadrupleFrill.a
    QuadrupleFrill.k2 = QuadrupleFrill.b
    QuadrupleFrill.k3 = QuadrupleFrill.c
    QuadrupleFrill.k4 = QuadrupleFrill.d


    conjure_quadruple_frill = produce_conjure_quadruple__4123(
                                  'quadruple-frill',
                                  QuadrupleFrill,
                                  quadruple_frill_cache,
                                  lookup_quadruple_frill,
                                  store_quadruple_frill,
                              )

    conjure_commented_xyz_frill = produce_conjure_quadruple__4123(
                                      'commented-xyz-frill',
                                      Commented_XYZ_Frill,
                                      quadruple_frill_cache,
                                      lookup_quadruple_frill,
                                      store_quadruple_frill,
                                  )


    append_cache('quadruple-frill', quadruple_frill_cache)


    share(
        'conjure_quadruple_frill',      conjure_quadruple_frill,
        'conjure_commented_xyz_frill',  conjure_commented_xyz_frill,
    )
