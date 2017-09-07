#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1')
def gem():
    show = 0


    require_gem('Sapphire.Core')
    require_gem('Sapphire.BinaryExpression')
    require_gem('Sapphire.BookcaseExpression')
    require_gem('Sapphire.ExpressionMany')
    require_gem('Sapphire.JoinedToken')
    require_gem('Sapphire.Match')
    require_gem('Sapphire.OtherExpression')
    require_gem('Sapphire.Parse1Atom')
    require_gem('Sapphire.Parse1Call')
    require_gem('Sapphire.Parse1Complex')
    require_gem('Sapphire.Parse1Expression')
    require_gem('Sapphire.Parse1ExpressionStatement')
    require_gem('Sapphire.Parse1From')
    require_gem('Sapphire.Parse1Function')
    require_gem('Sapphire.Parse1Import')
    require_gem('Sapphire.Parse1Simple')
    require_gem('Sapphire.PostfixExpression')
    require_gem('Sapphire.Statement')
    require_gem('Sapphire.Tokenize1Atom')
    require_gem('Sapphire.Tokenize1Header')
    require_gem('Sapphire.Tokenize1Name')
    require_gem('Sapphire.Tokenize1Operator')
    require_gem('Sapphire.UnaryExpression')


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

            return DecoratorHeader(operator_at_sign, CallExpression(identifier, operator), newline)

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
                             'class'  : parse1_statement_class_header,
                             'def'    : parse1_statement_function_header,
                             'for'    : parse1_statement_for,
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
