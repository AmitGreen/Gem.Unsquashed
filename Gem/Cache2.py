#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.Cache2')
def gem():
    require_gem('Gem.Absent')
    require_gem('Gem.Herd')
    require_gem('Gem.Horde')
    require_gem('Gem.LiquidMap')


    cache_names   = LiquidMap('cache_names')        #   Map String+ of Map
    lookup_cache  = cache_names.get
    provide_cache = cache_names.setdefault


    @export
    def create_cache(name, nub = none):
        assert name not in cache_names

        return provide_cache(
                   intern_string(name),
                   (LiquidMap(name)   if nub is none else   LiquidMap_WithNub(name, nub)),
               )


    @export
    def produce_conjure_by_name__V2(
            name, Meta,

            cache = absent,
    ):
        if cache is absent:
            cache = create_cache(name)

        lookup  = cache.get
        provide = cache.setdefault


        def conjure_by_name(k):
            r = lookup(k)

            if r is not none:
                return r

            interned_k = intern_string(k)

            return provide(interned_k, Meta(interned_k))


        if __debug__:
           return rename_function(intern_arrange('conjure_%s', name), conjure_by_name)


        return conjure_by_name


    @export
    def produce_conjure_unique_dual(
            name,
            Meta,

            cache  = absent,
            lookup = absent,
            store  = absent,
            nub    = none,
    ):
        if cache is absent:
            cache = create_cache(name, nub = nub)

        if lookup is absent:
            lookup = cache.get

        if store is absent:
            store = cache.__setitem__


        def conjure_unique_dual(k1, k2):
            first = lookup(k1, absent)

            if first.k2 is k2:
                return first

            if not first.is_herd:
                r = Meta(k1, k2)

                store(k1, (r   if first is absent else   create_herd_2(first.k2, k2, first, r)))

                return r

            return first.provision_dual(store, Meta, k1, k2)


        if __debug__:
            return rename_function(intern_arrange('conjure_%s', name), conjure_unique_dual)

        return conjure_unique_dual


    @export
    def produce_conjure_unique_dual__21(
            name,
            Meta,

            cache  = absent,
            lookup = absent,
            store  = absent,
            nub    = none,
    ):
        if cache is absent:
            cache = create_cache(name, nub = nub)

        if lookup is absent:
            lookup = cache.get

        if store is absent:
            store = cache.__setitem__


        def conjure_unique_dual__21(k1, k2):
            first = lookup(k2, absent)

            if first.k1 is k1:
                return first

            if not first.is_herd:
                r = Meta(k1, k2)

                store(k2, (r   if first is absent else   create_herd_2(first.k1, k1, first, r)))

                return r

            return first.provision_dual__21(store, Meta, k1, k2)


        if __debug__:
            return rename_function(intern_arrange('conjure_%s__21', name), conjure_unique_dual__21)

        return conjure_unique_dual__21


    @export
    def produce_conjure_unique_triple(
            name,
            Meta,

            cache  = absent,
            lookup = absent,
            store  = absent,
            nub    = none,
    ):
        if cache is absent:
            cache = create_cache(name, nub = nub)

        if lookup is absent:
            lookup = cache.get

        if store is absent:
            store = cache.__setitem__


        def conjure_unique_triple(k1, k2, k3):
            first = lookup(k1, absent)

            if first.k2 is k2:
                if first.k3 is k3:
                    return first

                r = Meta(k1, k2, k3)

                store(k1, create_horde_2(1, first.k3, k3, first, r))

                return r

            if not first.is_herd:
                r = Meta(k1, k2, k3)

                store(k1, (r   if first is absent else   create_herd_2(first.k2, k2, first, r)))

                return r

            return first.provision_triple(store, Meta, k1, k2, k3)


        if __debug__:
            return rename_function(intern_arrange('conjure_%s', name), conjure_unique_triple)

        return conjure_unique_triple


    @export
    def produce_conjure_unique_triple__312(
            name,
            Meta,

            cache  = absent,
            lookup = absent,
            store  = absent,
            nub    = none,
    ):
        if cache is absent:
            cache = create_cache(name, nub = nub)

        if lookup is absent:
            lookup = cache.get

        if store is absent:
            store = cache.__setitem__


        def conjure_unique_triple__312(k1, k2, k3):
            first = lookup(k3, absent)

            if first.k1 is k1:
                if first.k2 is k2:
                    return first

                r = Meta(k1, k2, k3)

                store(k3, create_horde_2(1, first.k2, k2, first, r))

                return r

            if not first.is_herd:
                r = Meta(k1, k2, k3)

                store(k3, (r   if first is absent else   create_herd_2(first.k1, k1, first, r)))

                return r

            return first.provision_triple__312(store, Meta, k1, k2, k3)


        if __debug__:
            return rename_function(intern_arrange('conjure_%s__312', name), conjure_unique_triple__312)

        return conjure_unique_triple__312


    share(
        'cache_names',      cache_names,
    )
