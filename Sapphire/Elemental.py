#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Elemental')
def gem():
    require_gem('Sapphire.Core')


    class KeywordAndOperatorBase(Token):
        def __repr__(t):
            return arrange('<%s>', t.s)


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
        __slots__ = (())


        def __repr__(t):
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


    @export
    class OperatorComma(KeywordAndOperatorBase):
        __slots__        = (())
        display_name     = ','
        is_comma         = true
        is_token_newline = false
        keyword          = ','


    @export
    class OperatorDot(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = '.'
        keyword      = '.'


    @export
    class OperatorEqualSign(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = '='
        keyword      = '='


    @export
    class OperatorLeftParenthesis(KeywordAndOperatorBase):
        __slots__           = (())
        display_name        = '('       #   )
        is_left_parenthesis = true
        keyword             = '('       #   )


    @export
    class OperatorLeftSquareBracket(KeywordAndOperatorBase):
        __slots__    = (())
        display_name = '['              #   ]
        keyword      = '['              #   ]


    @export
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
        __slots__    = (())
        #   [
        display_name = ']'
        #   [
        keyword      = ']'


    @share
    class SingleQuote(Token):
        __slots__ = (())


        def __repr__(t):
            return arrange('<%s>', t.s)


    @share
    class StatementReturn(Token):
        __slots__    = (())
        display_name = 'return'
        keyword      = 'return'


    @share
    class Symbol(Token):
        __slots__ = (())


        def __repr__(t):
            return arrange('<$%s>', t.s)


    [
            conjure_symbol, find_symbol, lookup_symbol,
    ] = produce_cache_functions(
            'Sapphire.symbol_cache', Symbol,

            produce_conjure = true,
            produce_find    = true,
            produce_lookup  = true,
        )


    find_atom_type = {
                         "'" : SingleQuote,
                         '.' : Number,

                         '0' : Number, '1' : Number, '2' : Number, '3' : Number, '4' : Number,
                         '5' : Number, '6' : Number, '7' : Number, '8' : Number, '9' : Number,

                         'A' : conjure_symbol, 'B' : conjure_symbol, 'C' : conjure_symbol, 'D' : conjure_symbol,
                         'E' : conjure_symbol, 'F' : conjure_symbol, 'G' : conjure_symbol, 'H' : conjure_symbol,
                         'I' : conjure_symbol, 'J' : conjure_symbol, 'K' : conjure_symbol, 'L' : conjure_symbol,
                         'M' : conjure_symbol, 'N' : conjure_symbol, 'O' : conjure_symbol, 'P' : conjure_symbol,
                         'Q' : conjure_symbol, 'R' : conjure_symbol, 'S' : conjure_symbol, 'T' : conjure_symbol,
                         'U' : conjure_symbol, 'V' : conjure_symbol, 'W' : conjure_symbol, 'X' : conjure_symbol,
                         'Y' : conjure_symbol, 'Z' : conjure_symbol,

                         '_' : conjure_symbol,

                         'a' : conjure_symbol, 'b' : conjure_symbol, 'c' : conjure_symbol, 'd' : conjure_symbol,
                         'e' : conjure_symbol, 'f' : conjure_symbol, 'g' : conjure_symbol, 'h' : conjure_symbol,
                         'i' : conjure_symbol, 'J' : conjure_symbol, 'k' : conjure_symbol, 'l' : conjure_symbol,
                         'm' : conjure_symbol, 'n' : conjure_symbol, 'o' : conjure_symbol, 'p' : conjure_symbol,
                         'q' : conjure_symbol, 'r' : conjure_symbol, 's' : conjure_symbol, 't' : conjure_symbol,
                         'u' : conjure_symbol, 'v' : conjure_symbol, 'w' : conjure_symbol, 'x' : conjure_symbol,
                         'y' : conjure_symbol, 'z' : conjure_symbol,
                     }.__getitem__


    export(
        'find_atom_type',   find_atom_type,
    )
