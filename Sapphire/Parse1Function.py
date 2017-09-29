#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1Function')
def gem():
    @share
    def parse1_statement_class_header(m):
        if m.end('newline') is not -1:
            raise_unknown_line()

        j = m.end()

        indented__keyword = evoke_indented_class(m.end('indented'), j)

        wi(j)
        wj(j)

        #
        #<name>
        #
        name = tokenize_name()

        if qn() is not none:
            raise_unknown_line()
        #</name>

        operator_1 = tokenize_header_parenthesis_atom()

        if operator_1.is__parameter_0__colon__line_marker:
            if qn() is not none:
                raise_unknown_line()

            return conjure_class_header(indented__keyword, name, operator_1)

        if not operator_1.is_left_parenthesis:
            raise_unknown_line()

        #
        #<parameter_1>
        #
        parameter_1 = tokenize_name()

        if qn() is not none:
            raise_unknown_line()
        #</parameter_1>

        operator_2 = tokenize_parameter_operator()

        if not operator_2.is__any__right_parenthesis__colon__newline:
            #my_line('operator_2: %s', operator_2)
            raise_unknown_line()

        if qn() is not none:
            raise_unknown_line()

        return conjure_class_header(
                   indented__keyword,
                   name,
                   conjure__parameter_1__colon__line_marker(operator_1, parameter_1, operator_2),
               )


    @share
    def parse1_statement_function_header(m):
        if m.end('newline') is not -1:
            raise_unknown_line()

        j = m.end()

        indented__keyword = evoke_indented_function(m.end('indented'), j)

        wi(j)
        wj(j)

        #
        #<name>
        #
        name = tokenize_name()

        if qn() is not none:
            raise_unknown_line()
        #</name>

        operator_1 = tokenize_header_parenthesis_atom()

        if operator_1.is__parameter_0__colon__line_marker:
            if qn() is not none:
                raise_unknown_line()

            return conjure_function_header(indented__keyword, name, operator_1)

        if not operator_1.is_left_parenthesis:
            raise_unknown_line()

        #
        #<parameter_1>
        #
        token_1 = tokenize_parameter_atom()

        if qn() is not none:
            raise_unknown_line()
        #</parameter_1>

        if token_1.is_right_parenthesis:
            raise_unknown_line()

        if token_1.is__right_parenthesis__colon__newline:
            return conjure_function_header(
                       indented__keyword,
                       name,
                       conjure__parameter_0__colon__line_marker(
                           operator_1,
                           token_1.a,
                           token_1.b,
                           token_1.c,
                       ),
                   )

        if not token_1.is_atom:
            raise_unknown_line()

        operator_2 = tokenize_parameter_operator()

        if operator_2.is_equal_sign:
            value = parse1_ternary_expression()

            token_1 = conjure_keyword_parameter(token_1, operator_2, value)

            operator_2 = qk()
            wk(none)

            if operator_2 is none:
                raise_unknown_line()

        if operator_2.is_right_parenthesis:
            [colon, line_marker] = tokenize_parameter_colon_newline()

            operator_2 = conjure__right_parenthesis__colon__line_marker(operator_2, colon, line_marker)

        if operator_2.is__any__right_parenthesis__colon__newline:
            if qn() is not none:
                raise_unknown_line()

            return conjure_function_header(
                       indented__keyword,
                       name,
                       conjure__parameter_1__colon__line_marker(operator_1, token_1, operator_2),
                   )

        if not operator_2.is_comma:
            my_line('operator_2: %r', operator_2)
            raise_unknown_line()

        token_7 = tokenize_parameter_atom()

        if qn() is not none:
            raise_unknown_line()

        if token_7.is__right_parenthesis__colon__newline:
            return conjure_function_header(
                       indented__keyword,
                       name,
                       conjure__parameter_1__colon__line_marker(
                           operator_1,
                           token_1,
                           evoke__comma__right_parenthesis__colon__line_marker(
                               operator_2,
                               token_7.a,
                               token_7.b,
                               token_7.c,
                           ),
                       ),
                   )

        if not token_7.is_atom:
            raise_unknown_line()

        many       = [token_1]
        many_frill = [operator_2]

        while 7 is 7:
            operator_7 = tokenize_parameter_operator()

            if operator_7.is_equal_sign:
                value = parse1_ternary_expression()

                token_7 = conjure_keyword_parameter(token_7, operator_7, value)

                operator_7 = qk()
                wk(none)

                if operator_7 is none:
                    raise_unknown_line()

                if operator_7.is_right_parenthesis:
                    [colon, line_marker] = tokenize_parameter_colon_newline()

                    operator_7 = conjure__right_parenthesis__colon__line_marker(operator_7, colon, line_marker)

            many.append(token_7)

            if operator_7.is__any__right_parenthesis__colon__newline:
                if qn() is not none:
                    raise_unknown_line()

                return conjure_function_header(
                           indented__keyword,
                           name,
                           conjure_parameter_colon_many(operator_1, many, many_frill, operator_7),
                       )

            if not operator_7.is_comma:
                #my_line('operator_7: %s; full_line: %r', operator_7, portray_string(qs()))
                raise_unknown_line()

            token_7 = tokenize_parameter_atom()

            if qn() is not none:
                raise_unknown_line()

            if token_7.is__right_parenthesis__colon__newline:
                return conjure_function_header(
                           indented__keyword,
                           name,
                           conjure_parameter_colon_many(
                               operator_1,
                               many,
                               many_frill,
                               conjure__comma__right_parenthesis__colon__line_marker(
                                   operator_7,
                                   token_7.a,
                                   token_7.b,
                                   token_7.c,
                               ),
                           ),
                       )

            if not token_7.is_atom:
                raise_unknown_line()

            many_frill.append(operator_7)
