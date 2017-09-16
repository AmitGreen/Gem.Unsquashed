#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.TripleToken')
def gem():
    def construct_triple_operator__line_marker_1(t, s, first, second, third):
        assert (t.ends_in_newline is t.line_marker is true) and (t.newlines is 1)
        assert s.count('\n') is 1
        assert s == first.s + second.s + third.s
        assert third.s[-1] == '\n'

        t.s      = s
        t.first  = first
        t.second = second
        t.third  = third


    class BaseTripleOperator(KeywordAndOperatorBase):
        __slots__ = ((
            'first',         #   Operator+
            'second',        #   Operator+
            'third',         #   Operator+
        ))


        def __init__(t, s, first, second, third):
            assert (t.ends_in_newline is t.line_marker is false) and (t.newlines is 0)
            assert '\n' not in s
            assert s == first.s + second.s + third.s

            t.s      = s
            t.first  = first
            t.second = second
            t.third  = third


        def __repr__(t):
            return arrange('<%s %r %r %r>', t.__class__.__name__, t.first, t.second, t.third)


        def display_full_token(t):
            display_name = t.display_name
            first_s      = t.first.s
            second_s     = t.second.s

            return arrange('<%s <%s> <%s>>',
                           display_name,
                           (portray_string(first_s)    if '\n' in first_s  else   first_s),
                           (portray_string(second_s)   if '\n' in second_s else   second_s))


        def display_token(t):
            display_name = t.display_name

            if display_name == t.s:
                return display_name

            first_s  = t.first .s
            second_s = t.second.s
            third_s  = t.third .s

            return arrange('<%s <%s> <%s> <%s>>',
                           display_name,
                           (portray_string(first_s)    if '\n' in first_s  else   first_s),
                           (portray_string(second_s)   if '\n' in second_s else   second_s),
                           (portray_string(third_s)    if '\n' in third_s  else   third_s))


        def write(t, w):
            w(t.first.s + t.second.s + t.third.s)


    class AllIndex(BaseTripleOperator):
        __slots__           = (())
        display_name        = '[:]'
        is_all_index        = true
        is_postfix_operator = true


    class Comma_RightParenthesis_Colon_LineMarker_1(BaseTripleOperator):
        __slots__                                  = (())
        display_name                               = r'):\n'
        ends_in_newline                            = true
        is__any__right_parenthesis__colon__newline = true
        line_marker                                = true
        newlines                                   = 1


        __init__ = construct_triple_operator__line_marker_1


    class Parameter_0__Colon__LineMarker_1(BaseTripleOperator):
        display_name                        = r'():\n'
        ends_in_newline                     = true
        is__parameter_0__colon__line_marker = true
        line_marker                         = true
        newlines                            = 1


        __init__ = construct_triple_operator__line_marker_1


    def construct_triple_token__with_newlines(t, s, first, second, third, newlines, ends_in_newline):
        assert newlines >= 1
        assert ends_in_newline is (s[-1] == '\n')
        assert t.line_marker is false

        t.s               = s
        t.first           = first
        t.second          = second
        t.third           = third
        t.newlines        = newlines
        t.ends_in_newline = ends_in_newline


    def construct_triple_token__line_marker__many(t, s, first, second, third, newlines):
        assert (t.ends_in_newline is t.line_marker is true) and (newlines >= 1) and (s[-1] == '\n')

        t.s        = s
        t.first    = first
        t.second   = second
        t.third    = third
        t.newlines = newlines


    def create_triple_token__with_newlines(Meta, first, second, third):
        s = intern_string(first.s + second.s + third.s)

        newlines = s.count('\n')

        return (
                   Meta(s, first, second, third)
                       if newlines is 0 else
                           (
                                 lookup_adjusted_meta(Meta)
                              or create_ActionWord_WithNewlines(Meta, construct_triple_token__with_newlines)
                           )(s, first, second, third, newlines, s[-1] == '\n')
               )


    def create_triple_token__line_marker(Meta, first, second, third):
        s = intern_string(first.s + second.s + third.s)

        newlines = s.count('\n')

        return (
                   Meta(s, first, second, third)
                       if newlines is 1 else
                       (
                             lookup_adjusted_meta(Meta)
                          or create_ActionWord_LineMarker_Many(Meta, construct_triple_token__line_marker__many)
                       )(s, first, second, third, newlines)
               )


    @privileged
    def produce_conjure_triple_token(name, Meta, line_marker = false):
        assert type(line_marker) is Boolean

        cache     = {}
        provide_1 = cache.setdefault
        lookup_1  = cache.get
        store_1   = cache.__setitem__

        create_triple_token = (
                create_triple_token__line_marker   if line_marker else
                create_triple_token__with_newlines
            )


        def conjure_triple_token(first, second, third):
            v = lookup_1(first)

            if v is none:
                return provide_1(first, create_triple_token(Meta, first, second, third))

            if type(v) is Map:
                w = v.get(second)

                if w is none:
                    return v.setdefault(second, create_triple_token(Meta, first, second, third))

                if type(w) is Map:
                    return (w.get(third)) or (w.setdefault(third, create_triple_token(Meta, first, second, third)))

                if w.third is third:
                    return w

                r = create_triple_token(Meta, first, second, third)

                v[second] = { w.third : v, third : r }

                return r

            if v.second is second:
                if v.third is third:
                    return v

                r = create_triple_token(Meta, first, second, third)

                store_1(first, { second : { third : v, third: r } })

                return r

            r = create_triple_token(Meta, first, second, third)

            store_1(first, { v.second : v , second : r })

            return r


        if __debug__:
            conjure_triple_token.__name__ = intern_arrange('conjure_%s', name)


        return conjure_triple_token


    conjure_all_index = produce_conjure_triple_token('all_index', AllIndex)

    conjure__comma__right_parenthesis__colon__line_marker = produce_conjure_triple_token(
            'comma__right_parenthesis__colon__line_marker',
            Comma_RightParenthesis_Colon_LineMarker_1,
            true,
        )

    conjure__parameter_0__colon__line_marker = produce_conjure_triple_token(
            'parameter_0__colon_newline',
            Parameter_0__Colon__LineMarker_1,
            true,
        )

    share(
        'conjure_all_index',    conjure_all_index,

        'conjure__comma__right_parenthesis__colon__line_marker',
            conjure__comma__right_parenthesis__colon__line_marker,

        'conjure__parameter_0__colon__line_marker',  conjure__parameter_0__colon__line_marker,
    )
