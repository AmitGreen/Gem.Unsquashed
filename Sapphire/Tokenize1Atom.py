#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Tokenize1Atom')
def gem():
    show = 7


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


    def tokenize_atom__X__atom_newline(m, atom_s):
        r = find_atom_type(atom_s[0])(atom_s)

        #
        #<similiar-to: tokenize_atom__X_quote_newline>
        #
        #   Differences:
        #
        #       Uses "m.end('atom')" instead of "quote_end"
        #       Uses "qs()" intead of "s"
        #
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
        #</similiar-to>


    def tokenize_atom__X__quote_newline(m, quote_start):
        quote_end = m.end('quote')
        s         = qs()

        #
        #   NOTE:
        #
        #       Use 'qj()' here to be sure to pick up any letters prefixing the quote, such as r'prefixed'
        #
        r = find_atom_type(s[quote_start])(s[qj() : quote_end])

        #
        #<similiar-to: tokenize_atom__X__atom_newline>
        #
        #   Differences:
        #
        #       Uses "quote_end" instead of "m.end('atom')"
        #       Uses "s" intead of "qs()"
        #
        if qd() is not 0:
            suffix = conjure_whitespace(s[quote_end : ])

            if qi() == qj():
                r = r.suffix_meta(r, suffix)
            else:
                r = r.bookcase_meta(
                        conjure_whitespace(s[qi() : qj()]),
                        r,
                        suffix,
                    )

            skip_tokenize_prefix()

            return r

        wn(conjure_token_newline(s[m.end('atom') : ]))

        if qi() == qj():
            return r

        return r.prefix_meta(conjure_whitespace(qs()[qi() : qj()]), r)
        #</similiar-to>


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


    def tokenize_atom__X2__newline(m):
        atom_s = m.group('atom')

        if atom_s is not none:
            return tokenize_atom__X__atom_newline(m, atom_s)

        quote_start = m.start('quote')

        if quote_start is not -1:
            return tokenize_atom__X__quote_newline(m, quote_start)

        keyword_s = m.group('keyword')

        if keyword_s is not none:
            j = m.end()

            conjure = find_operator_conjure_function(keyword_s)

            if qd() is not 0:
                r = conjure(s[qi() : ])

                skip_tokenize_prefix()

                return r

            keyword_end = m.end('keyword')
            s           = qs()

            r = conjure(s[qi() : keyword_end])

            wn(conjure_token_newline(s[keyword_end : ]))

            return r

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
        keyword_s = (m.group('keyword')) or (m.group('operator'))

        if keyword_s is not none:
            if is_close_operator(keyword_s) is 7:
                d = qd()

                if d is 1:
                    operator_end = m.end('operator')
                    s            = qs()

                    r = find_operator_conjure_function(keyword_s)(s[qi() : operator_end])

                    wd0()
                    wn(conjure_token_newline(s[operator_end : ]))

                    return r

                r = find_operator_conjure_function(keyword_s)(s[qi() : operator_end])

                skip_tokenize_prefix()

                return r

            if qd() is 0:
                operator_end = m.end('operator')
                s            = qs()

                r = find_operator_conjure_function(keyword_s)(s[qi() : operator_end])

                wn(conjure_token_newline(s[operator_end : ]))

                return r

            r = find_operator_conjure_function(keyword_s)(qs()[qi() : ])

            skip_tokenize_prefix()

            return r

        return tokenize_atom__X2__newline(m)


    @share
    def tokenize_atom():
        assert qk() is none
        assert qn() is none

        j = qj()

        m = atom_match(qs(), j)

        if m is none:
            my_line('full: %r; s: %r', portray_string(qs()), portray_string(qs()[j :]))
            assert 0
            raise_unknown_line(1)

        if m.start('comment_newline') is not -1:
            return tokenize_atom__X__newline(m)

        atom_s = m.group('atom')

        if atom_s is not none:
            r = find_atom_type(atom_s[0])(atom_s)

            if qi() != j:
                r = r.prefix_meta(conjure_whitespace(qs()[qi() : j]), r)

            wi(m.end('atom'))
            wj(m.end())

            return r

        quote_start = m.start('quote')
        s           = qs()

        if quote_start is not -1:
            quote_end = m.end('quote')

            r = find_atom_type(s[quote_start])(s[j : quote_end])

            if qi() != j:
                r = r.prefix_meta(conjure_whitespace(s[qi() : j]), r)

            wi(quote_end)
            wj(m.end())

            return r

        keyword_s = (m.group('keyword')) or (m.group('operator'))

        if keyword_s is not none:
            j = m.end()

            if is_close_operator(keyword_s) is 7:
                d            = qd()
                operator_end = m.end('operator')

                r = find_operator_conjure_function(keyword_s)(s[qi() : operator_end])

                if d is 0:
                    raise_unknown_line(2)

                assert d > 0

                wd(d - 1)
                wi(operator_end)
                wj(j)

                return r

            r = find_operator_conjure_function(keyword_s)(s[qi() : j])

            wi(j)
            wj(j)

            return r

        return tokenize_atom__X__left_parenthesis(m)
