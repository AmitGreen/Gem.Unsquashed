#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1Function')
def gem():
    @share
    def parse1_statement_function_header(m):
        if m.end('newline') is not -1:
            raise_unknown_line(1)

        keyword_function = KeywordFunction(m.group())

        j = m.end()

        wi(j)
        wj(j)

        #
        #<name>
        #
        name = tokenize_name()

        if qn() is not none:
            raise_unknown_line(1)
        #</name>

        operator_1 = tokenize_function_header_parenthesis_atom()

        if operator_1.is_parameter_colon_0:
            newline = qn()

            if newline is none:
                raise_unknown_line(2)

            return FunctionHeader(keyword_function, name, operator_1, newline)

        if not operator_1.is_left_parenthesis:
            raise_unknown_line(3)

        s = qs()

        #
        #<parameter_1>
        #
        m4 = name_match(s, qj())

        if m4 is none:
            raise_unknown_line(4)

        parameter_1 = m4.group()
        #</parameter_1>

        #
        #<right-parenthesis-colon-newline>
        #
        m5 = right_parenthesis__colon__match(s, m4.end())

        if m5 is none:
            raise_unknown_line(5)
        #</right-parenthesis-colon-newline>

        assert qd() is 1

        wd0()

        return FunctionHeader(
                   keyword_function,
                   name,
                   ParameterColon_1(
                       operator_1,
                       conjure_identifier(parameter_1),
                       OperatorRightParenthesisColon(m5.group('ow__right_parenthesis__colon')),
                   ),
                   conjure_token_newline(m5.group('ow_comment_newline')),
               )
