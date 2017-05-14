#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.ParseExpression')
def gem():
    require_gem('Sapphire.Core')


    show = false


    def parse7_arguments__atom__left_parenthesis(s, m0, atom):
        if show:
            line('parse7_arguments__atom__left_parenthesis: %s; %s; calling parse7_arguments__left_parenthesis',
                 atom, portray_raw_string(s[m0.end():]))

        [arguments, index] = parse7_arguments__left_parenthesis(s, m0)

        if arguments is none:
            return tuple_of_3_nones

        call = ExpressionCall(atom, arguments)
        m    = argument7_postfix_match(s, index)

        if m is none:
            line('parse7_arguments__atom__left_parenthesis: incomplete #1A: %r %r', call, s[m0.end():])
            return tuple_of_3_nones

        operator = m.group('operator')

        #   (
        if operator is ')':
            return (( call, OperatorRightParenthesis(m.group('operator__ow')), m.end() ))

        if operator is ',':
            return (( call, OperatorComma(m.group('operator__ow')), m.end() ))

        line('parse7_arguments__atom__left_parenthesis: incomplete #2: %r %r', call, operator)
        return tuple_of_3_nones


    def parse7_arguments__atom__left_square_bracket(s, m, array):
        left_square_bracket = OperatorLeftSquareBracket(m.group('operator__ow'))
        m                   = index_1_match(s, m.end())

        if m is none:
            line('parse7_arguments__atom__left_square_bracket: incomplete #3: %r %r', s[index:], left_square_bracket)
            return tuple_of_3_nones

        [name, number, operator] = m.group('name', 'number', 'operator')

        if name is not none:
            assert number is none

            index_1 = Symbol(name)
        else:
            assert number is not none

            index_1 = Number(number)

        if operator is ']':
            left = ExpressionIndex_1(array, left_square_bracket, index_1, OperatorRightSquareBracket(m.group('operator__ow')))
        else:
            line('parse7_arguments__atom__left_square_bracket: incomplete #4: %r %r', index_1, operator)
            return tuple_of_3_nones

        m = argument7_postfix_match(s, m.end())

        if m is none:
            line('parse7_arguments__atom__left_square_bracket: incomplete #5: %r %r', left, s[m.end():])
            return tuple_of_3_nones

        operator = m.group('operator')

        #   (
        if operator is ')':
            line('parse7_arguments__atom__left_square_bracket: incomplete #6: %r %r', left, operator)
            return tuple_of_3_nones

        if operator is ',':
            return (( left, OperatorComma(m.group('operator__ow')), m.end() ))

        line('parse7_arguments__atom__left_square_bracket: incomplete #7: %r %r', left, operator)
        return tuple_of_3_nones


    find__parse7_arguments__atom__operator = {
                                                '(' : parse7_arguments__atom__left_parenthesis,
                                                '[' : parse7_arguments__atom__left_square_bracket,
                                            }.__getitem__


    def parse7_arguments__left_parenthesis(s, m0):
        if show:
            line('parse7_arguments__left_parenthesis: %s', portray_raw_string(s[m0.end():]))
            line('m0: %s', m0)
            #assert 0,'stop#1'

        left_parenthesis_0 = OperatorLeftParenthesis(m0.group('operator__ow'))
        m                  = argument7_1_match(s, m0.end())

        if m is none:
            line('parse7_arguments__left_parenthesis: incomplete #8: %s', portray_string(s[m0.end():]))
            #assert 0, 'oops'
            return tuple_of_2_nones

        [name, number, single_quote, operator] = m.group('name', 'number', 'single_quote', 'operator')

        if name is not none:
            assert number is single_quote is none

            argument_0 = Symbol(name)
        elif number is not none:
            assert single_quote is none

            argument_0 = Number(number)
        else:
            assert single_quote is not none

            argument_0 = SingleQuote(single_quote)

        #   (
        if operator is ')':
            return ((
                       Arguments_1(left_parenthesis_0, argument_0, OperatorRightParenthesis(m.group('operator__ow'))),
                       m.end(),
                   ))

        return parse7_arguments__left_parenthesis__argument__operator(s, m, left_parenthesis_0, argument_0, operator)


    def parse7_arguments__left_parenthesis__argument_0(s, m0, argument_0):
        if show:
            line('parse7_arguments__left_parenthesis__argument_0: %r, %s', argument_0, portray_raw_string(s[m0.end():]))

        left_parenthesis_0 = OperatorLeftParenthesis(m0.group('operator__ow'))
        m                  = argument7_1A_match(s, m0.end())

        if m is none:
            line('parse7_arguments__left_parenthesis__argument_0: incomplete #9: %s', portray_string(s[m0.end():]))
            return tuple_of_2_nones

        operator = m.group('operator')

        #   (
        if operator is ')':
            return ((
                       Arguments_1(left_parenthesis_0, argument_0, OperatorRightParenthesis(m.group('operator__ow'))),
                       m.end(),
                   ))

        return parse7_arguments__left_parenthesis__argument__operator(s, m, left_parenthesis_0, argument_0, operator)


    def parse7_arguments__left_parenthesis__argument__operator(s, m0, left_parenthesis_0, argument_0, operator):
        if operator is ',':
            operator_0 = OperatorComma(m0.group('operator__ow'))
            index_0    = m0.end()
        else:
            if show:
                line('parse7_arguments__left_parenthesis__argument__operator: %s %s; %s %r; calling %s',
                     left_parenthesis_0, argument_0, portray_raw_string(s[m0.end():]), operator,
                     find__parse7_arguments__atom__operator(operator).__name__)

            [argument_0, operator_0, index_0] = find__parse7_arguments__atom__operator(operator)(s, m0, argument_0)

            if argument_0 is none:
                return tuple_of_2_nones

            if operator_0.is_right_parenthesis:
                return ((
                           Arguments_1(left_parenthesis_0, argument_0, operator_0),
                           index_0,
                       ))

            if not operator_0.is_comma:
                line('parse7_arguments__left_parenthesis__argument__operator: incomplete #10: %r %r', argument_0, operator_0)
                return tuple_of_2_nones

        m = argument7_2_match(s, index_0)

        if m is none:
            line('parse7_arguments__left_parenthesis__argument__operator: incomplete #11: %r %r %r', argument_0, operator_0, s[index_0:])
            return tuple_of_2_nones

        [name, number, single_quote, operator] = m.group('name', 'number', 'single_quote', 'operator')

        if name is not none:
            assert number is single_quote is none

            argument_1 = Symbol(name)
        elif number is not none:
            assert single_quote is none

            argument_1 = Number(number)
        else:
            assert single_quote is not none

            argument_1 = SingleQuote(single_quote)

        #   (
        if operator is ')':
            return ((
                       Arguments_2(left_parenthesis_0, argument_0, operator_0, argument_1, OperatorRightParenthesis(operator)),
                       m.end(),
                   ))

        if operator is ',':
            comma_1 = OperatorComma(operator)
            index_1 = m.end()
        else:
            [argument_1, operator_1, index_1] = find__parse7_arguments__atom__operator(operator)(s, m, argument_1)

            if argument_1 is none:
                return tuple_of_2_nones

            if operator_1.is_right_parenthesis:
                return ((
                           Arguments_2(left_parenthesis_0, argument_0, operator_0, argument_1, operator_1),
                           index_1,
                       ))

            line('parse7_arguments__left_parenthesis__argument__operator: incomplete #12: %r; %r; %r; %r; %r; %r',
                 left_parenthesis_0, argument_0, operator_0, argument_1, operator_1, s[index:])

            return tuple_of_2_nones

        line('parse7_arguments__left_parenthesis__argument__operator: incomplete #13: %r, %r', argument_1, operator)
        return tuple_of_2_nones


    @share
    def parse7_statement_expression__symbol(m0, s, name):
        m = statement_expression_match(s, m0.end())

        if m is none:
            return create_UnknownLine(parse7_statement_expression__symbol, 1)

        [
                dot, right, operator, name_0, number_0, single_quote_0, right_parenthesis,
                #ow_comment_newline,
        ] = m.group('dot', 'right', 'operator', 'name', 'number', 'single_quote', 'right_parenthesis')

        assert operator is '('

        if right_parenthesis is not none:
            left_parenthesis  = OperatorLeftParenthesis(m.group('operator__ow'))
            right_parenthesis = OperatorRightParenthesis(right_parenthesis)

            if name_0 is not none:
                assert number_0 is single_quote_0 is none

                arguments = Arguments_1(left_parenthesis, Symbol(name_0), right_parenthesis)
            elif number_0 is not none:
                assert single_quote_0 is none

                arguments = Arguments_1(left_parenthesis, Number(number_0), right_parenthesis)
            elif single_quote_0 is not none:
                arguments = Arguments_1(left_parenthesis, SingleQuote(single_quote_0), right_parenthesis)
            else:
                arguments = Arguments_0(left_parenthesis, right_parenthesis)

            if arguments is none:
                return create_UnknownLine(parse7_statement_expression__symbol, 2)

            ow_comment_newline = m.group('ow_comment_newline')
            index              = m.end()
        else:
            if name_0 is not none:
                assert number_0 is single_quote_0 is none

                [arguments, index] = parse7_arguments__left_parenthesis__argument_0(
                                         s, m, Symbol(name_0),
                                     )
            elif number_0 is not none:
                assert single_quote_0 is none

                [arguments, index] = parse7_arguments__left_parenthesis__argument_0(
                                         s, m, Number(number_0),
                                     )

            elif single_quote_0 is not none:
                [arguments, index] = parse7_arguments__left_parenthesis__argument_0(
                                         s, m, SingleQuote(single_quote_0),
                                     )
            else:
                return create_UnknownLine(parse7_statement_expression__symbol, 3)

                assert 0, 'oops#16'
                [arguments, index] = parse7_arguments__left_parenthesis(s, m)

            if arguments is none:
                return create_UnknownLine(parse7_statement_expression__symbol, 4)

            m = statement_postfix_match(s, index)

            if m is none:
                return create_UnknownLine(parse7_statement_expression__symbol, 5)

            ow_comment_newline = m.group('ow_comment_newline')


        indented = m0.group('indented')

        #line('indented: %r; ow_comment_newline: %r', indented, ow_comment_newline)

        if dot is none:
            return StatementCall(indented, Symbol(name), arguments, TokenNewline(ow_comment_newline))

        return StatementMethodCall(indented, Symbol(name), dot, right, arguments, ow_comment_newline)
