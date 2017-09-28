#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.QuadrupleToken')
def gem():
    conjure_line_marker  = Shared.conjure_line_marker       #   Due to privileged
    lookup_adjusted_meta = Shared.lookup_adjusted_meta      #   Due to privileged
    lookup_line_marker   = Shared.lookup_line_marker        #   Due to privileged
    lookup_normal_token  = Shared.lookup_normal_token       #   Due to privileged
    provide_line_marker  = Shared.provide_line_marker       #   Due to privileged
    provide_normal_token = Shared.provide_normal_token      #   Due to privileged
    qi                   = Shared.qi                        #   Due to privileged
    qs                   = Shared.qs                        #   Due to privileged


    def construct_quadruple_token(t, s, a, b, c, d):
        assert (t.ends_in_newline is t.line_marker is false) and (t.newlines is 0)
        assert s == a.s + b.s + c.s + d.s
        assert '\n' not in s

        t.s = s
        t.a = a
        t.b = b
        t.c = c
        t.d = d


    if 0:
        def construct_quadruple_token__with_newlines(t, s, a, b, c, d, ends_in_newline, newlines):
            assert t.line_marker is false
            assert s == a.s + b.s + c.s + d.s
            assert ends_in_newline is (d.s[-1] == '\n')
            assert newlines >= 1

            t.s               = s
            t.a               = a
            t.b               = b
            t.c               = c
            t.d               = d
            t.ends_in_newline = ends_in_newline
            t.newlines        = newlines


    def construct_quadruple_operator__line_marker_1(t, s, a, b, c, d):
        assert (t.ends_in_newline is t.line_marker is true) and (t.newlines is 1)
        assert s == a.s + b.s + c.s + d.s
        assert s.count('\n') is 1
        assert d.s[-1] == '\n'

        t.s = s
        t.a = a
        t.b = b
        t.c = c
        t.d = d


    def construct_quadruple_token__line_marker__many(t, s, a, b, c, d, newlines):
        assert (t.ends_in_newline is t.line_marker is true) and (newlines > 1)
        assert s == a.s + b.s + c.s + d.s
        assert s.count('\n') == newlines
        assert d.s[-1] == '\n'

        t.s        = s
        t.a        = a
        t.b        = b
        t.c        = c
        t.d        = d
        t.newlines = newlines


    def display_token__indented__keyword__colon__line_marker(t):
        return arrange('<%s +%d %s %s %s>',
                       t.display_name,
                       t.a.total,
                       t.b.display_token(),
                       t.c.display_token(),
                       t.d.display_token())


    class BaseQuadrupleOperator(KeywordAndOperatorBase):
        __slots__ = ((
            'a',                        #   Operator+
            'b',                        #   Operator+
            'c',                        #   Operator+
            'd',                        #   Operator+
        ))


        __init__ = construct_quadruple_token


        def __repr__(t):
            return arrange('<%s %r %r %r %r>', t.__class__.__name__, t.a, t.b, t.c, t.d)


        def display_full_token(t):
            display_name = t.display_name
            a_s          = t.a.s
            b_s          = t.b.s
            c_s          = t.c.s
            d_s          = t.d.s

            return arrange('<%s <%s> <%s> <%s> <%s>>',
                           display_name,
                           (portray_string(a_s)   if '\n' in a_s else   a_s),
                           (portray_string(b_s)   if '\n' in b_s else   b_s),
                           (portray_string(c_s)   if '\n' in b_s else   c_s),
                           (portray_string(d_s)   if '\n' in d_s else   d_s))


        def display_token(t):
            display_name = t.display_name

            if display_name == t.s:
                return display_name

            a_s = t.a.s
            b_s = t.b.s
            c_s = t.c.s
            d_s = t.d.s

            return arrange('<%s <%s> <%s> <%s> <%s>>',
                           display_name,
                           (portray_string(a_s)   if '\n' in a_s else   a_s),
                           (portray_string(b_s)   if '\n' in b_s else   b_s),
                           (portray_string(c_s)   if '\n' in c_s else   c_s),
                           (portray_string(d_s)   if '\n' in d_s else   d_s))


    def create_quadruple_token__with_newlines(Meta, s, a, b, c, d):
        assert s == a.s + b.s + c.s + d.s

        newlines = s.count('\n')

        return (
                   Meta(s, a, b, c, d)
                       if newlines is 0 else
                           conjure_ActionWord_WithNewlines(
                               Meta, construct_quadruple_token__with_newlines,
                           )(s, a, b, c, d, s[-1] == '\n', newlines)
               )


    def create_quadruple_token__line_marker(Meta, s, a, b, c, d):
        assert (s == a.s + b.s + c.s + d.s) and (s[-1] == '\n')

        newlines = s.count('\n')

        return (
                   Meta(s, a, b, c, d)
                       if newlines is 1 else
                           conjure_ActionWord_LineMarker_Many(
                               Meta, construct_quadruple_token__line_marker__many,
                           )(s, a, b, c, d, newlines)
               )


    @privileged
    def produce_conjure_quadruple_token(
            name, Meta,
            
            lookup      = lookup_normal_token,
            provide     = provide_normal_token,
            line_marker = false
    ):
        if line_marker:
            assert (lookup is lookup_normal_token) and (provide is provide_normal_token)

            create_quadruple_token = create_quadruple_token__line_marker
            lookup                 = lookup_line_marker
            provide                = provide_line_marker
        else:
            create_quadruple_token = create_quadruple_token__with_newlines


        def conjure_quadruple_token(a, b, c, d):
            s = a.s + b.s + c.s + d.s

            r = lookup(s)

            if r is not none:
                assert (r.a is a) and (r.b is b) and (r.c is c) and (r.d is d)

                return r

            s = intern_string(s)

            return provide(s, create_quadruple_token(Meta, s, a, b, c, d))


        if __debug__:
            conjure_quadruple_token.__name__ = intern_arrange('conjure_%s', name)

        return conjure_quadruple_token


    @privileged
    def produce_evoke_quadruple_token(
            name, Meta, conjure_a, conjure_b, conjure_c,
            
            conjure_d                  = absent,
            conjure_d__ends_in_newline = absent,
            lookup                     = lookup_normal_token,
            provide                    = provide_normal_token,
            line_marker                = false,
    ):
        assert type(line_marker) is Boolean


        if line_marker:
            assert (lookup is lookup_normal_token) and (provide is provide_normal_token)
            assert (conjure_d is conjure_d__ends_in_newline is absent)


            def evoke_quadruple_token(a_end, b_end, c_end):
                #
                #   Note: 'qi() <= a_end', since for indented token there might be no indentation
                #
                assert qi() <= a_end < b_end < c_end

                full = qs()[qi() : ]

                r = lookup_line_marker(full)
               
                if r is not none:
                    assert (type(r) is Meta) or (type(r) is lookup_adjusted_meta(Meta))

                    return r

                full = intern_string(full)
                s    = qs()

                return provide_line_marker(
                           full,
                           create_quadruple_token__line_marker(
                               Meta,
                               full,
                               conjure_a          (s[qi()  : a_end]),
                               conjure_b          (s[a_end : b_end]),
                               conjure_c          (s[b_end : c_end]),
                               conjure_line_marker(s[c_end :      ]),
                           ),
                       )
        else:
            def evoke_quadruple_token(a_end, b_end, c_end, d_end):
                assert qi() < a_end < b_end < c_end < d_end

                full = qs()[qi() : d_end]

                r = lookup(full)
               
                if r is not none:
                    assert (type(r) is Meta) or (type(r) is lookup_adjusted_meta(Meta))

                    return r

                full = intern_string(full)
                s    = qs()

                return provide(
                           full,
                           create_quadruple_token__with_newlines(
                               Meta,
                               full,
                               conjure_a(s[qi()  : a_end]),
                               conjure_b(s[a_end : b_end]),
                               conjure_c(s[b_end : c_end]),
                               (conjure_d__ends_in_newline   if d_end is none else   conjure_d)(s[c_end : d_end]),
                           ),
                       )


        if __debug__:
            evoke_quadruple_token.__name__ = intern_arrange('evoke_%s', name)


        return evoke_quadruple_token


    class Comma_RightParenthesis_Colon_LineMarker_1(BaseQuadrupleOperator):
        __slots__                                  = (())
        display_name                               = r',):\n'
        ends_in_newline                            = true
        is__any__right_parenthesis__colon__newline = true
        line_marker                                = true
        newlines                                   = 1


        __init__       = construct_quadruple_operator__line_marker_1
        count_newlines = count_newlines__line_marker


    class DotNameQuadruplet(BaseQuadrupleOperator):
        __slots__           = (())
        #   [
        display_name        = '.name-quadruplet'
        is_postfix_operator = true


    class Indented_Else_Colon_LineMarker(BaseQuadrupleOperator):
        __slots__       = (())
        display_name    = 'else'
        ends_in_newline = true
        keyword         = 'else'
        line_marker     = true
        newlines        = 1


        __init__       = construct_quadruple_operator__line_marker_1
        count_newlines = count_newlines__line_marker
        display_token  = display_token__indented__keyword__colon__line_marker
        indentation    = BaseQuadrupleOperator.a


    class Indented_Except_Colon_LineMarker(BaseQuadrupleOperator):
        __slots__       = (())
        display_name    = 'except'
        ends_in_newline = true
        keyword         = 'except'
        line_marker     = true
        newlines        = 1


        __init__       = construct_quadruple_operator__line_marker_1
        count_newlines = count_newlines__line_marker
        display_token  = display_token__indented__keyword__colon__line_marker
        indentation    = BaseQuadrupleOperator.a


    class Indented_Try_Colon_LineMarker(BaseQuadrupleOperator):
        __slots__       = (())
        display_name    = 'try'
        ends_in_newline = true
        keyword         = 'try'
        line_marker     = true
        newlines        = 1


        __init__       = construct_quadruple_operator__line_marker_1
        count_newlines = count_newlines__line_marker
        display_token  = display_token__indented__keyword__colon__line_marker
        indentation    = BaseQuadrupleOperator.a


    class Parameter_0__Colon__LineMarker_1(BaseQuadrupleOperator):
        display_name                        = r'():\n'
        ends_in_newline                     = true
        is__parameter_0__colon__line_marker = true
        line_marker                         = true
        newlines                            = 1


        __init__       = construct_quadruple_operator__line_marker_1
        count_newlines = count_newlines__line_marker


    conjure__comma__right_parenthesis__colon__line_marker = produce_conjure_quadruple_token(
            'comma__right_parenthesis__colon__line_marker',
            Comma_RightParenthesis_Colon_LineMarker_1,

            line_marker = true,
        )

    conjure_dot_name_quadruplet = produce_conjure_quadruple_token('.name-quadruplet', DotNameQuadruplet)

    conjure__parameter_0__colon__line_marker = produce_conjure_quadruple_token(
            'parameter_0__colon_newline',
            Parameter_0__Colon__LineMarker_1,

            line_marker = true,
        )

    evoke__comma__right_parenthesis__colon__line_marker = produce_evoke_quadruple_token(
            'comma__right_parenthesis__colon__line_marker',
            Comma_RightParenthesis_Colon_LineMarker_1,
            conjure_comma,
            conjure_right_parenthesis,
            conjure_colon,

            line_marker = true,
        )

    evoke_indented__else__colon__line_marker = produce_evoke_quadruple_token(
            'indented__else__colon__line_marker',
            Indented_Else_Colon_LineMarker,
            conjure_indentation,
            conjure_keyword_else,
            conjure_colon,

            line_marker = true,
        )

    evoke_indented__except__colon__line_marker = produce_evoke_quadruple_token(
            'indented__except__colon__line_marker',
            Indented_Except_Colon_LineMarker,
            conjure_indentation,
            conjure_keyword_except,
            conjure_colon,

            line_marker = true,
        )

    evoke_indented__try__colon__line_marker = produce_evoke_quadruple_token(
            'indented__try__colon__line_marker',
            Indented_Try_Colon_LineMarker,
            conjure_indentation,
            conjure_keyword_try,
            conjure_colon,

            line_marker = true,
        )

    evoke__parameter_0__colon__line_marker = produce_evoke_quadruple_token(
            'parameter_0__colon_newline',
            Parameter_0__Colon__LineMarker_1,
            conjure_left_parenthesis,
            conjure_right_parenthesis,
            conjure_colon,

            line_marker = true,
        )

    share(
        'conjure__comma__right_parenthesis__colon__line_marker',
            conjure__comma__right_parenthesis__colon__line_marker,

        'conjure_dot_name_quadruplet',                          conjure_dot_name_quadruplet,
        'conjure__parameter_0__colon__line_marker',             conjure__parameter_0__colon__line_marker,
        'evoke__comma__right_parenthesis__colon__line_marker',  evoke__comma__right_parenthesis__colon__line_marker,
        'evoke_indented__else__colon__line_marker',             evoke_indented__else__colon__line_marker,
        'evoke_indented__except__colon__line_marker',           evoke_indented__except__colon__line_marker,
        'evoke_indented__try__colon__line_marker',              evoke_indented__try__colon__line_marker,
        'evoke__parameter_0__colon__line_marker',               evoke__parameter_0__colon__line_marker,
    )
