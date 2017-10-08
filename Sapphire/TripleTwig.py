#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.TripleTwig')
def gem():
    triple_twig_cache  = {}
    lookup_triple_twig = triple_twig_cache.get
    store_triple_twig  = triple_twig_cache.__setitem__


    @share
    def construct__abc(t, a, b, c):
        t.a = a
        t.b = b
        t.c = c


    @share
    def count_newlines__abc(t):
        return t.a.count_newlines() + t.b.count_newlines() + t.c.count_newlines()


    @share
    def display_token__abc(t):
        return arrange('<%s %s %s %s>',
                       t.display_name,
                       t.a.display_token(),
                       t.b.display_token(),
                       t.b.display_token())


    @share
    def portray__abc(t):
        return arrange('<%s %r %r %r>', t.__class__.__name__, t.a, t.b, t.c)


    @share
    class TripleTwig(SapphireTrunk):
        __slots__ = ((
            'a',                        #   Any
            'b',                        #   Any
            'c',                        #   Any
        ))


        __init__       = construct__abc
        __repr__       = portray__abc
        count_newlines = count_newlines__abc
        display_token  = display_token__abc


        def dump_token(t, f, newline = true):
            f.partial('<%s ', t.display_name)

            t    .a.dump_token(f)
            t    .b.dump_token(f)
            r = t.c.dump_token(f, false)

            return f.token_result(r, newline)
            

        def write(t, w):
            t.a.write(w)
            t.b.write(w)
            t.c.write(w)


    TripleTwig.k1 = TripleTwig.a
    TripleTwig.k2 = TripleTwig.b
    TripleTwig.k3 = TripleTwig.c


    @share
    def produce_conjure_triple_twig(name, Meta):
        return produce_conjure_triple__312(name, Meta, triple_twig_cache, lookup_triple_twig, store_triple_twig)


    append_cache('triple-twig', triple_twig_cache)
