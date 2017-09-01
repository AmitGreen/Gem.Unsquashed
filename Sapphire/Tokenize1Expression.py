#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Tokenize1Expression')
def gem():
    show = 0


    @share
    def tokenize_nested_atom():
        s = qs()
        m = atom_match(s, qj())

        if m is none:
            raise_unknown_line(1)

        atom_s = m.group('atom')

        if atom_s is not none:
            if m.start('comment_newline') is not -1:
                raise_unknown_line(3)

            wi(m.end('atom'))
            wj(m.end())

            return find_atom_type(atom_s[0])(atom_s)

        left_parenthesis  = conjure_left_parenthesis(s[qi() : m.end('left_parenthesis__ow')])
        right_parenthesis = m.group('right_parenthesis')

        if right_parenthesis is not none:
            raise_unknown_line(2)

        if m.start('comment_newline') is not -1:
            raise_unknown_line(3)

        j = m.end()

        wi(j)
        wj(j)

        return left_parenthesis


    @share
    def tokenize_normal_atom():
        s = qs()
        m = atom_match(s, qj())

        if m is none:
            line('%s: %s', my_name(), portray_raw_string(s[qj():]))
            assert 0
            raise_unknown_line(1)

        atom_s = m.group('atom')

        if atom_s is not none:
            if m.start('comment_newline') is -1:
                wi(m.end('atom'))
                wj(m.end())
            else:
                wn(conjure_token_newline(s[m.end('atom'):]))

            return find_atom_type(atom_s[0])(atom_s)

        left_parenthesis  = conjure_left_parenthesis(s[qi() : m.end('left_parenthesis__ow')])
        right_parenthesis = m.group('right_parenthesis')

        if right_parenthesis is not none:
            raise_unknown_line(2)

        if m.start('comment_newline') is not -1:
            raise_unknown_line(3)

        j = m.end()

        wd(qd() + 1)
        wi(j)
        wj(j)

        return left_parenthesis


    @share
    def tokenize_operator():
        s = qs()
        m = operator_match(s, qj())

        if m is none:
            assert 0
            line('%s: %s', my_name(), portray_raw_string(s[qj():]))
            raise_unknown_line(1)

        operator_s = m.group('operator')

        if operator_s is not none:
            conjure = find_operator_conjure_function(operator_s)

            if m.end('comment_newline') is -1:
                if conjure is conjure_right_parenthesis:
                    d = qd()

                    if d is 0:
                        raise_unknown_line(2)

                    wd(d - 1)

                j = m.end()
                r = conjure(s[qi():j])

                wi(j)
                wj(j)

                return r

            d = qd()

            if d is 0:
                if conjure is conjure_colon:
                    return conjure_colon_newline(s[qi():])

                operator_end = m.end('operator')
                wn(conjure_token_newline(s[operator_end:]))

                return conjure(s[qi():operator_end])

            if d is 1:
                if conjure is conjure_right_parenthesis:
                    i = m.end('operator')

                    wd(0)
                    wn(conjure_token_newline(s[i:]))

                    return conjure_right_parenthesis(s[qi():i])

                raise_unknown_line(3)

            raise_unknown_line(4)

        left_parenthesis  = conjure_left_parenthesis(s[qi() : m.end('left_parenthesis__ow')])
        right_parenthesis = m.group('right_parenthesis')

        if right_parenthesis is not none:
            right_parenthesis = conjure_right_parenthesis(right_parenthesis)

            if m.end('comment_newline') is -1:
                wi(m.end('right_parenthesis'))
                wj(m.end())
            else:
                if qd() is 0:
                    wn(conjure_token_newline(s[m.end('right_parenthesis'):]))
                else:
                    raise_unknown_line(5)

            return Arguments_0(left_parenthesis, right_parenthesis)

        if m.end('comment_newline') is not -1:
            raise_unknown_line(6)

        j = m.end()

        wd(qd() + 1)
        wi(j)
        wj(j)

        return left_parenthesis
