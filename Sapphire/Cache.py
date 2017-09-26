#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Cache')
def gem():
    @share
    @privileged
    def produce_dual_cache_WithFrill(
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


        def conjure_dual(a, frill):
            #
            #   This is pretty much the same as produce_dual_cache with the following changes:
            #
            #       1.  Order is .frill, .a (intead of .a, .b)
            #
            #       2.  Instead of "Meta(a, b)" it creates a dynamic class as follows:
            #
            #               "conjure_Meta_WithFrill(Meta, a, frill)"
            #
            first = lookup(frill, absent)

            if first.__class__ is Map:
                return (
                              first.get(a)
                           or first.setdefault(a, conjure_Meta_WithFrill(Meta, a, frill))
                       )

            if first.a is a:
                return first

            r = conjure_Meta_WithFrill(Meta, a, frill)

            store(frill, (r   if first is absent else   { first.a : first, a : r }))

            return r


        if __debug__:
            conjure_dual.__name__ = intern_arrange('conjure_%s', name)

        return conjure_dual


    @share
    @privileged
    def produce_quadruple_cache_WithFrill(
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


        def conjure_quadruple(a, b, c, frill):
            #
            #   This is pretty much the same as produce_quadruple_cache_functions with the following changes:
            #
            #       1.  Order is .frill, .a, .b, .c (intead of .a, .b, .c, .d)
            #
            #       2.  Instead of "Meta(a, b, c, d)" it creates a dynamic class as follows:
            #
            #               "conjure_Meta_WithFrill(Meta, a, b, c, frill)"
            #
            first = lookup(frill, absent)

            if first.__class__ is Map:
                second = first.get(a, absent)

                if second.__class__ is Map:
                    third = first.get(b, absent)

                    if third.__class__ is Map:
                        return (
                                      third.get(c)
                                   or third.setdefault(c, conjure_Meta_WithFrill(Meta, a, b, c, frill))
                               )

                    if third.c is c:
                        return third

                    r = conjure_Meta_WithFrill(Meta, a, b, c, frill)

                    second[b] = (r   if third is absent else   { third.c : third, c : r })

                    return r

                if second.b is b:
                    if second.c is c:
                        return second

                    r = conjure_Meta_WithFrill(Meta, a, b, c, frill)

                    first[a] = { b : { second.c : second, c : r } }

                    return r

                r = conjure_Meta_WithFrill(Meta, a, b, c, frill)

                first[a] = (r   if second is absent else   { second.b : second, b : r })

                return r

            if first.a is a:
                if first.b is b:
                    if first.c is c:
                        return first

                    r = conjure_Meta_WithFrill(Meta, a, b, c, frill)

                    store(frill, { a : { b : { first.c : first, c : r } } })

                    return r

                r = conjure_Meta_WithFrill(Meta, a, b, c, frill)

                store(frill, { a : { first.b : first, b : r } })

                return r

            r = conjure_Meta_WithFrill(Meta, a, b, c, frill)

            store(frill, (r   if first is absent else   { first.a : first, a : r }))

            return r


        if __debug__:
            conjure_quadruple.__name__ = intern_arrange('conjure_%s', name)

        return conjure_quadruple


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


        def conjure_triple(a, b, frill):
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
            conjure_triple.__name__ = intern_arrange('conjure_%s', name)

        return conjure_triple
