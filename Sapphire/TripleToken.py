#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.TripleToken')
def gem():
    conjure_line_marker = Shared.conjure_line_marker        #   Due to privileged
    lookup_line_marker  = Shared.lookup_line_marker         #   Due to privileged
    provide_line_marker = Shared.provide_line_marker        #   Due to privileged
    qi                  = Shared.qi                         #   Due to privileged
    qs                  = Shared.qs                         #   Due to privileged


    def construct_triple_token(t, s, first, second, third):
        assert (t.ends_in_newline is t.line_marker is false) and (t.newlines is 0)
        assert s == first.s + second.s + third.s
        assert '\n' not in s

        t.s      = s
        t.first  = first
        t.second = second
        t.third  = third


    def construct_triple_token__with_newlines(t, s, first, second, third, newlines, ends_in_newline):
        assert t.line_marker is false
        assert s == first.s + second.s + third.s
        assert ends_in_newline is (third.s[-1] == '\n')
        assert newlines >= 1

        t.s               = s
        t.first           = first
        t.second          = second
        t.third           = third
        t.newlines        = newlines
        t.ends_in_newline = ends_in_newline


    def construct_triple_operator__line_marker_1(t, s, first, second, third):
        assert (t.ends_in_newline is t.line_marker is true) and (t.newlines is 1)
        assert s == first.s + second.s + third.s
        assert s.count('\n') is 1
        assert third.s[-1] == '\n'

        t.s      = s
        t.first  = first
        t.second = second
        t.third  = third


    def construct_triple_token__line_marker__many(t, s, first, second, third, newlines):
        assert (t.ends_in_newline is t.line_marker is true) and (newlines > 1)
        assert s == first.s + second.s + third.s
        assert s.count('\n') == newlines
        assert third.s[-1] == '\n'

        t.s        = s
        t.first    = first
        t.second   = second
        t.third    = third
        t.newlines = newlines


    class BaseTripleOperator(KeywordAndOperatorBase):
        __slots__ = ((
            'first',         #   Operator+
            'second',        #   Operator+
            'third',         #   Operator+
        ))


        __init__ = construct_triple_token


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


    class RightParenthesis_Colon_LineMarker_1(BaseTripleOperator):
        __slots__                                  = (())
        display_name                               = r'):\n'
        ends_in_newline                            = true
        is__any__right_parenthesis__colon__newline = true
        is__right_parenthesis__colon__newline      = true
        line_marker                                = true
        newlines                                   = 1


        __init__ = construct_triple_operator__line_marker_1


    #
    #   ===  OLD  ===
    #
    def OLD__create_triple_token__with_newlines(Meta, first, second, third):
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


    def OLD__create_triple_token__line_marker(Meta, first, second, third):
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
    def OLD__produce_conjure_triple_token(name, Meta, line_marker = false):
        assert type(line_marker) is Boolean

        cache     = {}
        provide_1 = cache.setdefault
        lookup_1  = cache.get
        store_1   = cache.__setitem__

        create_triple_token = (
                OLD__create_triple_token__line_marker   if line_marker else
                OLD__create_triple_token__with_newlines
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


    conjure_all_index = OLD__produce_conjure_triple_token('all_index', AllIndex)

    conjure__comma__right_parenthesis__colon__line_marker = OLD__produce_conjure_triple_token(
            'comma__right_parenthesis__colon__line_marker',
            Comma_RightParenthesis_Colon_LineMarker_1,
            true,
        )

    conjure__parameter_0__colon__line_marker = OLD__produce_conjure_triple_token(
            'parameter_0__colon_newline',
            Parameter_0__Colon__LineMarker_1,
            true,
        )

    #
    #   ===  NEW  ===
    #
    def create_triple_token__with_newlines(Meta, s, first, second, third):
        assert s == first.s + second.s + third.s

        newlines = s.count('\n')

        return (
                   Meta(s, first, second, third)
                       if newlines is 0 else
                           (
                                 lookup_adjusted_meta(Meta)
                              or create_ActionWord_WithNewlines(Meta, construct_triple_token__with_newlines)
                           )(s, first, second, newlines, third, s[-1] == '\n')
               )


    def create_triple_token__line_marker(Meta, s, first, second, third):
        assert (s == first.s + second.s + third.s) and (s[-1] == '\n')

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
    def produce_conjure_triple_token(
            name, Meta, lookup, provide, conjure_first, conjure_second, conjure_third, conjure_third__ends_in_newline,
            
            line_marker = false,
    ):
        assert type(line_marker) is Boolean

        create_triple_token = (
                create_triple_token__line_marker   if line_marker else
                create_triple_token__with_newlines
            )


        def conjure_triple_token(middle_1, middle_2, end):
            triple_s = qs()[qi() : end]

            r = lookup(triple_s)
           
            if r is not none:
                assert (type(r) is Meta) or (type(r) is lookup_adjusted_meta(Meta))

                return r

            s        = qs()
            triple_s = intern_string(triple_s)

            return provide(
                       triple_s,
                       create_triple_token(
                           Meta,
                           triple_s,
                           conjure_first (s[qi()     : middle_1]),
                           conjure_second(s[middle_1 : middle_2]),
                           (conjure_third__ends_in_newline   if end is none else   conjure_third)(s[middle_2 : end]),
                       ),
                   )


        if __debug__:
            conjure_triple_token.__name__ = intern_arrange('conjure_%s', name)


        return conjure_triple_token


    @privileged
    def produce_evoke_triple_token__line_marker(name, Meta):
        def evoke_triple_token__line_marker(first, second, third):
            s = first.s + second.s + third.s

            r = lookup_line_marker(s)

            if r is not none:
                assert (r.first is first) and (r.second is second) and (r.third is third)

                return r

            s = intern_string(s)

            return provide_line_marker(s, create_triple_token__line_marker(Meta, s, first, second, third))


        if __debug__:
            evoke_triple_token__line_marker.__name__ = intern_arrange('evoke_%s__line_marker', name)

        return evoke_triple_token__line_marker



    @privileged
    def produce_conjure_triple_token__line_marker(name, Meta, conjure_first, conjure_second):
        def conjure_triple_token__line_marker(middle_1, middle_2):
            assert qi() < middle_1 < middle_2

            triple_s = qs()[qi() : ]

            r = lookup_line_marker(triple_s)
           
            if r is not none:
                assert (type(r) is Meta) or (type(r) is lookup_adjusted_meta(Meta))

                return r

            s        = qs()
            triple_s = intern_string(triple_s)

            return provide_line_marker(
                       triple_s,
                       create_triple_token__line_marker(
                           Meta,
                           triple_s,
                           conjure_first      (s[qi()     : middle_1]),
                           conjure_second     (s[middle_1 : middle_2]),
                           conjure_line_marker(s[middle_2 :         ]),
                       ),
                   )


        if __debug__:
            conjure_triple_token__line_marker.__name__ = intern_arrange('conjure_%s__line_marker', name)


        return conjure_triple_token__line_marker


    conjure__right_parenthesis__colon__line_marker = produce_conjure_triple_token__line_marker(
                                                         'right_parenthesis__colon__line_marker',
                                                         RightParenthesis_Colon_LineMarker_1,
                                                         conjure_right_parenthesis,
                                                         conjure_colon,
                                                     )

    evoke__right_parenthesis__colon__line_marker = produce_evoke_triple_token__line_marker(
                                                        'right_parenthesis__colon__line_marker',
                                                        RightParenthesis_Colon_LineMarker_1,
                                                    )


    #
    #   ===  SHARE  ===
    #
    share(
        #
        #   ===  OLD  ===
        #
        'conjure_all_index',    conjure_all_index,

        'conjure__comma__right_parenthesis__colon__line_marker',
            conjure__comma__right_parenthesis__colon__line_marker,

        'conjure__parameter_0__colon__line_marker',  conjure__parameter_0__colon__line_marker,

        #
        #   ===  NEW  ===
        #
        'conjure__right_parenthesis__colon__line_marker',   conjure__right_parenthesis__colon__line_marker,
        'evoke__right_parenthesis__colon__line_marker',     evoke__right_parenthesis__colon__line_marker,
    )
