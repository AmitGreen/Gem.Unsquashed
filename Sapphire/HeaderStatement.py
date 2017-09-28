#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.HeaderStatement')
def gem():
    require_gem('Sapphire.Tree')


    class HeaderStatement(SapphireTrunk):
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


        def count_newlines(t):
            return t.keyword.count_newlines() + t.name.count_newlines() + t.parameters_colon.count_newlines()


        def display_token(t):
            keyword = t.keyword

            return arrange('<%s +%d %s %s %s>',
                           t.display_name,
                           keyword.a.total,
                           keyword.b         .display_token(),
                           t.name            .display_token(),
                           t.parameters_colon.display_token())


        @property
        def indentation(t):
            return t.keyword.a

            
        def write(t, w):
            w(t.keyword.s + t.name.s)
            t.parameters_colon.write(w)


    HeaderStatement.k1 = HeaderStatement.keyword
    HeaderStatement.k2 = HeaderStatement.name
    HeaderStatement.k3 = HeaderStatement.parameters_colon


    class ClassHeader(HeaderStatement):
        __slots__    = (())
        display_name = 'class-header'


    class FunctionHeader(HeaderStatement):
        __slots__    = (())
        display_name = 'function-header'


    conjure_class_header    = produce_conjure_triple__312('class-header',    ClassHeader)
    conjure_function_header = produce_conjure_triple__312('function-header', FunctionHeader)


    share(
        'conjure_class_header',     conjure_class_header,
        'conjure_function_header',  conjure_function_header,
    )
