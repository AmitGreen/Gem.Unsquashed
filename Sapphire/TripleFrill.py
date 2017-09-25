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


    cache  = {}
    lookup = cache.get
    store  = cache.__setitem__


    @share
    def conjure_triple_frill(a, b, c):
        first = lookup(a, absent)

        if first.__class__ is Map:
            second = first.get(b, absent)

            if second.__class__ is Map:
                return (second.get(c)) or (second.setdefault(c, TripleFrill(a, b, c)))

            if second.c is c:
                return second

            r = TripleFrill(a, b, c)

            first[b] = (r   if second is absent else   { second.c : second, c : r })

            return r

        if first.b is b:
            if first.c is c:
                return first

            r = TripleFrill(a, b, c)

            store(a, { first.b : { first.c : first, c : r } })

            return r

        r = TripleFrill(a, b, c)

        store(a, (r   if first is absent else   { first.b : first, b : r }))

        return r


    @share
    def dump_triple_frill_cache():
        dump_cache('triple_frill_cache', cache)
