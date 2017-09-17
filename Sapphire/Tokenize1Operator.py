#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Tokenize1Operator')
def gem():
    show = 0


    @share
    def skip_tokenize_prefix():
        next = next_method(parse_context.iterate_lines)

        next()

        m = next_nested_line_match(qs())

        if m is none:
            raise_unknown_line()

        if m.group('comment_newline') is none:
            wj(m.end())
            return

        many = [qs()]

        while 7 is 7:
            next()

            s = qs()
            m = next_nested_line_match(s)

            if m is none:
                raise_unknown_line()

            if m.group('comment_newline') is none:
                prefix = ''.join(many)
                total  = length(prefix)

                ws(prefix + s)
                wj(total + m.end())

                return

            many.append(s)


    @share
    def tokenize_operator():
        assert qk() is none
        assert qn() is none

        s = qs()

        if show is 7:
            my_line('d: %d; s: %s', qd(), portray_string(s[qj() : ]))

        m = operator_match(s, qj())

        if m is none:
            #my_line(portray_string(s[qj() : ]))
            raise_unknown_line()

        if m.end('comment_newline') is -1:
            operator_s = m.group('operator')

            if operator_s is not none:
                if is_close_operator(operator_s) is 7:
                    d = qd()

                    if d is 0:
                        #my_line('d: %d; operator_s: %r; s: %s', d, operator_s, portray_string(s[qj() : ]))
                        raise_unknown_line()

                    operator_end = m.end('operator')

                    r = conjure_action_word(operator_s, s[qi() : operator_end])

                    wd(d - 1)
                    wi(operator_end)
                    wj(m.end())

                    return r

                j = m.end()

                r = conjure_action_word(operator_s, s[qi() : j])

                wi(j)
                wj(j)

                return r

            #
            #<similiar-to: 'keyword_is__ow' below>
            #
            #   Differences:
            #
            #       See each of them for documented differences
            #
            #   NOTE:
            #       As this is an 'operator' the meaning of '()' must be 'Arguments_0' instead of 'Tuple_0'
            #       (Tuple_0 is an atom)
            #
            left_end = m.end('left_parenthesis__ow')

            if left_end is not -1:
                right_end = m.end('right_parenthesis')

                if right_end is not -1:
                    r = conjure_arguments_0(left_end, right_end)

                    wi(m.end('right_parenthesis'))
                    wj(m.end())

                    return r

                left = conjure_left_parenthesis(s[qi() : left_end])

                wd(qd() + 1)
                wi(left_end)
                wj(left_end)

                return left
            #</similiar-to>

            left_end = m.end('left_square_bracket__ow')

            if left_end is not -1:
                left            = conjure_left_square_bracket(s[qi() : left_end])
                tail_index__end = m.end('tail_index__ow')

                if tail_index__end is not -1:
                    colon   = conjure_colon(s[left_end : tail_index__end])
                    RSB_end = m.end('right_square_bracket')

                    if RSB_end is not -1:
                        j = m.end()

                        wi(RSB_end)
                        wj(j)

                        return conjure_all_index(
                                   left,
                                   colon,
                                   conjure_right_square_bracket(s[tail_index__end : RSB_end]),
                                )

                    wd(qd() + 1)
                    wi(tail_index__end)
                    wj(m.end())

                    return conjure__left_square_bracket__colon(left, colon)

                wd(qd() + 1)
                wi(left_end)
                wj(left_end)

                return left

            if m.start('colon') is not -1:
                head_index__s = m.group('head_index')

                if head_index__s is not none:
                    d = qd()

                    if d is 0:
                        raise_unknown_line()

                    r = conjure__colon__right_square_bracket(
                            conjure_colon(s[qi() : m.start('head_index')]),
                            conjure_right_square_bracket(head_index__s),
                        )

                    wd(d - 1)
                    wi(m.end('head_index'))
                    wj(m.end())

                    return r

                j = m.end()

                r = conjure_colon(s[qi() : j])

                wi(j)
                wj(j)

                return r

            keyword_s = m.group('keyword')

            if keyword_s is not none:
                j = m.end()

                r = conjure_action_word(keyword_s, s[qi() : j])

                wi(j)
                wj(j)

                return r

            #
            #<similiar-to: {left_parenthesis__ow} above>
            #
            #   Differences:
            #       Uses keyword_is*  instead of left_parenthesis*
            #       Uses keyword_not* instead of right_parenthesis*
            #       Uses IsNot        instead of Arguments_0
            #
            #       Does not increment depth when parsing the 'is' keyword.
            #
            #   NOTE:
            #       When parsing 'is not' the whitespace after 'not' is treated as part of the 'not' keyword
            #
            #       This is different than ')', ']' & '}', none of which treat the whitespace as part of
            #       of the closing operator.
            #
            #       This subtle difference is implemented in three ways:
            #
            #           1.  By the regular pattern, which includes the whitespace as part of the 'not' keyword
            #               (but not included as part of ')', ']', and '}')
            #
            #           2.  The code below on setting 'wi' is different than the code above.
            #
            #           3.  The 'return IsNot()' statement is also optimized since it is able to use 'right_s'
            #               to construct the 'not' keyword.
            #
            left_end = m.end('keyword_is__ow')

            if left_end is not -1:
                right_end = m.end('is_not')

                if right_end is not -1:
                    r = conjure_is_not(left_end, right_end)

                    j = m.end()

                    wi(j)
                    wj(j)

                    return r

                r = conjure_keyword_is(s[qi() : left_end])

                j = m.end()

                wi(j)
                wj(j)

                return r
            #</similiar-to>


            #
            #<similiar-to: {keyword_is__ow} above>
            #
            #   Differences:
            #       Uses keyword_not* instead of keyword_is
            #       Uses keyword_in*  instead of keyword_in
            #       Uses NotIn        instead of IsNot
            #
            left_end = m.end('keyword_not__ow')

            if left_end is not -1:
                right_end = m.end('not_in')

                if right_end is not -1:
                    r = conjure_not_in(left_end, right_end)

                    j = m.end()

                    wi(j)
                    wj(j)

                    return r

                r = conjure_keyword_not(s[qi() : left_end])

                j = m.end()

                wi(j)
                wj(j)

                return r
            #</similiar-to>

            raise_unknown_line()


        #
        #   Newline version
        #
        operator_s = m.group('operator')

        if operator_s is not none:
            if is_close_operator(operator_s) is 7:
                d = qd()

                if d is 1:
                    i = m.end('operator')

                    r = conjure_action_word(operator_s, s[qi() : i])

                    wd0()
                    wn(conjure_token_newline(s[i : ]))

                    return r

                if d is 0:
                    raise_unknown_line()

                wd(d - 1)
            elif qd() is 0:
                operator_end = m.end('operator')

                r = conjure_action_word(operator_s, s[qi() : operator_end])

                wn(conjure_token_newline(s[operator_end : ]))

                return r

            r = conjure_action_word__ends_in_newline(operator_s, s[qi() : ])

            skip_tokenize_prefix()

            return r

        left_end = m.end('left_parenthesis__ow')

        if left_end is not -1:
            right_end = m.end('right_parenthesis')

            if right_end is not -1:
                d = qd()

                r = conjure_arguments_0(left_end, (right_end   if d is 0 else   none))

                if qd() is 0:
                    wn(conjure_token_newline(s[right_end : ]))
                else:
                    skip_tokenize_prefix()

                return r

            left = conjure_left_parenthesis__ends_in_newline(s[qi() : ])

            skip_tokenize_prefix()

            wd(qd() + 1)

            return left

        left_end = m.end('left_square_bracket__ow')

        if left_end is not -1:
            tail_index__end = m.end('tail_index__ow')

            if tail_index__end is not -1:
                left      = conjure_left_square_bracket(s[qi() : left_end])
                right_end = m.end('right_square_bracket')

                if right_end is not -1:
                    colon = conjure_colon(s[left_end : tail_index__end])

                    if qd() is 0:
                        right = conjure_right_square_bracket(s[tail_index__end : right_end])

                        wn(conjure_token_newline(s[right_end : ]))
                    else:
                        right = conjure_right_square_bracket(s[tail_index__end : ])

                        skip_tokenize_prefix()

                    return conjure_all_index(left, colon, right)

                left = conjure__left_square_bracket__colon(left, conjure_colon__ends_in_newline(s[left_end : ]))
            else:
                left = conjure_left_square_bracket__ends_in_newline(s[qi() : ])

            skip_tokenize_prefix()

            wd(qd() + 1)

            return left

        if m.start('colon') is not -1:
            head_index__end = m.end('head_index')

            if head_index__end is not -1:
                head_index__start = m.start('head_index')

                colon = conjure_colon(s[qi() : head_index__start])

                d = qd()

                if d is 1:
                    wd0()

                    r = conjure__colon__right_square_bracket(
                            colon,
                            conjure_right_square_bracket(s[head_index__start : head_index__end])
                        )

                    wn(conjure_token_newline(s[head_index__end : ]))

                    return r

                assert d > 1

                wd(d - 1)

                r = conjure__colon__right_square_bracket(
                        colon,
                        conjure_right_square_bracket__with_newlines(s[head_index__start : ])
                    )

                skip_tokenize_prefix()

                return r

            if qd() is 0:
                return conjure_colon__line_marker(s[qi() : ])

            r = conjure_colon__ends_in_newline(s[qi() : ])

            skip_tokenize_prefix()

            return r

        keyword_s = m.group('keyword')

        if keyword_s is not none:
            if qd() is 0:
                keyword_end = m.end('keyword')

                r = conjure_action_word(keyword_s, s[qi() : keyword_end])

                wn(conjure_token_newline(s[keyword_end : ]))

                return r

            r = conjure_action_word__ends_in_newline(keyword_s, s[qi() : ])

            skip_tokenize_prefix()

            return r

        raise_unknown_line()
