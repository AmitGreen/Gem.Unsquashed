#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Tree')
def gem():
    @share
    class SapphireTrunk(Object):
        __slots__ = (())


        is__right_parenthesis__colon__newline = false
        is_right_brace                        = false
        is_right_parenthesis                  = false
        is_right_square_bracket               = false
        is_statement                          = false


        def display_full_token(t):
            return t.display_token()
