#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1')
def gem():
    show = 0


    require_gem('Sapphire.Core')

    require_gem('Sapphire.ActionWord')
    require_gem('Sapphire.Atom')
    require_gem('Sapphire.BinaryExpression')
    require_gem('Sapphire.BookcaseDualExpression')
    require_gem('Sapphire.BookcaseDualStatement')
    require_gem('Sapphire.BookcaseExpression')
    require_gem('Sapphire.BookcaseManyExpression')
    require_gem('Sapphire.BookcaseManyFrill')
    require_gem('Sapphire.BookcaseManyStatement')
    require_gem('Sapphire.BookcaseStatement')
    require_gem('Sapphire.BookcaseTriple')
    require_gem('Sapphire.CallStatement')
    require_gem('Sapphire.Comment')
    require_gem('Sapphire.ConditionStatement')
    require_gem('Sapphire.DualFrill')
    require_gem('Sapphire.DualToken')
    require_gem('Sapphire.HeaderStatement')
    require_gem('Sapphire.Indentation')
    require_gem('Sapphire.LineMarker')
    require_gem('Sapphire.ManyExpression')
    require_gem('Sapphire.ManyFrill')
    require_gem('Sapphire.Match')
    require_gem('Sapphire.MemberExpression')
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
    require_gem('Sapphire.QuadrupleFrill')
    require_gem('Sapphire.QuadrupleToken')
    require_gem('Sapphire.TernaryExpression')
    require_gem('Sapphire.TokenCache')
    require_gem('Sapphire.Tokenize1Atom')
    require_gem('Sapphire.Tokenize1Header')
    require_gem('Sapphire.Tokenize1Name')
    require_gem('Sapphire.Tokenize1Operator')
    require_gem('Sapphire.Tree')
    require_gem('Sapphire.TripleFrill')
    require_gem('Sapphire.TripleToken')
    require_gem('Sapphire.UnaryExpression')
    require_gem('Sapphire.UnaryStatement')
    require_gem('Sapphire.Whitespace')


    if __debug__:
        require_gem('Sapphire.Dump')


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
                                conjure_expression_statement(
                                    conjure_indentation(m.group('indented')),
                                    conjure_name(atom_s),
                                    conjure_line_marker(s[m.end('atom'):]),
                                ),
                            )

                            assert qd() is 0
                            continue

                        wi(m.end('atom'))
                        wj(m.end())

                        append(
                            parse1_statement_expression__atom(
                                m.group('indented'),
                                conjure_name(atom_s),
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

                    comment_end = m.end('comment')

                    if comment_end is not -1:
                        append(conjure_any_comment_line(m.end('indented'), comment_end))
                        continue

                    if m.end('newline') is -1:
                        raise_unknown_line()

                    append(conjure_empty_line(m.group()))

                #conjure_colon__line_marker('\n\n:\n')
                #dump_binary_expression_cache_many()
                #dump_bookcase_dual_expression_cache_many()
                #dump_bookcase_expression_cache_many()
                #dump_bookcase_many_expression_cache_many()
                #dump_bookcase_many_frill_cache()
                #dump_comment_line_cache()
                #dump_dual_frill_cache()
                #dump_empty_line_cache()
                #dump_indentation_cache()
                #dump_many_expression_cache_many()
                #dump_many_frill_cache()
                #dump_member_expression_cache()
                #dump_postfix_expression_cache()
                #dump_ternary_expression_cache_many()
                #dump_token_caches()
                #dump_tuple_of_expression_cache()
                #dump_unary_expression_cache_many()

        return ((data, parse_context.data_lines, many))
