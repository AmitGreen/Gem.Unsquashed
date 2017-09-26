#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Cache')
def gem():
    produce_dual_cache_functions = Shared.produce_dual_cache_functions      #   Due to privileged


    @share
    @privileged
    def produce_triple_cache_WithFrill(
            name,
            Meta,
            conjure_Meta_WithFrill,

            cache  = absent,
            lookup = absent,
            store  = absent
    ):
        if cache is absent:
            cache = {}

        if lookup is absent:
            lookup = cache.get

        if store is absent:
            store = cache.__setitem__


        def conjure_triple(a, frill, b):
            #
            #   This is pretty much the same as produce_triple_cache_functions with the following changes:
            #
            #       1.  Order is .frill, .a, .b (intead of .a, .b, .c)
            #
            #       2.  Instead of "Meta(a, b, c)" it creates a dynamic class as follows:
            #
            #               "conjure_Meta_WithFrill(Meta, a, b, frill)"
            #
            first = lookup(frill, absent)

            if first.__class__ is Map:
                second = first.get(a, absent)

                if second.__class__ is Map:
                    return (second.get(b)) or (second.setdefault(b, conjure_Meta_WithFrill(Meta, a, b, frill)))

                if second.b is b:
                    return second

                r = conjure_Meta_WithFrill(Meta, a, b, frill)

                first[a] = (r   if second is absent else   { second.b : second, b : r })

                return r

            if first.a is a:
                if first.b is b:
                    return first

                r = conjure_Meta_WithFrill(Meta, a, b, frill)

                store(frill, { first.a : { first.b : first, b : r } })

                return r

            r = conjure_Meta_WithFrill(Meta, a, b, frill)

            store(frill, (r   if first is absent else   { first.a : first, a : r }))

            return r


        if __debug__:
            conjure_triple.__name__ = intern_arrange('conjure_%s__X__triple', name)

        return conjure_triple
