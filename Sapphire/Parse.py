#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse')
def gem():
    require_gem('Sapphire.Expression')
    require_gem('Sapphire.Match')
    require_gem('Sapphire.ParseExpression')
    require_gem('Sapphire.Statement')
    require_gem('Sapphire.Token')


    show = true


    def parse_expression(m):
        [
                name, left_parenthesis, single_quote, right_parenthesis,
        ] = m.group('name', 'left_parenthesis', 'single_quote', 'right_parenthesis')

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


    def parse_statement_class(m0, s):
        if show:
            line(portray_raw_string(s[m0.end():]))

        m = class_match(s, m0.end())

        if m is none:
            return UnknownLine(s)

        [
            name_1, left_parenthesis, name_2, right_parenthesis__colon, newline,
        ] = m.group('name_1', 'left_parenthesis', 'name_2', 'right_parenthesis__colon', 'newline')

        parameters = ParameterColon_1(
                         OperatorLeftParenthesis(left_parenthesis),
                         Symbol(name_2),
                         OperatorRightParenthesisColon(right_parenthesis__colon),
                     )

        return ClassHeader(KeywordClass(m0.group('indented') + m0.group('keyword__ow')), name_1, parameters, newline)


    def parse_statement_decorator_header(m0, s):
        m = expression_match(s, m0.end())

        if m is none:
            return UnknownLine(s)

        return DecoratorHeader(
                   OperatorAtSign(m0.group('indented') + m0.group('keyword__ow')),
                   parse_expression(m),
                   m.group('newline'),
               )


    def parse_statement_define_header(m0, s):
        m = define_match(s, m0.end())

        if m is none:
            return UnknownLine(s)

        [
            name_1, left_parenthesis, name_2, right_parenthesis__colon, newline,
        ] = m.group('name_1', 'left_parenthesis', 'name_2', 'right_parenthesis__colon', 'newline')

        if name_2 is none:
            parameters = ParameterColon_0(left_parenthesis + right_parenthesis__colon)
        else:
            parameters = ParameterColon_1(
                             OperatorLeftParenthesis(left_parenthesis),
                             Symbol(name_2),
                             OperatorRightParenthesisColon(right_parenthesis__colon),
                         )

        return DefineHeader(KeywordDefine(m0.group('indented') + m0.group('keyword__ow')), name_1, parameters, newline)


    def parse_statement_from(m0, s):
        m = from_1_match(s, m0.end())

        if m is none:
            return UnknownLine(s)

        [
                name_1, dot, name_2, keyword__import__w, name_3, keyword__as__w, name_4, comma
        ] = m.group('name_1', 'dot', 'name_2', 'keyword__import__w', 'name_3', 'keyword__as__w', 'name_4', 'comma')

        if dot is none:
            module = name_1
        else:
            module = ExpressionDot(Symbol(name_1), OperatorDot(dot), name_2)

        as_fragment = AsFragment(name_3, KeywordAs(keyword__as__w), name_4)

        if comma is none:
            return StatementFromImport(
                       KeywordFrom(m0.group('indented') + m0.group('keyword__ow')),
                       Symbol(module),
                       KeywordImport(keyword__import__w),
                       as_fragment,
                       m.group('newline'),
                   )

        m2 = from_2_match(s, m.end())

        if m2 is none:
            return UnknownLine(s)

        [
                name_1, keyword__as__w, name_2, comma_2
        ] = m2.group('name_1', 'keyword__as__w', 'name_2', 'comma')

        as_fragment_2 = AsFragment(name_1, KeywordAs(keyword__as__w), name_2)

        if comma_2 is none:
            return StatementFromImport(
                       KeywordFrom(m0.group('indented') + m0.group('keyword__ow')),
                       module,
                       KeywordImport(keyword__import__w),
                       ExpressionComma(as_fragment, OperatorComma(comma), as_fragment_2),
                       m2.group('newline'),
                   )

        raise_runtime_error('parse_statement_from: incomplete')


    def parse_statement_import(m0, s):
        m = import_match(s, m0.end())

        if m is none:
            return UnknownLine(s)

        return StatementImport(
                   KeywordImport(m0.group('indented') + m0.group('keyword__ow')),
                   Symbol(m.group('name_1')),
                   m.group('newline'),
               )


    def parse_statement_return(m0, s):
        m = expression_match(s, m0.end())

        if m is none:
            return UnknownLine(s)

        return StatementReturnExpression(
                   KeywordReturn(m0.group('indented') + m0.group('keyword__ow')),
                   parse_expression(m),
                   m.group('newline'),
               )


    find_parse_line = {
                          'class'  : parse_statement_class,
                          'def'    : parse_statement_define_header,
                          'from'   : parse_statement_from,
                          'import' : parse_statement_import,
                          'return' : parse_statement_return,
                          '@'      : parse_statement_decorator_header,
                      }.__getitem__


    @share
    def parse_python_from_path(path):
        data   = read_text_from_path(path)
        many   = []
        append = many.append

        for s in data.splitlines(true):
            m = line_match(s)

            if m is none:
                append(UnknownLine(s))
                continue

            [keyword, name] = m.group('keyword', 'name')

            if keyword is not none:
                assert name is none

                append(find_parse_line(keyword)(m, s))
                continue

            if name:
                append(parse_statement_expression__symbol(m, s, name))
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
