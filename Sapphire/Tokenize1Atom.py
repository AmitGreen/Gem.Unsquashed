#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Tokenize1Atom')
def gem():
    show = 0


    def parse1__argument_first_atom__X__left_parenthesis__newline(m):
        s = qs()

        atom_end = m.end('atom')

        wn(conjure_token_newline(s[atom_end : ]))

        return conjure_right_parenthesis(s[qi() : atom_end])


    @share
    def parse1__argument_first_atom():
        #
        #<different-from: tokenize_atom>
        #
        assert qd() > 0
        #</different-from>

        j = qj()
        s = qs()

        #
        #<different-from: tokenize_atom>
        #
        m = argument_first_atom_match(s, j)
        #</different-from>

        if m is none:
            my_line(portray_string(s[j : ]))
            raise_unknown_line(1)

        atom_s = m.group('atom')

        if atom_s is not none:
            #
            #<different-from: tokenize_atom>
            #
            conjure = find_atom_type(atom_s[0])

            if conjure is conjure_right_parenthesis:
                d = qd()

                wd(d - 1)

                if m.start('comment_newline') is -1:
                    j = m.end()

                    wi(j)
                    wj(j)

                    return conjure_right_parenthesis(s[qi() : j])

                return parse1__argument_first_atom__X__left_parenthesis__newline(m)
            #</different-from>

            i = qi()

            if m.start('comment_newline') is -1:
                wi(m.end('atom'))
                wj(m.end())
            else:
                #
                #<different-from: tokenize_atom>
                #
                raise_unknown_line(3)
                #</different-from>

            #
            #   NOTE:
            #       See note in 'tokenize_atom'
            #
            if i == j:
                #
                #<different-from: tokenize_atom>
                #
                return conjure(atom_s)
                #</different-from>

            #
            #<different-from: tokenize_atom>
            #
            return PrefixAtom(s[i : j], conjure(atom_s))
            #</different-from>

        left_parenthesis       = conjure_left_parenthesis(s[qi() : m.end('left_parenthesis__ow')])
        right_parenthesis__end = m.end('right_parenthesis')

        if m.start('comment_newline') is not -1:
            raise_unknown_line(4)

        if right_parenthesis__end is not -1:
            wi(right_parenthesis__end)
            wj(m.end())

            return EmptyTuple(left_parenthesis, conjure_right_parenthesis(m.group('right_parenthesis')))

        j = m.end()

        wd(qd() + 1)
        wi(j)
        wj(j)

        return left_parenthesis


    @share
    def tokenize_atom():
        j = qj()
        s = qs()
        m = atom_match(s, j)

        if m is none:
            #my_line(portray_string(s[j : ]))
            raise_unknown_line(1)

        atom_s = m.group('atom')

        if atom_s is not none:
            i = qi()

            if m.start('comment_newline') is -1:
                wi(m.end('atom'))
                wj(m.end())
            else:
                if qd() is not 0:
                    raise_unknown_line(2)

                wn(conjure_token_newline(s[m.end('atom') : ]))

            #
            #   Note:
            #       Can't optimize this to 'i is j' since they might be generated from two different
            #       calls is empty.  The different calls might have been:
            #
            #           1.  m.end('atom'); .vs.
            #           2.  m.end()
            #
            #       with 'ow' is empty -- and thus have the same value (but different addresses).
            #
            if i == j:
                return find_atom_type(atom_s[0])(atom_s)

            return PrefixAtom(s[i : j], find_atom_type(atom_s[0])(atom_s))

        left_parenthesis       = conjure_left_parenthesis(s[qi() : m.end('left_parenthesis__ow')])
        right_parenthesis__end = m.end('right_parenthesis')

        if m.start('comment_newline') is not -1:
            my_line('%r %r', left_parenthesis, right_parenthesis__end)
            raise_unknown_line(3)

        if right_parenthesis__end is not -1:
            wi(right_parenthesis__end)
            wj(m.end())

            return EmptyTuple(left_parenthesis, conjure_right_parenthesis(m.group('right_parenthesis')))

        j = m.end()

        wd(qd() + 1)
        wi(j)
        wj(j)

        return left_parenthesis
