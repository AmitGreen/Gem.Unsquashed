#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.DualFrill')
def gem():
    dual_frill_cache  = {}
    lookup_dual_frill = dual_frill_cache.get
    store_dual_frill  = dual_frill_cache.__setitem__


    class VW_Frill(Object):
        __slots__ = ((
            'a',                        #   SapphireToken+
            'b',                        #   SapphireToken+
        ))

        comment        = 0
        display_name   = 'vw-frill'
        frill_estimate = 2

        __init__       = construct__ab
        __repr__       = portray__ab
        count_newlines = count_newlines__ab
        display_token  = display_token__ab


    VW_Frill.v = VW_Frill.a
    VW_Frill.w = VW_Frill.b

    #VW_Frill.k1 = VW_Frill.a
    VW_Frill.k2 = VW_Frill.b


    conjure_vw_frill = produce_conjure_dual(
                           'vw-frill',
                           VW_Frill,
                           dual_frill_cache,
                           lookup_dual_frill,
                           store_dual_frill
                       )


    VW_Frill.mutate    = produce_mutate__ab   ('vw_frill', conjure_vw_frill)
    VW_Frill.transform = produce_transform__ab('vw_frill', conjure_vw_frill)


    append_cache('dual-frill', dual_frill_cache)


    share(
        'conjure_vw_frill',     conjure_vw_frill,
    )
