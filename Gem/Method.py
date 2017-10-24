#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.Method')
def gem():
    @export
    def return_self(t):
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
