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


        def display_token(t):
            return arrange('<dual-frill %s %s>', t.a.display_token(), t.b.display_token())



    dual_frill_cache   = {}
    lookup_dual_frill  = dual_frill_cache.get
    provide_dual_frill = dual_frill_cache.setdefault
    store_dual_frill   = dual_frill_cache.__setitem__


    @share
    def conjure_dual_frill(a, b):
        first = lookup_dual_frill(a, absent)

        if first.__class__ is Map:
            return (first.get(b)) or (first.setdefault(b, DualFrill(a, b)))

        if first.b is b:
            return first

        r = DualFrill(a, b)

        store_dual_frill(a, (r   if first is absent else   { first.b : first, b : r }))

        return r


    @share
    def dump_dual_frill_cache():
        dump_cache('dual_frill_cache', dual_frill_cache)
