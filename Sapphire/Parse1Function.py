#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1Function')
def gem():
    @share
    def parse1_statement_function_header(m1):
        if m1.end('newline') is not -1:
            raise_unknown_line(1)

        keyword_function = KeywordFunction(m1.group())

        s = qs()

        #
        #<name>
        #
        m2 = name_match(s, m1.end())

        if m2 is none:
            raise_unknown_line(2)

        name   = m2.group()
        m2_end = m2.end()
        #</name>

        #
        #<parenthesis>
        #
        m3 = define_parenthesis_match1(s, m2_end)

        if m3 is none:
            raise_unknown_line(3)

        comment_newline = m3.group('ow_comment_newline')
        #</parenthesis>

        if comment_newline is not none:
            return FunctionHeader(
                       keyword_function,
                       name,
                       ParameterColon_0(s[m2_end : m3.start('ow_comment_newline')]),
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
