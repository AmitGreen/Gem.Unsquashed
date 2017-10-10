#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.Cache')
def gem():
    require_gem('Gem.Absent')


    @export
    @privileged
    def produce_cache_functions(
            name,
            Meta                    = absent,
            cache                   = absent,
            produce_cache           = false,
            produce_conjure_by_name = false,
            produce_find            = false,
            produce_insert_interned = false,
            produce_lookup          = false,
    ):
        result = []
        append = result.append

        if cache is absent:
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
    def produce_conjure_by_name(name, Meta, cache = absent):
        [conjure_by_name] = produce_cache_functions(name, Meta, cache = cache, produce_conjure_by_name = true)

        return conjure_by_name


    @export
    @privileged
    def produce_conjure_dual(
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
    def produce_conjure_dual__21(
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
    def produce_conjure_quadruple__4123(
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


        def conjure_quadruple__4123(k1, k2, k3, k4):
            first = lookup(k4, absent)

            if first.__class__ is Map:
                second = first.get(k1, absent)

                if second.__class__ is Map:
                    third = first.get(k2, absent)

                    if third.__class__ is Map:
                        return (
                                      third.get(k3)
                                   or third.setdefault(k3, Meta(k1, k2, k3, k4))
                               )

                    if third.k3 is k3:
                        return third

                    r = Meta(k1, k2, k3, k4)

                    second[k2] = (r   if third is absent else   { third.k3 : third, k3 : r })

                    return r

                if second.k2 is k2:
                    if second.k3 is k3:
                        return second

                    r = Meta(k1, k2, k3, k4)

                    first[k1] = { k2 : { second.k3 : second, k3 : r } }

                    return r

                r = Meta(k1, k2, k3, k4)

                first[k1] = (r   if second is absent else   { second.k2 : second, k2 : r })

                return r

            if first.k1 is k1:
                if first.k2 is k2:
                    if first.k3 is k3:
                        return first

                    r = Meta(k1, k2, k3, k4)

                    store(k4, { k1 : { k2 : { first.k3 : first, k3 : r } } })

                    return r

                r = Meta(k1, k2, k3, k4)

                store(k4, { k1 : { first.k2 : first, k2 : r } })

                return r

            r = Meta(k1, k2, k3, k4)

            store(k4, (r   if first is absent else   { first.k1 : first, k1 : r }))

            return r


        if __debug__:
            conjure_quadruple__4123.__name__ = intern_arrange('conjure_%s__4123', name)

        return conjure_quadruple__4123


    @export
    @privileged
    def produce_conjure_single(
            name,
            Meta,

            cache = absent,
    ):
        if cache is absent:
            cache = {}

        lookup  = cache.get
        provide = cache.setdefault


        def conjure_single(k1):
            r = lookup(k1)

            if r is not none:
                return r

            r = Meta(k1)

            return provide(r, r)


        if __debug__:
            conjure_single.__name__ = intern_arrange('conjure_%s', name)

        return conjure_single


    @export
    @privileged
    def produce_conjure_triple(
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


        def conjure_triple(k1, k2, k3):
            first = lookup(k1, absent)

            if first.__class__ is Map:
                second = first.get(k2, absent)

                if second.__class__ is Map:
                    return (second.get(k3)) or (second.setdefault(k3, Meta(k1, k2, k3)))

                if second.k3 is k3:
                    return second

                r = Meta(k1, k2, k3)

                first[k2] = (r   if second is absent else   { second.k3 : second, k3 : r })

                return r

            if first.k2 is k2:
                if first.k3 is k3:
                    return first

                r = Meta(k1, k2, k3)

                store(k1, { first.k2 : { first.k3 : first, k3 : r } })

                return r

            r = Meta(k1, k2, k3)

            store(k1, (r   if first is absent else   { first.k2 : first, k2 : r }))

            return r


        if __debug__:
            conjure_triple.__name__ = intern_arrange('conjure_%s', name)

        return conjure_triple


    @export
    @privileged
    def produce_conjure_triple__213(
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


        def conjure_triple__213(k1, k2, k3):
            first = lookup(k2, absent)

            if first.__class__ is Map:
                second = first.get(k1, absent)

                if second.__class__ is Map:
                    return (second.get(k3)) or (second.setdefault(k3, Meta(k1, k2, k3)))

                if second.k3 is k3:
                    return second

                r = Meta(k1, k2, k3)

                first[k1] = (r   if second is absent else   { second.k3 : second, k3 : r })

                return r

            if first.k1 is k1:
                if first.k3 is k3:
                    return first

                r = Meta(k1, k2, k3)

                store(k2, { first.k1 : { first.k3 : first, k3 : r } })

                return r

            r = Meta(k1, k2, k3)

            store(k2, (r   if first is absent else   { first.k1 : first, k1 : r }))

            return r


        if __debug__:
            conjure_triple__213.__name__ = intern_arrange('conjure_%s__213', name)

        return conjure_triple__213


    @export
    @privileged
    def produce_conjure_tuple(
            name,
            Meta,

            cache   = absent,
            provide = absent,
    ):
        if cache is absent:
            cache = {}

        if provide is absent:
            provide = cache.setdefault


        def conjure_tuple(many):
            r = Meta(many)

            return provide(r, r)


        if __debug__:
            conjure_tuple.__name__ = intern_arrange('conjure_%s', name)

        return conjure_tuple


    @export
    @privileged
    def produce_conjure_triple__312(
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


        def conjure_triple(k1, k2, k3):
            first = lookup(k3, absent)

            if first.__class__ is Map:
                second = first.get(k1, absent)

                if second.__class__ is Map:
                    return (second.get(k2)) or (second.setdefault(k2, Meta(k1, k2, k3)))

                if second.k2 is k2:
                    return second

                r = Meta(k1, k2, k3)

                first[k1] = (r   if second is absent else   { second.k2 : second, k2 : r })

                return r

            if first.k1 is k1:
                if first.k2 is k2:
                    return first

                r = Meta(k1, k2, k3)

                store(k3, { first.k1 : { first.k2 : first, k2 : r } })

                return r

            r = Meta(k1, k2, k3)

            store(k3, (r   if first is absent else   { first.k1 : first, k1 : r }))

            return r


        if __debug__:
            conjure_triple.__name__ = intern_arrange('conjure_%s', name)

        return conjure_triple
