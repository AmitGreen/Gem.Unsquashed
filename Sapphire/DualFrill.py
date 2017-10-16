#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.DualFrill')
def gem():
    dual_frill_cache  = {}
    lookup_dual_frill = dual_frill_cache.get
    store_dual_frill  = dual_frill_cache.__setitem__


    @share
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
        dump_token     = dump_token__12


        #
        #   NOTE:
        #       Do not simplify this to a .mutate method with a single parameter; even though as used
        #       .morph takes an 'a_priority' & 'b_priority' with exactly the same value.
        #
        #       This is deliberatly called .morph, as its not appropriate to do .mutate on a general
        #       wrapper like VW_frill.
        #
        #       Thus the specific method .morph here is to indicate [for code clarity of the reader] that
        #       something special is going on -- even though [for the computer] it really looks like
        #       a .mutate method with redundant parameters.
        #
        def morph(t, vary, a_priority, b_priorty):
            a = t.a
            b = t.b

            a__2 = a.mutate(vary, a_priority)
            b__2 = b.mutate(vary, a_priority)

            if (a is a__2) and (b is b__2):
                return t

            return conjure_vw_frill(a__2, b__2)


    VW_Frill.v = VW_Frill.a
    VW_Frill.w = VW_Frill.b

    VW_Frill.k1 = VW_Frill.a
    VW_Frill.k2 = VW_Frill.b


    conjure_vw_frill = produce_conjure_dual(
                           'vw-frill',
                           VW_Frill,
                           dual_frill_cache,
                           lookup_dual_frill,
                           store_dual_frill
                       )


    VW_Frill.transform = produce_transform__ab('vw_frill', conjure_vw_frill)


    append_cache('dual-frill', dual_frill_cache)


    share(
        'conjure_vw_frill',     conjure_vw_frill,
    )
