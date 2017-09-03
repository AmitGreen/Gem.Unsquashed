#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Tokenize1Atom')
def gem():
    show = 0


    #
    #   Note:
    #       Below a few tests of 'i == j'.  None of these tests can be optimized to 'i is j'
    #       since [the original] 'i' & 'j' could have been created with two different calls, such as:
    #
    #           1.  m.end('atom'); .vs.
    #           2.  m.end()
    #
    #       with 'ow' is empty -- and thus have the same value (but different internal addresses).
    #
    #   Note #2:
    #       The previous note also applies to tests like 'qi() != j', cannot replace this with 'qi() is not j'
    #


    def tokenize__argument_first_atom__X__newline(m):
        atom_s = m.group('atom')

        if atom_s is not none:
            conjure = find_atom_type(atom_s[0])

            if conjure is conjure_right_parenthesis:
                if qd() is 1:
                    atom_end = m.end('atom')
                    s        = qs()

                    r = conjure_right_parenthesis(s[qi() : atom_end])

                    wd0()
                    wn(conjure_token_newline(s[atom_end : ]))

                    return r

                assert qd() > 0

                wd(qd() - 1)

                r = conjure_right_parenthesis(qs()[qi() : ])

                skip_tokenize_prefix()

                return r

            raise_unknown_line(1)

        return tokenize__atom__X__left_parenthesis__newline(m)


    @share
    def tokenize__argument_first_atom():
        if show is 7:
            my_line(portray_string(qs()[qj() : ]))

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
            #my_line(portray_string(s[j : ]))
            raise_unknown_line(1)

        if m.start('comment_newline') is not -1:
            return tokenize__argument_first_atom__X__newline(m)

        atom_s = m.group('atom')

        if atom_s is not none:
            #
            #<different-from: tokenize_atom>
            #
            conjure = find_atom_type(atom_s[0])

            if conjure is conjure_right_parenthesis:
                j = m.end()

                wd(qd() - 1)
                wi(j)
                wj(j)

                return conjure_right_parenthesis(s[qi() : j])

            r = conjure(atom_s)
            #</different-from>

            if qi() != j:
                r = PrefixAtom(s[qi() : j], r)

            wi(m.end('atom'))
            wj(m.end())

            return r

        left_parenthesis       = conjure_left_parenthesis(s[qi() : m.end('left_parenthesis__ow')])
        right_parenthesis__end = m.end('right_parenthesis')

        if right_parenthesis__end is not -1:
            wi(right_parenthesis__end)
            wj(m.end())

            return EmptyTuple(left_parenthesis, conjure_right_parenthesis(m.group('right_parenthesis')))

        j = m.end()

        wd(qd() + 1)
        wi(j)
        wj(j)

        return left_parenthesis


    def tokenize__atom__X__left_parenthesis__newline(m):
        right_parenthesis__end = m.end('right_parenthesis')

        if right_parenthesis__end is not -1:
            left_parenthesis__ow__end = m.end('left_parenthesis__ow')

            if qd() is 0:
                raise_unknown_line(1)

            s = qs()
            r = EmptyTuple(
                    conjure_left_parenthesis (s[qi() : left_parenthesis__ow__end]),
                    conjure_right_parenthesis(s[left_parenthesis__ow__end : ]),
                )

            skip_tokenize_prefix()

            return r

        if qd() is 0:
            raise_unknown_line(2)

        r = conjure_left_parenthesis(qs()[qi() : ])

        skip_tokenize_prefix()

        return r


    def tokenize_atom__X__newline(m):
        atom_s = m.group('atom')

        if atom_s is not none:
            if qd() is not 0:
                raise_unknown_line(1)

            r = find_atom_type(atom_s[0])(atom_s)

            wn(conjure_token_newline(qs()[m.end('atom') : ]))

            if qi() == qj():
                return r

            return PrefixAtom(qs()[qi() : qj()], r)

        return tokenize__atom__X__left_parenthesis__newline(m)


    @share
    def tokenize_atom():
        j = qj()
        s = qs()
        m = atom_match(s, j)

        if m is none:
            raise_unknown_line(1)

        if m.start('comment_newline') is not -1:
            return tokenize_atom__X__newline(m)

        atom_s = m.group('atom')

        if atom_s is not none:
            r = find_atom_type(atom_s[0])(atom_s)

            if qi() != j:
                r = PrefixAtom(s[qi() : j], r)

            wi(m.end('atom'))
            wj(m.end())

            return r

        left_parenthesis       = conjure_left_parenthesis(s[qi() : m.end('left_parenthesis__ow')])
        right_parenthesis__end = m.end('right_parenthesis')

        if right_parenthesis__end is not -1:
            wi(right_parenthesis__end)
            wj(m.end())

            return EmptyTuple(left_parenthesis, conjure_right_parenthesis(m.group('right_parenthesis')))

        j = m.end()

        wd(qd() + 1)
        wi(j)
        wj(j)

        return left_parenthesis
