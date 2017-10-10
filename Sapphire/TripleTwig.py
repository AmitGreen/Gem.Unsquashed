#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.TripleTwig')
def gem():
    require_gem('Sapphire.Method')


    triple_twig_cache  = {}
    lookup_triple_twig = triple_twig_cache.get
    store_triple_twig  = triple_twig_cache.__setitem__


    @share
    class TripleTwig(SapphireTrunk):
        __slots__ = ((
            'a',                        #   Any
            'b',                        #   Any
            'c',                        #   Any
        ))


        __init__       = construct__123
        __repr__       = portray__123
        count_newlines = count_newlines__123
        display_token  = display_token__123
        dump_token     = dump_token__123
        write          = write__123


    TripleTwig.k1 = TripleTwig.a
    TripleTwig.k2 = TripleTwig.b
    TripleTwig.k3 = TripleTwig.c


    @share
    def produce_conjure_triple_twig(name, Meta):
        return produce_conjure_triple__312(name, Meta, triple_twig_cache, lookup_triple_twig, store_triple_twig)


    append_cache('triple-twig', triple_twig_cache)
