#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.CallStatement')
def gem():
    require_gem('Sapphire.MemberExpression')
    require_gem('Sapphire.Tree')


    class CallStatementBase(SapphireTrunk):
        __slots__ = ((
            'frill',                    #   DualFrill
            'left',                     #   Expression
            'arguments',                #   Arguments*
        ))


        is_statement = true


        def __init__(t, frill, left, arguments):
            t.frill     = frill
            t.left      = left
            t.arguments = arguments


        def __repr__(t):
            return arrange('<%s %r %r %r %r>', t.__class__.__name__, t.frill, t.left, t.arguments)


        def count_newlines(t):
            return t.frill.count_newlines() + t.left.count_newlines() + t.arguments.count_newlines()


        @property
        def indentation(t):
            return t.frill.a


        def display_token(t):
            frill = t.frill

            return arrange('<%s +%d %s %s %s>',
                           t.display_name,
                           frill.a.total,
                           t.left     .display_token(),
                           t.arguments.display_token(),
                           frill.b    .display_token())


        def write(t, w):
            frill = t.frill

            w(frill.a.s)
            t.left     .write(w)
            t.arguments.write(w)
            w(frill.b.s)


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
