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
    def tokenize_argument_operator():
        s = qs()
        m = argument_operator_match1(s, qj())

        if m is none:
            raise_unknown_line(1)

        conjure = find_operator_conjure_function(m.group('operator'))

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
