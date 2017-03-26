#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Tremolite.Match')
def gem():
    require_gem('Tremolite.Build')


    class TremoliteMatch(Object):
        __slots__ = ((
            'name',                     #   String
            'pattern',                  #   TremoliteBase+
        ))

        
        def __init__(t, name, pattern):
            t.name    = name
            t.pattern = pattern


        def __repr__(t):
            return arrange('<TremoliteMatch %s %r>', t.name, t.pattern)


    [cache, insert] = produce_cache_and_insert_function('tremolite.match')


    @export
    def MATCH(name, pattern):
        assert (type(name) is String) and (length(name) > 0)

        if type(pattern) is String:
            pattern = INVISIBLE_EXACT(pattern)

        name = intern_string(name)

        return insert(name, TremoliteMatch(name, pattern))


    @export
    def dump_match_cache(): 
        line('dump_match_cache:')

        for [k, v] in iterate_items_sorted_by_key(cache):
            line('%s:  %s', k, v)
