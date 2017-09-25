#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Indentation')
def gem():
    indentation_cache = {}

    lookup_indentation  = indentation_cache.get
    provide_indentation = indentation_cache.setdefault


    class Indentation(SapphireToken):
        __slots__ = ((
            'total',                    #   Integer {> 0}
        ))


        display_name      = 'indented'
        is_token_indented = true


        def __init__(t, s):
            t.s     = intern_string(s)
            t.total = length(s)


        def count_newlines(t):
            assert (t.ends_in_newline is t.line_marker is false) and (t.newlines is 0)
            assert '\n' not in s

            return 0


    def conjure_indentation(s):
        r = lookup_indentation(s)

        if r is not none:
            return r

        s = intern_string(s)

        return provide_indentation(s, Indentation(s))


    empty_indentation = conjure_indentation('')


    if __debug__:
        @share
        def dump_indentation_cache():
            dump_cache('indentation-cache', indentation_cache)


    share(
        'conjure_indentation',  conjure_indentation,
        'empty_indentation',    empty_indentation,
    )
