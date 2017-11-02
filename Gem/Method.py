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
    #   disperse
    #
    if __debug__:
        @share
        def disperse__herd_many(t, k, v):
            v__2 = map__provide(t, k, v)
            assert v is v__2
            return t
    else:
        @share
        def disperse__herd_many(t, k, v):
            map__provide(t, k, v)
            return t


    #
    #   .items_sorted_by_key
    #
    if is_python_2:
        @share
        def items_sorted_by_key__herd_many(t):
            keys  = t.keys()
            value = t.__getitem__

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
    #   .return_self
    #
    @export
    def return_self(t):
        return t
