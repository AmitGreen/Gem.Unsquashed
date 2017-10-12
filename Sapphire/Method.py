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
    @privileged
    def produce_transform__uncommented(name, uncommented):
        def transform(t, mutate):
            if mutate.remove_comments:
                return uncommented

            return t


        if __debug__:
            transform.__name__ = intern_arrange('transform__%s', name)

        return transform


    @share
    def transform__ab(t, mutate):
        assert mutate.remove_comments

        a = t.a
        b = t.b

        a__2 = a.transform(mutate)
        b__2 = b.transform(mutate)

        if (a is a__2) and (b is b__2):
            return t

        return t.conjure(a__2, b__2)


    @share
    def transform__frill_a(t, mutate):
        frill = t.frill
        a     = t.a

        frill__2 = frill.transform(mutate)
        a__2     = a    .transform(mutate)

        if (frill is frill__2) and (a is a__2):
            return t

        return t.conjure_with_frill(frill__2, a__2)


    @share
    def transform__frill_ab(t, mutate):
        frill = t.frill
        a     = t.a
        b     = t.b

        frill__2 = frill.transform(mutate)
        a__2     = a    .transform(mutate)
        b__2     = b    .transform(mutate)

        if (frill is frill__2) and (a is a__2) and (b is b__2):
            return t

        return t.conjure_with_frill(frill__2, a__2, b__2)


    @share
    def transform__remove_comments_0(t, mutate):
        assert mutate.remove_comments

        if mutate.remove_comments:
            return 0

        return t


    @share
    def transform__self(t, mutate):
        return t
