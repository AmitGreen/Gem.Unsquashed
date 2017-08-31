#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1Call')
def gem():
    show = 0


    @share
    def parse1_expression_call(left, left_parenthesis):
        return ExpressionCall(left, parse1_arguments__left_parenthesis(left_parenthesis))


    def tokenize_atom():
        m = atom_match(qs(), qj())

        if m is none:
            #line('%s: %s', my_name(), portray_raw_string(qs()[qj():]))
            raise_unknown_line(1)

        wi(m.start('ow'))
        wj(m.end())

        s1 = m.group('atom')

        return find_atom_type(s1[0])(s1)


    def tokenize_argument1_operator():
        s = qs()
        m = argument1_operator_match1(s, qj())

        if m is none:
            #line('%s: %s', my_name(), portray_raw_string(s[qj():]))
            raise_unknown_line(1)

        conjure = find_operator_conjure_function(m.group('operator'))

        if conjure is conjure_right_parenthesis:
            if m.start('comment_newline') is -1:
                raise_unknown_line(2)

            i = m.end('operator')

            wn(conjure_token_newline(s[i:]))

            return conjure(s[qi():i])
        
        if m.start('comment_newline') is not -1:
            raise_unknown_line(3)

        j = m.end()
        r = conjure(s[qi():j])

        wi(j)
        wj(j)

        return r


    def tokenize_argument7_operator():
        s = qs()
        m = argument7_operator_match1(s, qj())

        if m is none:
            #line('%s: %s', my_name(), portray_raw_string(s[qj():]))
            raise_unknown_line(1)

        conjure = find_operator_conjure_function(m.group('operator'))

        if conjure is conjure_right_parenthesis:
            if m.start('comment_newline') is -1:
                raise_unknown_line(2)

            i = m.end('operator')

            wn(conjure_token_newline(s[i:]))

            return conjure(s[qi():i])
        
        if m.start('comment_newline') is not -1:
            raise_unknown_line(3)

        j = m.end()
        r = conjure(s[qi():j])

        wi(j)
        wj(j)

        return r


    @share
    def parse1_arguments__left_parenthesis(left_parenthesis):
        atom_1     = tokenize_atom()
        operator_1 = tokenize_argument1_operator()

        if operator_1.is_right_parenthesis:
            return Arguments_1(left_parenthesis, atom_1, operator_1)

        if operator_1.is_comma:
            atom_2     = tokenize_atom()
            operator_2 = tokenize_argument7_operator()

            if operator_2.is_right_parenthesis:
                return Arguments_2(left_parenthesis, atom_1, operator_1, atom_2, operator_2)

            raise_unknown_line(2)

        raise_unknown_line(3)
