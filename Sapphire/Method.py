#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Method')
def gem():
    require_gem('Sapphire.DumpToken')
    require_gem('Sapphire.TupleOfExpression')

    conjure_tuple_of_many_expression = Shared.conjure_tuple_of_many_expression      #   Due to privileged
    dump_token                       = Shared.dump_token                            #   Due to privileged


    #
    #   construct
    #
    @share
    def construct__123(t, k1, k2, k3):
        t.k1 = k1
        t.k2 = k2
        t.k3 = k3


    #
    #   count_newlines
    #
    @share
    def count_newlines__123(t):
        return t.k1.count_newlines() + t.k2.count_newlines() + t.k3.count_newlines()


    #
    #   display_token
    #
    @share
    def display_token__123(t):
        return arrange('<%s %s %s %s>',
                       t.display_name,
                       t.k1.display_token(),
                       t.k2.display_token(),
                       t.k3.display_token())


    #
    #   dump_token
    #
    @share
    def dump_token__12(t, f, newline = true):
        f.partial('<%s ', t.display_name)

        t    .k1.dump_token(f)
        r = t.k2.dump_token(f, false)

        return f.token_result(r, newline)


    #
    #   dump_token
    #
    @share
    def dump_token__123(t, f, newline = true):
        f.partial('<%s ', t.display_name)

        t    .k1.dump_token(f)
        t    .k2.dump_token(f)
        r = t.k3.dump_token(f, false)

        return f.token_result(r, newline)


    #
    #   find_require_gem
    #
    @share
    def find_require_gem__0(t, e):
        pass


    #
    #   is_name
    #
    @share
    def is_name__0(t, name):
        return false


    #
    #   mutate
    #
    @share
    def mutate__self(t, vary, priority):
        return t


    #
    #   portray
    #
    @share
    def portray__123(t):
        return arrange('<%s %s %r %r>', t.__class__.__name__, t.k1, t.k2, t.k3)


    #
    #   produce_mutate
    #
    @share
    @privileged
    def produce_mutate__ab(name, conjure):
        def mutate(t, vary, priority):
            a = t.a
            b = t.b

            a__2 = a.mutate(vary, priority)
            b__2 = b.mutate(vary, priority)

            if (a is a__2) and (b is b__2):
                return t

            return conjure(a__2, b__2)


        if __debug__:
            mutate.__name__ = intern_arrange('mutate__%s', name)

        return mutate


    @share
    @privileged
    def produce__mutate__ab__priority(name, conjure, a_priority, b_priority):
        def mutate(t, vary, priority):
            a = t.a
            b = t.b

            a__2 = a.mutate(vary, a_priority)
            b__2 = b.mutate(vary, b_priority)

            if (a is a__2) and (b is b__2):
                return t

            return conjure(a__2, b__2)


        if __debug__:
            mutate.__name__ = intern_arrange('mutate__%s', name)

        return mutate


    @share
    @privileged
    def produce_mutate__abc(name, conjure):
        def mutate(t, vary, priority):
            a = t.a
            b = t.b
            c = t.c

            a__2 = a.mutate(vary, priority)
            b__2 = b.mutate(vary, priority)
            c__2 = c.mutate(vary, priority)

            if (a is a__2) and (b is b__2) and (c is c__2):
                return t

            return conjure(a__2, b__2, c__2)


        if __debug__:
            mutate.__name__ = intern_arrange('mutate__%s', name)

        return mutate


    @share
    @privileged
    def produce_mutate__frill__a__priority(name, priority):
        def mutate(t, vary, priority):
            frill = t.frill
            a     = t.a

            frill__2 = frill.mutate(vary, priority)
            a__2     = a    .mutate(vary, priority)

            if (frill is frill__2) and (a is a__2):
                return t

            return t.conjure_with_frill(frill__2, a__2)


        if __debug__:
            mutate.__name__ = intern_arrange('mutate_%s', name)

        return mutate


    @share
    @privileged
    def produce_mutate__frill__a_with_priority(name, a_priority, conjure_with_frill):
        def mutate(t, vary, priority):
            frill = t.frill
            a     = t.a

            frill__2 = frill.transform(vary)
            a__2     = a    .mutate   (vary, a_priority)

            if (frill is frill__2) and (a is a__2):
                return t

            return conjure_with_frill(frill__2, a__2)


        if __debug__:
            mutate.__name__ = intern_arrange('mutate_%s', name)

        return mutate


    @share
    @privileged
    def produce_mutate__frill__ab__priority(name, frill_priority, a_priority, b_priority, conjure_with_frill = 0):
        def mutate(t, vary, priority):
            frill = t.frill
            a     = t.a
            b     = t.b

            frill__2 = frill.mutate(vary, frill_priority)
            a__2     = a    .mutate(vary, a_priority)
            b__2     = b    .mutate(vary, b_priority)

            if (frill is frill__2) and (a is a__2) and (b is b__2):
                return t

            return ((conjure_with_frill) or (t.conjure_with_frill))(frill__2, a__2, b__2)


        if __debug__:
            mutate.__name__ = intern_arrange('mutate_%s', name)

        return mutate


    @share
    @privileged
    def produce_mutate__frill__ab_with_priority(name, a_priority, b_priority, conjure_with_frill):
        def mutate(t, vary, priority):
            frill = t.frill
            a     = t.a
            b     = t.b

            frill__2 = frill.transform(vary)
            a__2     = a    .mutate   (vary, a_priority)
            b__2     = b    .mutate   (vary, b_priority)

            if (frill is frill__2) and (a is a__2) and (b is b__2):
                return t

            return conjure_with_frill(frill__2, a__2, b__2)


        if __debug__:
            mutate.__name__ = intern_arrange('mutate_%s', name)

        return mutate


    @share
    @privileged
    def produce_mutate__frill__many(name, first_priority, middle_priority, last_priority, conjure_with_frill):
        def mutate(t, vary, priority):
            frill = t.frill
            many  = t.many

            frill__2 = frill .transform(vary)
            many__2  = t.many.morph    (vary, first_priority, middle_priority, last_priority)

            if (frill is frill__2) and (many is many__2):
                return t

            return conjure_with_frill(frill__2, many__2)


        if __debug__:
            mutate.__name__ = intern_arrange('mutate_%s', name)

        return mutate


    @share
    @privileged
    def produce_mutate__uncommented(name, uncommented):
        def mutate(t, vary, priority):
            if vary.remove_comments:
                return uncommented

            return t


        if __debug__:
            mutate.__name__ = intern_arrange('mutate__%s', name)

        return mutate


    #
    #   produce_transform
    #
    @share
    @privileged
    def produce_transform__ab(name, conjure):
        def transform(t, vary):
            a = t.a
            b = t.b

            a__2 = a.transform(vary)
            b__2 = b.transform(vary)

            if (a is a__2) and (b is b__2):
                return t

            return conjure(a__2, b__2)


        if __debug__:
            transform.__name__ = intern_arrange('transform_%s', name)

        return transform


    @share
    @privileged
    def produce_transform__abc(name, conjure):
        def transform(t, vary):
            a = t.a
            b = t.b
            c = t.c

            a__2 = a.transform(vary)
            b__2 = b.transform(vary)
            c__2 = c.transform(vary)

            if (a is a__2) and (b is b__2) and (c is c__2):
                return t

            return conjure(a__2, b__2, c__2)


        if __debug__:
            transform.__name__ = intern_arrange('transform_%s', name)

        return transform


    @share
    @privileged
    def produce_transform__abcd(name, conjure):
        def transform(t, vary):
            a = t.a
            b = t.b
            c = t.c
            d = t.d

            a__2 = a.transform(vary)
            b__2 = b.transform(vary)
            c__2 = c.transform(vary)
            d__2 = d.transform(vary)

            if (a is a__2) and (b is b__2) and (c is c__2) and (d is d__2):
                return t

            return conjure(a__2, b__2, c__2, d__2)


        if __debug__:
            transform.__name__ = intern_arrange('transform_%s', name)

        return transform


    @share
    @privileged
    def produce_transform__frill_a(name, conjure_with_frill):
        def transform(t, vary):
            frill = t.frill
            a     = t.a

            frill__2 = frill.transform(vary)
            a__2     = a    .transform(vary)

            if (frill is frill__2) and (a is a__2):
                return t

            return conjure_with_frill(frill__2, a__2)


        if __debug__:
            transform.__name__ = intern_arrange('transform_%s', name)

        return transform


    @share
    @privileged
    def produce_transform__frill_ab(name, conjure_with_frill):
        def transform(t, vary):
            frill = t.frill
            a     = t.a
            b     = t.b

            frill__2 = frill.transform(vary)
            a__2     = a    .transform(vary)
            b__2     = b    .transform(vary)

            if (frill is frill__2) and (a is a__2) and (b is b__2):
                return t

            return conjure_with_frill(frill__2, a__2, b__2)


        if __debug__:
            transform.__name__ = intern_arrange('transform_%s', name)

        return transform


    @share
    @privileged
    def produce_transform__frill__a_with_priority(name, priority, conjure_with_frill):
        def transform(t, vary):
            frill = t.frill
            a     = t.a

            frill__2 = frill.transform(vary)
            a__2     = a    .mutate   (vary, priority)

            if (frill is frill__2) and (a is a__2):
                return t

            return conjure_with_frill(frill__2, a__2)


        if __debug__:
            transform.__name__ = intern_arrange('transform_%s', name)

        return transform


    @share
    @privileged
    def produce_transform__frill__ab_with_priority(name, a_priority, b_priority, conjure_with_frill):
        def transform(t, vary):
            frill = t.frill
            a     = t.a
            b     = t.b

            frill__2 = frill.transform(vary)
            a__2     = a    .mutate(vary, a_priority)
            b__2     = b    .mutate(vary, b_priority)

            if (frill is frill__2) and (a is a__2) and (b is b__2):
                return t

            return conjure_with_frill(frill__2, a__2, b__2)


        if __debug__:
            transform.__name__ = intern_arrange('transform_%s', name)

        return transform


    @share
    @privileged
    def produce_transform__uncommented(name, uncommented):
        def transform(t, vary):
            if vary.remove_comments:
                return uncommented

            return t


        if __debug__:
            transform.__name__ = intern_arrange('transform__%s', name)

        return transform


    @share
    @privileged
    def produce_transform__frill__many(name, many_priority, conjure_with_frill):
        def transform(t, vary):
            frill    = t.frill
            many     = t.many
            iterator = iterate(many)

            frill_2 = frill.transform(vary)

            i = 0

            for v in iterator:
                v__2 = v.transform(vary)

                if v is not v__2:
                    break

                i += 1
            else:
                if frill is frill_2:
                    return t

                return conjure_with_frill(frill__2, many)

            many__2 = (
                          []          if i is 0 else
                          [many[0]]   if i is 1 else
                          List(many[:i])
                      )

            append = many__2.append

            append(v__2)

            for v in iterator:
                append(v.transform(vary))

            return conjure_with_frill(frill_2, conjure_tuple_of_many_expression(many__2))


        if __debug__:
            transform.__name__ = intern_arrange('transform_%s', name)

        return transform


    #
    #   transform
    #
    @share
    def transform__remove_comments_0(t, vary):
        if vary.remove_comments:
            return 0

        return t


    @share
    def transform__self(t, vary):
        return t


    #
    #   write
    #
    @share
    def write__123(t, w):
        t.k1.write(w)
        t.k2.write(w)
        t.k3.write(w)
