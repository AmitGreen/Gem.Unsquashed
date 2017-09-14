#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Tokenize1Atom')
def gem():
    show = 7


    #
    #   Note:
    #       Below a few tests of 'i == j' (or the equivalent 'qi() = qj()').
    #
    #       None of these tests can be optimized to 'i is j' since [the original] 'i' & 'j' could have been created
    #       with two different calls, such as:
    #
    #           1.  m.end('atom'); .vs.
    #           2.  m.end()
    #
    #       with 'ow' is empty -- and thus have the same value (but different internal addresses).
    #
    #   Note #2:
    #       The previous note also applies to tests like 'qi() != j', cannot replace this with 'qi() is not j'
    #
    @share
    def analyze_atom(m):
        if m.start('comment_newline') is -1:
            atom_s = m.group('atom')

            if atom_s is not none:
                conjure = lookup_keyword_conjure_function(atom_s)

                if conjure is not none:
                    j = m.end()

                    r = conjure(qs()[qi() : j])

                    wi(j)
                    wj(j)

                    return r

                r = find_atom_type(atom_s[0])(atom_s)

                if qi() != qj():
                    prefix = qs()[qi() : qj()]

                    r = r.prefix_meta(
                            (conjure_whitespace_line   if '\n' in prefix else   conjure_whitespace)(prefix),
                            r,
                        )

                wi(m.end('atom'))
                wj(m.end())

                return r

            operator_s = m.group('operator')

            if operator_s is not none:
                s = qs()

                if is_close_operator(operator_s) is 7:
                    d            = qd()
                    operator_end = m.end('operator')

                    r = conjure_operator(operator_s, s[qi() : operator_end])

                    if d is 0:
                        raise_unknown_line()

                    assert d > 0

                    wd(d - 1)
                    wi(operator_end)
                    wj(m.end())

                    return r

                j = m.end()

                r = conjure_operator(operator_s, s[qi() : j])

                wi(j)
                wj(j)

                return r

            #
            #<similiar-to: 'left_{brace,square_bracket}__end' below>
            #
            #   Differences:
            #       Uses '*parenthesis' instead of '*{brace,square_bracket}'
            #       Uses 'EmptyTuple' instead of 'Empty{Map,List}'
            #
            left_parenthesis__end = m.end('left_parenthesis__ow')

            if left_parenthesis__end is not -1:
                left_parenthesis       = conjure_left_parenthesis(qs()[qi() : left_parenthesis__end])
                right_parenthesis__end = m.end('right_parenthesis')

                if right_parenthesis__end is not -1:
                    wi(right_parenthesis__end)
                    wj(m.end())

                    return conjure_empty_tuple(
                               left_parenthesis,
                               conjure_right_parenthesis(m.group('right_parenthesis')),
                           )

                j = m.end()

                wd(qd() + 1)
                wi(j)
                wj(j)

                return left_parenthesis
            #</similiar-to>

            #
            #<similiar-to: 'left_parenthesis__end' above>
            #
            #   Differences:
            #       Uses '*brace' instead of '*parenthesis'
            #       Uses 'EmptyMap' instead of 'EmptyTuple'
            #
            left_brace__end = m.end('left_brace__ow')

            if left_brace__end is not -1:
                left_brace       = conjure_left_brace(qs()[qi() : left_brace__end])
                right_brace__end = m.end('right_brace')

                if right_brace__end is not -1:
                    wi(right_brace__end)
                    wj(m.end())

                    return conjure_empty_map(left_brace, conjure_right_brace(m.group('right_brace')))

                j = m.end()

                wd(qd() + 1)
                wi(j)
                wj(j)

                return left_brace
            #</similiar-to>

            #
            #<similiar-to: 'left_parenthesis__end' above>
            #
            #   Differences:
            #       Uses '*square_bracket' instead of '*parenthesis'
            #       Uses 'EmptyMap' instead of 'EmptyTuple'
            #
            left_square_bracket__end = m.end('left_square_bracket__ow')

            if left_square_bracket__end is not -1:
                left_square_bracket       = conjure_left_square_bracket(qs()[qi() : left_square_bracket__end])
                right_square_bracket__end = m.end('right_square_bracket')

                if right_square_bracket__end is not -1:
                    wi(right_square_bracket__end)
                    wj(m.end())

                    return conjure_empty_list(
                               left_square_bracket,
                               conjure_right_square_bracket(m.group('right_square_bracket')),
                           )

                j = m.end()

                wd(qd() + 1)
                wi(j)
                wj(j)

                #my_line('d: %d; left_square_bracket: %r', qd(), left_square_bracket)
                return left_square_bracket
            #</similiar-to>

            quote_start = m.start('quote')

            if quote_start is not -1:
                quote_end = m.end('quote')
                j         = qj()
                s         = qs()

                r = find_atom_type(s[quote_start])(s[j : quote_end])

                if qi() != j:
                    prefix = s[qi() : j]

                    r = r.prefix_meta(
                            (conjure_whitespace_line   if '\n' in prefix else   conjure_whitespace)(prefix),
                            r,
                        )

                wi(quote_end)
                wj(m.end())

                return r

            raise_unknown_line()

        #
        #   Newline
        #
        atom_s = m.group('atom')

        if atom_s is not none:
            conjure = lookup_keyword_conjure_function(atom_s)

            if conjure is not none:
                if qd() is 0:
                    atom_end = m.end('atom')

                    r = conjure(atom_s)(qs()[qi() : atom_end])

                    wn(conjure_token_newline(s[atom_end : ]))

                    return r

                r = conjure(atom_s)(qs()[qi() : ])

                skip_tokenize_prefix()

                return r

            r = find_atom_type(atom_s[0])(atom_s)

            #
            #<similiar-to: {quote_s} below>
            #
            #   Differences:
            #
            #       Uses "m.end('atom')" instead of "quote_end"
            #       Uses "qs()" intead of "s"
            #
            if qd() is not 0:
                suffix = conjure_whitespace_line(qs()[m.end('atom') : ])

                if qi() == qj():
                    r = r.suffix_meta(r, suffix)
                else:
                    prefix = qs()[qi() : qj()]

                    r = r.bookcase_meta(
                            (conjure_whitespace_line   if '\n' in prefix else   conjure_whitespace)(prefix),
                            r,
                            suffix,
                        )

                skip_tokenize_prefix()

                return r

            wn(conjure_token_newline(qs()[m.end('atom') : ]))

            if qi() == qj():
                return r

            prefix = qs()[qi() : qj()]

            return r.prefix_meta(
                       (conjure_whitespace_line   if '\n' in prefix else   conjure_whitespace)(prefix),
                       r,
                   )
            #</similiar-to>

        operator_s = m.group('operator')

        if operator_s is not none:
            if is_close_operator(operator_s) is 7:
                d = qd()

                if d is 1:
                    operator_end = m.end('operator')
                    s            = qs()

                    r = conjure_operator(operator_s, s[qi() : operator_end])

                    wd0()
                    wn(conjure_token_newline(s[operator_end : ]))

                    return r

                wd(d - 1)

                r = conjure_operator__with_newlines(operator_s, qs()[qi() : ])

                skip_tokenize_prefix()

                return r

            if qd() is 0:
                operator_end = m.end('operator')

                s = qs()

                r = conjure_operator(operator_s, s[qi() : operator_end])

                wn(conjure_token_newline(s[operator_end : ]))

                return r

            r = conjure_operator__with_newlines(operator_s, qs()[qi() : ])

            skip_tokenize_prefix()

            return r

        #
        #<same-as: 'left_{brace,square_bracket}__end' below>
        #
        #   Differences:
        #       Uses '*parenthesis' instead of '*brace'
        #       Uses 'EmptyTuple' instead of 'Empty{Map,List}'
        #
        left_parenthesis__end = m.end('left_parenthesis__ow')

        if left_parenthesis__end is not -1:
            right_parenthesis__end = m.end('right_parenthesis')

            if right_parenthesis__end is not -1:
                s = qs()

                left_parenthesis = conjure_left_parenthesis(s[qi() : left_parenthesis__end])

                if qd() is 0:
                    right_parenthesis__end = m.end('right_parenthesis')

                    r = conjure_empty_tuple(
                            left_parenthesis,
                            conjure_right_parenthesis(s[left_parenthesis__end : right_parenthesis__end])
                        )

                    wn(conjure_token_newline(s[right_parenthesis__end : ]))

                    return r

                r = conjure_empty_tuple(
                        left_parenthesis,
                        conjure_right_parenthesis(s[left_parenthesis__end : ]),
                    )

                skip_tokenize_prefix()

                return r

            wd(qd() + 1)

            r = conjure_left_parenthesis__with_newlines(qs()[qi() : ])

            skip_tokenize_prefix()

            return r
        #</same-as>

        #
        #<same-as: 'left_parenthesis__end' above>
        #
        #   Differences:
        #       Uses '*brace' instead of '*parenthesis'
        #       Uses 'EmptyList' instead of 'EmptyTuple'
        #
        left_brace__end = m.end('left_brace__ow')

        if left_brace__end is not -1:
            right_brace__end = m.end('right_brace')

            if right_brace__end is not -1:
                s = qs()

                left_brace = conjure_left_brace(s[qi() : left_brace__end])

                if qd() is 0:
                    right_brace__end = m.end('right_brace')

                    r = conjure_empty_map(
                            left_brace,
                            conjure_right_brace(s[left_brace__end : right_brace__end])
                        )

                    wn(conjure_token_newline(s[right_brace__end : ]))

                    return r

                r = conjure_empty_map(
                        left_brace,
                        conjure_right_brace(s[left_brace__end : ]),
                    )

                skip_tokenize_prefix()

                return r

            wd(qd() + 1)

            r = conjure_left_brace__with_newlines(qs()[qi() : ])

            skip_tokenize_prefix()

            return r
        #</same-as>

        #
        #<same-as: 'left_parenthesis__end' above>
        #
        #   Differences:
        #       Uses '*square_bracket' instead of '*parenthesis'
        #       Uses 'EmptyList' instead of 'EmptyTuple'
        #
        left_square_bracket__end = m.end('left_square_bracket__ow')

        if left_square_bracket__end is not -1:
            right_square_bracket__end = m.end('right_square_bracket')

            if right_square_bracket__end is not -1:
                s = qs()

                left_square_bracket = conjure_left_square_bracket(s[qi() : left_square_bracket__end])

                if qd() is 0:
                    right_square_bracket__end = m.end('right_square_bracket')

                    r = conjure_empty_list(
                            left_square_bracket,
                            conjure_right_square_bracket(s[left_square_bracket__end : right_square_bracket__end])
                        )

                    wn(conjure_token_newline(s[right_square_bracket__end : ]))

                    return r

                r = conjure_empty_list(
                        left_square_bracket,
                        conjure_right_square_bracket(s[left_square_bracket__end : ]),
                    )

                skip_tokenize_prefix()

                return r

            wd(qd() + 1)

            r = conjure_left_square_bracket__with_newlines(qs()[qi() : ])

            skip_tokenize_prefix()

            return r
        #</same-as>

        quote_start = m.start('quote')

        if quote_start is not -1:
            quote_end = m.end('quote')
            s         = qs()

            #
            #   NOTE:
            #
            #       Use 'qj()' here to be sure to pick up any letters prefixing the quote, such as r'prefixed'
            #
            r = find_atom_type(s[quote_start])(s[qj() : quote_end])

            #
            #<similiar-to: {atom_s} above>
            #
            #   Differences:
            #
            #       Uses "quote_end" instead of "m.end('atom')"
            #       Uses "s" intead of "qs()"
            #
            if qd() is not 0:
                suffix = conjure_whitespace_line(s[quote_end : ])

                if qi() == qj():
                    r = r.suffix_meta(r, suffix)
                else:
                    prefix = s[qi() : qj()]

                    r = r.bookcase_meta(
                            (conjure_whitespace_line   if '\n' in prefix else   conjure_whitespace)(prefix),
                            r,
                            suffix,
                        )

                skip_tokenize_prefix()

                return r

            wn(conjure_token_newline(s[m.end('quote') : ]))

            if qi() == qj():
                return r

            prefix = s[qi() : qj()]

            return r.prefix_meta(
                       (conjure_whitespace_line   if '\n' in prefix else   conjure_whitespace)(prefix),
                       r,
                   )
            #</similiar-to>

        raise_unknown_line()
