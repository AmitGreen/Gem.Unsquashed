#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1')
def gem():
    show = 0


    require_gem('Sapphire.Core')

    require_gem('Sapphire.BinaryExpression')
    require_gem('Sapphire.BookcaseExpression')
    require_gem('Sapphire.DualToken')
    require_gem('Sapphire.ExpressionMany')
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
    require_gem('Sapphire.TripleToken')
    require_gem('Sapphire.UnaryExpression')


    find_parse1_colon_line = {
                                 'else'    : parse1_statement_else_colon,
                                 'except'  : parse1_statement_except_colon,
                                 'finally' : parse1_statement_finally_colon,
                                 'try'     : parse1_statement_try_colon,
                             }.__getitem__


    lookup_parse1_line = {
                             '@'      : parse1_statement_decorator_header,
                             'assert' : parse1_statement_assert,
                             'class'  : parse1_statement_class_header,
                             'def'    : parse1_statement_function_header,
                             'del'    : parse1_statement_delete,
                             'elif'   : parse1_statement_else_if,
                             'except' : parse1_statement_except,
                             'for'    : parse1_statement_for,
                             'from'   : parse1_statement_from,
                             'if'     : parse1_statement_if,
                             'import' : parse1_statement_import,
                             'pass'   : parse1_statement_pass,
                             'raise'  : parse1_statement_raise,
                             'return' : parse1_statement_return,
                             'yield'  : parse1_statement_yield,
                             'while'  : parse1_statement_while,
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
                    assert qd() is 0

                    m = line_match(s)

                    if m is none:
                        raise_unknown_line()

                    atom_s = m.group('atom')

                    if atom_s is not none:
                        parse1_line = lookup_parse1_line(atom_s)

                        if parse1_line is not none:
                            append(parse1_line(m))

                            assert qd() is 0
                            continue

                        if m.start('comment_newline') is not -1:
                            append(
                                StatementExpression(
                                    m.group('indented'),
                                    conjure_identifier(atom_s),
                                    conjure_token_newline(s[m.end('atom'):]),
                                ),
                            )

                            assert qd() is 0
                            continue

                        wi(m.end('atom'))
                        wj(m.end())

                        append(
                            parse1_statement_expression__atom(
                                m.group('indented'),
                                conjure_identifier(atom_s),
                            ),
                        )

                        assert qd() is 0
                        continue

                    keyword = m.group('keyword')

                    if keyword is not none:
                        append(find_parse1_colon_line(keyword)(m))

                        assert qd() is 0
                        continue

                    if m.start('something') is not -1:
                        j = m.end('indented')

                        wi(j)
                        wj(j)

                        append(
                            parse1_statement_expression__atom(
                                m.group('indented'),
                                analyze_atom(m)
                            ),
                        )

                        assert qd() is 0
                        continue

                    [comment, newline] = m.group('comment', 'newline')

                    if newline is none:
                        assert comment is none

                        raise_unknown_line()

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

                line('Passed#1: identical dump from parse tree.  Total: %d line%s',
                     length(many), (''   if length(many) is 0 else   's'))

                if 7:
                    #conjure_colon__line_marker('\n\n:\n')
                    dump_newline_meta_cache()
