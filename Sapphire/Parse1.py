#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1')
def gem():
    #require_gem('Sapphire.Expression')
    require_gem('Sapphire.Match')
    require_gem('Sapphire.Parse7')
    require_gem('Sapphire.Parse7Expression')
    require_gem('Sapphire.Statement')
    #require_gem('Sapphire.Token')


    show = true


    def parse1_statement_define_header(m1, s):
        if m1.end('newline') is not -1:
            line('parse1_statement_define_header: incomplete#1')
            return UnknownLine(s)

        #
        #   name1
        #
        m2 = name_match(s, m1.end())

        if m2 is none:
            return UnknownLine(s)

        name1 = m2.group()
        #</name1>

        m2_end = m2.end()

        #
        #   parenthesis
        #
        m3 = define1_parenthesis_match(s, m2_end)

        if m3 is none:
            return UnknownLine(s)

        newline = m3.group('newline')
        #</parenthesis>

        if newline is not none:
            parameters = ParameterColon_0(s[m2_end : m3.start('newline')])
        else:
            #
            #   name2
            #
            m4 = name_match(s, m3.end())

            if m4 is none:
                return UnknownLine(s)

            name2 = m4.group()
            #</name2>

            #
            #   right-parenthesis
            #
            m5 = define1__right_parenthesis__colon__match(s, m4.end())

            if m5 is none:
                return UnknownLine(s)

            newline = m5.group('newline')
            #</parenthesis>

            parameters = ParameterColon_1(
                             OperatorLeftParenthesis(m3.group()),
                             Symbol(name2),
                             OperatorRightParenthesisColon(m5.group('right_parenthesis__colon')),
                         )

        return DefineHeader(KeywordDefine(m1.group()), name1, parameters, newline)


    lookup_parse1_line = {
                             #'class'  : parse7_statement_class,
                             'def'    : parse1_statement_define_header,
                             #'from'   : parse7_statement_from,
                             #'import' : parse7_statement_import,
                             #'return' : parse7_statement_return,
                             #'@'      : parse7_statement_decorator_header,
                         }.get


    @share
    def parse1_python_from_path(path):
        data   = read_text_from_path(path)
        many   = []
        append = many.append

        for s in data.splitlines(true):
            m = line1_match(s)

            if m is none:
                append(UnknownLine(s))
                continue

            token = m.group('token')

            if token is not none:
                parse1_line = lookup_parse1_line(token)

                if parse1_line is not none:
                    append(parse1_line(m, s))
                    continue

                if m.end('newline') is not none:
                    line('parse1_python_from_path: incomplete#1')
                    append(UnknownLine(s))
                    continue

                line('parse1_python_from_path: incomplete#2')
                append(UnknownLine(s))

                append(parse7_statement_expression__symbol(m, s, name))
                continue

            comment = m.group('comment')

            if comment is not none:
                [indented, newline] = m.group('indented', 'newline')

                assert newline is not none

                if indented is none:
                    append(Comment(comment, newline))
                    continue

                append(IndentedComment(indented, comment, newline))
                continue

            append(EmptyLine(m.group()))
            continue

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
