#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Statement')
def gem():
    require_gem('Sapphire.Tree')


    #
    #   TODO: Update this to a BookcaseExpression
    #
    @share
    class ParameterColon_1(SapphireTrunk):
        __slots__ = ((
            'left_parenthesis',             #   OperatorLeftParenthesis
            'argument_1',                   #   Expression*
            'right_parenthesis__colon',     #   OperatorRightParenthesis
        ))


        def __init__(t, left_parenthesis, argument_1, right_parenthesis__colon):
            t.left_parenthesis         = left_parenthesis
            t.argument_1               = argument_1
            t.right_parenthesis__colon = right_parenthesis__colon


        def  __repr__(t):
            return arrange('<(1): %r %r %r>',
                           t.left_parenthesis, t.argument_1, t.right_parenthesis__colon)


        def count_newlines(t):
            return (
                         t.left_parenthesis        .count_newlines()
                       + t.argument_1              .count_newlines()
                       + t.right_parenthesis__colon.count_newlines()
                   )


        def  display_token(t):
            return arrange('<(1): %s %s %s>',
                           t.left_parenthesis        .display_token(),
                           t.argument_1              .display_token(),
                           t.right_parenthesis__colon.display_token())


        def write(t, w):
            t.left_parenthesis        .write(w)
            t.argument_1              .write(w)
            t.right_parenthesis__colon.write(w)
