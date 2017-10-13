#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Priority')
def gem():
    share(
        'PRIORITY_ATOM',                     1,     #   atom
        'PRIORITY_TUPLE',                    2,     #   tuple
        'PRIORITY_POSTFIX',                  3,     #   . () and []
        'PRIORITY_POWER',                    4,     #   **
        'PRIORITY_UNARY',                    5,     #   ~ unary- 
        'PRIORITY_MULTIPLY',                 6,     #   *
        'PRIORITY_ARITHMETIC',               7,     #   +
        'PRIORITY_SHIFT',                    8,     #   << and >>
        'PRIORITY_LOGICAL_AND',              9,     #   &
        'PRIORITY_LOGICAL_EXCLUSIVE_OR',    10,     #   ^
        'PRIORITY_LOGICAL_OR',              11,     #   |
        'PRIORITY_NORMAL_LIST',             12,     #   Comma expression of PRIORITY_LOGICAL_OR
        'PRIORITY_COMPARE',                 13,     #   ==
        'PRIORITY_NOT',                     14,     #   not
        'PRIORITY_BOOLEAN_AND',             15,     #   'and'
        'PRIORITY_BOOLEAN_OR',              16,     #   'or'
        'PRIORITY_TERNARY',                 17,     #   'if'
        'PRIORITY_TERNARY_LIST',            18,     #   Comma expression of PRIORITY_TERNARY
        'PRIORITY_YIELD',                   19,     #   'yield'
        'PRIORITY_COMPREHENSION',           20,     #   'for'
        'PRIORITY_PARAMETER',               21,     #   function parameter
        'PRIORITY_STATEMENT',               22,     #   statement
    )
