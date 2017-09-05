#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1Function')
def gem():
    @share
    def parse1_statement_class_header(m):
        if m.end('newline') is not -1:
            raise_unknown_line(1)

        keyword_class = KeywordClass(m.group())

        j = m.end()

        wi(j)
        wj(j)

        #
        #<name>
        #
        name = tokenize_name()

        if qn() is not none:
            raise_unknown_line(1)
        #</name>

        operator_1 = tokenize_header_parenthesis_atom()

        if operator_1.is_any_parameter_colon_0:
            if qn() is not none:
                raise_unknown_line(2)

            return ClassHeader(keyword_class, name, operator_1)

        if not operator_1.is_left_parenthesis:
            raise_unknown_line(3)

        #
        #<parameter_1>
        #
        parameter_1 = tokenize_name()

        if qn() is not none:
            raise_unknown_line(4)
        #</parameter_1>

        operator_2 = tokenize_parameter_operator()

        if not operator_2.is__any__right_parenthesis__colon__newline:
            my_line('operator_2: %s', operator_2)
            raise_unknown_line(5)

        if qn() is not none:
            raise_unknown_line(6)
            
        return ClassHeader(
                   keyword_class,
                   name,
                   ParameterColon_1(operator_1, parameter_1, operator_2),
               )


    @share
    def parse1_statement_function_header(m):
        if m.end('newline') is not -1:
            raise_unknown_line(1)

        keyword_function = KeywordFunction(m.group())

        j = m.end()

        wi(j)
        wj(j)

        #
        #<name>
        #
        name = tokenize_name()

        if qn() is not none:
            raise_unknown_line(1)
        #</name>

        operator_1 = tokenize_header_parenthesis_atom()

        if operator_1.is_any_parameter_colon_0:
            if qn() is not none:
                raise_unknown_line(2)

            return FunctionHeader(keyword_function, name, operator_1)

        if not operator_1.is_left_parenthesis:
            raise_unknown_line(3)

        #
        #<parameter_1>
        #
        token_1 = tokenize_parameter_atom()

        if qn() is not none:
            raise_unknown_line(4)
        #</parameter_1>

        if token_1.is__right_parenthesis__colon__newline:
            return FunctionHeader(
                       keyword_function,
                       name,
                       Comma_RightParenthesis_Colon_Newline(operator_1, token_1.first, token_1.second),
                    )

        if not token_1.is_atom:
            raise_unknown_line(5)

        operator_2 = tokenize_parameter_operator()

        if operator_2.is__any__right_parenthesis__colon__newline:
            if qn() is not none:
                raise_unknown_line(6)
                
            return FunctionHeader(
                       keyword_function,
                       name,
                       ParameterColon_1(operator_1, token_1, operator_2),
                   )

        if operator_2.is_equal_sign:
            value = parse1_expression()

            token_1 = KeywordParameter(token_1, operator_2, value)

            operator_2 = qk()
            wk(none)

            if operator_2 is none:
                raise_unknown_line(7)

        if not operator_2.is_comma:
            raise_unknown_line(8)

        token_7 = tokenize_parameter_atom()

        if qn() is not none:
            raise_unknown_line(9)

        if token_7.is__right_parenthesis__colon__newline:
            return FunctionHeader(
                       keyword_function,
                       name,
                       ParameterColon_1(
                           operator_1,
                           token_1, 
                           Comma_RightParenthesis_Colon_Newline(operator_2, token_7.first, token_7.second),
                       ),
                   )

        if not token_7.is_atom:
            raise_unknown_line(10)

        many = [operator_1, token_1, operator_2, token_7]

        while 7 is 7:
            operator_7 = tokenize_parameter_operator()

            if operator_7.is__any__right_parenthesis__colon__newline:
                if qn() is not none:
                    raise_unknown_line(11)
                    
                many.append(operator_7)

                return FunctionHeader(keyword_function, name, ParameterColon_Many(Tuple(many)))

            if not operator_7.is_comma:
                raise_unknown_line(12)

            token_7 = tokenize_parameter_atom()

            if qn() is not none:
                raise_unknown_line(13)

            if token_7.is__right_parenthesis__colon__newline:
                many.append(Comma_RightParenthesis_Colon_Newline(operator_7, token_7.first, token_7.second))

                return FunctionHeader(keyword_function, name, ParameterColon_Many(Tuple(many)))

            if not token_7.is_atom:
                raise_unknown_line(14)

            many.append(operator_7)
            many.append(token_7)
