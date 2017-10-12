#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Priority')
def gem():
    share(
        'PRIORITY_ATOM',                     0,     #   . () and []
        'PRIORITY_POSTFIX',                  1,     #   . () and []
        'PRIORITY_POWER',                    2,     #   **
        'PRIORITY_UNARY',                    3,     #   ~ unary- 
        'PRIORITY_MULTIPLY',                 4,     #   *
        'PRIORITY_ARITHMETIC',               5,     #   +
        'PRIORITY_SHIFT',                    6,     #   << and >>
        'PRIORITY_LOGICAL_AND',              7,     #   &
        'PRIORITY_LOGICAL_EXCLUSIVE_OR',     8,     #   ^
        'PRIORITY_LOGICAL_OR',               9,     #   |
        'PRIORITY_NORMAL_LIST',             10,     #   Comma expression of PRIORITY_LOGICAL_OR
        'PRIORITY_COMPARE',                 11,     #   ==
        'PRIORITY_NOT',                     12,     #   not
        'PRIORITY_BOOLEAN_AND',             13,     #   'and'
        'PRIORITY_BOOLEAN_OR',              14,     #   'or'
        'PRIORITY_TERNARY',                 15,     #   'if'
        'PRIORITY_TERNARY_LIST',            16,     #   Comma expression of PRIORITY_TERNARY
        'PRIORITY_YIELD',                   17,     #   'yield'
        'PRIORITY_COMPREHENSION',           18,     #   'for'
        'PRIORITY_PARAMETER',               19,     #   function parameter
        'PRIORITY_STATEMENT',               20,     #   statement
    )
