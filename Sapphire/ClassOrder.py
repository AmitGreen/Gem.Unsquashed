#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.CLASS_ORDER')
def gem():
    share(
        'CLASS_ORDER__ATOM',                         1,     #   Atom

        'CLASS_ORDER__NORMAL_TOKEN',                 2,     #   Normal token
        'CLASS_ORDER__ARGUMENT_0',                   3,     #   Arguments_0 token
        'CLASS_ORDER__PARAMETERS_0',                 4,     #   Parameters_0 token
        'CLASS_ORDER__INDENTATION',                  5,     #   Indentation token
        'CLASS_ORDER__LINE_MARKER',                  6,     #   LineMarker token
        'CLASS_ORDER__EMPTY_LINE',                   7,     #   EmptyLine token
        'CLASS_ORDER__COMMENT_LINE',                 8,     #   CommentLine token
        'CLASS_ORDER__JOIN_TOKEN',                   9,     #   Join token

        'CLASS_ORDER__FRILL_2',                     10,     #   Dual_Frill
        'CLASS_ORDER__FRILL_MANY',                  11,     #   Frill_Many
        'CLASS_ORDER__BOOKCASE_MANY_FRILL',         12,     #   BookcaseManyFrill

        'CLASS_ORDER__ARGUMENTS_1',                 20,     #   Arguments_1
        'CLASS_ORDER__ARGUMENTS_2',                 21,     #   Arguments_2
        'CLASS_ORDER__ARGUMENTS_MANY',              22,     #   Arguments_Many
        'CLASS_ORDER__MEMBER_EXPRESSION',           23,     #   Member expression
        'CLASS_ORDER__PARENTHESIZED_EXPRESSION',    24,     #   Parenthesized expression
        'CLASS_ORDER__CALL_EXPRESSION',             25,     #   Call expression
        'CLASS_ORDER__INDEX_EXPRESSION',            26,     #   Index expression
        'CLASS_ORDER__MULTIPLY_EXPRESSION',         27,     #   * expression
        'CLASS_ORDER__ARITHMETIC_1',                28,     #   + expression
        'CLASS_ORDER__ARITHMETIC_MANY',             20,     #   + expression
        'CLASS_ORDER__LOGICAL_OR_1',                30,     #   | expression
        'CLASS_ORDER__LOGICAL_OR_MANY',             31,     #   | expression, many
        'CLASS_ORDER__TERNARY_EXPRESSION',          32,     #   ?: expression
        'CLASS_ORDER__TUPLE_OF_EXPRESSION',         33,     #   Tuple of expressions

        'CLASS_ORDER__SUITE',                       40,     #   Suite
    )
