#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Whitespace')
def gem():
    empty_line_cache   = {}
    lookup_empty_line  = empty_line_cache.get
    provide_empty_line = empty_line_cache.setdefault


    class EmptyLine(String):
        __slots__       = (())
        display_name    = 'empty-line'
        ends_in_newline = true
        line_marker     = false
        newlines        = 1


        def __repr__(t):
            return arrange('<EmptyLine %s>', portray_string(t))


        def count_newlines(t):
            assert (t.ends_in_newline is true) and (t.newlines is 1) and (t.line_marker is false)
            assert (t.count('\n') is 1) and (t[-1] == '\n')

            return 1


        def display_token(t):
            if t is empty_line:
                return '<empty-line>'

            return arrange('<empty-line %s>', portray_string(t))


        def write(t, w):
            w(t)


    @export
    class TokenIndented(SapphireToken):
        display_name      = 'indented'
        is_token_indented = true


    class TokenWhitespace(SapphireToken):
        display_name = 'whitespace'


        def __init__(t, s):
            assert '\n' not in s

            t.s = s


    def conjure_empty_line(s):
        r = lookup_empty_line(s)

        if r is not none:
            return r

        r = EmptyLine(s)

        return provide_empty_line(r, r)


    empty_line = conjure_empty_line('\n')


    [
            conjure_whitespace, conjure_whitespace__ends_in_newline,
    ] = produce_conjure_action_word('whitespace', TokenWhitespace, produce_ends_in_newline = true)


    if __debug__:
        @share
        def dump_empty_line_cache():
            dump_cache('empty_line', empty_line_cache)


    share(
        'conjure_empty_line',                   conjure_empty_line,
        'conjure_whitespace',                   conjure_whitespace,
        'conjure_whitespace__ends_in_newline',  conjure_whitespace__ends_in_newline,
    )
