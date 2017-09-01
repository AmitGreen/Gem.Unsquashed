#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Tokenize1Expression')
def gem():
    show = 0


    @share
    def tokenize_nested_atom():
        m = atom_match(qs(), qj())

        if m is none:
            raise_unknown_line(1)

        atom_s = m.group('atom')

        if m.start('comment_newline') is not -1:
            raise_unknown_line(2)

        wi(m.end('atom'))
        wj(m.end())

        return find_atom_type(atom_s[0])(atom_s)


    @share
    def tokenize_nested_operator():
        s = qs()
        m = nested_operator_match1(s, qj())

        if m is none:
            raise_unknown_line(1)

        conjure = find_operator_conjure_function(m.group('operator'))

        if show is 7:
            line('%s: %s; conjure; %s; comment_newline: %s',
                 my_name(), portray_raw_string(s[qj():]), conjure, m.start('comment_newline'))

        if m.start('comment_newline') is not -1:
            if conjure is conjure_right_parenthesis:
                i = m.end('operator')

                wn(conjure_token_newline(s[i:]))

                return conjure(s[qi():i])

            raise_unknown_line(2)
        
        j = m.end()
        r = conjure(s[qi():j])

        wi(j)
        wj(j)

        return r


    @share
    def tokenize_normal_atom():
        s = qs()
        m = atom_match(s, qj())

        if m is none:
            raise_unknown_line(1)

        atom_s = m.group('atom')

        if m.start('comment_newline') is -1:
            wi(m.end('atom'))
            wj(m.end())
        else:
            wn(conjure_token_newline(s[m.end('atom'):]))

        return find_atom_type(atom_s[0])(atom_s)


    @share
    def tokenize_postfix_operator():
        s = qs()
        m = postfix_operator_match1(s, qj())

        if m is none:
            line('%s: %s', my_name(), portray_raw_string(s[qj():]))
            raise_unknown_line(1)

        operator_s = m.group('operator')

        if operator_s is not none:
            j = m.end()
            r = find_operator_conjure_function(operator_s)(s[qi():j])

            wi(j)
            wj(j)

            return r

        left_parenthesis  = conjure_left_parenthesis(s[qi() : m.end('left_parenthesis__ow')])
        right_parenthesis = m.group('right_parenthesis')

        if right_parenthesis is not none:
            right_parenthesis = conjure_right_parenthesis(right_parenthesis)

            if m.end('comment_newline') is not -1:
                wn(conjure_token_newline(s[m.end('right_parenthesis'):]))

                return Arguments_0(left_parenthesis, right_parenthesis)

            raise_unknown_line(3)

        if m.end('comment_newline') is not -1:
            raise_unknown_line(4)

        j = m.end()

        wi(j)
        wj(j)

        return left_parenthesis
