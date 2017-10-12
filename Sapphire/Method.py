#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Method')
def gem():
    @share
    def find_require_gem__0(t, e):
        pass


    @share
    def is_name__0(t, name):
        return false


    @share
    def mutate__self(t, vary, priority):
        return t


    @share
    def mutate__ab(t, vary, priority):
        assert vary.remove_comments

        a = t.a
        b = t.b

        a__2 = a.mutate(vary, priority)
        b__2 = b.mutate(vary, priority)

        if (a is a__2) and (b is b__2):
            return t

        return t.conjure(a__2, b__2)


    @share
    def mutate__abc(t, vary, priority):
        assert vary.remove_comments

        a = t.a
        b = t.b
        c = t.c

        a__2 = a.mutate(vary, priority)
        b__2 = b.mutate(vary, priority)
        c__2 = c.mutate(vary, priority)

        if (a is a__2) and (b is b__2) and (c is c__2):
            return t

        return t.conjure(a__2, b__2, c__2)


    @share
    @privileged
    def produce__mutate__ab__priority(name, a_priority, b_priority):
        def mutate(t, vary, priority):
            assert vary.remove_comments

            a = t.a
            b = t.b

            a__2 = a.mutate(vary, a_priority)
            b__2 = b.mutate(vary, b_priority)

            if (a is a__2) and (b is b__2):
                return t

            return t.conjure(a__2, b__2)


        if __debug__:
            mutate.__name__ = intern_arrange('mutate__%s', name)

        return mutate


    @share
    @privileged
    def produce_mutate___frill__a__priority(name, priority):
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
    def produce_mutate___frill__a_with_priority(name, a_priority):
        def mutate(t, vary, priority):
            frill = t.frill
            a     = t.a

            frill__2 = frill.transform(vary)
            a__2     = a    .mutate   (vary, a_priority)

            if (frill is frill__2) and (a is a__2):
                return t

            return t.conjure_with_frill(frill__2, a__2)

        if __debug__:
            mutate.__name__ = intern_arrange('mutate_%s', name)

        return mutate


    @share
    @privileged
    def produce_mutate__frill__ab__priority(name, frill_priority, a_priority, b_priority):
        def mutate(t, vary, priority):
            frill = t.frill
            a     = t.a
            b     = t.b

            frill__2 = frill.mutate(vary, frill_priority)
            a__2     = a    .mutate(vary, a_priority)
            b__2     = b    .mutate(vary, b_priority)

            if (frill is frill__2) and (a is a__2) and (b is b__2):
                return t

            return t.conjure_with_frill(frill__2, a__2, b__2)

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


    @share
    @privileged
    def produce_transform___frill__a_with_priority(name, priority):
        def transform(t, vary):
            frill = t.frill
            a     = t.a

            frill__2 = frill.transform(vary)
            a__2     = a    .mutate   (vary, priority)

            if (frill is frill__2) and (a is a__2):
                return t

            return t.conjure_with_frill(frill__2, a__2)

        if __debug__:
            transform.__name__ = intern_arrange('transform_%s', name)

        return transform


    @share
    @privileged
    def produce_transform___frill__ab_with_priority(name, a_priority, b_priority):
        def transform(t, vary):
            frill = t.frill
            a     = t.a
            b     = t.b

            frill__2 = frill.transform(vary)
            a__2     = a    .mutate(vary, a_priority)
            b__2     = b    .mutate(vary, b_priority)

            if (frill is frill__2) and (a is a__2) and (b is b__2):
                return t

            return t.conjure_with_frill(frill__2, a__2, b__2)

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
    def transform__ab(t, vary):
        a = t.a
        b = t.b

        a__2 = a.transform(vary)
        b__2 = b.transform(vary)

        if (a is a__2) and (b is b__2):
            return t

        return t.conjure(a__2, b__2)


    @share
    def transform__abc(t, vary):
        a = t.a
        b = t.b
        c = t.c

        a__2 = a.transform(vary)
        b__2 = b.transform(vary)
        c__2 = c.transform(vary)

        if (a is a__2) and (b is b__2) and (c is c__2):
            return t

        return t.conjure(a__2, b__2, c__2)


    @share
    def transform__frill_a(t, vary):
        frill = t.frill
        a     = t.a

        frill__2 = frill.transform(vary)
        a__2     = a    .transform(vary)

        if (frill is frill__2) and (a is a__2):
            return t

        return t.conjure_with_frill(frill__2, a__2)


    @share
    def transform__frill_ab(t, vary):
        frill = t.frill
        a     = t.a
        b     = t.b

        frill__2 = frill.transform(vary)
        a__2     = a    .transform(vary)
        b__2     = b    .transform(vary)

        if (frill is frill__2) and (a is a__2) and (b is b__2):
            return t

        return t.conjure_with_frill(frill__2, a__2, b__2)


    @share
    def transform__remove_comments_0(t, vary):
        assert vary.remove_comments

        if vary.remove_comments:
            return 0

        return t


    @share
    def transform__self(t, vary):
        return t
