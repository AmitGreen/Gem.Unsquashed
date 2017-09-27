#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.Cache')
def gem():
    require_gem('Gem.Absent')


    @export
    def produce_conjure_by_name(name, Meta):
        [conjure_by_name] = produce_cache_functions(name, Meta, produce_conjure_by_name = true)

        return conjure_by_name


    @export
    @privileged
    def produce_cache_functions(
            name,
            Meta                    = absent,
            produce_cache           = false,
            produce_conjure_by_name = false,
            produce_find            = false,
            produce_insert_interned = false,
            produce_lookup          = false,
    ):
        result = []
        append = result.append

        cache = {}

        if (produce_conjure_by_name) or (produce_insert_interned):
            provide = cache.setdefault

        if (produce_conjure_by_name) or (produce_lookup):
            lookup = cache.get

        if (produce_find) or (produce_insert_interned):
            find = cache.__getitem__

        if produce_cache:
            append(cache)

        if produce_conjure_by_name:
            assert Meta is not absent


            def conjure_by_name(k):
                r = lookup(k)

                if r is not none:
                    return r

                interned_k = intern_string(k)

                return provide(interned_k, Meta(interned_k))


            if __debug__:
                conjure_by_name.__name__ = arrange('conjure_%s', name)


            append(conjure_by_name)

        if produce_find:
            append(find)

        if produce_insert_interned:
            contains = cache.__contains__


            if __debug__:
                def insert_interned(interned_k, v):
                    if contains(interned_k):
                        raise_runtime_error('cache %s: attempt to insert key %r with value %r (already has value %r)',
                                            name, interned_k, v, find(interned_k))

                    return provide(interned_k, v)


                insert_interned.__name__ = arrange('insert_interned_%s', name)


                append(insert_interned)
            else:
                append(provide)

        if produce_lookup:
            append(lookup)

        return Tuple(result)


    @export
    @privileged
    def produce_dual_cache(
            name,
            Meta,

            cache  = absent,
            lookup = absent,
            store  = absent,
    ):
        if cache is absent:
            cache = {}

        if lookup is absent:
            lookup = cache.get

        if store is absent:
            store = cache.__setitem__


        def conjure_dual(k1, k2):
            first = lookup(k1, absent)

            if first.__class__ is Map:
                return (first.get(k2)) or (first.setdefault(k2, Meta(k1, k2)))

            if first.k2 is k2:
                return first

            r = Meta(k1, k2)

            store(k1, (r   if first is absent else   { first.k2 : first, k2 : r }))

            return r


        if __debug__:
            conjure_dual.__name__ = intern_arrange('conjure_%s', name)

        return conjure_dual


    @export
    @privileged
    def produce_dual_cache__12A(
            name,
            Meta,

            cache  = absent,
            lookup = absent,
            store  = absent,
    ):
        if cache is absent:
            cache = {}

        if lookup is absent:
            lookup = cache.get

        if store is absent:
            store = cache.__setitem__


        def conjure_dual__12A(k1, k2):
            first = lookup(k1, absent)

            if first.__class__ is Map:
                second = first.get(k2, absent)

                if second.__class__ is Map:
                    return (second.get(absent)) or (second.setdefault(absent, Meta(k1, k2)))

                if second.k3 is absent:
                    return second

                r = Meta(k1, k2)

                first[k2] = (r   if second is absent else   { second.k3 : second, absent : r })

                return r

            if first.k2 is k2:
                if first.k3 is absent:
                    return first

                r = Meta(k1, k2)

                store(k1, { first.k2 : { first.k3 : first, absent : r } })

                return r

            r = Meta(k1, k2)

            store(k1, (r   if first is absent else   { first.k2 : first, k2 : r }))

            return r


        if __debug__:
            conjure_dual__12A.__name__ = intern_arrange('conjure_%s__12A', name)

        return conjure_dual__12A


    @export
    @privileged
    def produce_dual_cache__21(
            name,
            Meta,

            cache  = absent,
            lookup = absent,
            store  = absent,
    ):
        if cache is absent:
            cache = {}

        if lookup is absent:
            lookup = cache.get

        if store is absent:
            store = cache.__setitem__


        def conjure_dual__21(k1, k2):
            first = lookup(k2, absent)

            if first.__class__ is Map:
                return (first.get(k1)) or (first.setdefault(k1, Meta(k1, k2)))

            if first.k1 is k1:
                return first

            r = Meta(k1, k2)

            store(k2, (r   if first is absent else   { first.k1 : first, k1 : r }))

            return r


        if __debug__:
            conjure_dual__21.__name__ = intern_arrange('conjure_%s__21', name)

        return conjure_dual__21


    @export
    @privileged
    def produce_quadruple_cache(
            name,
            Meta,

            cache  = absent,
            lookup = absent,
            store  = absent,
    ):
        if cache is absent:
            cache = {}

        if lookup is absent:
            lookup = cache.get

        if store is absent:
            store = cache.__setitem__


        def conjure_quadruple(kq1, kq2, kq3, kq4):
            first = lookup(kq1, absent)

            if first.__class__ is Map:
                second = first.get(kq2, absent)

                if second.__class__ is Map:
                    third = first.get(kq3, absent)

                    if third.__class__ is Map:
                        return (
                                      third.get(kq4)
                                   or third.setdefault(kq4, Meta(kq1, kq2, kq3, kq4))
                               )

                    if third.kq4 is kq4:
                        return third

                    r = Meta(kq1, kq2, kq3, kq4)

                    second[kq3] = (r   if third is absent else   { third.kq4 : third, kq4 : r })

                    return r

                if second.kq3 is kq3:
                    if second.kq4 is kq4:
                        return second

                    r = Meta(kq1, kq2, kq3, kq4)

                    first[kq2] = { kq3 : { second.kq4 : second, kq4 : r } }

                    return r

                r = Meta(kq1, kq2, kq3, kq4)

                first[kq2] = (r   if second is absent else   { second.kq3 : second, kq3 : r })

                return r

            if first.kq2 is kq2:
                if first.kq3 is kq3:
                    if first.kq4 is kq4:
                        return first

                    r = Meta(kq1, kq2, kq3, kq4)

                    store(kq1, { kq2 : { kq3 : { first.kq4 : first, kq4 : r } } })

                    return r

                r = Meta(kq1, kq2, kq3, kq4)

                store(kq1, { kq2 : { first.kq3 : first, kq3 : r } })

                return r

            r = Meta(kq1, kq2, kq3, kq4)

            store(kq1, (r   if first is absent else   { first.kq2 : first, kq2 : r }))

            return r


        if __debug__:
            conjure_quadruple.__name__ = intern_arrange('conjure_%s', name)

        return conjure_quadruple


    @export
    @privileged
    def produce_triple_cache(
            name,
            Meta,

            cache  = absent,
            lookup = absent,
            store  = absent,
    ):
        if cache is absent:
            cache = {}

        if lookup is absent:
            lookup = cache.get

        if store is absent:
            store = cache.__setitem__


        def conjure_triple(kt1, kt2, kt3):
            first = lookup(kt1, absent)

            if first.__class__ is Map:
                second = first.get(kt2, absent)

                if second.__class__ is Map:
                    return (second.get(kt3)) or (second.setdefault(kt3, Meta(kt1, kt2, kt3)))

                if second.kt3 is kt3:
                    return second

                r = Meta(kt1, kt2, kt3)

                first[kt2] = (r   if second is absent else   { second.kt3 : second, kt3 : r })

                return r

            if first.kt2 is kt2:
                if first.kt3 is kt3:
                    return first

                r = Meta(kt1, kt2, kt3)

                store(kt1, { first.kt2 : { first.kt3 : first, kt3 : r } })

                return r

            r = Meta(kt1, kt2, kt3)

            store(kt1, (r   if first is absent else   { first.kt2 : first, kt2 : r }))

            return r


        if __debug__:
            conjure_triple.__name__ = intern_arrange('conjure_%s', name)

        return conjure_triple
