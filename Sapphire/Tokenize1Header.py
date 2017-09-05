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
            raise_unknown_line(1)

        comment_newline = m.group('comment_newline')

        if comment_newline is not none:
            RP__colon__start = m.start('right_parenthesis__colon')

            if RP__colon__start is not -1:
                RP__start = m.start('right_parenthesis')

                return ParameterColon_0_Newline(
                           conjure_left_parenthesis (s[qi()             : RP__start       ]),
                           conjure_right_parenthesis(s[RP__start        : RP__colon__start]),
                           conjure_colon_newline    (s[RP__colon__start :                 ]),
                       )

            r = conjure_left_parenthesis(s[qi() : ])

            wd1()
            skip_tokenize_prefix()

            return r

        if m.end('right_parenthesis__colon') is not -1:
            raise_unknown_line(1)

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
                raise_unknown_line(1)

            wd0()

            return RightParenthesis_Colon_Newline(
                       conjure_right_parenthesis(s[qi()                   : right_parenthesis__end]),
                       conjure_colon_newline    (s[right_parenthesis__end :                       ]),
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

        m = parameter_argument_match(s, j)

        if m is none:
            my_line(portray_string(qs()[qj() : ]))
            raise_unknown_line(1)

        name = m.group('name')

        if name is not none:
            if m.start('comment_newline') is not -1:
                raise_unknown_line(2)

            r = conjure_identifier(name)

            if qi() != j:
                r = PrefixAtom(s[qi() : j], r)

            wi(m.end('name'))
            wj(m.end())

            return r

        return tokenize_parameter_operator__X__right_parenthesis(m)

                
    @share
    def tokenize_parameter_operator():
        assert qd() is 1
        assert qk() is none
        assert qn() is none

        s = qs()

        m = parameter_operator_match(s, qj())

        if m is none:
            raise_unknown_line(1)

        comma_end = m.end('comma')

        if comma_end is not -1:
            comma_RP_end = m.end('comma_RP')

            if comma_RP_end is not -1:
                if m.start('comma_RP_colon') is not -1:
                    if m.end('comment_newline') is -1:
                        raise_unknown_line(2)

                    wd0()

                    comma_RP_start = m.start('comma_RP')

                    return Comma_RightParenthesis_Colon_Newline(
                               conjure_comma            (s[qi()           : comma_RP_start]),
                               conjure_right_parenthesis(s[comma_RP_start : comma_RP_end  ]),
                               conjure_colon            (s[comma_RP_end   :               ])
                           )

                raise_unknown_line(3)

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