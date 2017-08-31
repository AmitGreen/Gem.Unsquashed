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
    def parse1_arguments__left_parenthesis(left_parenthesis):
        atom_1     = tokenize_nested_atom()
        operator_1 = tokenize_argument1_operator()

        if operator_1.is_right_parenthesis:
            return Arguments_1(left_parenthesis, atom_1, operator_1)

        if operator_1.is_comma:
            atom_2     = tokenize_atom()
            operator_2 = tokenize_argument7_operator()

            if operator_2.is_right_parenthesis:
                return Arguments_2(left_parenthesis, atom_1, operator_1, atom_2, operator_2)

            raise_unknown_line(2)

        raise_unknown_line(3)
