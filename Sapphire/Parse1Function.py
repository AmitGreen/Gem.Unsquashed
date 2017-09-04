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

        s = qs()

        #
        #<parenthesis>
        #
        m3 = define_parenthesis_match1(s, qj())

        if m3 is none:
            raise_unknown_line(3)

        comment_newline = m3.group('ow_comment_newline')
        #</parenthesis>

        if comment_newline is not none:
            return FunctionHeader(
                       keyword_function,
                       name,
                       ParameterColon_0(s[qj() : m3.start('ow_comment_newline')]),
                       conjure_token_newline(comment_newline),
                   )

        #
        #<parameter_1>
        #
        m4 = name_match(s, m3.end())

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

        return FunctionHeader(
                   keyword_function,
                   name,
                   ParameterColon_1(
                       conjure_left_parenthesis(m3.group()),
                       conjure_identifier(parameter_1),
                       OperatorRightParenthesisColon(m5.group('ow__right_parenthesis__colon')),
                   ),
                   conjure_token_newline(m5.group('ow_comment_newline')),
               )
