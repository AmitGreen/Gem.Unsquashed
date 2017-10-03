#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.DualTwig')
def gem():
    dual_twig_cache  = {}
    lookup_dual_twig = dual_twig_cache.get
    store_dual_twig  = dual_twig_cache.__setitem__


    @share
    class DualTwig(SapphireTrunk):
        __slots__ = ((
            'a',                        #   Any
            'b',                        #   Any
        ))


        def __init__(t, a, b):
            t.a = a
            t.b = b


        def __repr__(t):
            return arrange('<%s %r %r>', t.__class__.__name__, t.a, t.b)


        def count_newlines(t):
            return t.a.count_newlines() + t.b.count_newlines()


        def display_token(t):
            return arrange('<%s %s %s>', t.display_name, t.a.display_token(), t.b.display_token())


        def dump_token(t, newline = true):
            partial('<%s ', t.display_name)
            t.a.dump_token()
            r = t.b.dump_token(false)

            if (r) and (newline):
                line('>')
                return false

            partial('>')
            return r
            

        def write(t, w):
            t.a.write(w)
            t.b.write(w)


    DualTwig.k1 = DualTwig.a
    DualTwig.k2 = DualTwig.b


    @share
    def produce_conjure_dual_twig(name, Meta):
        return produce_conjure_dual__21(name, Meta, dual_twig_cache, lookup_dual_twig, store_dual_twig)


    append_cache('dual-twig', dual_twig_cache)
