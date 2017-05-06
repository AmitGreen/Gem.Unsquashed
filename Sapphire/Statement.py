#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Statement')
def gem():
    require_gem('Sapphire.Token')


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


        def write(t, w):
            w('#' + t.comment + t.newline)


    @share
    class ClassOrDefineHeaderBase(Object):
        __slots__ = ((
            'keyword',                  #   KeywordClass | KeywordDefine
            'name',                     #   String
            'parameters_colon',         #   Parameter_0 | Parameter_1
            'newline',                  #   String
        ))


        def __init__(t, keyword, name, parameters_colon, newline):
            assert newline.is_token_newline

            t.keyword          = keyword
            t.name             = name
            t.parameters_colon = parameters_colon
            t.newline          = newline


        def  __repr__(t):
            return arrange('<%s %s %s %r %r>', t.__class__.__name__, t.keyword, t.name, t.parameters_colon, t.newline)


        def write(t, w):
            w(t.keyword.s + t.name)
            t.parameters_colon.write(w)
            w(t.newline.s)


    @share
    class ClassHeader(ClassOrDefineHeaderBase):
        __slots__ = (())


    @share
    class DefineHeader(ClassOrDefineHeaderBase):
        __slots__ = (())


    @share
    class DecoratorHeader(Object):
        __slots__ = ((
            'operator_decorator',       #   OperatorAtSign
            'expresssion',              #   Any
            'newline',                  #   String
        ))


        def __init__(t, operator_decorator, expresssion, newline):
            assert newline.is_token_newline

            t.operator_decorator = operator_decorator
            t.expresssion        = expresssion
            t.newline            = newline


        def  __repr__(t):
            return arrange('<DecoratorHeader %r %r %r>', t.operator_decorator, t.expresssion, t.newline)


        def write(t, w):
            w(t.operator_decorator.s)
            t.expresssion.write(w)
            w(t.newline.s)


    @share
    class EmptyLine(Token):
        __slots__ = (())


        def __repr__(t):
            if t.s is '':
                return '<EmptyLine>'

            return arrange('<EmptyLine %r>', t.s)


    @share
    class FromAsFragment(Object):
        __slots__ = ((
            'left_name',                #   String+
            'keyword_as',               #   KeywordAs
            'right_name',               #   String+
        ))


        def __init__(t, left_name, keyword_as, right_name):
            assert type(left_name)  is not String
            assert type(right_name) is not String

            t.left_name  = left_name
            t.keyword_as = keyword_as
            t.right_name = right_name


        def __repr__(t):
            return arrange('<FromAsFragment %s %s %s>', t.left_name, t.keyword_as, t.right_name)


        def write(t, w):
            w(t.left_name.s + t.keyword_as.s + t.right_name.s)


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


        def write(t, w):
            w(t.indented + '#' + t.comment + t.newline)


    @share
    class ModuleAsFragment(Object):
        __slots__ = ((
            'module',                   #   Expression
            'keyword_as',               #   KeywordAs
            'right_name',               #   String+
        ))


        def __init__(t, module, keyword_as, right_name):
            assert type(module)  is not String
            assert type(right_name) is not String

            t.module     = module
            t.keyword_as = keyword_as
            t.right_name = right_name


        def __repr__(t):
            return arrange('<ModuleAsFragment %s %s %s>', t.module, t.keyword_as, t.right_name)


        def write(t, w):
            t.module.write(w)
            w(t.keyword_as.s + t.right_name.s)


    @share
    class ParameterColon_0(Token):
        pass


    @share
    class ParameterColon_1(Object):
        __slots__ = ((
            'left_parenthesis',             #   OperatorLeftParenthesis
            'argument_1',                   #   Expression*
            'right_parenthesis__colon',     #   OperatorRightParenthesis
        ))


        def __init__(t, left_parenthesis, argument_1, right_parenthesis__colon):
            assert left_parenthesis        .is_left_parenthesis
            assert type(argument_1) is not String
            assert right_parenthesis__colon.is__right_parenthesis__colon


            t.left_parenthesis         = left_parenthesis
            t.argument_1               = argument_1
            t.right_parenthesis__colon = right_parenthesis__colon


        def  __repr__(t):
            return arrange('<ParameterColon_1 %r %r %r>', t.left_parenthesis, t.argument_1, t.right_parenthesis__colon)


        def write(t, w):
            t.left_parenthesis        .write(w)
            t.argument_1              .write(w)
            t.right_parenthesis__colon.write(w)


    @share
    class StatementCall(Object):
        __slot__ = ((
            'indented',                 #   String+
            'left',                     #   Expression
            'arguments',                #   Arguments*
            'newline',                  #   String+
        ))


        def __init__(t, indented, left, arguments, newline):
            assert newline.is_token_newline

            t.indented  = indented
            t.left      = left
            t.arguments = arguments
            t.newline   = newline


        def __repr__(t):
            return arrange('<StatementCall %r %r %r %r>', t.indented, t.left, t.arguments, t.newline)


        def write(t, w):
            w(t.indented)
            t.left     .write(w)
            t.arguments.write(w)
            w(t.newline.s)


    @share
    class StatementExpression(Object):
        __slot__ = ((
            'indented',                 #   String+
            'expression',               #   Expression
            'newline',                  #   String+
        ))


        def __init__(t, indented, expression, newline):
            t.indented   = indented
            t.expression = expression
            t.newline    = newline


        def __repr__(t):
            return arrange('<StatementExpression %r %r %r>', t.indented, t.expression, t.newline)


        def write(t, w):
            w(t.indented)
            t.expression.write(w)
            w(t.newline.s)


    @share
    class StatementFromImport(Object):
        __slots__ = ((
            'keyword_from',             #   KeywordFrom
            'module',                   #   String+
            'keyword_import',           #   KeywordImport
            'imported',                 #   String+ | FromAsFragment
            'newline',                  #   String+
        ))


        def __init__(t, keyword_from, module, keyword_import, imported, newline):
            assert type(module) is not String
            assert newline.is_token_newline

            t.keyword_from   = keyword_from
            t.module         = module
            t.keyword_import = keyword_import
            t.imported       = imported
            t.newline        = newline


        def __repr__(t):
            return arrange('<StatementFrom %r %r %r %r %r>',
                           t.keyword_from, t.module, t.keyword_import, t.imported, t.newline)


        def write(t, w):
            w(t.keyword_from.s)
            t.module.write(w)
            w(t.keyword_import.s)
            t.imported.write(w)
            w(t.newline.s)


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


        def write(t, w):
            w(t.indented)
            t.left.write(w)
            w(t.dot + t.right)
            t.arguments.write(w)
            w(t.newline)


    @share
    class StatementImport(Object):
        __slots__ = ((
            'keyword_import',           #   KeywordImport
            'module',                   #   String+
            'newline',                  #   String+
        ))


        def __init__(t, keyword_import, module, newline):
            assert type(module) is not String
            assert newline.is_token_newline

            t.keyword_import = keyword_import
            t.module         = module
            t.newline        = newline


        def __repr__(t):
            return arrange('<StatementImport %r %r %r>', t.keyword_import, t.module, t.newline)


        def write(t, w):
            w(t.keyword_import.s)
            t.module.write(w)
            w(t.newline.s)


    @share
    class StatementReturnExpression(Object):
        __slots__ = ((
            'keyword_return',           #   String
            'expression',               #   String
            'newline',                  #   String
        ))


        def __init__(t, keyword_return, expression, newline):
            assert newline.is_token_newline

            t.keyword_return = keyword_return
            t.expression     = expression
            t.newline        = newline


        def  __repr__(t):
            return arrange('<Return %r %r %r>', t.keyword_return, t.expression, t.newline)


        def write(t, w):
            w(t.keyword_return.s)
            t.expression.write(w)
            w(t.newline.s)
