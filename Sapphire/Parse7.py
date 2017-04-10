#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse7')
def gem():
    require_gem('Sapphire.Expression')
    require_gem('Sapphire.Match')
    require_gem('Sapphire.Parse7Expression')
    require_gem('Sapphire.Statement')
    require_gem('Sapphire.Token')


    show = false


    def parse7_expression(m):
        [
                name, left_parenthesis, single_quote, right_parenthesis,
        ] = m.group('name', 'left_parenthesis', 'single_quote', 'OLD__right_parenthesis')

        expression = Symbol(name)

        if left_parenthesis is none:
            return expression

        if single_quote is none:
            return ExpressionCall(
                       expression,
                       Arguments_0(
                           OperatorLeftParenthesis(left_parenthesis),
                           OperatorRightParenthesis(right_parenthesis),
                       ),
                   )

        return ExpressionCall(
                   expression,
                   Arguments_1(
                       OperatorLeftParenthesis(left_parenthesis),
                       SingleQuote(single_quote),
                       OperatorRightParenthesis(right_parenthesis),
                   ),
               )


    def parse7_statement_class(m0, s):
        if show:
            line(portray_raw_string(s[m0.end():]))

        m = class_match(s, m0.end())

        if m is none:
            return UnknownLine(s)

        [
            name1, left_parenthesis, name2, right_parenthesis__colon, newline,
        ] = m.group('name1', 'left_parenthesis', 'name2', 'ow__right_parenthesis__colon__ow', 'newline')

        parameters = ParameterColon_1(
                         OperatorLeftParenthesis(left_parenthesis),
                         Symbol(name2),
                         OperatorRightParenthesisColon(right_parenthesis__colon),
                     )

        return ClassHeader(KeywordClass(m0.group('indented') + m0.group('keyword__ow')), name1, parameters, newline)


    def parse7_statement_decorator_header(m0, s):
        m = expression_match(s, m0.end())

        if m is none:
            return UnknownLine(s)

        return DecoratorHeader(
                   OperatorAtSign(m0.group('indented') + m0.group('keyword__ow')),
                   parse7_expression(m),
                   m.group('ow_comment_newline'),
               )


    def parse7_statement_define_header(m0, s):
        m = define7_match(s, m0.end())

        if m is none:
            return UnknownLine(s)

        [
            name1, left_parenthesis, name2, right_parenthesis__colon, comment_newline,
        ] = m.group('name1', 'left_parenthesis', 'name2', 'ow__right_parenthesis__colon__ow', 'comment_newline')

        if name2 is none:
            parameters = ParameterColon_0(left_parenthesis + right_parenthesis__colon)
        else:
            parameters = ParameterColon_1(
                             OperatorLeftParenthesis(left_parenthesis),
                             Symbol(name2),
                             OperatorRightParenthesisColon(right_parenthesis__colon),
                         )

        return DefineHeader(
                   KeywordDefine(m0.group('indented') + m0.group('keyword__ow')), name1, parameters, comment_newline,
               )


    def parse7_statement_from(m0, s):
        m = from_1_match(s, m0.end())

        if m is none:
            return UnknownLine(s)

        [
                name1, dot, name2, w_import_w, name3, w_as_w, name4, comma
        ] = m.group('name1', 'dot', 'name2', 'w_import_w', 'name3', 'w_as_w', 'name4', 'comma')

        if dot is none:
            module = name1
        else:
            module = ExpressionDot(Symbol(name1), OperatorDot(dot), name2)

        as_fragment = AsFragment(name3, KeywordAs(w_as_w), name4)

        if comma is none:
            return StatementFromImport(
                       KeywordFrom(m0.group('indented') + m0.group('keyword__ow')),
                       Symbol(module),
                       KeywordImport(w_import_w),
                       as_fragment,
                       m.group('ow_comment_newline'),
                   )

        m2 = from_2_match(s, m.end())

        if m2 is none:
            return UnknownLine(s)

        [
                name1, w_as_w, name2, comma_2
        ] = m2.group('name1', 'w_as_w', 'name2', 'comma')

        as_fragment_2 = AsFragment(name1, KeywordAs(w_as_w), name2)

        if comma_2 is none:
            return StatementFromImport(
                       KeywordFrom(m0.group('indented') + m0.group('keyword__ow')),
                       module,
                       KeywordImport(w_import_w),
                       ExpressionComma(as_fragment, OperatorComma(comma), as_fragment_2),
                       m2.group('ow_comment_newline'),
                   )

        raise_runtime_error('parse7_statement_from: incomplete')


    def parse7_statement_import(m0, s):
        m = import_match(s, m0.end())

        if m is none:
            return UnknownLine(s)

        return StatementImport(
                   KeywordImport(m0.group('indented') + m0.group('keyword__ow')),
                   Symbol(m.group('name1')),
                   m.group('ow_comment_newline'),
               )


    def parse7_statement_return(m0, s):
        m = expression_match(s, m0.end())

        if m is none:
            return UnknownLine(s)

        return StatementReturnExpression(
                   KeywordReturn(m0.group('indented') + m0.group('keyword__ow')),
                   parse7_expression(m),
                   m.group('ow_comment_newline'),
               )


    find_parse7_line = {
                          'class'  : parse7_statement_class,
                          'def'    : parse7_statement_define_header,
                          'from'   : parse7_statement_from,
                          'import' : parse7_statement_import,
                          'return' : parse7_statement_return,
                          '@'      : parse7_statement_decorator_header,
                      }.__getitem__


    @share
    def parse7_python_from_path(path):
        data   = read_text_from_path(path)
        many   = []
        append = many.append

        for s in data.splitlines(true):
            m = line7_match(s)

            if m is none:
                append(UnknownLine(s))
                continue

            [keyword, name] = m.group('keyword', 'name')

            if keyword is not none:
                assert name is none

                append(find_parse7_line(keyword)(m, s))
                continue

            if name:
                append(parse7_statement_expression__symbol(m, s, name))
                continue

            [indented, comment, newline_2] = m.group('indented', 'comment', 'newline_2')

            assert newline_2 is not none

            if comment is not none:
                if indented is '':
                    append(Comment(comment, newline_2))
                    continue

                append(IndentedComment(indented, comment, newline_2))
                continue

            append(EmptyLine(indented + newline_2))
            continue

        if show:
            for v in many:
                line('%r', v)

        with create_StringOutput() as f:
            w = f.write

            for v in many:
                v.write(w)

        if data != f.result:
            with FileOutput('oops.txt') as f:
                f.write(f.result)

            raise_runtime_error('mismatch on %r: output saved in %r', path, 'oops.txt')
