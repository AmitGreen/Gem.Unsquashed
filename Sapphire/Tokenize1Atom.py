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


    def tokenize_atom__X__left_parenthesis(m):
        left_parenthesis       = conjure_left_parenthesis(qs()[qi() : m.end('left_parenthesis__ow')])
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


    def tokenize_atom__X__open_newline(m):
        left_parenthesis__ow__end = m.end('left_parenthesis__ow')

        if left_parenthesis__ow__end is not -1:
            right_parenthesis__end = m.end('right_parenthesis')

            if right_parenthesis__end is not -1:
                if qd() is 0:
                    raise_unknown_line(1)

                s = qs()
                r = EmptyTuple(
                        conjure_left_parenthesis (s[qi() : left_parenthesis__ow__end]),
                        conjure_right_parenthesis(s[left_parenthesis__ow__end : ]),
                    )

                skip_tokenize_prefix()

                return r

            wd(qd() + 1)

            r = conjure_left_parenthesis(qs()[qi() : ])

            skip_tokenize_prefix()

            return r

        right_brace__end = m.end('right_brace')

        if right_brace__end is not -1:
            left_brace__ow__end = m.end('left_brace__ow')

            s = qs()

            left_brace = conjure_left_brace(s[qi() : left_brace__ow__end])

            if qd() is 0:
                right_brace__end = m.end('right_brace')

                r = EmptyMap(
                        left_brace,
                        conjure_right_brace(s[left_brace__ow__end : right_brace__end])
                    )

                wn(conjure_token_newline(s[right_brace__end : ]))

                return r

            r = EmptyMap(
                    left_brace,
                    conjure_right_brace(s[left_brace__ow__end : ]),
                )

            skip_tokenize_prefix()

            return r

        if qd() is 0:
            raise_unknown_line(4)

        r = conjure_left_brace(qs()[qi() : ])

        skip_tokenize_prefix()

        return r


    def tokenize_atom__X__newline(m):
        atom_s = m.group('atom')

        if atom_s is not none:
            r = find_atom_type(atom_s[0])(atom_s)

            if qd() is not 0:
                suffix = conjure_whitespace(qs()[m.end('atom') : ])

                if qi() == qj():
                    r = r.suffix_meta(r, suffix)
                else:
                    r = r.bookcase_meta(
                            conjure_whitespace(qs()[qi() : qj()]),
                            r,
                            suffix,
                        )

                skip_tokenize_prefix()

                return r

            wn(conjure_token_newline(qs()[m.end('atom') : ]))

            if qi() == qj():
                return r

            return r.prefix_meta(conjure_whitespace(qs()[qi() : qj()]), r)

        return tokenize_atom__X__open_newline(m)


    def tokenize_comma_atom__X__newline(m):
        #
        #<similiar-to: tokenize_comma_atom__X__newline>
        #
        #   Difference: Uses 'right-parenthesis' instead of 'right-square-bracket'
        #
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

        return tokenize_atom__X__open_newline(m)
        #</similiar-to>


    def tokenize_index_atom__X__newline(m):
        #
        #<similiar-to: tokenize_comma_atom__X__newline>
        #
        #   Difference: Uses 'right-square-bracket' instead of 'right-parenthesis'
        #
        atom_s = m.group('atom')

        if atom_s is not none:
            conjure = find_atom_type(atom_s[0])

            if conjure is conjure_right_square_bracket:
                if qd() is 1:
                    atom_end = m.end('atom')
                    s        = qs()

                    r = conjure_right_square_bracket(s[qi() : atom_end])

                    wd0()
                    wn(conjure_token_newline(s[atom_end : ]))

                    return r

                assert qd() > 0

                wd(qd() - 1)

                r = conjure_right_square_bracket(qs()[qi() : ])

                skip_tokenize_prefix()

                return r

            raise_unknown_line(1)

        return tokenize_atom__X__open_newline(m)
        #</similiar-to>


    @share
    def tokenize_atom():
        assert qk() is none
        assert qn() is none

        #
        #<similiar-to: tokenize_{comma,index}_atom>
        #
        #   Difference:
        #       Uses atom_match instead of {comma,index}_atom_match
        #       Calls tokenize_atom__X__newline instead of tokenize_{comma,index}_atom__X__newline
        #
        j = qj()

        m = atom_match(qs(), j)

        if m is none:
            my_line('s: %r', portray_string(qs()[j :]))
            raise_unknown_line(1)

        if m.start('comment_newline') is not -1:
            return tokenize_atom__X__newline(m)
        #<similiar-to: tokenize_{comma,index}_atom>

        atom_s = m.group('atom')

        if atom_s is not none:
            r = find_atom_type(atom_s[0])(atom_s)

            #
            #<same-as: tokenize_argument_atom & tokenize_comma_atom>
            #
            if qi() != j:
                r = r.prefix_meta(conjure_whitespace(qs()[qi() : j]), r)

            wi(m.end('atom'))
            wj(m.end())

            return r
            #</same-as>

        #
        #<same-as: tokenize_argument_atom & tokenize_comma_atom>
        #
        keyword_s = (m.group('keyword')) or (m.group('operator'))

        if keyword_s is not none:
            j = m.end()

            r = find_operator_conjure_function(keyword_s)(qs()[qi() : j])

            wi(j)
            wj(j)

            return r

        return tokenize_atom__X__left_parenthesis(m)
        #</same-as>


    @share
    def tokenize_argument_atom():
        #
        #   Temporary hack, will allow '*' later
        # 
        return tokenize_comma_atom()


    @share
    def tokenize_comma_atom():
        assert qk() is none
        assert qn() is none

        j = qj()

        #
        #<similiar-to: tokenize_atom>
        #
        #   Difference:
        #       Uses comma_atom_match instead of atom_match
        #       Calls tokenize_comma_atom__X__newline instead of tokenize_atom__X__newline
        #
        m = argument_atom_match(qs(), j)

        if m is none:
            raise_unknown_line(1)

        if m.start('comment_newline') is not -1:
            return tokenize_comma_atom__X__newline(m)

        atom_s = m.group('atom')
        #</similiar-to: tokenize_atom>

        if atom_s is not none:
            conjure = find_atom_type(atom_s[0])

            #
            #<similiar-to: tokenize_index_atom>
            #
            #   Difference: Deals with right-parenthesis instead of right-square-bracket 
            #
            if conjure is conjure_right_parenthesis:
                d = qd()
                j = m.end()

                if d is 0:
                    raise_unknown_line(2)

                assert d > 0

                r = conjure_right_parenthesis(qs()[qi() : j])

                wd(d - 1)
                wi(j)
                wj(j)

                return r
            #</similiar-to: tokenize_comma-atom>

            r = conjure(atom_s)

            #
            #<same-as: tokenize_atom>
            #
            if qi() != j:
                r = r.prefix_meta(conjure_whitespace(qs()[qi() : j]), r)

            wi(m.end('atom'))
            wj(m.end())

            return r
            #</same-as>

        #
        #<same-as: tokenize_atom>
        #
        keyword_s = (m.group('keyword')) or (m.group('operator'))

        if keyword_s is not none:
            j = m.end()

            r = find_operator_conjure_function(keyword_s)(qs()[qi() : j])

            wi(j)
            wj(j)

            return r

        return tokenize_atom__X__left_parenthesis(m)
        #</same-as>


    @share
    def tokenize_index_atom():
        assert qk() is none
        assert qn() is none

        #
        #<similiar-to: tokenize_atom>
        #
        #   Difference:
        #       Uses index_atom_match instead of atom_match
        #       Calls tokenize_index_atom__X__newline instead of tokenize_atom__X__newline
        #
        j = qj()

        m = index_atom_match(qs(), j)

        if m is none:
            raise_unknown_line(1)

        if m.start('comment_newline') is not -1:
            return tokenize_index_atom__X__newline(m)
        #</similiar-to: tokenize_atom>

        atom_s = m.group('atom')

        if atom_s is not none:
            conjure = find_atom_type(atom_s[0])

            #
            #<similiar-to: tokenize_comma-atom>
            #
            #   Difference: Deals with right-square-bracket instead of right-parenthesis
            #
            if conjure is conjure_right_square_bracket:
                d = qd()
                j = m.end()

                if d is 0:
                    raise_unknown_line(2)

                assert d > 0

                r = conjure_right_square_bracket(qs()[qi() : j])

                wd(d - 1)
                wi(j)
                wj(j)

                return r
            #</similiar-to: tokenize_comma-atom>

            r = conjure(atom_s)

            #
            #<same-as: tokenize_atom>
            #
            if qi() != j:
                r = r.prefix_meta(conjure_whitespace(qs()[qi() : j]), r)

            wi(m.end('atom'))
            wj(m.end())

            return r
            #</same-as>

        #
        #<same-as: tokenize_atom>
        #
        keyword_s = (m.group('keyword')) or (m.group('operator'))

        if keyword_s is not none:
            j = m.end()

            r = find_operator_conjure_function(keyword_s)(qs()[qi() : j])

            wi(j)
            wj(j)

            return r

        return tokenize_atom__X__left_parenthesis(m)
        #</same-as>
