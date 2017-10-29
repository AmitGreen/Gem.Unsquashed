#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.Method')
def gem():
    map__provide = Map.setdefault


    #
    #   .count_nested
    #
    @share
    def count_nested__map(t):
        total = 0

        for v in t.values():
            total += (v.count_nested()    if v.is_herd else   1)

        return total


    #
    #   .items_sorted_by_key
    #
    if is_python_2:
        @share
        def items_sorted_by_key__herd_many(t):
            keys  = t.keys()
            value = t.__getitem__

            saw = 0
            for k in keys:
                if type(k) is not saw:
                    if saw is 0:
                        saw = type(k)
                    else:
                        for k in keys:
                            line('keys: %r', keys)
                            line('MIXED: %r,%r', k, value(k))
                            #if value(k).is_herd:
                            #    line('a,v: %r,%r', value(k).a, value(k).v)
                            #    line('b,w: %r,%r', value(k).b, value(k).w)
                            #    line('c,x: %r,%r', value(k).c, value(k).x)
                            yield (( k, value (k) ))
                        return

            for k in sorted_list(keys, key = keys[0].nub):
                yield (( k, value(k) ))
    else:
        @share
        def items_sorted_by_key__herd_many(t):
            keys  = List(t.keys())
            value = t.__getitem__

            for k in sorted_list(keys, key = keys[0].nub):
                yield (( k, value(k) ))


    #
    #   def provision
    #
    @share
    def provision__herd_many(t, k, v):
        map__provide(t, k, v)
        return t

    #
    #   .return_self
    #
    @export
    def return_self(t):
        return t
