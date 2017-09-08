#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Tokenize1Operator')
def gem():
    show = 0


    @share
    def skip_tokenize_prefix():
        parse_context.iterate_lines.next()

        m = next_nested_line_match(qs())

        if m is none:
            raise_unknown_line(1)

        if m.group('comment_newline') is none:
            wj(m.end())
            return

        many = [qs()]

        while 7 is 7:
            parse_context.iterate_lines.next()

            s = qs()
            m = next_nested_line_match(s)

            if m is none:
                raise_unknown_line(2)

            if m.group('comment_newline') is none:
                prefix = ''.join(many)
                total  = length(prefix)

                ws(prefix + s)
                wj(total + m.end())

                return

            many.append(s)


    @share
    def tokenize_operator():
        s = qs()

        if show is 7:
            my_line('d: %d; s: %s', qd(), portray_string(s[qj() : ]))

        m = operator_match(s, qj())

        if m is none:
            my_line(portray_string(s[qj() : ]))
            raise_unknown_line(1)

        if m.end('comment_newline') is -1:
            operator_s = m.group('operator')

            if operator_s is not none:
                if is_close_operator(operator_s) is 7:
                    d = qd()

                    if d is 0:
                        raise_unknown_line(2)

                    operator_end = m.end('operator')

                    r = find_operator_conjure_function(operator_s)(s[qi() : operator_end])

                    wd(d - 1)
                    wi(operator_end)
                    wj(m.end())

                    return r

                j = m.end()
                r = find_operator_conjure_function(operator_s)(s[qi() : j])

                wi(j)
                wj(j)

                return r

            #
            #<similiar-to: {left_square_bracket__ow} below>
            #
            #   Differences:
            #       Uses *parenthesis* instead of *square_bracket*
            #
            left_end = m.end('left_parenthesis__ow')

            if left_end is not -1:
                left    = conjure_left_parenthesis(s[qi() : left_end])
                RP_s = m.group('right_parenthesis')

                if RP_s is not none:
                    right = conjure_right_parenthesis(RP_s)

                    wi(m.end('right_parenthesis'))
                    wj(m.end())

                    return Arguments_0(left, right)

                j = m.end()

                wd(qd() + 1)
                wi(j)
                wj(j)

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
                r = find_operator_conjure_function(keyword_s)(s[qi() : j])

                wi(j)
                wj(j)

                return r

            raise_unknown_line(3)


        #
        #   Newline version
        #
        operator_s = m.group('operator')

        if operator_s is not none:
            conjure = find_operator_conjure_function(operator_s)

            d = qd()

            if d is 0:
                if conjure is conjure_colon:
                    return conjure_colon_newline(s[qi() : ])

                operator_end = m.end('operator')
                wn(conjure_token_newline(s[operator_end : ]))

                return conjure(s[qi():operator_end])

            if is_close_operator(operator_s) is 7:
                if d is 1:
                    i = m.end('operator')

                    wd0()
                    wn(conjure_token_newline(s[i : ]))

                    return conjure(s[qi() : i])

                wd(d - 1)

            r = conjure(s[qi() : ])

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

                return Arguments_0(left, right)

            left = conjure_left_parenthesis(s[qi() : ])

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
            if qd() is 0:
                keyword_end = m.end('keyword')

                r = find_operator_conjure_function(keyword_s)(s[qi() : keyword_end])

                wn(conjure_token_newline(s[keyword_end : ]))

                return r

            r = find_operator_conjure_function(keyword_s)(s[qi() : ])

            skip_tokenize_prefix()

            return r

        raise_unknown_line(4)
