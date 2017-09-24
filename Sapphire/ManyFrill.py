#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.ManyFrill')
def gem():
    cache   = {}
    provide = cache.setdefault


    class ManyFrill(Tuple):
        __slots__ = (())


        frill_estimate = 7


        def __repr__(t):
            return arrange('<%s %s>', t.__class__.__name__, ' '.join(portray(v)   for v in t))


        def display_token(t):
            return arrange('<many-frill %s>', ' '.join(v.display_token()   for v in t))


        def iterate_write(t, w):
            for v in t:
                w(v.s)
                yield


    @share
    def conjure_many_frill(many):
        total = length(many)

        if total is 1:
            assert many[0].frill_estimate is 1

            return many[0]

        if total is 2:
            return conjure_dual_frill(many[0], many[1])

        if total is 3:
            return conjure_triple_frill(many[0], many[1], many[2])

        r = ManyFrill(many)

        return provide(r, r)


    if __debug__:
        @share
        def dump_many_frill_cache():
            dump_cache('many-frill-cache', cache)
