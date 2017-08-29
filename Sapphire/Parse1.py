#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1')
def gem():
    require_gem('Sapphire.Core')
    require_gem('Sapphire.Match')
    require_gem('Sapphire.Parse1From')
    require_gem('Sapphire.Parse1Import')
    require_gem('Sapphire.Parse1Expression')
    require_gem('Sapphire.Parse7')
    require_gem('Sapphire.Parse7Expression')
    require_gem('Sapphire.Statement')


    show = 1


    def parse1__newline(j):
        #
        #<ow-comment-newline>
        #
        m1 = ow_comment_newline_match(qs(), j)

        if m1 is none:
            return parse_incomplete(1)

        return conjure_token_newline(m1.group())
        #</ow-comment-newline>


    def parse1_arguments__left_parenthesis(left_parenthesis, j):
        s = qs()

        if show is 7:
            line('parse1_arguments__left_parenthesis: left_parenthesis: %s; s: %s',
                 left_parenthesis, portray_raw_string(s[j:]))

        #
        #<single_quote>
        #
        m1 = single_quote_match(s, j)

        if m1 is none:
            return parse_incomplete(1)

        argument_1 = SingleQuote(m1.group())
        #</single_quote>

        #
        #<right-parenthesis>
        #
        m2 = statement_argument1_operator_match1(s, m1.end())

        if m2 is none:
            return parse_incomplete(2)

        right_parenthesis = OperatorRightParenthesis(m2.group())
        #</right-parenthesis>

        wj(m2.end())

        return Arguments_1(left_parenthesis, argument_1, right_parenthesis)


    def parse1_expression_call(j, left, left_parenthesis):
        arguments = parse1_arguments__left_parenthesis(left_parenthesis, j)

        return ExpressionCall(left, arguments)


    def parse1_statement_class(m1):
        if m1.end('newline') is not -1:
            return create_UnknownLine(1)

        keyword_class = KeywordClass(m1.group())
        s             = qs()

        #
        #<name>
        #
        m2 = name_match(s, m1.end())

        if m2 is none:
            return create_UnknownLine(2)

        name   = m2.group()
        m2_end = m2.end()
        #</name>

        #
        #<choice: left-parenthesis [right-parenthesis colon newline] | newline>
        #
        m3 = class_parenthesis_match1(s, m2_end)

        if m3 is none:
            return create_UnknownLine(3)

        newline_2 = m3.group('ow_comment_newline_2')

        if newline_2 is not none:
            return ClassHeader(
                       keyword_class,
                       name,
                       OperatorColon(s[m2_end : m3.start('ow_comment_newline_2')]),
                       conjure_token_newline(newline_2),
                   )

        newline_1 = m3.group('ow_comment_newline_1')

        if newline_1 is not none:
            return ClassHeader(
                       keyword_class,
                       name,
                       ParameterColon_0(s[m2_end : m3.start('ow_comment_newline_1')]),
                       conjure_token_newline(newline_1),
                   )

        operator_left_parenthesis = OperatorLeftParenthesis(m3.group())
        #</choice>

        #
        #<parameter_1>
        #
        m4 = name_match(s, m3.end())

        if m4 is none:
            return create_UnknownLine(4)

        parameter_1 = m4.group()
        m2_end      = m4.end()
        #</parameter_1>

        #
        #<right-parenthesis-colon-newline>
        #
        m5 = right_parenthesis__colon__match(s, m4.end())

        if m5 is none:
            return create_UnknownLine(5)
        #</right-parenthesis-colon-newline>

        return ClassHeader(
                   keyword_class,
                   name,
                   ParameterColon_1(
                       operator_left_parenthesis,
                       conjure_identifier(parameter_1),
                       OperatorRightParenthesisColon(m5.group('ow__right_parenthesis__colon')),
                   ),
                   conjure_token_newline(m5.group('ow_comment_newline')),
               )


    def parse1_statement_decorator_header(m1):
        if m1.end('newline') is not -1:
            return create_UnknownLine(1)

        operator_at_sign = OperatorAtSign(m1.group())
        s                = qs()

        #
        #<name>
        #
        m2 = name_match(s, m1.end())

        if m2 is none:
            return create_UnknownLine(2)

        identifier = conjure_identifier(m2.group())
        m2_end     = m2.end()
        #</name>

        #
        #<postfix>
        #
        m3 = decorator_postfix_match1(s, m2_end)

        if m3 is none:
            return create_UnknownLine(3)

        left_parenthesis__end = m3.end('left_parenthesis__ow')
        #</postfix>

        if left_parenthesis__end is -1:
            return DecoratorHeader(operator_at_sign, identifier, conjure_token_newline(m3.group()))

        left_parenthesis  = OperatorLeftParenthesis(s[m2_end : left_parenthesis__end])
        right_parenthesis = m3.group('right_parenthesis')

        if right_parenthesis is not none:
            right_parenthesis = OperatorRightParenthesis(right_parenthesis)

            if m3.end('comment_newline') is not -1:
                return DecoratorHeader(
                           operator_at_sign,
                           ExpressionCall(identifier, Arguments_0(left_parenthesis, right_parenthesis)),
                           conjure_token_newline(s[m3.end('right_parenthesis'):]),
                       )

            return create_UnknownLine(4)

        expression = parse1_expression_call(m3.end(), identifier, left_parenthesis)

        if expression is none:
            return create_UnknownLine_0()

        #
        #<newline>
        #
        newline = parse1__newline(qj())

        if newline is none:
            return create_UnknownLine(5)
        #</newline>

        return DecoratorHeader(operator_at_sign, expression, newline)


    def parse1_statement_define_header(m1):
        if m1.end('newline') is not -1:
            return create_UnknownLine(1)

        keyword_define = KeywordDefine(m1.group())
        s              = qs()

        #
        #<name>
        #
        m2 = name_match(s, m1.end())

        if m2 is none:
            return create_UnknownLine(2)

        name   = m2.group()
        m2_end = m2.end()
        #</name>

        #
        #<parenthesis>
        #
        m3 = define_parenthesis_match1(s, m2_end)

        if m3 is none:
            return create_UnknownLine(3)

        comment_newline = m3.group('ow_comment_newline')
        #</parenthesis>

        if comment_newline is not none:
            return DefineHeader(
                       keyword_define,
                       name,
                       ParameterColon_0(s[m2_end : m3.start('ow_comment_newline')]),
                       conjure_token_newline(comment_newline),
                   )

        #
        #<parameter_1>
        #
        m4 = name_match(s, m3.end())

        if m4 is none:
            return create_UnknownLine(4)

        parameter_1 = m4.group()
        #</parameter_1>

        #
        #<right-parenthesis-colon-newline>
        #
        m5 = right_parenthesis__colon__match(s, m4.end())

        if m5 is none:
            return create_UnknownLine(5)
        #</right-parenthesis-colon-newline>

        return DefineHeader(
                   keyword_define,
                   name,
                   ParameterColon_1(
                       OperatorLeftParenthesis(m3.group()),
                       conjure_identifier(parameter_1),
                       OperatorRightParenthesisColon(m5.group('ow__right_parenthesis__colon')),
                   ),
                   conjure_token_newline(m5.group('ow_comment_newline')),
               )


    def parse1_statement_pass(m1):
        if m1.end('newline') is -1:
            return create_UnknownLine(1)

        return StatementPass(m1.group())


    def parse1_statement_return(m1):
        if m1.end('newline') is not -1:
            return StatementReturn(m1.group())

        keyword_return = KeywordReturn(m1.group())
        s              = qs()

        #
        #<atom1>
        #
        m2 = atom_match1(s, m1.end())

        if m2 is none:
            return create_UnknownLine(1)

        s2     = m2.group()
        atom   = find_atom_type(s2[0])(s2)
        m2_end = m2.end()
        #</atom1>

        #
        #<postfix>
        #
        m3 = statement_postfix_match1(s, m2_end)

        if m3 is none:
            return create_UnknownLine(2)

        left_parenthesis__end = m3.end('left_parenthesis__ow')
        #</postfix>

        if left_parenthesis__end is -1:
            return StatementReturnExpression(keyword_return, atom, conjure_token_newline(m3.group()))

        left_parenthesis  = OperatorLeftParenthesis(s[m2_end : left_parenthesis__end])
        right_parenthesis = m3.group('right_parenthesis')

        if right_parenthesis is not none:
            right_parenthesis = OperatorRightParenthesis(right_parenthesis)

            if m3.end('comment_newline') is not -1:
                return StatementReturnExpression(
                           keyword_return,
                           ExpressionCall(atom, Arguments_0(left_parenthesis, right_parenthesis)),
                           conjure_token_newline(s[m3.end('right_parenthesis'):]),
                       )

            return create_UnknownLine(3)

        expression = parse1_expression_call(s, m3.end(), atom, left_parenthesis)

        if expression is none:
            return create_UnknownLine_0()

        #
        #<newline>
        #
        newline = parse1__newline(qj())

        if newline is none:
            return create_UnknownLine(4)
        #</newline>

        return StatementReturnExpression(keyword_return, expression, newline)


    lookup_parse1_line = {
                             'class'  : parse1_statement_class,
                             'def'    : parse1_statement_define_header,
                             'from'   : parse1_statement_from,
                             'import' : parse1_statement_import,
                             'pass'   : parse1_statement_pass,
                             'return' : parse1_statement_return,
                             '@'      : parse1_statement_decorator_header,
                         }.get


    @share
    def parse1_python_from_path(path):
        data = read_text_from_path(path)

        parse_context = z_initialize(data)

        append        = parse_context.append
        many          = parse_context.many
        iterate_lines = parse_context.iterate_lines

        for LOOP in parse_context:
            with parse_context:
                for s in iterate_lines:
                    m = line_match1(s)

                    if m is none:
                        append(create_UnknownLine(1))
                        continue

                    token = m.group('token')

                    if token is not none:
                        parse1_line = lookup_parse1_line(token)

                        if parse1_line is not none:
                            append(parse1_line(m))
                            continue

                        if m.start('newline') is not -1:
                            append(
                                StatementExpression(
                                    m.group('indented'),
                                    conjure_identifier(token),
                                    conjure_token_newline(s[m.end('token'):]),
                                ),
                            )

                            continue

                        append(
                            parse1_statement_expression__symbol(
                                m.group('indented'),
                                conjure_identifier(token),
                                m.end('token'),
                            ),
                        )

                        continue

                    [comment, newline] = m.group('comment', 'newline')

                    if newline is none:
                        assert comment is none

                        append(create_UnknownLine(4))
                        continue

                    if comment is not none:
                        indented = m.group('indented')

                        if indented is '':
                            append(Comment(comment, newline))
                            continue

                        append(IndentedComment(indented, comment, newline))
                        continue

                    append(EmptyLine(m.group()))

                if show:
                    for v in many:
                        line('%r', v)

                with create_StringOutput() as f:
                    w = f.write

                    for v in many:
                        v.write(w)

                if data != f.result:
                    with create_DelayedFileOutput('oops.txt') as oops:
                        oops.write(f.result)

                    raise_runtime_error('mismatch on %r: output saved in %r', path, 'oops.txt')
