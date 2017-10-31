#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.CLASS_ORDER')
def gem():
    share(
        'CLASS_ORDER__NORMAL_TOKEN',                     2,     #   Normal token
        'CLASS_ORDER__ARGUMENT_0',                       3,     #   Arguments_0 token
        'CLASS_ORDER__PARAMETERS_0',                     4,     #   Parameters_0 token
        'CLASS_ORDER__INDENTATION',                      5,     #   Indentation token
        'CLASS_ORDER__LINE_MARKER',                      6,     #   LineMarker token
        'CLASS_ORDER__EMPTY_LINE',                       7,     #   EmptyLine token
        'CLASS_ORDER__COMMENT_LINE',                     8,     #   CommentLine token
        'CLASS_ORDER__JOIN_TOKEN',                       9,     #   Join token

        'CLASS_ORDER__FRILL_2',                         10,     #   Commented_V_Frill & VW_Frill
        'CLASS_ORDER__FRILL_MANY',                      12,     #   Frill_Many
        'CLASS_ORDER__BOOKCASE_MANY_FRILL',             13,     #   BookcaseManyFrill

        'CLASS_ORDER__BINARY_EXPRESSION',               20,     #   * expression
        'CLASS_ORDER__BOOKCASE_DUAL_EXPRESSION',        21,     #   BookcaseDualExpression+
        'CLASS_ORDER__BOOKCASE_EXPRESSION',             22,     #   BookcaseExpression+
        'CLASS_ORDER__BOOKCASE_MANY_EXPRESSION',        23,     #   BookcaseManyExpression+
        'CLASS_ORDER__DUAL_TWIG',                       24,     #   DualTwig
        'CLASS_ORDER__MANY_EXPRESSION',                 25,     #   + expression
        'CLASS_ORDER__MEMBER_EXPRESSION',               26,     #   Member expression
        'CLASS_ORDER__TRIPLE_EXPRESSION',               27,     #   ?: expression
        'CLASS_ORDER__TRIPLE_TWIG',                     28,     #   Commented_VW_Frill & VWX_Frill
        'CLASS_ORDER__TUPLE',                           29,     #   Tuple of expressions
        'CLASS_ORDER__UNARY_EXPRESSION',                30,     #   * expression
    )
