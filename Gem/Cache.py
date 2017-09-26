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
    def produce_dual_cache_functions(
            name,
            Meta,

            cache = absent,
    ):
        if cache is absent:
            cache = {}

        lookup = cache.get
        store  = cache.__setitem__


        def conjure_dual(a, b):
            first = lookup(a, absent)

            if first.__class__ is Map:
                return (first.get(b)) or (first.setdefault(b, Meta(a, b)))

            if first.b is b:
                return first

            r = Meta(a, b)

            store(a, (r   if first is absent else   { first.b : first, b : r }))

            return r


        if __debug__:
            conjure_dual.__name__ = intern_arrange('conjure_%s', name)

        return conjure_dual


    @export
    @privileged
    def produce_triple_cache_functions(
            name,
            Meta,

            cache = absent,
    ):
        if cache is absent:
            cache = {}

        lookup = cache.get
        store  = cache.__setitem__


        def conjure_triple(a, b, c):
            first = lookup(a, absent)

            if first.__class__ is Map:
                second = first.get(b, absent)

                if second.__class__ is Map:
                    return (second.get(c)) or (second.setdefault(c, Meta(a, b, c)))

                if second.c is c:
                    return second

                r = Meta(a, b, c)

                first[b] = (r   if second is absent else   { second.c : second, c : r })

                return r

            if first.b is b:
                if first.c is c:
                    return first

                r = Meta(a, b, c)

                store(a, { first.b : { first.c : first, c : r } })

                return r

            r = Meta(a, b, c)

            store(a, (r   if first is absent else   { first.b : first, b : r }))

            return r


        if __debug__:
            conjure_triple.__name__ = intern_arrange('conjure_%s', name)

        return conjure_triple
