#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.QuadrupleFrill')
def gem():
    require_gem('Sapphire.QuadrupleTwig')


    quadruple_frill_cache  = {}
    lookup_quadruple_frill = quadruple_frill_cache.get
    store_quadruple_frill  = quadruple_frill_cache.__setitem__


    class VWXY_Frill(QuadrupleTwig):
        __slots__ = (())
        v         = QuadrupleTwig.a
        w         = QuadrupleTwig.b
        x         = QuadrupleTwig.c
        y         = QuadrupleTwig.d

        frill_estimate = 4


    class Commented_VWX_Frill(QuadrupleTwig):
        __slots__ = (())
        comment   = QuadrupleTwig.a
        v         = QuadrupleTwig.b
        w         = QuadrupleTwig.c
        x         = QuadrupleTwig.d


    conjure_vwxy_frill = produce_conjure_quadruple__4123(
                             'vwxy-frill',
                             VWXY_Frill,
                             quadruple_frill_cache,
                             lookup_quadruple_frill,
                             store_quadruple_frill,
                         )

    conjure_commented_vwx_frill = produce_conjure_quadruple__4123(
                                      '#vwx-frill',
                                      Commented_VWX_Frill,
                                      quadruple_frill_cache,
                                      lookup_quadruple_frill,
                                      store_quadruple_frill,
                                  )


    append_cache('quadruple-frill', quadruple_frill_cache)


    share(
        'conjure_vwxy_frill',           conjure_vwxy_frill,
        'conjure_commented_vwx_frill',  conjure_commented_vwx_frill,
    )
