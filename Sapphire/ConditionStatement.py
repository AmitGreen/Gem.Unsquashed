#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.ConditionStatement')
def gem():
    require_gem('Sapphire.DualToken')


    append_cache                = Shared.append_cache                   #   Due to privileged
    conjure_dual_frill          = Shared.conjure_dual_frill             #   Due to privileged
    lookup_adjusted_meta        = Shared.lookup_adjusted_meta           #   Due to privileged
    produce_conjure_dual        = Shared.produce_conjure_dual           #   Due to privileged
    produce_conjure_triple__312 = Shared.produce_conjure_triple__312    #   Due to privileged
    store_adjusted_meta         = Shared.store_adjusted_meta            #   Due to privileged


    class ConditionStatement(SapphireTrunk):
        __slots__ = ((
            'condition',                #   Expression
            'body',                     #   *Statement
        ))


        is_statement        = true
        is_statement_header = false


        def __init__(t, condition, body):
            t.condition = condition
            t.body      = body


        def  __repr__(t):
            return arrange('<%s %r r %r>',
                           t.__class__.__name__, t.condition, t.body)


        def count_newlines(t):
            return t.condition.count_newlines() + t.body.count_newlines() + t.frill.count_newlines()


        def display_token(t):
            return arrange('<%s +%d s %s %s>',
                           t.display_name,
                           t.frill.a.a.total,
                           t.condition.display_token(),
                           t.body     .display_token())


        def dump_token(t, newline = true):
            assert newline is true

            frill       = t.frill
            frill_a     = frill.a
            indentation = frill_a.a

            partial('%s<%s +%d ', indentation.s, t.display_name, indentation.total)
            frill.a.b.dump_token()
            t.condition.dump_token()
            frill.b.dump_token()
            r = t.body.dump_token(false)

            if (r) and (newline):
                line('>')
                return false

            partial('>')
            return r


        @property
        def indentation(t):
            return t.frill.a.a


        def write(t, w):
            frill = t.frill

            w(frill.a.s)
            t.condition.write(w)
            w(frill.b.s)
            t.body     .write(w)


    ConditionStatement.k1 = ConditionStatement.condition
    ConditionStatement.k2 = ConditionStatement.body


    @share
    @privileged
    def produce_conjure_condition_statement(name, Meta):
        cache  = {}
        lookup = cache.get
        store  = cache.__setitem__


        def conjure_Meta_WithFrill(condition, body, frill):
            ConditionStatement_WithFrill = lookup_adjusted_meta(Meta)

            if ConditionStatement_WithFrill is none:
                class ConditionStatement_WithFrill(Meta):
                    __slots__ = ((
                        'frill',                #   DualFrill
                    ))


                    def __init__(t, condition, body, frill):
                        t.condition = condition
                        t.body      = body
                        t.frill     = frill


                    def __repr__(t):
                        return arrange('<%s %r %r %r>', t.__class__.__name__, t.frill, t.condition, t.body)


                    def display_token(t):
                        frill = t.frill

                        frill_a = frill.a

                        return arrange('<%s+frill +%d %s %s %s %s>',
                                       t.display_name,
                                       frill_a.a.total,
                                       frill_a.b  .display_token(),
                                       t.condition.display_token(),
                                       frill.b    .display_token(),
                                       t.body     .display_token())


                ConditionStatement_WithFrill.k3 = ConditionStatement_WithFrill.frill


                if __debug__:
                    ConditionStatement_WithFrill.__name__ = intern_arrange('%s_WithFrill', Meta.__name__)

                store_adjusted_meta(Meta, ConditionStatement_WithFrill)

            return ConditionStatement_WithFrill(condition, body, frill)


        conjure_dual   = produce_conjure_dual       (name, Meta,                   cache, lookup, store)
        conjure_triple = produce_conjure_triple__312(name, conjure_Meta_WithFrill, cache, lookup, store)

        meta_frill_a = Meta.frill.a
        meta_frill_b = Meta.frill.b


        def conjure_condition_statement(indented_keyword, condition, colon, body):
            if (indented_keyword is meta_frill_a) and (colon is meta_frill_b):
                return conjure_dual(condition, body)

            return conjure_triple(condition, body, conjure_dual_frill(indented_keyword, colon))


        if __debug__:
            conjure_condition_statement.__name__ = intern_arrange('conjure_%s', name)

            append_cache(name, cache)

        return conjure_condition_statement


    class ElseIfStatement(ConditionStatement):
        __slots__    = (())
        display_name = 'else-if-statement'
        frill        = conjure_dual_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_else_if('elif ')),
                           conjure_colon(': '),
                       )


    class IfStatement(ConditionStatement):
        __slots__    = (())
        display_name = 'if-statement'
        frill        = conjure_dual_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_if('if ')),
                           conjure_colon(': '),
                       )


    class WhileStatement(ConditionStatement):
        __slots__    = (())
        display_name = 'while-statement'
        frill        = conjure_dual_frill(
                           conjure_indented_token(empty_indentation, conjure_keyword_while('while ')),
                           conjure_colon(': '),
                       )

    conjure_else_if_statement = produce_conjure_condition_statement('else-if-statement', ElseIfStatement)
    conjure_if_statement      = produce_conjure_condition_statement('if-statement',      IfStatement)
    conjure_while_statement   = produce_conjure_condition_statement('while-statement',   WhileStatement)


    share(
        'conjure_else_if_statement',    conjure_else_if_statement,
        'conjure_if_statement',         conjure_if_statement,
        'conjure_while_statement',      conjure_while_statement,
    )