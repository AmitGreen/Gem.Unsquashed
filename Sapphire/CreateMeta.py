#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.CreateMeta')
def gem():
    adjusted_meta_cache = {}

    lookup_adjusted_meta = adjusted_meta_cache.get
    store_adjusted_meta  = adjusted_meta_cache.__setitem__


    @share
    def count_newlines__line_marker(t):
        assert (t.ends_in_newline is t.line_marker is true)
        assert t.s[-1] == '\n'
        assert t.newlines == t.s.count('\n')

        return t.newlines


    @share
    def conjure_ActionWord_WithNewlines(Meta, constructor):
        ActionWord_WithNewlines = lookup_adjusted_meta(Meta)

        if ActionWord_WithNewlines is none:
            class ActionWord_WithNewlines(Meta):
                __slots__ = ((
                    'ends_in_newline',                          #   Boolean
                    'newlines',                                 #   Integer > 0
                ))

                __init__ = constructor


                def count_newlines(t):
                    assert t.ends_in_newline is (t.s[-1] == '\n')
                    assert t.line_marker is false
                    assert t.newlines == t.s.count('\n')

                    return t.newlines


            if __debug__:
                ActionWord_WithNewlines.__name__ = intern_arrange('%s_WithNewlines', Meta.__name__)

            store_adjusted_meta(Meta, ActionWord_WithNewlines)

        return ActionWord_WithNewlines


    @share
    def conjure_ActionWord_LineMarker_Many(Meta, constructor):
        assert Meta.__name__.endswith('_1')

        Actionword_LineMarker_Many = lookup_adjusted_meta(Meta)

        if Actionword_LineMarker_Many is none:
            class Actionword_LineMarker_Many(Meta):
                __slots__ = ((
                    'newlines',                                 #   Integer > 1
                ))

                __init__ = constructor



            if __debug__:
                Actionword_LineMarker_Many.__name__ = intern_arrange('%s_Many', Meta.__name__[:-2])

            store_adjusted_meta(Meta, Actionword_LineMarker_Many)

        return Actionword_LineMarker_Many


    @share
    def dump_newline_meta_cache():
        for k in iterate_values_sorted_by_key({ k.__name__ : k   for k in adjusted_meta_cache }):
            line('%s:', k.__name__)
            line('    %s', adjusted_meta_cache[k].__name__)


    share(
        'lookup_adjusted_meta',     lookup_adjusted_meta,
        'store_adjusted_meta',      store_adjusted_meta,
    )
