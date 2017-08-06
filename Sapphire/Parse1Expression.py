#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1Expression')
def gem():
    require_gem('Sapphire.Core')


    show = 0


    lookup_operator = {
                          none : none,
                          '.' : OperatorDot,
                          '=' : OperatorEqualSign,
                      }.__getitem__



    @share
    def parse1_statement_expression__symbol(indented, identifier, index):
        s = qs()

        if show:
            line('indented: %r, identifier: %r; s: %r', indented, identifier, s[index:])

        #
        #<postfix1-operator>
        #
        m2 = statement_postfix_operator_match1(s, index)

        if m2 is none:
            return create_UnknownLine(parse1_statement_expression__symbol, 1)

        right_parenthesis = m2.group('right_parenthesis')
        #</postfix1-operator>

        if right_parenthesis is not none:
            if m2.start('comment_newline') is not -1:
                return StatementCall(
                           indented,
                           identifier,
                           Arguments_0(
                               OperatorLeftParenthesis(s[index:m2.start('right_parenthesis')]),
                               OperatorRightParenthesis(right_parenthesis),
                           ),
                           conjure_token_newline(s[m2.end('right_parenthesis'):]),
                       )

            return create_UnknownLine(parse1_statement_expression__symbol, 2)

        OperatorMeta = lookup_operator(m2.group('operator'))

        if OperatorMeta is not none:
            operator = OperatorMeta(m2.group())

            if OperatorMeta is OperatorDot:
                #
                #<name1>
                #
                m3 = name_match(s, m2.end())

                if m3 is none:
                    return create_UnknownLine(parse1_statement_expression__symbol, 1)
                #</name1>

                left = ExpressionDot(identifier, operator, conjure_identifier(m3.group()))
                
                #line('left: %r; s: %s', left, portray_raw_string(s[m3.end():]))

                #
                #<postfix1-operator>
                #
                m4 = statement_postfix_operator_match1(s, m3.end())

                if m4 is none:
                    return create_UnknownLine(parse1_statement_expression__symbol, 2)

                right_parenthesis = m4.group('right_parenthesis')
                #</postfix1-operator>

                if right_parenthesis is not none:
                    return create_UnknownLine(parse1_statement_expression__symbol, 3)
                
                left_parenthesis = m4.group('left_parenthesis')

                if left_parenthesis is not none:
                    assert m4.start('comment_newline') is -1

                    arguments = parse1_arguments__left_parenthesis(OperatorLeftParenthesis(left_parenthesis), m4.end())

                    return create_UnknownLine(parse1_statement_expression__symbol, 5)
                
                return create_UnknownLine(parse1_statement_expression__symbol, 6)

            #
            #<atom1>
            #
            m3 = atom_match1(s, m2.end())

            if m3 is none:
                return create_UnknownLine(parse1_statement_expression__symbol, 6)

            s3     = m3.group()
            atom   = find_atom_type(s3[0])(s3)
            m3_end = m3.end()
            #</atom1>

            line('indented: %r; identifier: %r; operator: %r; atom: %r',
                 indented, identifier, operator, atom)

            return create_UnknownLine(parse1_statement_expression__symbol, 7)

        return create_UnknownLine(parse1_statement_expression__symbol, 8)
