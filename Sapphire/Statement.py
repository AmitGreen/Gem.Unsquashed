#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Statement')
def gem():
    require_gem('Sapphire.Token')


    @share
    class AsFragment(Object):
        __slots__ = ((
            'left_name',                #   String+
            'keyword_as',               #   KeywordAs
            'right_name',               #   String+
        ))


        def __init__(t, left_name, keyword_as, right_name):
            t.left_name  = left_name
            t.keyword_as = keyword_as
            t.right_name = right_name


        def __repr__(t):
            return arrange('<AsFragment %s %s %s>', t.left_name, t.keyword_as, t.right_name)


    @share
    class Comment(Object):
        __slots__ = ((
            'comment',                  #   Comment
            'newline',                  #   String
        ))


        def __init__(t, comment, newline):
            t.comment = comment
            t.newline = newline


        def __repr__(t):
            if t.comment is '':
                return arrange('<# %r>', t.newline)

            return arrange('<# %r %r>', t.comment, t.newline)


    @share
    class DecoratorHeader(Object):
        __slots__ = ((
            'operator_decorator',       #   OperatorAtSign
            'expresssion',              #   Any
            'newline',                  #   String
        ))


        def __init__(t, operator_decorator, expresssion, newline):
            t.operator_decorator = operator_decorator
            t.expresssion        = expresssion
            t.newline            = newline


        def  __repr__(t):
            return arrange('<DecoratorHeader %r %r %r>', t.operator_decorator, t.expresssion, t.newline)


    @share
    class DefineHeader(Object):
        __slots__ = ((
            'keyword_define',           #   KeywordDefine
            'name',                     #   String
            'parameters_colon',         #   Parameter_0 | Parameter_1
            'newline',                  #   String
        ))


        def __init__(t, keyword_define, name, parameters_colon, newline):
            t.keyword_define   = keyword_define
            t.name             = name
            t.parameters_colon = parameters_colon
            t.newline          = newline


        def  __repr__(t):
            return arrange('<DefineHeader %s %s %r %r>', t.keyword_define, t.name, t.parameters_colon, t.newline)


    @share
    class EmptyLine(Token):
        __slots__ = (())


        def __repr__(t):
            if t.s is '':
                return '<EmptyLine>'

            return arrange('<EmptyLine %r>', t.s)


    @share
    class IndentedComment(Object):
        __slots__ = ((
            'indented',                 #   String
            'comment',                  #   Comment
            'newline',                  #   String
        ))


        def __init__(t, indented, comment, newline):
            t.indented = indented
            t.comment  = comment
            t.newline  = newline


        def __repr__(t):
            if t.comment is '':
                return arrange('<+# %r %r>', t.indented, t.newline)

            return arrange('<+# %r %r %r>', t.indented, t.comment, t.newline)


    @share
    class ParameterColon_0(Token):
        pass


    @share
    class ParameterColon_1(Object):
        __slots__ = ((
            'left_parenthesis',         #   String
            'argument_1',               #   String
            'right_parenthesis__colon', #   String
        ))


        def __init__(t, left_parenthesis, argument_1, right_parenthesis__colon):
            t.left_parenthesis         = left_parenthesis
            t.argument_1               = argument_1
            t.right_parenthesis__colon = right_parenthesis__colon


        def  __repr__(t):
            return arrange('<ParameterColon_1 %s %s %s>',
                           portray_string(t.left_parenthesis),
                           t.argument_1,
                           portray_string(t.right_parenthesis__colon))


    @share
    class StatementCall(Object):
        __slot__ = ((
            'indented',                 #   String+
            'left',                     #   Expression
            'arguments',                #   Arguments*
            'newline',                  #   String+
        ))


        def __init__(t, indented, left, arguments, newline):
            t.indented  = indented
            t.left      = left
            t.arguments = arguments
            t.newline   = newline


        def __repr__(t):
            return arrange('<StatementCall %r %r %r %r>', t.indented, t.left, t.arguments, t.newline)


    @share
    class StatementFromImport(Object):
        __slots__ = ((
            'keyword_from',             #   KeywordFrom
            'module',                   #   String+
            'keyword_import',           #   KeywordImport
            'imported',                 #   String+ | AsFragment
            'newline',                  #   String+
        ))


        def __init__(t, keyword_from, module, keyword_import, imported, newline):
            t.keyword_from   = keyword_from
            t.module         = module
            t.keyword_import = keyword_import
            t.imported       = imported
            t.newline        = newline


        def __repr__(t):
            return arrange('<StatementFrom %r %r %r %r %r>',
                           t.keyword_from, t.module, t.keyword_import, t.imported, t.newline)


    @share
    class StatementMethodCall(Object):
        __slot__ = ((
            'indented',                 #   String+
            'left',                     #   Expression
            'dot',                      #   OperatorDot
            'right',                    #   Symbol
            'arguments',                #   Arguments*
            'newline',                  #   String+
        ))


        def __init__(t, indented, left, dot, right, arguments, newline):
            t.indented  = indented
            t.left      = left
            t.dot       = dot
            t.right     = right
            t.arguments = arguments
            t.newline   = newline


        def __repr__(t):
            return arrange('<StatementCall %r %r %r %r %r %r>',
                           t.indented, t.left, t.dot, t.right, t.arguments, t.newline)


    @share
    class StatementImport(Object):
        __slots__ = ((
            'keyword_import',           #   KeywordImport
            'module',                   #   String+
            'newline',                  #   String+
        ))


        def __init__(t, keyword_import, module, newline):
            t.keyword_import = keyword_import
            t.module         = module
            t.newline        = newline


        def __repr__(t):
            return arrange('<StatementImport %r %r %r>', t.keyword_import, t.module, t.newline)


    @share
    class StatementReturnExpression(Token):
        __slots__ = ((
            'keyword_return',           #   String
            'expression',               #   String
            'newline',                  #   String
        ))


        def __init__(t, keyword_return, expression, newline):
            t.keyword_return = keyword_return
            t.expression     = expression
            t.newline        = newline


        def  __repr__(t):
            return arrange('<Return %r %r %r>', t.keyword_return, t.expression, t.newline)
