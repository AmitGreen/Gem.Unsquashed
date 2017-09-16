#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Statement')
def gem():
    require_gem('Sapphire.Core')


    @share
    class AssignFragment(Object):
        __slots__ = ((
            'left',                     #   Expression+
            'assign_operator',          #   OperatorEqualSign
        ))


        def __init__(t, left, assign_operator):
            t.left            = left
            t.assign_operator = assign_operator


        def __repr__(t):
            return arrange('<AssignFragment %r %r>', t.left, t.assign_operator)


        def display_token(t):
            return arrange('<assign-fragment %s %s>', t.left.display_token(), t.assign_operator.display_token())


        def write(t, w):
            t.left.write(w)
            w(t.assign_operator.s)



    @share
    class AssignStatement_Many(Object):
        __slot__ = ((
            'indented',                 #   String+
            'left_many',                #   Tuple of AssignFragment
            'right',                    #   Expression
            'newline',                  #   String+
        ))


        def __init__(t, indented, left_many, right, newline):
            t.indented  = indented
            t.left_many = left_many
            t.right     = right
            t.newline   = newline


        def __repr__(t):
            return arrange('<AssignStatementMany %r <%r> %r r %r>',
                           t.indented, ' '.join(portray(v)   for v in t.left_many), t.right, t.newline)


        def display_token(t):
            return arrange('<assign-many %s <%s> %s %s>',
                           portray_string(t.indented),
                           ' '.join(v.display_token()   for v in t.left_many),
                           t.right   .display_token(),
                           t.newline .display_token())


        def write(t, w):
            w(t.indented)

            for v in t.left_many:
                v.write(w)

            t.right.write(w)
            w(t.newline.s)


    @share
    class ChangeStatement(Object):
        __slot__ = ((
            'indented',                 #   String+
            'left',                     #   Expression
            'operator',                 #   Operator+
            'right',                    #   Expression
            'newline',                  #   String+
        ))


        def __init__(t, indented, left, operator, right, newline):
            assert newline.is_token_newline

            t.indented = indented
            t.left     = left
            t.operator = operator
            t.right    = right
            t.newline  = newline


        def __repr__(t):
            return arrange('<%s %r %r %r %r %r>',
                           t.__class__.__name__, t.indented, t.left, t.operator, t.right, t.newline)


        def display_token(t):
            return arrange('<%s %s %s %s %s %s>',
                           t.display_name,
                           portray_string(t.indented),
                           t.left    .display_token(),
                           t.operator.display_token(),
                           t.right   .display_token(),
                           t.newline .display_token())


        def write(t, w):
            w(t.indented)
            t.left .write(w)
            w(t.operator.s)
            t.right.write(w)
            w(t.newline.s)


    @share
    class AssignStatement_1(ChangeStatement):
        __slots__    = (())
        display_name = '='


    @share
    class ModifyStatement(ChangeStatement):
        __slots__    = (())
        display_name = 'modify-statement'


    class ClassOrFunctionHeaderBase(Object):
        __slots__ = ((
            'keyword',                  #   KeywordClass | KeywordFunction
            'name',                     #   String
            'parameters_colon',         #   Parameter_0 | Parameter_1
        ))


        def __init__(t, keyword, name, parameters_colon):
            t.keyword          = keyword
            t.name             = name
            t.parameters_colon = parameters_colon


        def  __repr__(t):
            return arrange('<%s %s %r %r>', t.__class__.__name__, t.keyword, t.name, t.parameters_colon)


        def display_token(t):
            return arrange('<%s <%s> %s %s>',
                           t.display_name,
                           t.keyword.s,
                           t.name            .display_token(),
                           t.parameters_colon.display_token())


        def write(t, w):
            w(t.keyword.s + t.name.s)
            t.parameters_colon.write(w)


    @share
    class ClassHeader(ClassOrFunctionHeaderBase):
        __slots__    = (())
        display_name = 'class'


    @share
    class FunctionHeader(ClassOrFunctionHeaderBase):
        __slots__    = (())
        display_name = 'function'


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


        display_token = __repr__


        def write(t, w):
            w('#' + t.comment + t.newline)


    @share
    class ConditionHeader(Object):
        __slots__ = ((
            'keyword',                  #   KeywordIf | KeywordWith
            'condition',                #   Expression
            'colon_newline',            #   OperatorColon_PythonNewline
        ))


        def __init__(t, keyword, condition, colon_newline):
            t.keyword       = keyword
            t.condition     = condition
            t.colon_newline = colon_newline


        def  __repr__(t):
            return arrange('<%s %r %r %r>',
                           t.__class__.__name__, t.keyword, t.condition, t.colon_newline)


        def display_token(t):
            return arrange('<%s <%s> %s %s>',
                           t.display_name,
                           t.keyword      .s,
                           t.condition    .display_token(),
                           t.colon_newline.display_token())


        def write(t, w):
            w(t.keyword.s)
            t.condition.write(w)
            w(t.colon_newline.s)


    @share
    class ElseIfHeader(ConditionHeader):
        __slots__    = (())
        display_name = 'else-if'


    @share
    class IfHeader(ConditionHeader):
        __slots__    = (())
        display_name = 'if'


    @share
    class WhileHeader(ConditionHeader):
        __slots__    = (())
        display_name = 'while'


    @share
    class WithHeader_1(ConditionHeader):
        __slots__    = (())
        display_name = 'with'


    @share
    class ConditionStatement(Object):
        __slots__ = ((
            'keyword',                  #   KeywordIf | KeywordWhile
            'condition',                #   Expression
            'colon',                    #   OperatorColon
            'body',                     #   *Statement
        ))


        def __init__(t, keyword, condition, colon, body):
            t.keyword   = keyword
            t.condition = condition
            t.colon     = colon
            t.body      = body


        def  __repr__(t):
            return arrange('<%s %r %r %r %r>',
                           t.__class__.__name__, t.keyword, t.condition, t.colon, t.body)


        def display_token(t):
            return arrange('<%s <%s> %s %s %s>',
                           t.display_name,
                           t.keyword  .s,
                           t.condition.display_token(),
                           t.colon    .display_token(),
                           t.body     .display_token())


        def write(t, w):
            w(t.keyword.s)
            t.condition.write(w)
            w(t.colon.s)
            t.body     .write(w)


    @share
    class ElseIfStatement(ConditionStatement):
        __slots__    = (())
        display_name = 'else-if-statement'


    @share
    class IfStatement(ConditionStatement):
        __slots__    = (())
        display_name = 'if-statement'


    @share
    class WhileStatement(ConditionStatement):
        __slots__    = (())
        display_name = 'while-statement'


    @share
    class DeleteStatement_Many(Object):
        __slots__ = ((
            'keyword',                  #   KeywordDelete
            'many',                     #   Tuple of (Expression | OperatorComma)
            'newline',                  #   newline
        ))


        def __init__(t, keyword, many, newline):
            t.keyword = keyword
            t.many    = many
            t.newline = newline


        def  __repr__(t):
            return arrange('<DeleteStatement_Many %r <%r> %r>',
                           t.keyword,
                           ' '.join(portray(v)   for v in t.many),
                           t.newline)


        def display_token(t):
            return arrange('<delete-* %s <%s> %s>',
                           t.keyword.display_token(),
                           ' '.join(v.display_token()   for v in t.many),
                           t.newline.display_token())


        def write(t, w):
            w(t.keyword.s)

            for v in t.many:
                v.write(w)

            w(t.newline.s)


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


        def  display_token(t):
            if t.operator_decorator.s == '@':
                return arrange('<@ %s %s>', t.expresssion.display_token(), t.newline.display_token())

            return arrange('<@ %s %s %s>',
                           portray_string(t.operator_decorator.s),
                           t.expresssion.display_token(),
                           t.newline.display_token())


        def write(t, w):
            w(t.operator_decorator.s)
            t.expresssion.write(w)
            w(t.newline.s)


    @share
    class ElseStatement(Object):
        __slots__ = ((
            'keyword_colon',            #   KeywordElseColon
            'body',                     #   *Statement
        ))


        def __init__(t, keyword_colon, body):
            t.keyword_colon = keyword_colon
            t.body          = body


        def  __repr__(t):
            return arrange('<ElseStatement %r %r>', t.keyword_colon, t.body)


        def display_token(t):
            return arrange('<else-statement <%s> %s>',
                           t.keyword_colon.s,
                           t.body.display_token())


        def write(t, w):
            w(t.keyword_colon.s)
            t.body.write(w)


    @share
    class EmptyLine(Token):
        __slots__       = (())
        display_name    = 'empty-line'
        ends_in_newline = true
        newlines        = 1


        def __init__(t, s):
            assert s[-1] == '\n'
            assert s.count('\n') is 1

            t.s = s


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


        def display_token(t):
            return arrange('<as %s <%s> %s>',
                           t.left_name .display_token(),
                           t.keyword_as.s,
                           t.right_name.display_token())


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


        display_token = __repr__


        def write(t, w):
            w(t.indented + '#' + t.comment + t.newline)


    class KeywordBinaryStatement(Object):
        __slots__ = ((
            'keyword',                  #   KeywordFor | KeywordWith
            'left',                     #   Expression
            'middle',                   #   KeywordAs | KeywordIn
            'right',                    #   Expression
            'colon_newline',            #   OperatorColon_PythonNewline
        ))


        def __init__(t, keyword, left, middle, right, colon_newline):
            t.keyword       = keyword
            t.left          = left
            t.middle        = middle
            t.right         = right
            t.colon_newline = colon_newline


        def  __repr__(t):
            return arrange('<%s %r %r %r %r %r>',
                           t.__class__.__name__,
                           t.keyword, t.left, t.middle, t.right, t.colon_newline)


        def display_token(t):
            return arrange('<%s <%s> %s <%s> %s %s>',
                           t.display_name,
                           t.keyword      .s,
                           t.left         .display_token(),
                           t.middle       .s,
                           t.right        .display_token(),
                           t.colon_newline.display_token())


        def write(t, w):
            w(t.keyword.s)
            t.left.write(w)
            w(t.middle.s)
            t.right.write(w)
            w(t.colon_newline.s)


    @share
    class ExceptHeader_2(KeywordBinaryStatement):
        __slots__    = (())
        display_name = 'except'


    @share
    class ForHeader(KeywordBinaryStatement):
        __slots__    = (())
        display_name = 'for'


    @share
    class WithHeader_2(KeywordBinaryStatement):
        __slots__    = (())
        display_name = 'with'


    @share
    class KeywordExpressionStatement_1(Object):
        __slots__ = ((
            'keyword',                  #   KeywordDelete | KeywordReturn
            'expression',               #   Expression
            'newline',                  #   newline
        ))


        def __init__(t, keyword, expression, newline):
            t.keyword    = keyword
            t.expression = expression
            t.newline    = newline


        def  __repr__(t):
            return arrange('<%s %r %r %r>', t.__class__.__name__, t.keyword, t.expression, t.newline)


        def display_token(t):
            return arrange('<%s %s %s %s>',
                           t.display_name,
                           t.keyword   .display_token(),
                           t.expression.display_token(),
                           t.newline   .display_token())


        def write(t, w):
            w(t.keyword.s)
            t.expression.write(w)
            w(t.newline.s)


    @share
    class AssertStatement_1(KeywordExpressionStatement_1):
        __slots__    = (())
        display_name = 'assert-statement-1'


    @share
    class DeleteStatement_1(KeywordExpressionStatement_1):
        __slots__    = (())
        display_name = 'delete-statement-1'


    @share
    class RaiseStatement_1(KeywordExpressionStatement_1):
        __slots__    = (())
        display_name = 'raise-statement-1'


    @share
    class ReturnStatement_1(KeywordExpressionStatement_1):
        __slots__    = (())
        display_name = 'return-statement-1'


    @share
    class YieldStatement(KeywordExpressionStatement_1):
        __slots__    = (())
        display_name = 'yield-statement'


    class KeywordExpressionStatement_2(Object):
        __slots__ = ((
            'keyword',                  #   KeywordAssert
            'left',                     #   Expression
            'comma',                    #   OperatorComma
            'right',                    #   Expression
            'newline',                  #   newline
        ))


        def __init__(t, keyword, left, comma, right, newline):
            t.keyword = keyword
            t.left    = left
            t.comma   = comma
            t.right   = right
            t.newline = newline


        def  __repr__(t):
            return arrange('<%s %r %r %r %r>',
                           t.__class__.__nane__, t.keyword, t.left, t.comma, t.right, t.newline)


        def display_token(t):
            return arrange('<%s %s %s %s %s %s>',
                           t.display_name,
                           t.keyword.display_token(),
                           t.left   .display_token(),
                           t.comma  .display_token(),
                           t.right  .display_token(),
                           t.newline.display_token())


        def write(t, w):
            w(t.keyword.s)
            t.left .write(w)
            t.comma.write(w)
            t.right.write(w)
            w(t.newline.s)


    @share
    class AssertStatement_2(KeywordExpressionStatement_2):
        __slots__    = (())
        display_name = 'assert-statement-2'


    @share
    class RaiseStatement_2(KeywordExpressionStatement_2):
        __slots__    = (())
        display_name = 'raise-statement-2'


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
    class ParameterColon_1(Object):
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


        def  display_token(t):
            return arrange('<(1): %s %s %s>',
                           t.left_parenthesis        .display_token(),
                           t.argument_1              .display_token(),
                           t.right_parenthesis__colon.display_token())


        def write(t, w):
            t.left_parenthesis        .write(w)
            t.argument_1              .write(w)
            t.right_parenthesis__colon.write(w)


    @share
    class RaiseStatement_3(Object):
        __slots__ = ((
            'keyword',                  #   KeywordAssert
            'left',                     #   Expression
            'comma_1',                  #   OperatorComma
            'middle',                   #   Expression
            'comma_2',                  #   OperatorComma
            'right',                    #   Expression
            'newline',                  #   newline
        ))


        def __init__(t, keyword, left, comma_1, middle, comma_2, right, newline):
            t.keyword = keyword
            t.left    = left
            t.comma_1 = comma_1
            t.middle  = middle
            t.comma_2 = comma_2
            t.right   = right
            t.newline = newline


        def  __repr__(t):
            return arrange('<RaiseStatement_3 %r %r %r %r %r %r %r>',
                           t.keyword, t.left, t.comma_1, t.middle, comma_2, t.right, t.newline)


        def display_token(t):
            return arrange('<raise-3 %s %s %s %s %s %s %s>',
                           t.keyword.display_token(),
                           t.left   .display_token(),
                           t.comma_1.display_token(),
                           t.middle .display_token(),
                           t.comma_2.display_token(),
                           t.right  .display_token(),
                           t.newline.display_token())


        def write(t, w):
            w(t.keyword.s)
            t.left   .write(w)
            t.comma_1.write(w)
            t.middle .write(w)
            t.comma_2.write(w)
            t.right  .write(w)
            w(t.newline.s)


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


        def display_token(t):
            return arrange('<call-statement %s %s %s %s>',
                           portray_string(t.indented),
                           t.left     .display_token(),
                           t.arguments.display_token(),
                           t.newline  .display_token())


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


        def display_token(t):
            return arrange('<expression-statement %r %s %s>',
                           t.indented,
                           t.expression.display_token(),
                           t.newline   .display_token())

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

        def display_token(t):
            return arrange('<from <%s> %s <%s> %s %s>',
                           t.keyword_from.s,
                           t.module        .display_token(),
                           t.keyword_import.s,
                           t.imported      .display_token(),
                           t.newline       .display_token())


        def write(t, w):
            w(t.keyword_from.s)
            t.module.write(w)
            w(t.keyword_import.s)
            t.imported.write(w)
            w(t.newline.s)


    @share
    class MethodCallStatement_1(Object):
        __slot__ = ((
            'indented',                 #   String+
            'left',                     #   Expression
            'dot',                      #   OperatorDot
            'right',                    #   Identifier
            'arguments',                #   Arguments*
            'newline',                  #   String+
        ))


        is_statement = true


        def __init__(t, indented, left, dot, right, arguments, newline):
            t.indented  = indented
            t.left      = left
            t.dot       = dot
            t.right     = right
            t.arguments = arguments
            t.newline   = newline


        def __repr__(t):
            return arrange('<MethodCallStatement_1 %r %r %r %r %r %r>',
                           t.indented, t.left, t.dot, t.right, t.arguments, t.newline)


        def display_token(t):
            return arrange('<method-call-statement-1 %s %s %s %s %s %s>',
                           portray_string(t.indented),
                           t.left.display_token(),
                           t.dot.display_token(),
                           t.right.display_token(),
                           t.arguments.display_token(),
                           t.newline.display_token())


        def write(t, w):
            w(t.indented)
            t.left.write(w)
            t.dot.write(w)
            t.right.write(w)
            t.arguments.write(w)
            t.newline.write(w)


    @share
    class MethodCallStatement_2(Object):
        __slot__ = ((
            'indented',                 #   String+
            'left',                     #   Expression
            'dot_1',                    #   OperatorDot
            'middle',                   #   Identifier
            'dot_2',                    #   OperatorDot
            'right',                    #   Identifier
            'arguments',                #   Arguments*
            'newline',                  #   String+
        ))


        is_statement = true


        def __init__(t, indented, left, dot_1, middle, dot_2, right, arguments, newline):
            t.indented  = indented
            t.left      = left
            t.dot_1     = dot_1
            t.middle    = middle
            t.dot_2     = dot_2
            t.right     = right
            t.arguments = arguments
            t.newline   = newline


        def __repr__(t):
            return arrange('<MethodCallStatement_2 %r %r %r %r %r %r %r %r>',
                           t.indented, t.left, t.dot_1, t.middle, t.dot_2, t.right, t.arguments, t.newline)


        def display_token(t):
            return arrange('<method-call-statement-2 %s %s %s %s %s %s %s %s>',
                           portray_string(t.indented),
                           t.left     .display_token(),
                           t.dot_1    .display_token(),
                           t.middle   .display_token(),
                           t.dot_2    .display_token(),
                           t.right    .display_token(),
                           t.arguments.display_token(),
                           t.newline  .display_token())


        def write(t, w):
            w(t.indented)
            t.left     .write(w)
            t.dot_1    .write(w)
            t.middle   .write(w)
            t.dot_2    .write(w)
            t.right    .write(w)
            t.arguments.write(w)
            t.newline  .write(w)


    @share
    class StatementImport_1(Object):
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


        def display_token(t):
            return arrange('<import %s %s %s>',
                           t.keyword_import.display_token(),
                           t.module        .display_token(),
                           t.newline       .display_token())


        def write(t, w):
            w(t.keyword_import.s)
            t.module.write(w)
            w(t.newline.s)


    @share
    class StatementImport_Many(Object):
        __slots__ = ((
            'keyword_import',           #   KeywordImport
            'module_many',              #   Tuple of String
            'newline',                  #   String+
        ))


        def __init__(t, keyword_import, module_many, newline):
            t.keyword_import = keyword_import
            t.module_many    = module_many
            t.newline        = newline


        def __repr__(t):
            return arrange('<StatementImport %r %r %r>', t.keyword_import, t.module_many, t.newline)


        def display_token(t):
            return arrange('<import %s <%s> %s>',
                           t.keyword_import.display_token(),
                           ' '.join(portray(v)   for v in t.module_many),
                           t.newline       .display_token())


        def write(t, w):
            w(t.keyword_import.s)

            for v in t.module_many:
                if type(v) is String:
                    w(v)
                else:
                    v.write(w)

            w(t.newline.s)


    @share
    class StatementPass(Token):
        __slots__    = (())
        display_name = 'pass'
        keyword      = 'pass'


    @share
    class StatementReturn(Token):
        __slots__    = (())
        display_name = 'return'
        keyword      = 'return'
