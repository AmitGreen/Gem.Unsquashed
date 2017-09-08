#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.JoinedToken')
def gem():
    construct_KeywordAndOperatorBase = KeywordAndOperatorBase.__init__


    class BaseDualOperator(KeywordAndOperatorBase):
        __slots__ = ((
            'first',         #   Operator+
            'second',        #   Operator+
        ))


        def __init__(t, first, second):
            construct_KeywordAndOperatorBase(t, first.s + second.s)

            t.first  = first
            t.second = second


        def __repr__(t):
            return arrange('<%s %r %r>',
                           t.__class__.__name__, t.first, t.second)


        def display_full_token(t):
            display_name = t.display_name
            first_s      = t.first.s
            second_s     = t.second.s

            return arrange('<%s <%s> <%s>>',
                           display_name,
                           portray_string(first_s)    if '\n' in first_s  else   first_s,
                           portray_string(second_s)   if '\n' in second_s else   second_s)


        def display_token(t):
            display_name = t.display_name

            if display_name == t.s:
                return display_name

            first_s  = t.first .s
            second_s = t.second.s

            return arrange('<%s <%s> <%s>>',
                           display_name,
                           portray_string(first_s)    if '\n' in first_s  else   first_s,
                           portray_string(second_s)   if '\n' in second_s else   second_s)


        def write(t, w):
            w(t.first.s + t.second.s)


    @share
    class Arguments_0(BaseDualOperator):
        __slots__                             = (())
        display_name                          = '(0)'
        is__arguments_0__or__left_parenthesis = true
        is_arguments_0                        = true
        is_postfix_operator                   = true


    @share
    class Colon_RightSquareBracket(BaseDualOperator):
        __slots__      = (())
        #   [
        display_name   = ':['


    @share
    class Comma_RightParenthesis(BaseDualOperator):
        __slots__      = (())
        #   (
        display_name   = ',)'


    @share
    class Comma_RightSquareBracket(BaseDualOperator):
        __slots__      = (())
        #   [
        display_name   = ',]'


    @share
    class EmptyList(BaseDualOperator):
        __slots__                          = (())
        display_name                       = '[,]'
        is__atom__or__right_close_operator = true
        is_atom                            = true


    @share
    class EmptyMap(BaseDualOperator):
        __slots__                          = (())
        display_name                       = '{:}'
        is__atom__or__right_close_operator = true
        is_atom                            = true


    @share
    class EmptyTuple(BaseDualOperator):
        __slots__                          = (())
        display_name                       = '{,}'
        is__atom__or__right_close_operator = true
        is_atom                            = true


    @share
    class RightParenthesis_Colon_Newline(BaseDualOperator):
        __slots__                                  = (())
        display_name                               = r'):\n'
        is__any__right_parenthesis__colon__newline = true
        is__right_parenthesis__colon__newline      = true


    class BaseTripleOperator(KeywordAndOperatorBase):
        __slots__ = ((
            'first',         #   Operator+
            'second',        #   Operator+
            'third',         #   Operator+
        ))


        def __init__(t, first, second, third):
            construct_KeywordAndOperatorBase(t, first.s + second.s + third.s)

            t.first  = first
            t.second = second
            t.third  = third


        def __repr__(t):
            return arrange('<%s %r %r %r>',
                           t.__class__.__name__, t.first, t.second, t.third)


        def display_full_token(t):
            display_name = t.display_name
            first_s      = t.first.s
            second_s     = t.second.s

            return arrange('<%s <%s> <%s>>',
                           display_name,
                           portray_string(first_s)    if '\n' in first_s  else   first_s,
                           portray_string(second_s)   if '\n' in second_s else   second_s)


        def display_token(t):
            display_name = t.display_name

            if display_name == t.s:
                return display_name

            first_s  = t.first .s
            second_s = t.second.s
            third_s  = t.third .s

            return arrange('<%s <%s> <%s> <%s>>',
                           display_name,
                           portray_string(first_s)    if '\n' in first_s  else   first_s,
                           portray_string(second_s)   if '\n' in second_s else   second_s,
                           portray_string(third_s)    if '\n' in third_s  else   third_s)


        def write(t, w):
            w(t.first.s + t.second.s + t.third.s)


    @share
    class Comma_RightParenthesis_Colon_Newline(BaseTripleOperator):
        __slots__                                  = (())
        display_name                               = r',):\n'
        is__any__right_parenthesis__colon__newline = true


    @share
    class ParameterColon_0_Newline(BaseTripleOperator):
        display_name                 = r'():\n'
        is_any_parameter_colon_0     = true
        is_parameter_colon_0_newline = true
