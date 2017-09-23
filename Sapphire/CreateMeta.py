#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.CreateMeta')
def gem():
    adjusted_meta_cache = {}

    lookup_adjusted_meta  = adjusted_meta_cache.get
    provide_adjusted_meta = adjusted_meta_cache.setdefault


    @share
    def create_ActionWord_WithNewlines(Meta, constructor):
        assert lookup_adjusted_meta(Meta) is none


        class ActionWord_WithNewlines(Meta):
            __slots__ = ((
                'newlines',                                 #   Integer > 0
                'ends_in_newline',                          #   Boolean
            ))

            __init__ = constructor


        if __debug__:
            ActionWord_WithNewlines.__name__ = intern_arrange('%s_WithNewlines', Meta.__name__)

        return provide_adjusted_meta(Meta, ActionWord_WithNewlines)


    @share
    def create_ActionWord_LineMarker_Many(Meta, constructor):
        assert Meta.__name__.endswith('_1')
        assert lookup_adjusted_meta(Meta) is none


        class Actionword_LineMarker_Many(Meta):
            __slots__ = ((
                'newlines',                                 #   Integer > 1
            ))

            __init__ = constructor


        if __debug__:
            Actionword_LineMarker_Many.__name__ = intern_arrange('%s_Many', Meta.__name__[:-2])

        return provide_adjusted_meta(Meta, Actionword_LineMarker_Many)


    @share
    def create_BookcaseDualExpression_WithFrill(Meta):
        assert lookup_adjusted_meta(Meta) is none


        class BookcaseDualExpression_WithFrill(Meta):
            __slots__ = ((
                'frill',                #   TripleFrill
            ))


            def __init__(t, a, b, frill):
                t.a     = a
                t.b     = b
                t.frill = frill


            def __repr__(t):
                return arrange('<%s %r %r %r>', t.__class__.__name__, t.a, t.b, t.frill)


            def display_token(t):
                frill = t.frill

                return arrange('<%s %s %s %s %s %s>',
                               t.display_name,
                               frill.a.display_token(),
                               t.a    .display_token(),
                               frill.b.display_token(),
                               t.b    .display_token(),
                               frill.c.display_token())


        if __debug__:
            BookcaseDualExpression_WithFrill.__name__ = intern_arrange('%s_WithFrill', Meta.__name__)


        return provide_adjusted_meta(Meta, BookcaseDualExpression_WithFrill)


    @share
    def create_BookcaseExpression_WithFrill(Meta):
        assert lookup_adjusted_meta(Meta) is none


        class BookcaseExpression_WithFrill(Meta):
            __slots__ = ((
                'frill',                #   DualFrill
            ))


            def __init__(t, a, frill):
                t.a     = a
                t.frill = frill

            def __repr__(t):
                return arrange('<%s %r %r>', t.__class__.__name__, t.a, t.frill)


            def display_token(t):
                frill = t.frill

                return arrange('<%s %s %s %s>',
                               t.display_name,
                               frill.a.display_token(),
                               t.a    .display_token(),
                               frill.b.display_token())


        if __debug__:
            BookcaseExpression_WithFrill.__name__ = intern_arrange('%s_WithFrill', Meta.__name__)


        return provide_adjusted_meta(Meta, BookcaseExpression_WithFrill)


    @share
    def dump_newline_meta_cache():
        for k in iterate_values_sorted_by_key({ k.__name__ : k   for k in adjusted_meta_cache }):
            line('%s:', k.__name__)
            line('    %s', adjusted_meta_cache[k].__name__)


    share(
        'lookup_adjusted_meta',     lookup_adjusted_meta,
        'provide_adjusted_meta',    provide_adjusted_meta,
    )
