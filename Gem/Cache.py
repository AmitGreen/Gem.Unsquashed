#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.Cache')
def gem():
    require_gem('Gem.Absent')


    @export
    def produce_cache_functions(
            name,
            meta                    = absent,
            produce_cache           = false,
            produce_conjure_by_name = false,
            produce_find            = false,
            produce_insert          = false,
            produce_lookup          = false,
    ):
        result = []
        append = result.append

        cache = {}

        if (produce_conjure_by_name) or (produce_insert):
            provide = cache.setdefault

        if (produce_conjure_by_name) or (produce_lookup):
            lookup = cache.get

        if (produce_find) or (produce_insert):
            find = cache.__getitem__

        if produce_cache:
            append(cache)

        if produce_conjure_by_name:
            assert meta is not absent


            def conjure_by_name(k):
                r = lookup(k)
                
                if r is not none:
                    return r
                    
                interned_k = intern_string(k)
                
                return provide(interned_k, meta(interned_k))


            append(conjure_by_name)

        if produce_find:
            append(find)

        if produce_insert:
            contains = cache.__contains__


            if __debug__:
                def insert(interned_k, v):
                    if contains(interned_k):
                        raise_runtime_error('cache %s: attempt to insert key %r with value %r (already has value %r)',
                                            name, interned_k, v, find(interned_k))

                    return provide(interned_k, v)


                append(insert)
            else:
                append(provide)

        if produce_lookup:
            append(lookup)

        return Tuple(result)
