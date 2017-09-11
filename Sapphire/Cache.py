#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Cache')
def gem():
    cache_many        = []
    append_cache_many = cache_many.append


    if __debug__:
        @share
        def append_cache(name, cache):
            append_cache_many( ((name, cache)) )
    else:
        @share
        def append_cache(name, cache):
            pass


    if __debug__:
        def dump_cache(name, cache):
            line('===  %s  ===', name)

            for [k, v] in iterate_items_sorted_by_key(cache):
                line('%s:', (portray_string(k)  if k.__class__ is String else   k.display_token()))

                if v.__class__ is Map:
                    for [k2, w] in iterate_items_sorted_by_key(v):
                        line('  %s:', k2.display_token())

                        if w.__class__ is Map:
                            for [k3, x] in iterate_items_sorted_by_key(w):
                                line('    %s:', k3.display_token())

                                if x.__class__ is Map:
                                    for [k4, y] in iterate_items_sorted_by_key(x):
                                        line('      %s:', k4.display_token())
                                        line('        %s', y.display_token())

                                    continue

                                line('      %s', x.display_token())

                            continue

                        line('    %s', w.display_token())

                    continue

                line('  %s', v.display_token())


        @export
        def dump_caches(use_name = none):
            if use_name is none:
                for [name, cache] in cache_many:
                    line('%s: %d', name, length(cache))

                return

            for [name, cache] in cache_many:
                if use_name == name:
                    dump_cache(name, cache)
                    break
            else:
                raise_runtime_error('did not find cache named %r', portray_string(use_name))
    else:
        @export
        def dump_caches(use_name = none):
            pass
