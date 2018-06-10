#
#   Copyright (c) 2017-2018 Amit Green.  All rights reserved.
#
@gem('Pearl.ClassOrder')
def gem():
    export(
        'CLASS_ORDER__NORMAL_TOKEN',                     1,     #   Normal token
        'CLASS_ORDER__ARGUMENT_0',                       2,     #   Arguments_0 token
        'CLASS_ORDER__PARAMETERS_0',                     3,     #   Parameters_0 token
        'CLASS_ORDER__INDENTATION',                      4,     #   Indentation token
        'CLASS_ORDER__LINE_MARKER',                      5,     #   LineMarker token
        'CLASS_ORDER__EMPTY_LINE',                       6,     #   EmptyLine token
        'CLASS_ORDER__COMMENT_LINE',                     7,     #   CommentLine token
        'CLASS_ORDER__COMMENT_LINE__STRING',             8,     #   CommentLine token, inherited from String

        'CLASS_ORDER__FRILL_2',                         10,     #   Commented_V_Frill & VW_Frill
        'CLASS_ORDER__FRILL_MANY',                      11,     #   Frill_Many
        'CLASS_ORDER__BOOKCASE_MANY_FRILL',             12,     #   BookcaseManyFrill

        'CLASS_ORDER__BINARY_EXPRESSION',               20,     #   * expression
        'CLASS_ORDER__BOOKCASE_DUAL_EXPRESSION',        21,     #   BookcaseDualExpression+
        'CLASS_ORDER__BOOKCASE_EXPRESSION',             22,     #   BookcaseExpression+
        'CLASS_ORDER__BOOKCASE_MANY_EXPRESSION',        23,     #   BookcaseManyExpression+
        'CLASS_ORDER__BOOKCASE_TRIPLE_EXPRESSION',      24,     #   BookcaseTripleExpression+
        'CLASS_ORDER__CALL_STATEMENT',                  25,     #   CallStatementBase+
        'CLASS_ORDER__DEFINITION_HEADER',               26,     #   DefinitionHeader+
        'CLASS_ORDER__DUAL_TWIG',                       27,     #   DualTwig
        'CLASS_ORDER__MANY_EXPRESSION',                 28,     #   + expression
        'CLASS_ORDER__MEMBER_EXPRESSION',               29,     #   Member expression
        'CLASS_ORDER__QUADRUPLE_TWIG',                  30,     #   Commented_VWX_Frill & VWXY_Frill
        'CLASS_ORDER__TRIPLE_EXPRESSION',               31,     #   ?: expression
        'CLASS_ORDER__TRIPLE_TWIG',                     32,     #   Commented_VW_Frill & VWX_Frill
        'CLASS_ORDER__TUPLE',                           33,     #   Tuple of expressions
        'CLASS_ORDER__UNARY_EXPRESSION',                34,     #   * expression
    )
