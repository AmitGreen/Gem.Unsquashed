#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Indentation')
def gem():
    class Indentation(SapphireToken):
        __slots__ = ((
            'total',                    #   Integer {> 0}
        ))


        is_indentation = true


        def __init__(t, s):
            t.s     = intern_string(s)
            t.total = length(s)


        def count_newlines(t):
            assert (t.ends_in_newline is t.line_marker is false) and (t.newlines is 0)
            assert '\n' not in t.s

            return 0


        def display_short_token(t):
            return arrange('{+%d}', t.total)


        def display_token(t):
            if t.total is 0:
                return '{+0}'

            return arrange('{+%d %s}', t.total, portray_string(t.s))


        def transform(t, mutate):
            return t


    def conjure_indentation(s):
        r = lookup_indentation(s)

        if r is not none:
            return r

        s = intern_string(s)

        return provide_indentation(s, Indentation(s))


    empty_indentation = conjure_indentation('')


    share(
        'conjure_indentation',  conjure_indentation,
        'empty_indentation',    empty_indentation,
    )
