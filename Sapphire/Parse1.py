#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1')
def gem():
    show = 7


    require_gem('Sapphire.Core')
    require_gem('Sapphire.Expression')
    require_gem('Sapphire.Match')
    require_gem('Sapphire.Parse1Atom')
    require_gem('Sapphire.Parse1Call')
    require_gem('Sapphire.Parse1Complex')
    require_gem('Sapphire.Parse1Expression')
    require_gem('Sapphire.Parse1ExpressionStatement')
    require_gem('Sapphire.Parse1From')
    require_gem('Sapphire.Parse1Function')
    require_gem('Sapphire.Parse1Import')
    require_gem('Sapphire.Parse1Simple')
    require_gem('Sapphire.Statement')
    require_gem('Sapphire.Tokenize1Atom')
    require_gem('Sapphire.Tokenize1Name')
    require_gem('Sapphire.Tokenize1Operator')


    def parse1_statement_class(m1):
        if m1.end('newline') is not -1:
            raise_unknown_line(1)

        keyword_class = KeywordClass(m1.group())
        s             = qs()

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
        #<choice: left-parenthesis [right-parenthesis colon newline] | newline>
        #
        m3 = class_parenthesis_match1(s, m2_end)

        if m3 is none:
            raise_unknown_line(3)

        newline_2 = m3.group('ow_comment_newline_2')

        if newline_2 is not none:
            return ClassHeader(
                       keyword_class,
                       name,
                       conjure_colon(s[m2_end : m3.start('ow_comment_newline_2')]),
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

        operator_left_parenthesis = conjure_left_parenthesis(m3.group())
        #</choice>

        #
        #<parameter_1>
        #
        m4 = name_match(s, m3.end())

        if m4 is none:
            raise_unknown_line(4)

        parameter_1 = m4.group()
        m2_end      = m4.end()
        #</parameter_1>

        #
        #<right-parenthesis-colon-newline>
        #
        m5 = right_parenthesis__colon__match(s, m4.end())

        if m5 is none:
            raise_unknown_line(5)
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


    def parse1_statement_decorator_header(m):
        if m.end('newline') is not -1:
            raise_unknown_line(1)

        operator_at_sign = OperatorAtSign(m.group())
        s                = qs()

        j = m.end()

        wi(j)
        wj(j)

        identifier = tokenize_name()
        newline    = qn()

        if newline is not none:
            return DecoratorHeader(operator_at_sign, identifier, newline)

        operator = tokenize_operator()

        if operator.is_arguments_0:
            newline = qn()

            if newline is none:
                raise_unknown_line(2)

            return DecoratorHeader(operator_at_sign, ExpressionCall(identifier, operator), newline)

        if not operator.is_left_parenthesis:
            raise_unknown_line(3)

        call = parse1_call_expression__left__operator(identifier, operator)

        newline = qn()

        if newline is none:
            raise_unknown_line(4)

        return DecoratorHeader(operator_at_sign, call, newline)


    find_parse1_colon_line = {
                                 'except' : parse1_statement_except_colon,
                                 'try'    : parse1_statement_try_colon,
                             }.__getitem__


    lookup_parse1_line = {
                             '@'      : parse1_statement_decorator_header,
                             'class'  : parse1_statement_class,
                             'def'    : parse1_statement_function_header,
                             'from'   : parse1_statement_from,
                             'if'     : parse1_statement_if,
                             'import' : parse1_statement_import,
                             'pass'   : parse1_statement_pass,
                             'return' : parse1_statement_return,
                             'with'   : parse1_statement_with,
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
                        raise_unknown_line(1)

                    token = m.group('token')

                    if token is not none:
                        parse1_line = lookup_parse1_line(token)

                        if parse1_line is not none:
                            append(parse1_line(m))

                            assert qd() is 0
                            continue

                        if m.start('newline') is not -1:
                            append(
                                StatementExpression(
                                    m.group('indented'),
                                    conjure_identifier(token),
                                    conjure_token_newline(s[m.end('token'):]),
                                ),
                            )

                            assert qd() is 0
                            continue

                        wi(m.end('token'))
                        wj(m.end())

                        append(
                            parse1_statement_expression__symbol(
                                m.group('indented'),
                                conjure_identifier(token),
                            ),
                        )

                        assert qd() is 0
                        continue

                    keyword = m.group('keyword')

                    if keyword is not none:
                        append(find_parse1_colon_line(keyword)(m))

                        assert qd() is 0
                        continue

                    [comment, newline] = m.group('comment', 'newline')

                    if newline is none:
                        assert comment is none

                        raise_unknown_line(2)

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
                        line('%s', v.display_token())

                with create_StringOutput() as f:
                    w = f.write

                    for v in many:
                        v.write(w)

                if data != f.result:
                    with create_DelayedFileOutput('oops.txt') as oops:
                        oops.write(f.result)

                    raise_runtime_error('mismatch on %r: output saved in %r', path, 'oops.txt')

                line('Passed: identical dump from parse tree.  Total: %d line%s',
                     length(many), (''   if length(many) is 0 else   's'))
