#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.DualFrill')
def gem():
    dual_frill_cache  = {}
    lookup_dual_frill = dual_frill_cache.get
    store_dual_frill  = dual_frill_cache.__setitem__


    class XY_Frill(Object):
        __slots__ = ((
            'a',                        #   SapphireToken+
            'b',                        #   SapphireToken+
        ))

        comment        = 0
        display_name   = 'xy-frill'
        frill_estimate = 2

        __init__       = construct__ab
        __repr__       = portray__ab
        count_newlines = count_newlines__ab
        display_token  = display_token__ab


    XY_Frill.x = XY_Frill.a
    XY_Frill.y = XY_Frill.b

    #XY_Frill.k1 = XY_Frill.a
    XY_Frill.k2 = XY_Frill.b


    conjure_xy_frill = produce_conjure_dual(
                           'xy-frill',
                           XY_Frill,
                           dual_frill_cache,
                           lookup_dual_frill,
                           store_dual_frill
                       )


    append_cache('dual-frill', dual_frill_cache)


    share(
        'conjure_xy_frill',     conjure_xy_frill,
    )
