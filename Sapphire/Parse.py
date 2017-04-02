#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse')
def gem():
    require_gem('Sapphire.Expression')
    require_gem('Sapphire.Match')
    require_gem('Sapphire.Statement')
    require_gem('Sapphire.Token')


    show = true


    class FunctionCall_0(Object):
        __slot__ = ((
            'left',                         #   Expression
            'pair_of_parenthesis',          #   String
        ))


        def __init__(t, left, pair_of_parenthesis):
            t.left                = left
            t.pair_of_parenthesis = pair_of_parenthesis


        def __repr__(t):
            return arrange('<FunctionCall_0 %r %r>', t.left, t.pair_of_parenthesis)


    class FunctionCall_1(Object):
        __slot__ = ((
            'left',                         #   Expression
            'left_parenthesis',             #   String
            'argument_1',                   #   Any
            'right_parenthesis',            #   String
        ))


        def __init__(t, left, left_parenthesis, argument_1, right_parenthesis):
            t.left              = left
            t.left_parenthesis  = left_parenthesis
            t.argument_1        = argument_1
            t.right_parenthesis = right_parenthesis


        def __repr__(t):
            return arrange('<FunctionCall_1 %r %r %r %r>',
                           t.left, t.left_parenthesis, t.argument_1, t.right_parenthesis)


    class ReturnExpression(Token):
        __slots__ = ((
            'keyword_return',               #   String
            'expression',                   #   String
        ))


        def __init__(t, keyword_return, expression):
            t.keyword_return = keyword_return
            t.expression     = expression


        def  __repr__(t):
            return arrange('<Return %r %s>', t.keyword_return, t.expression)


    def parse_expression(m):
        [
                name_1, left_parenthesis, single_quote, right_parenthesis,
        ] = m.group('name_1', 'left_parenthesis', 'single_quote', 'right_parenthesis')

        expression = Symbol(name_1)

        if left_parenthesis is none:
            return expression

        if single_quote is none:
            return FunctionCall_0(expression, left_parenthesis + right_parenthesis)

        return FunctionCall_1(expression, left_parenthesis, SingleQuote(single_quote), right_parenthesis)


    def parse_statement_decorator_header(m0, s):
        m = expression_match(s, m0.end())

        if m is none:
            return UnknownLine(s)

        return DecoratorHeader(OperatorAtSign(m0.group('indented') + m0.group('keyword__ow')), parse_expression(m))


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
            module = ExpressionDot(name_1, dot, name_2)

        as_fragment = AsFragment(name_3, KeywordAs(keyword__as__w), name_4)

        if comma is none:
            return StatementFromImport(
                       KeywordFrom(m0.group('indented') + m0.group('keyword__ow')),
                       module,
                       KeywordImport(keyword__import__w),
                       as_fragment,
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
                       ExpressionComma(as_fragment, OperatorComma(comma), as_fragment_2)
                   )

        raise_runtime_error('parse_statement_from: incomplete')


    def parse_statement_import(m0, s):
        #if show:
        #    line(portray_raw_string(s[m0.end():]))

        m = import_match(s, m0.end())

        if m is none:
            return UnknownLine(s)

        name_1 = m.group('name_1')

        return StatementImport(
                   KeywordImport(m0.group('indented') + m0.group('keyword__ow')),
                   name_1,
               )


    def parse_statement_define_header(m0, s):
        m = define_match(s, m0.end())

        if m is none:
            return UnknownLine(s)

        [
            name_1, left_parenthesis, name_2, right_parenthesis__colon,
        ] = m.group('name_1', 'left_parenthesis', 'name_2', 'right_parenthesis__colon')

        if name_2 is none:
            parameters = ParameterColon_0(left_parenthesis + right_parenthesis__colon)
        else:
            parameters = ParameterColon_1(left_parenthesis, name_2, right_parenthesis__colon)

        return DefineHeader(KeywordDefine(m0.group('indented') + m0.group('keyword__ow')), name_1, parameters)


    def parse_statement_return(m0, s):
        m = expression_match(s, m0.end())

        if m is none:
            return UnknownLine(s)

        return ReturnExpression(KeywordReturn(m0.group('indented') + m0.group('keyword__ow')), parse_expression(m))


    keyword_define  .parse_line = parse_statement_define_header
    keyword_from    .parse_line = parse_statement_from
    keyword_import  .parse_line = parse_statement_import
    keyword_return  .parse_line = parse_statement_return
    operator_at_sign.parse_line = parse_statement_decorator_header


    @share
    def parse_python_from_path(path):
        data        = read_text_from_path('../Sapphire/Main.py')
        many        = []
        append_line = many.append

        for s in data.splitlines(true):
            m = line_match(s)

            if m is none:
                append_line(UnknownLine(s))
                continue

            [
                    indented, keyword, comment, newline_2,
            ] = m.group('indented', 'keyword', 'comment', 'newline_2')

            if keyword is not none:
                assert comment is newline_2 is none

                append_line(lookup_symbol(keyword).parse_line(m, s))
                continue

            assert newline_2 is not none

            if comment is not none:
                if indented is '':
                    if comment is '':
                        append_line(empty_comment)
                        continue

                    append_line(Comment(comment))
                    continue

                append_line(IndentedComment(indented, comment))
                continue

            if indented is '':
                append_line(empty_line)
                continue

            append_line(EmptyLine(indented))
            continue

        for v in many:
            line('%r', v)
