#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1Call')
def gem():
    show = 0


    require_gem('Sapphire.Tokenize1Expression')


    @share
    def parse1_expression_call(left, left_parenthesis):
        return ExpressionCall(left, parse1_arguments__left_parenthesis(left_parenthesis))


    @share
    def parse_argument7(left):
        while 7 is 7:
            operator = tokenize_argument_operator()

            if operator.is_left_parenthesis:
                left = parse1_expression_call(left, operator)
                continue

            if operator.is_right_parenthesis:
                wk(operator)

                return left

            raise_unknown_line(1)

    
    @share
    def parse1_arguments__left_parenthesis(left_parenthesis):
        atom = tokenize_nested_atom()

        while 7 is 7:
            operator = tokenize_argument_operator()

            if operator.is_left_parenthesis:
                atom = parse1_arguments__left_parenthesis(operator)
                continue

            if operator.is_right_parenthesis:
                return Arguments_1(left_parenthesis, atom, operator)

            if operator.is_comma:
                break

            raise_unknown_line(1)

        atom_2     = tokenize_nested_atom()
        atom_2     = parse_argument7(atom_2)
        operator_2 = qk()

        if operator_2.is_right_parenthesis:
            return Arguments_2(left_parenthesis, atom, operator, atom_2, operator_2)

        #line('%s: operator_1: %r', my_name(), operator_1)
        raise_unknown_line(2)
