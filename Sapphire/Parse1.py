#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1')
def gem():
    require_gem('Sapphire.Match')
    require_gem('Sapphire.Parse1From')
    require_gem('Sapphire.Parse1Import')
    require_gem('Sapphire.Parse7')
    require_gem('Sapphire.Parse7Expression')
    require_gem('Sapphire.Statement')
    require_gem('Sapphire.Tokenizer')


    show = true


    find_atom_type = {
                         "'" : SingleQuote,
                         '.' : Number,

                         '0' : Number, '1' : Number, '2' : Number, '3' : Number, '4' : Number,
                         '5' : Number, '6' : Number, '7' : Number, '8' : Number, '9' : Number,

                         'A' : Symbol, 'B' : Symbol, 'C' : Symbol, 'D' : Symbol, 'E' : Symbol, 'F' : Symbol,
                         'G' : Symbol, 'H' : Symbol, 'I' : Symbol, 'J' : Symbol, 'K' : Symbol, 'L' : Symbol,
                         'M' : Symbol, 'N' : Symbol, 'O' : Symbol, 'P' : Symbol, 'Q' : Symbol, 'R' : Symbol,
                         'S' : Symbol, 'T' : Symbol, 'U' : Symbol, 'V' : Symbol, 'W' : Symbol, 'X' : Symbol,
                         'Y' : Symbol, 'Z' : Symbol,

                         '_' : Symbol,

                         'a' : Symbol, 'b' : Symbol, 'c' : Symbol, 'd' : Symbol, 'e' : Symbol, 'f' : Symbol,
                         'g' : Symbol, 'h' : Symbol, 'i' : Symbol, 'J' : Symbol, 'k' : Symbol, 'l' : Symbol,
                         'm' : Symbol, 'n' : Symbol, 'o' : Symbol, 'p' : Symbol, 'q' : Symbol, 'r' : Symbol,
                         'S' : Symbol, 't' : Symbol, 'u' : Symbol, 'v' : Symbol, 'w' : Symbol, 'x' : Symbol,
                         'y' : Symbol, 'z' : Symbol,
                     }.__getitem__


    def parse1_statement_call(i, left, left_parenthesis):
        s = qs()

        #
        #<single_quote>
        #
        m1 = single_quote_match(s, i)

        if m1 is none:
            return parse_incomplete(parse1_statement_call, 1)

        argument_1 = SingleQuote(m1.group())
        m1_end     = m1.end()
        #</single_quote>

        #
        #<right-parenthesis>
        #
        m2 = statement_argument1_operator1_match(s, m1_end)

        if m2 is none:
            return parse_incomplete(parse1_statement_call, 2)

        right_parenthesis__end = m2.end('right_parenthesis')

        if right_parenthesis__end is -1:
            return parse_incomplete(parse1_statement_call, 3)
        #</right-parenthesis>

        right_parenthesis = OperatorRightParenthesis(s[m1_end : right_parenthesis__end])

        wk(TokenNewline(s[right_parenthesis__end:]))

        return ExpressionCall(left, Arguments_1(left_parenthesis, argument_1, right_parenthesis))


    def parse1_statement_decorator_header(m1):
        operator_at_sign = OperatorAtSign(m1.group())
        s                = qs()

        #
        #<atom>
        #
        m2 = atom1_match(s, m1.end())

        if m2 is none:
            return create_UnknownLine(parse1_statement_decorator_header, 1)

        s1     = m2.group()
        atom   = find_atom_type(s1[0])(s1)
        m2_end = m2.end()
        #</atom1>

        #
        #<postfix>
        #
        m3 = statement_postfix1_match(s, m2_end)

        if m3 is none:
            return create_UnknownLine(parse1_statement_decorator_header, 2)

        left_parenthesis__end = m3.end('left_parenthesis__ow')
        #</postfix>

        if left_parenthesis__end is -1:
            return DecoratorHeader(operator_at_sign, atom, TokenNewline(m3.group()))

        left_parenthesis  = OperatorLeftParenthesis(s[m2_end : left_parenthesis__end])
        right_parenthesis = m3.group('right_parenthesis')

        if right_parenthesis is not none:
            right_parenthesis = OperatorRightParenthesis(right_parenthesis)

            if m3.end('comment_newline') is not -1:
                return DecoratorHeader(
                           operator_at_sign,
                           ExpressionCall(atom, Arguments_0(left_parenthesis, right_parenthesis)),
                           TokenNewline(s[m3.end('right_parenthesis'):]),
                       )

            return create_UnknownLine(parse1_statement_decorator_header, 3)

        expression = parse1_statement_call(m3.end(), atom, left_parenthesis)

        if expression is none:
            return create_UnknownLine()

        return DecoratorHeader(operator_at_sign, expression, qx())


    def parse1_statement_define_header(m1):
        if m1.end('newline') is not -1:
            return create_UnknownLine(parse1_statement_define_header, 1)

        keyword_define = KeywordDefine(m1.group())
        s              = qs()

        #
        #<name1>
        #
        m2 = name_match(s, m1.end())

        if m2 is none:
            return create_UnknownLine(parse1_statement_define_header, 2)

        name1 = m2.group()
        #</name1>

        m2_end = m2.end()

        #
        #<parenthesis>
        #
        m3 = define1_parenthesis_match(s, m2_end)

        if m3 is none:
            return create_UnknownLine(parse1_statement_define_header, 3)

        comment_newline = m3.group('comment_newline')
        #</parenthesis>

        if comment_newline is not none:
            parameters = ParameterColon_0(s[m2_end : m3.start('comment_newline')])
        else:
            #
            #<name2>
            #
            m4 = name_match(s, m3.end())

            if m4 is none:
                return create_UnknownLine(parse1_statement_define_header, 4)

            name2 = m4.group()
            #</name2>

            #
            #<right-parenthesis>
            #
            m5 = define1__right_parenthesis__colon__match(s, m4.end())

            if m5 is none:
                return create_UnknownLine(parse1_statement_define_header, 5)

            comment_newline = m5.group('comment_newline')
            #</parenthesis>

            parameters = ParameterColon_1(
                             OperatorLeftParenthesis(m3.group()),
                             Symbol(name2),
                             OperatorRightParenthesisColon(m5.group('ow__right_parenthesis__colon__ow')),
                         )

        return DefineHeader(keyword_define, name1, parameters, TokenNewline(comment_newline))


    def parse1_statement_return(m1):
        if m1.end('newline') is not -1:
            return StatementReturn(m1.group())

        keyword_return = KeywordReturn(m1.group())
        s              = qs()

        #
        #<atom>
        #
        m2 = atom1_match(s, m1.end())

        if m2 is none:
            return create_UnknownLine(parse1_statement_return, 1)

        s1     = m2.group()
        atom   = find_atom_type(s1[0])(s1)
        m2_end = m2.end()
        #</atom1>

        #
        #<postfix>
        #
        m3 = statement_postfix1_match(s, m2_end)

        if m3 is none:
            return create_UnknownLine(parse1_statement_return, 2)

        left_parenthesis__end = m3.end('left_parenthesis__ow')
        #</postfix>

        if left_parenthesis__end is -1:
            return StatementReturnExpression(keyword_return, atom, TokenNewline(m3.group()))

        left_parenthesis  = OperatorLeftParenthesis(s[m2_end : left_parenthesis__end])
        right_parenthesis = m3.group('right_parenthesis')

        if right_parenthesis is not none:
            right_parenthesis = OperatorRightParenthesis(right_parenthesis)

            if m3.end('comment_newline') is not -1:
                return StatementReturnExpression(
                           keyword_return,
                           ExpressionCall(atom, Arguments_0(left_parenthesis, right_parenthesis)),
                           TokenNewline(s[m3.end('right_parenthesis'):]),
                       )

            return create_UnknownLine(parse1_statement_return, 3)

        expression = parse1_statement_call(s, m3.end(), atom, left_parenthesis)

        if expression is none:
            return create_UnknownLine()

        return StatementReturnExpression(keyword_return, expression, qk())


    lookup_parse1_line = {
                             #'class'  : parse7_statement_class,
                             'def'    : parse1_statement_define_header,
                             'from'   : parse1_statement_from,
                             'import' : parse1_statement_import,
                             'return' : parse1_statement_return,
                             '@'      : parse1_statement_decorator_header,
                         }.get


    @share
    def parse1_python_from_path(path):
        data   = read_text_from_path(path)
        many   = []
        append = many.append

        iterate_lines = z_initialize(data)

        for s in iterate_lines:
            m = line1_match(s)

            if m is none:
                append(create_UnknownLine(parse1_python_from_path, 1))
                continue

            token = m.group('token')

            if token is not none:
                parse1_line = lookup_parse1_line(token)

                if parse1_line is not none:
                    append(parse1_line(m))
                    continue

                if m.end('newline') is not none:
                    append(create_UnknownLine(parse1_python_from_path, 2))
                    continue

                append(create_UnknownLine(parse1_python_from_path, 3))
                continue

            [comment, newline] = m.group('comment', 'newline')

            if newline is none:
                assert comment is none

                append(create_UnknownLine(parse1_python_from_path, 4))
                continue

            if comment is not none:
                indented = m.group('indented')

                if indented is none:
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
