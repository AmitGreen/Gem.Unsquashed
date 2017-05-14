#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Tremolite.Name')
def gem():
    class TremoliteMatch(Object):
        __slots__ = ((
            'name',                     #   String
            'pattern',                  #   TremoliteBase+
            'debug',                    #   Boolean

            'code',                     #   None | String | Tuple of (Integer | Long)
            'groups',                   #   None | Tuple of (None| String)
            'flags',                    #   None | Integer
        ))


        def __init__(t, name, pattern, debug):
            t.name    = name
            t.pattern = pattern
            t.debug   = debug

            t.flags = t.groups = t.code = none


        def __repr__(t):
            return arrange('<%s %s %r%s>',
                           t.__class__.__name__, t.name, t.pattern, ('; debug'    if t.debug else    ''))


        def parse_ascii_regular_expression(t):
            assert t.code is t.groups is t.flags is none

            [t.code, t.groups, t.flags] = parse_ascii_regular_expression(t.pattern.regular_expression)


    [
            match_cache, match_insert,
    ] = produce_cache_functions('Tremolite.match_cache', TremoliteMatch, produce_cache = true, produce_insert = true)


    @export
    def FULL_MATCH(name, pattern, debug = false):
        assert (type(name) is String) and (length(name) > 0)

        if type(pattern) is String:
            pattern = INVISIBLE_EXACT(pattern)

        name = intern_string(name)

        return match_insert(name, TremoliteMatch(name, pattern + END_OF_PATTERN, debug))


    @export
    def MATCH(name, pattern, debug = false):
        assert (type(name) is String) and (length(name) > 0)

        if type(pattern) is String:
            pattern = INVISIBLE_EXACT(pattern)

        name = intern_string(name)

        return match_insert(name, TremoliteMatch(name, pattern, debug))


    share(
        'match_cache',  match_cache,
    )
