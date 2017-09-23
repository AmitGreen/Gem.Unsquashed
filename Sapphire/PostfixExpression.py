#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Expression')
def gem():
    @privileged
    def produce_conjure_postfix_expression(name, Meta):
        cache   = {}
        lookup  = cache.get
        provide = cache.setdefault
        store   = cache.__setitem__

        meta_frill = Meta.frill


        def conjure_binary_expression(a, frill, b):
            if frill is meta_frill:
                first = lookup(a, absent)

                if first.__class__ is Map:
                    return (first.get(b)) or (first.setdefault(b, Meta(a, b)))

                if first.b is b:
                    return first

                r = Meta(a, b)

                store(a, (r   if first is absent else   { first.b : first, b : r }))

                return r

            first = lookup(frill, absent)

            if first.__class__ is Map:
                second = first.get(a, absent)

                if second.__class__ is Map:
                    return (
                                  second.get(b)
                               or second.setdefault(b, conjure_BinaryExpression_WithFrill(Meta, a, frill, b))
                           )

                if second.b is b:
                    return second

                r = conjure_BinaryExpression_WithFrill(Meta, a, frill, b)

                first[a] = (r   if second is absent else   { second.b : second, b : r })

                return r

            if first.a is a:
                if first.b is b:
                    return first

                r = conjure_BinaryExpression_WithFrill(Meta, a, frill, b)

                store(frill, { a : { first.b : first, b : r } })

                return r

            r = conjure_BinaryExpression_WithFrill(Meta, a, frill, b)

            store(frill, (r   if first is absent else   { first.a : first, a : r }))

            return r


        if __debug__:
            conjure_binary_expression.__name__ = intern_arrange('conjure_%s', name)

            cache_many.append( ((name, cache)) )

        return conjure_binary_expression


    class PostfixExpression(SapphireTrunk):
        __slots__ = ((
            'left',                     #   Expression
            'postfix',                  #   Operator*
        ))


        def __init__(t, left, postfix):
            t.left    = left
            t.postfix = postfix


        def __repr__(t):
            return arrange('<%s %r %r>', t.__class__.__name__, t.left, t.postfix)


        def display_token(t):
            return arrange('<%s %s %s>', t.display_name, t.left.display_token(), t.postfix.display_token())


        def write(t, w):
            t.left   .write(w)
            t.postfix.write(w)


    @share
    class CallExpression(PostfixExpression):
        __slot__     = (())
        display_name = 'call'


    @share
    class IndexExpression(PostfixExpression):
        __slots__    = (())
        display_name = 'index'


    @share
    class MethodCallExpression(PostfixExpression):
        __slot__     = (())
        display_name = 'method-call'
