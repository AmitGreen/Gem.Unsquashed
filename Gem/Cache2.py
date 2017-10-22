#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.Cache2')
def gem():
    require_gem('Gem.Absent')
    require_gem('Gem.Horde')


    map__get     = Map.get
    map__provide = Map.setdefault


    class LiquidMap(Map):
        __slots__ = (())


        def iterate_items_sorted_by_key(t):
            value = t.__getitem__

            for k in sorted_list(t):
                yield (( k, value(k) ))


        lookup  = map__get
        provide = map__provide


    class LiquidMap_WithNub(Map):
        __slots__ = ((
            'nub',                              #   Method
        ))


        def __init__(t, nub):
            t.nub = nub


        def iterate_items_sorted_by_key(t):
            value = t.__getitem__

            for k in sorted_list(t, key = t.nub):
                yield (( k, value(k) ))


        lookup  = map__get
        provide = map__provide


    cache_names   = LiquidMap()                 #   Map String+ of Map
    lookup_cache  = cache_names.get
    provide_cache = cache_names.setdefault


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
            nub    = none,
            lookup = absent,
            store  = absent,
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

            if not first.is_horde:
                r = Meta(k1, k2)

                store(k1, (r   if first is absent else   create_horde_23(first.k2, k2, first, r )))

                return r

            r = first.glimpse(k2)

            if r is not none:
                assert r.k2 is k2

                return r

            r = Meta(k1, k2)

            first__2 = first.insert(k2, r)

            if first is not first__2:
                store(k1, first_2)

            return r


        if __debug__:
            return rename_function(intern_arrange('conjure_%s', name), conjure_unique_dual)

        return conjure_unique_dual



    @export
    def create_cache(name, nub = none):
        assert name not in cache_names

        return provide_cache(
                   intern_string(name),
                   (LiquidMap()   if nub is none else   LiquidMap_WithNub(nub)),
               )


    if __debug__:
        def dump_single_cache(name, cache):
            line('===  %s  ===', name)

            for [k, v] in cache.iterate_items_sorted_by_key():
                if not v.is_horde:
                    line('%s: %s',
                         (
                            portray_string(k)  if k.__class__ is String  else
                            k                  if k.__class__ is Integer else
                            k.display_token()
                         ),
                         v.display_token())

                    continue

                line('%s:',
                     (
                        portray_string(k)  if k.__class__ is String  else
                        k                  if k.__class__ is Integer else
                        k.display_token()
                     ))

                for [k2, w] in v.iterate_items_sorted_by_key():
                    if not w.is_horde:
                        line('  %s: %s',
                             (
                                portray_string(k2)  if k2.__class__ is String  else
                                k2                  if k2.__class__ is Integer else
                                k2.display_token()
                             ),
                             w.display_token())

                        continue

                    line('  %s:',
                         (
                            portray_string(k2)  if k2.__class__ is String  else
                            k2                  if k2.__class__ is Integer else
                            k2.display_token()
                         ))

                    for [k3, x] in w.iterate_items_sorted_by_key():
                        if not x.is_horde:
                            line('    %s: %s', k3.display_token(), x.display_token())
                            continue

                        line('    %s:', k3.display_token())

                        for [k4, y] in x.iterate_items_sorted_by_key():
                            line('      %s:', k4.display_token())
                            line('        %s', y.display_token())

        @export
        def dump_caches(use_name = none):
            if use_name is none:
                line('Total caches: %d', length(cache_names))

                for [name, cache] in iterate_items_sorted_by_key(cache_names):
                    line('%s: %d', name, length(cache))

                return

            dump_single_cache(use_name, cache_names[use_name])
    else:
        @export
        def dump_caches(use_name = none):
            pass
