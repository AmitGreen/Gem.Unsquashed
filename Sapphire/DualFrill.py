#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.DualFrill')
def gem():
    class DualFrill(Object):
        __slots__ = ((
            'a',                        #   Token+
            'b',                        #   Token+
        ))


        def __init__(t, a, b):
            t.a = a
            t.b = b


        def __repr__(t):
            return arrange('<%s %r %r>', t.__class__.__name__, t.a, t.b)


    dual_frill_cache   = {}
    lookup_dual_frill  = dual_frill_cache.get
    provide_dual_frill = dual_frill_cache.setdefault
    store_dual_frill   = dual_frill_cache.__setitem__


    @share
    def conjure_dual_frill(a, b):
        first = lookup_dual_frill(a, absent)

        if first is none:
            return provide_dual_frill(a, DualFrill(a, b))

        if first.__class__ is Map:
            return (first.get(a)) or (first.setdefault(a, DualFrill(a, b)))

        if first.b is b:
            return first

        r = DualFrill(a, b)

        store_dual_frill(a, { first.b : first, b : r })

        return r


    @share
    def dump_dual_frill_cache():
        line('===  dual_frill_cache  ===')

        for [k, v] in iterate_items_sorted_by_key(dual_frill_cache):
            if v.__class__ is Map:
                line('%s:', k)

                for [k2, w2] in view_items(v):
                    line('  %s: %s', k2, w2)

                continue

            line('%s: %s', k, v)
