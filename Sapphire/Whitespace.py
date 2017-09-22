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


    [
            conjure_whitespace, conjure_whitespace__ends_in_newline,
    ] = produce_conjure_action_word('whitespace', TokenWhitespace, produce_ends_in_newline = true)


    share(
        'conjure_whitespace',                   conjure_whitespace,
        'conjure_whitespace__ends_in_newline',  conjure_whitespace__ends_in_newline,
    )
