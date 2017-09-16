#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Whitespace')
def gem():
    @export
    class TokenIndented(Token):
        display_name      = 'indented'
        is_token_indented = true


    class TokenWhitespace(Token):
        display_name = 'whitespace'


        def __init__(t, s):
            assert '\n' not in s

            t.s = s


    class TokenWhitespaceLine(Token):
        display_name = 'whitespace-line'


        def __init__(t, s):
            assert '\n' in s

            t.s = s


    conjure_whitespace      = produce_conjure_by_name('whitespace',      TokenWhitespace)
    conjure_whitespace_line = produce_conjure_by_name('whitespace_line', TokenWhitespaceLine)


    share(
        'conjure_whitespace',       conjure_whitespace,
        'conjure_whitespace_line',  conjure_whitespace_line,
    )
