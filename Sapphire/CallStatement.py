#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.CallStatement')
def gem():
    require_gem('Sapphire.BookcaseExpression')
    require_gem('Sapphire.MemberExpression')
    require_gem('Sapphire.Tree')


    class CallStatementBase(SapphireTrunk):
        __slots__ = ((
            'frill',                    #   XY_Frill | Commented_XY_Frill
            'left',                     #   Expression
            'arguments',                #   Arguments*
        ))


        is_statement_header = false
        is_statement        = true


        def __init__(t, frill, left, arguments):
            frill.comment

            t.frill     = frill
            t.left      = left
            t.arguments = arguments


        def __repr__(t):
            return arrange('<%s %r %r %r>', t.__class__.__name__, t.frill, t.left, t.arguments)


        def count_newlines(t):
            return t.frill.count_newlines() + t.left.count_newlines() + t.arguments.count_newlines()


        @property
        def indentation(t):
            return t.frill.x


        def display_token(t):
            frill   = t.frill
            comment = frill.comment

            return arrange('<%s +%d%s %s %s %s>',
                           t.display_name,
                           frill.x.total,
                           (''   if comment is 0 else   '' + comment.display_token()),
                           t.left     .display_token(),
                           t.arguments.display_token(),
                           frill.y    .display_token())


        def dump_token(t, f, newline = true):
            frill   = t.frill
            comment = frill.comment

            if comment is 0:
                f.partial('<%s +%d ', t.display_name, frill.x.total)
                t.left.dump_token(f)
                t.arguments.dump_token(f)
                r = frill.y.dump_token(f, false)

                if (r) and (newline):
                    f.line('>')
                    return false

                f.partial('>')
                return r

            with f.line(arrange('<%s +%d', t.display_name, frill.x.total), '>'):
                comment    .dump_token(f)
                t.left     .dump_token(f)
                t.arguments.dump_token(f)
                frill.y    .dump_token(f)


        def write(t, w):
            frill   = t.frill
            comment = frill.comment

            if comment is not 0:
                comment.write(w)

            w(frill.x.s)
            t.left     .write(w)
            t.arguments.write(w)
            w(frill.y.s)


    CallStatementBase.k1 = CallStatementBase.frill
    CallStatementBase.k2 = CallStatementBase.left
    CallStatementBase.k3 = CallStatementBase.arguments


    @share
    class CallStatement(CallStatementBase):
        __slots__    = (())
        display_name = 'call-statement'


    @share
    class MethodCallStatement(CallStatementBase):
        __slots__    = (())
        display_name = 'method-call-statement'


    conjure_call_statement        = produce_conjure_triple__312('call-statement',        CallStatement)
    conjure_method_call_statement = produce_conjure_triple__312('method-call-statement', MethodCallStatement)


    static_conjure_call_statement = static_method(conjure_call_statement)

    MemberExpression.call_statement = static_method(conjure_method_call_statement)
    SapphireToken   .call_statement = static_conjure_call_statement
    SapphireTrunk   .call_statement = static_conjure_call_statement
