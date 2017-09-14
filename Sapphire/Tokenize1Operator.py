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
            my_line(portray_string(s[qj() : ]))
            raise_unknown_line()

        if m.end('comment_newline') is -1:
            operator_s = m.group('operator')

            if operator_s is not none:
                if is_close_operator(operator_s) is 7:
                    d = qd()

                    if d is 0:
                        my_line('d: %d; operator_s: %r; s: %s', d, operator_s, portray_string(s[qj() : ]))
                        raise_unknown_line()

                    operator_end = m.end('operator')

                    full = s[qi() : operator_end]

                    r = (find_lookup_operator(operator_s)(full)) or (find_insert_operator(operator_s)(full))

                    wd(d - 1)
                    wi(operator_end)
                    wj(m.end())

                    return r

                j = m.end()

                full = s[qi() : j]

                r = (find_lookup_operator(operator_s)(full)) or (find_insert_operator(operator_s)(full))

                wi(j)
                wj(j)

                return r

            #
            #<similiar-to: '{keyword_is,left_square_bracket}__ow' below>
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
                left    = conjure_left_parenthesis(s[qi() : left_end])
                right_s = m.group('right_parenthesis')

                if right_s is not none:
                    right = conjure_right_parenthesis(right_s)

                    wi(m.end('right_parenthesis'))
                    wj(m.end())

                    return conjure_arguments_0(left, right)

                j = m.end()

                wd(qd() + 1)
                wi(j)
                wj(j)

                return left
            #</similiar-to>

            #
            #<similiar-to: {left_parenthesis__ow} above>
            #
            #   Differences:
            #       Uses *square_bracket* instead of *parenthesis* 
            #       Uses EmptyIndex       instead of Arguments_0
            #
            left_end = m.end('left_square_bracket__ow')

            if left_end is not -1:
                left    = conjure_left_square_bracket(s[qi() : left_end])
                RSB_s = m.group('right_square_bracket')

                if RSB_s is not none:
                    right = conjure_right_square_bracket(RSB_s)

                    wi(m.end('right_square_bracket'))
                    wj(m.end())

                    return EmptyIndex(left, right)

                j = m.end()

                wd(qd() + 1)
                wi(j)
                wj(j)

                return left
            #</similiar-to>

            keyword_s = m.group('keyword')

            if keyword_s is not none:
                j = m.end()

                full = s[qi() : j]

                r = (find_lookup_operator(keyword_s)(full)) or (find_insert_operator(keyword_s)(full))

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
                left    = conjure_keyword_is(s[qi() : left_end])
                right_s = m.group('is_not')

                if right_s is not none:
                    j = m.end()

                    wi(j)
                    wj(j)

                    return conjure_is_not(left, conjure_keyword_not(right_s))

                j = m.end()

                wi(j)
                wj(j)

                return left
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
                left    = conjure_keyword_not(s[qi() : left_end])
                right_s = m.group('not_in')

                if right_s is not none:
                    j = m.end()

                    wi(j)
                    wj(j)

                    return conjure_not_in(left, conjure_keyword_in(right_s))

                j = m.end()

                wi(j)
                wj(j)

                return left
            #</similiar-to>

            raise_unknown_line()


        #
        #   Newline version
        #
        operator_s = m.group('operator')

        if operator_s is not none:
            lookup = find_lookup_operator(operator_s)

            d = qd()

            if d is 0:
                if lookup is lookup_colon:
                    return conjure_colon_python_newline(s[qi() : ])

                operator_end = m.end('operator')
                wn(conjure_token_newline(s[operator_end : ]))

                full = s[qi() : operator_end]

                return (lookup(full)) or (find_insert_operator(operator_s)(full))

            if is_close_operator(operator_s) is 7:
                if d is 1:
                    i = m.end('operator')

                    wd0()
                    wn(conjure_token_newline(s[i : ]))

                    full = s[qi() : i]

                    return (lookup(full)) or (find_insert_operator(operator_s)(full))

                wd(d - 1)

            full = s[qi() : ]

            r = (lookup(full)) or (find_insert_operator_with_newline(operator_s)(full))

            skip_tokenize_prefix()

            return r

        #
        #<similiar-to: {left_square_bracket__ow} below>
        #
        #   Differences:
        #       Uses *parenthesis* instead of *square_bracket*
        #
        left_end = m.end('left_parenthesis__ow')

        if left_end is not -1:
            right_end = m.end('right_parenthesis')

            if right_end is not -1:
                left = conjure_left_parenthesis(s[qi() : left_end])

                if qd() is 0:
                    right = conjure_right_parenthesis(s[left_end : right_end])

                    wn(conjure_token_newline(s[right_end : ]))
                else:
                    right = conjure_right_parenthesis(s[left_end : ])

                    skip_tokenize_prefix()

                return conjure_arguments_0(left, right)

            left = conjure_left_parenthesis__with_newline(s[qi() : ])

            skip_tokenize_prefix()

            wd(qd() + 1)

            return left
        #</similiar-to>

        #
        #<similiar-to: {left_parenthesis__ow} below>
        #
        #   Differences:
        #       Uses *square_bracket* instead of *parenthesis* 
        #
        left_end = m.end('left_square_bracket__ow')

        if left_end is not -1:
            right_end = m.end('right_square_bracket')

            if right_end is not -1:
                left = conjure_left_square_bracket(s[qi() : left_end])

                if qd() is 0:
                    right = conjure_right_square_bracket(s[left_end : right_end])

                    wn(conjure_token_newline(s[right_end : ]))
                else:
                    right = conjure_right_square_bracket(s[left_end : ])

                    skip_tokenize_prefix()

                return EmptyIndex(left, right)

            left = conjure_left_square_bracket(s[qi() : ])

            skip_tokenize_prefix()

            wd(qd() + 1)

            return left
        #</similiar-to>

        keyword_s = m.group('keyword')

        if keyword_s is not none:
            lookup = find_lookup_operator(keyword_s)

            if qd() is 0:
                keyword_end = m.end('keyword')

                full = s[qi() : keyword_end]

                r = (lookup(full)) or (find_insert_operator(keyword_s)(full))

                wn(conjure_token_newline(s[keyword_end : ]))

                return r

            full = s[qi() : ]

            r = (lookup(full)) or (find_insert_operator_with_newline(keyword_s)(full))

            skip_tokenize_prefix()

            return r

        raise_unknown_line()
