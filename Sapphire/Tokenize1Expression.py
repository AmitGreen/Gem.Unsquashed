#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Tokenize1Expression')
def gem():
    show = 0


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
            my_line('%s', portray_string(s[j : ]))
            raise_unknown_line(1)

        atom_s = m.group('atom')

        if atom_s is not none:
            #
            #<different-from: tokenize_atom>
            #
            conjure = find_atom_type(atom_s[0])

            if conjure is conjure_right_parenthesis:
                if m.start('comment_newline') is -1:
                    j = m.end()

                    wi(j)
                    wj(j)

                    return conjure_right_parenthesis(s[qi() : j])

                atom_end = m.end('atom')

                wn(conjure_token_newline(s[atom_end : ]))

                return conjure_right_parenthesis(s[qi() : atom_end])
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
            #my_line('%s', portray_string(s[j : ]))
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


    def skip_tokenize_prefix():
        parse_context.iterate_lines.next()

        m = next_nested_line_match(qs())

        if m is none:
            raise_unknown_line(1)

        if m.group('comment_newline') is not none:
            raise_unknown_line(2)

        wj(m.end())


    @share
    def tokenize_operator():
        s = qs()
        m = operator_match(s, qj())

        if m is none:
            #my_line('%s', portray_raw_string(s[qj() : ]))
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
                r = conjure(s[qi() : j])

                wi(j)
                wj(j)

                return r

            d = qd()

            if d is 0:
                if conjure is conjure_colon:
                    return conjure_colon_newline(s[qi() : ])

                operator_end = m.end('operator')
                wn(conjure_token_newline(s[operator_end : ]))

                return conjure(s[qi():operator_end])

            if conjure is conjure_right_parenthesis:
                if d is 1:
                    i = m.end('operator')

                    wd(0)
                    wn(conjure_token_newline(s[i : ]))

                    return conjure_right_parenthesis(s[qi() : i])

                wd(d - 1)

            r = conjure(s[qi() : ])

            skip_tokenize_prefix()

            return r

        left_parenthesis__ow__end = m.end('left_parenthesis__ow')
        right_parenthesis         = m.group('right_parenthesis')

        if right_parenthesis is not none:
            left_parenthesis = conjure_left_parenthesis(s[qi() : left_parenthesis__ow__end])

            if m.end('comment_newline') is -1:
                right_parenthesis = conjure_right_parenthesis(right_parenthesis)

                wi(m.end('right_parenthesis'))
                wj(m.end())
            else:
                if qd() is 0:
                    right_parenthesis = conjure_right_parenthesis(right_parenthesis)

                    wn(conjure_token_newline(s[m.end('right_parenthesis') : ]))
                else:
                    right_parenthesis = conjure_right_parenthesis(s[left_parenthesis__ow__end : ])

                    skip_tokenize_prefix()

            return Arguments_0(left_parenthesis, right_parenthesis)

        if m.end('comment_newline') is -1:
            left_parenthesis = conjure_left_parenthesis(s[qi() : left_parenthesis__ow__end])

            j = m.end()

            wd(qd() + 1)
            wi(j)
            wj(j)

            return left_parenthesis

        left_parenthesis = conjure_left_parenthesis(s[qi() : ])

        skip_tokenize_prefix()

        wd(qd() + 1)

        if show is 7:
            my_line('%r; %s', left_parenthesis, portray_string(s[qj() : ]))

        return left_parenthesis
