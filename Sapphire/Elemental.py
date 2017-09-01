#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Elemental')
def gem():
    require_gem('Sapphire.Core')


    @share
    class KeywordAndOperatorBase(Token):
        is_arguments_0          = false
        is_dot                  = false
        is_left_parenthesis     = false
        is_left_square_bracket  = false
        is_right_square_bracket = false


        def __repr__(t):
            return arrange('<%s>', t.s)


        def display_token(t):
            if t.s == t.display_name:
                return arrange('<%s>', t.display_name)

            return arrange('<%s %s>', t.display_name, portray_string(t.s))


    @export
    class KeywordAs(KeywordAndOperatorBase):
        __slots__        = (())
        display_name     = 'as'
        is_token_newline = false
        keyword          = 'as'


    @export
    class KeywordClass(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'class'
        keyword      = 'class'


    @export
    class KeywordDefine(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'define'
        keyword      = 'def'


    @export
    class KeywordFrom(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'from'
        keyword      = 'from'


    @export
    class KeywordImport(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'import'
        keyword      = 'import'


    @export
    class KeywordReturn(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = 'return'
        keyword      = 'return'


    @share
    class Number(Token):
        __slots__    = (())
        display_name = 'number'


        def display_token(t):
            return t.s



    @export
    class OperatorAtSign(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = '@'
        keyword      = '@'


    @export
    class OperatorColon(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = ':'
        keyword      = ':'


    class OperatorComma(KeywordAndOperatorBase):
        __slots__        = (())
        display_name     = ','
        is_comma         = true
        is_token_newline = false
        keyword          = ','


    class OperatorDot(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = '.'
        is_dot       = true
        keyword      = '.'


    @export
    class OperatorEqualSign(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = '='
        keyword      = '='


    class OperatorLeftParenthesis(KeywordAndOperatorBase):
        __slots__           = (())
        display_name        = '('       #   )
        is_left_parenthesis = true
        keyword             = '('       #   )


    @export
    class OperatorLeftSquareBracket(KeywordAndOperatorBase):
        __slots__              = (())
        is_left_square_bracket = true
        display_name           = '['              #   ]
        keyword                = '['              #   ]


    class OperatorRightParenthesis(KeywordAndOperatorBase):
        __slots__            = (())
        #  (
        display_name         = ')'
        is_right_parenthesis = true
        #  (
        keyword              = ')'


    @export
    class OperatorRightParenthesisColon(KeywordAndOperatorBase):
        __slots__                    = (())
        #  ([
        display_name                 = '):'
        is__right_parenthesis__colon = true
        #  ([
        keyword                      = '):'


    @export
    class OperatorRightSquareBracket(KeywordAndOperatorBase):
        __slots__               = (())
        is_right_square_bracket = true
        #   [[
        display_name            = ']'
        keyword                 = ']'


    @share
    class SingleQuote(Token):
        __slots__    = (())
        display_name = "'"


        def display_token(t):
            return arrange('<%s>', t.s)


    [conjure_comma] = produce_cache_functions(
                          'comma',
                          OperatorComma,

                          produce_conjure_by_name = true,
                      )

    [conjure_dot] = produce_cache_functions(
                        'dot',
                        OperatorDot,

                        produce_conjure_by_name = true,
                    )

    [conjure_left_parenthesis] = produce_cache_functions(
                                     'left_parenthesis',
                                     OperatorLeftParenthesis,

                                     produce_conjure_by_name = true,
                                 )

    [conjure_left_square_bracket] = produce_cache_functions(
                                        'left_square_brakcet',
                                        OperatorLeftSquareBracket,

                                        produce_conjure_by_name = true,
                                    )

    [conjure_right_parenthesis] = produce_cache_functions(
                                      'right_parenthesis',
                                      OperatorRightParenthesis,

                                      produce_conjure_by_name = true,
                                  )

    [conjure_right_square_bracket] = produce_cache_functions(
                                         'right_square_brakcet',
                                         OperatorRightSquareBracket,

                                         produce_conjure_by_name = true,
                                     )


    find_atom_type = {
                         "'" : SingleQuote,
                         '.' : Number,

                         '0' : Number, '1' : Number, '2' : Number, '3' : Number, '4' : Number,
                         '5' : Number, '6' : Number, '7' : Number, '8' : Number, '9' : Number,

                         'A' : conjure_identifier, 'B' : conjure_identifier, 'C' : conjure_identifier,
                         'D' : conjure_identifier, 'E' : conjure_identifier, 'F' : conjure_identifier,
                         'G' : conjure_identifier, 'H' : conjure_identifier, 'I' : conjure_identifier,
                         'J' : conjure_identifier, 'K' : conjure_identifier, 'L' : conjure_identifier,
                         'M' : conjure_identifier, 'N' : conjure_identifier, 'O' : conjure_identifier,
                         'P' : conjure_identifier, 'Q' : conjure_identifier, 'R' : conjure_identifier,
                         'S' : conjure_identifier, 'T' : conjure_identifier, 'U' : conjure_identifier,
                         'V' : conjure_identifier, 'W' : conjure_identifier, 'X' : conjure_identifier,
                         'Y' : conjure_identifier, 'Z' : conjure_identifier, '_' : conjure_identifier,

                         'a' : conjure_identifier, 'b' : conjure_identifier, 'c' : conjure_identifier,
                         'd' : conjure_identifier, 'e' : conjure_identifier, 'f' : conjure_identifier,
                         'g' : conjure_identifier, 'h' : conjure_identifier, 'i' : conjure_identifier,
                         'J' : conjure_identifier, 'k' : conjure_identifier, 'l' : conjure_identifier,
                         'm' : conjure_identifier, 'n' : conjure_identifier, 'o' : conjure_identifier,
                         'p' : conjure_identifier, 'q' : conjure_identifier, 'r' : conjure_identifier,
                         's' : conjure_identifier, 't' : conjure_identifier, 'u' : conjure_identifier,
                         'v' : conjure_identifier, 'w' : conjure_identifier, 'x' : conjure_identifier,
                         'y' : conjure_identifier, 'z' : conjure_identifier,
                     }.__getitem__


    find_operator_conjure_function = {
                                         '(' : conjure_left_parenthesis,
                                         ')' : conjure_right_parenthesis,
                                         ',' : conjure_comma,
                                         '.' : conjure_dot,
                                         '[' : conjure_left_square_bracket,
                                         ']' : conjure_right_square_bracket,
                                     }.__getitem__


    share(
        'conjure_comma',                    conjure_comma,
        'conjure_dot',                      conjure_dot,
        'conjure_left_parenthesis',         conjure_left_parenthesis,
        'conjure_right_parenthesis',        conjure_right_parenthesis,
        'find_atom_type',                   find_atom_type,
        'find_operator_conjure_function',   find_operator_conjure_function,
    )
