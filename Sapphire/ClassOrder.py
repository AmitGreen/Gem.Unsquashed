#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.CLASS_ORDER')
def gem():
    share(
        'CLASS_ORDER__ATOM',                         1,      #   Atom

        'CLASS_ORDER__NORMAL_TOKEN',                 2,      #   Normal token
        'CLASS_ORDER__ARGUMENT_0',                   3,      #   Arguments_0 token
        'CLASS_ORDER__PARAMETERS_0',                 4,      #   Parameters_0 token
        'CLASS_ORDER__INDENTATION',                  5,      #   Indentation token
        'CLASS_ORDER__LINE_MARKER',                  6,      #   LineMarker token
        'CLASS_ORDER__EMPTY_LINE',                   7,      #   EmptyLine token
        'CLASS_ORDER__COMMENT_LINE',                 8,      #   CommentLine token
        'CLASS_ORDER__JOIN_TOKEN',                   9,      #   Join token

        'CLASS_ORDER__DUAL_FRILL',                  10,      #   Dual Frill

        'CLASS_ORDER__ARGUMENTS_1',                 11,      #   Arguments_1
        'CLASS_ORDER__ARGUMENTS_2',                 12,      #   Arguments_2
        'CLASS_ORDER__MEMBER_EXPRESSION',           13,      #   Member expression
        'CLASS_ORDER__PARENTHESIZED_EXPRESSION',    14,      #   Parenthesized expression
        'CLASS_ORDER__CALL_EXPRESSION',             15,      #   Call expression
        'CLASS_ORDER__MULTIPLY_EXPRESSION',         16,      #   Multiply expression
        'CLASS_ORDER__ARITHMETIC_EXPRESSION',       17,      #   Arithmetic expression

        'CLASS_ORDER__SUITE',                       18,      #   Suite
    )
