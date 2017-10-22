#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.LiquidMap')
def gem():
    map__get     = Map.get
    map__provide = Map.setdefault
    map__store   = Map.__setitem__


    def scrub__cache(t):
        append_remove = 0
        value         = t.__getitem__
        store         = t.__setitem__

        for k in t.keys():
            v       = value(k)
            v_scrub = v.scrub

            if v_scrub is 0:
                if reference_count(v) is not 3:
                    continue

                if append_remove is 0:
                    remove_many   = [k]
                    append_remove = remove_many.append
                    continue

                append_remove(k)
                continue

            v = v_scrub()

            if v is 0:
                if append_remove is 0:
                    remove_many   = [k]
                    append_remove = remove_many.append
                    continue

                append_remove(k)
                continue

            store(k, v)

        if append_remove is 0:
            return

        if length(remove_many) == length(t):
            t.clear()
            return

        zap = t.__delitem__

        for v in remove_many:
            zap(v)


    @share
    class LiquidMap(Map):
        __slots__ = ((
            'name',                             #   String+
        ))


        def __init__(t, name):
            t.name = name


        count_nested = count_nested__map


        def items_sorted_by_key(t):
            value = t.__getitem__

            for k in sorted_list(t):
                yield (( k, value(k) ))


        lookup  = map__get
        provide = map__provide
        scrub   = scrub__cache
        store   = map__store


    @share
    class LiquidMap_WithNub(Map):
        __slots__ = ((
            'name',                             #   String+
            'nub',                              #   Method
        ))


        def __init__(t, name, nub):
            t.name = name
            t.nub  = nub


        count_nested = count_nested__map


        def items_sorted_by_key(t):
            value = t.__getitem__

            for k in sorted_list(t, key = t.nub):
                yield (( k, value(k) ))


        lookup  = map__get
        provide = map__provide
        scrub   = scrub__cache
        store   = map__store


        if is_python_2:
            keys   = Map.iterkeys
            values = Map.itervalues
