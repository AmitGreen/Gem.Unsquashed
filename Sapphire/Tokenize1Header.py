#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Tokenize1Header')
def gem():
    show = 0


    @share
    def tokenize_header_parenthesis_atom():
        assert qd() is 0
        assert qk() is none
        assert qn() is none

        s = qs()

        m = header_parenthesis_match1(s, qj())

        if m is none:
            raise_unknown_line()

        right_parenthesis__start = m.start('right_parenthesis')

        if m.start('comment_newline') is not -1:
            right_parenthesis__start = m.start('right_parenthesis')

            if right_parenthesis__start is not -1:
                colon_start = m.start('colon')

                if colon_start is not -1:
                    right_parenthesis__start = m.start('right_parenthesis')

                    return ParameterColon_0_Newline(
                               conjure_left_parenthesis    (s[qi()                     : right_parenthesis__start]),
                               conjure_right_parenthesis   (s[right_parenthesis__start : colon_start             ]),
                               conjure_colon_python_newline(s[colon_start              :                         ]),
                           )

                raise_unknown_line()

            r = conjure_left_parenthesis(s[qi() : ])

            wd1()
            skip_tokenize_prefix()

            return r

        if right_parenthesis__start is not -1:
            raise_unknown_line()

        j = m.end()

        r = conjure_left_parenthesis(s[qi() : j])

        wd1()
        wi(j)
        wj(j)

        return r


    def tokenize_parameter_operator__X__right_parenthesis(m):
        s = qs()

        right_parenthesis__end = m.end('right_parenthesis')

        if m.start('colon') is not -1:
            if m.end('comment_newline') is -1:
                raise_unknown_line()

            wd0()

            return conjure__right_parenthesis__colon__python_newline(
                       conjure_right_parenthesis   (s[qi()                   : right_parenthesis__end]),
                       conjure_colon_python_newline(s[right_parenthesis__end :                       ]),
                   )

        if m.end('comment_newline') is -1:
            return conjure_right_parenthesis(s[qi() :])

        r = conjure_right_parenthesis(s[qi() : right_parenthesis__end])

        wd0()
        wi(right_parenthesis__end)
        wj(m.end())

        return r


    @share
    def tokenize_parameter_atom():
        assert qd() is 1
        assert qk() is none
        assert qn() is none

        j = qj()
        s = qs()

        m = parameter_atom_match(s, j)

        if m is none:
            my_line(portray_string(qs()[qj() : ]))
            raise_unknown_line()

        name = m.group('name')

        if name is not none:
            if m.start('comment_newline') is not -1:
                raise_unknown_line()

            r = conjure_identifier(name)

            star_end = m.end('star')

            if star_end is -1:
                if qi() != j:
                    prefix = s[qi() : j]

                    r = PrefixIdentifier(
                            (conjure_whitespace_line   if '\n' in prefix else   conjure_whitespace)(prefix),
                            r,
                        )

                wi(m.end('name'))
                wj(m.end())

                return r

            r = TupleParameter(conjure_star_sign(s[qi() : star_end]), r)

            j = m.end()

            wi(j)
            wj(j)

            return r

        return tokenize_parameter_operator__X__right_parenthesis(m)


    @share
    def tokenize_parameter_colon_newline():
        assert qd() is 0
        assert qk() is none
        assert qn() is none

        s = qs()

        m = parameter_colon_newline_match(s, qj())

        if m is none:
            raise_unknown_line()

        return conjure_colon_python_newline(s[qi() : ])


    def tokenize_nested__X__equal_sign__blankline():
        r = conjure_equal_sign(s[qi() : ])

        skip_tokenize_prefix()

        return r


    @share
    def tokenize_parameter_operator():
        assert qd() is 1
        assert qk() is none
        assert qn() is none

        s = qs()

        m = parameter_operator_match(s, qj())

        if m is none:
            raise_unknown_line()

        equal_sign__end = m.end('equal_sign')

        if equal_sign__end is not -1:
            if m.start('comment_newline') is not -1:
                return tokenize_nested__X__equal_sign__blankline()

            j = m.end()

            r = conjure_equal_sign(s[qi() : j])

            wi(j)
            wj(j)

            return r

        comma_end = m.end('comma')

        if comma_end is not -1:
            comma_RP_end = m.end('comma_RP')

            if comma_RP_end is not -1:
                if m.start('comma_RP_colon') is not -1:
                    if m.end('comment_newline') is -1:
                        raise_unknown_line()

                    wd0()

                    comma_RP_start = m.start('comma_RP')

                    return Comma_RightParenthesis_Colon_Newline(
                               conjure_comma            (s[qi()           : comma_RP_start]),
                               conjure_right_parenthesis(s[comma_RP_start : comma_RP_end  ]),
                               conjure_colon            (s[comma_RP_end   :               ])
                           )

                raise_unknown_line()

            if m.end('comment_newline') is not -1:
                r = conjure_comma(s[qi() :])

                skip_tokenize_prefix()

                return r

            j = m.end()

            r = conjure_comma(s[qi() : j])

            wi(j)
            wj(j)

            return r

        return tokenize_parameter_operator__X__right_parenthesis(m)
