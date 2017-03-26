#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Tremolite.Build')
def gem():
    require_gem('Tremolite.Core')
    require_gem('Tremolite.Parse')


    class TremoliteBase(Object):
        __slots__ = ((
            'pattern',          #   String
            'portray',          #   String
        ))


        is_tremolite_or = false


        #def __init__(t, pattern, portray):
        #    t.pattern = pattern
        #    t.portray = portray


        def __add__(t, that):
            if type(that) is String:
                that = wrap_string(that)
            elif that.is_tremolite_or:
                that = wrap_parenthesis(that)

            return TremoliteAdd(t.pattern + that.pattern, t.portray + ' + ' + that.portray, ((t, that)) )


        def __or__(t, that):
            if type(that) is String:
                that = wrap_string(that)
            else:
                assert not that.is_tremolite_or

            return TremoliteOr(t.pattern + '|' + that.pattern, t.portray + ' | ' + that.portray, ((t, that)) )


        def __radd__(t, that):
            return wrap_string(that) + t


        def __ror__(t, that):
            return wrap_string(that) | t


        def __str__(t):
            return t.portray


        def compile_ascii_regular_expression(t):
            return compile_regular_expression(t.pattern, *parse_ascii_regular_expression(t.pattern))


    class TremoliteAdd(TremoliteBase):
        __slots__ = ((
            'many',             #   Tuple of TremoliteBase+
        ))


        repeatable = true
        singular   = false


        def __init__(t, pattern, portray, many):
            t.pattern = pattern
            t.portray = portray
            t.many    = many


        def __repr__(t):
            return arrange('<TremoliteAdd %s %s>',
                           portray_string(t.pattern),
                           ' '.join((portray_string(v)   if type(v) is String else   portray(v))  for v in t.many))


        def __add__(t, that):
            if type(that) is String:
                that = wrap_string(that)
            elif that.is_tremolite_or:
                that = wrap_parenthesis(that)

            return TremoliteAdd(t.pattern + that.pattern, t.portray + ' + ' + that.portray, t.many + ((that,)) )


    class TremoliteAnyOf(TremoliteBase):
        __slots__ = ((
            'many',             #   Tuple of String
        ))


        repeatable = true
        singular   = true


        def __init__(t, pattern, portray, many):
            t.pattern = pattern
            t.portray = portray
            t.many    = many


        def __repr__(t):
            return arrange('<TremoliteAnyOf %s %s>',
                           portray_string(t.pattern),
                           ' '.join(portray_string(v)  for v in t.many))


    class TremoliteEmpty(TremoliteBase):
        __slots__ = (())


        repeatable = false
        singular   = false


        def __init__(t):
            t.pattern = ''
            t.portray = intern_string('EMPTY')


        @static_method
        def __repr__():
            return '<TremoliteEmpty>'


    class TremoliteGroup(TremoliteBase):
        __slots__ = ((
            'group_name',       #   String
            'inside',           #   String
        ))


        repeatable = true
        singular   = true


        def __init__(t, pattern, portray, group_name, inside):
            t.pattern    = pattern
            t.portray    = portray
            t.group_name = group_name
            t.inside     = inside


        def __repr__(t):
            return arrange('<TremoliteGroup %s %r>', t.group_name, t.inside)


    class TremoliteOr(TremoliteBase):
        __slots__ = ((
            'many',             #   Tuple of TremoliteBase+
        ))


        is_tremolite_or = true
        repeatable      = true
        singular        = false


        def __init__(t, pattern, portray, many):
            t.pattern = pattern
            t.portray = portray
            t.many    = many


        def __repr__(t):
            return arrange('<TremoliteOr %s %s>',
                           portray_string(t.pattern),
                           ' '.join((portray_string(v)   if type(v) is String else   portray(v))  for v in t.many))


        def __add__(t, that):
            return wrap_parenthesis(t) + that


        def __or__(t, that):
            if type(that) is String:
                that = wrap_string(that)

            return TremoliteOr(t.pattern + '|' + that.pattern, t.portray + ' | ' + that.portray, t.many + ((that,)) )


    class TremoliteMultiple(TremoliteBase):
        __slots__ = ((
            'exact',            #   String
        ))


        repeatable = true
        singular   = false


        def __init__(t, pattern, portray, exact):
            t.pattern  = pattern
            t.portray  = portray
            t.exact    = exact


        def __repr__(t):
            if t.pattern is t.exact:
                return arrange('<TremoliteMultiple %s>', portray_string(t.pattern))

            return arrange('<TremoliteMultiple %s %s>', portray_string(t.pattern), portray_string(t.exact))


    class TremoliteParenthesis(TremoliteBase):
        __slots__ = ((
            'inside',                   #   String
        ))


        repeatable = true
        singular   = true


        def __init__(t, pattern, portray, inside):
            assert inside.repeatable

            t.pattern = intern_string(pattern)
            t.portray = portray
            t.inside  = inside


        def __repr__(t):
            return arrange('<TremoliteParenthesis %s %r>', portray_string(t.pattern), t.inside)


    class TremoliteRepeat(TremoliteBase):
        __slots__ = ((
            'repeated',                 #   String
        ))


        repeatable = false
        singular   = true


        def __init__(t, pattern, portray, repeated):
            t.pattern  = pattern
            t.portray  = portray
            t.repeated = repeated


        def __repr__(t):
            return arrange('<TremoliteRepeat %s %r>', portray_string(t.pattern), t.repeated)


    class TremoliteSingular(TremoliteBase):
        __slots__ = ((
            'exact',                    #   String
        ))


        repeatable = true
        singular   = true


        def __init__(t, pattern, portray, exact):
            t.pattern  = pattern
            t.portray  = portray
            t.exact    = exact


        def __repr__(t):
            if t.pattern is t.exact:
                return arrange('<TremoliteSingular %s>', portray_string(t.pattern))

            return arrange('<TremoliteSingular %s %s>', portray_string(t.pattern), portray_string(t.exact))


    class TremoliteSpecialSingular(TremoliteBase):
        __slots__ = ((
            'repeatable',               #   Boolean
        ))


        singular = true


        def __init__(t, pattern, portray, repeatable):
            t.pattern    = intern_string(pattern)
            t.portray    = intern_string(portray)
            t.repeatable = repeatable


        def __repr__(t):
            return arrange('<TremoliteSpecialSingular %s %s>', portray_string(t.pattern), t.portray)


    def create_exact(s):
        assert length(s) >= 1

        many   = []
        append = many.append

        for c in s:
            a = lookup_ascii(c)

            if not a.is_printable:
                raise_runtime_error('invalid character <%s> passed to EXACT(%s)', portray_string(c), portray_string(s))

            append(a.pattern)

        return intern_string(''.join(many))


    def create_repeat(name, inside, suffix):
        if type(inside) is String:
            inside = wrap_string(inside)
        else:
            assert inside.repeatable

        return TremoliteRepeat(
                   (
                       intern_arrange(inside.pattern + suffix)
                           if inside.singular else
                               intern_arrange('(?:%s)%s', inside.pattern, suffix)
                   ),
                   arrange('%s(%s)', name, inside),
                   inside,
               )


    def wrap_parenthesis(inside, invisible = false):
        assert not inside.singular

        return TremoliteParenthesis(
                   intern_arrange('(?:%s)', inside.pattern),
                   (inside.portray   if invisible else   intern_arrange('(%s)', inside.portray)),
                   inside,
               )


    def wrap_string(s):
        assert (type(s) is String) and (length(s) >= 1)

        return (TremoliteMultiple   if length(s) > 1 else   TremoliteSingular)(
                   create_exact(s), intern_string(portray_string(s)), intern_string(s),
               )


    @export
    def ANY_OF(*arguments):
        assert length(arguments) > 0

        many   = ['[']
        append = many.append

        for s in arguments:
            if length(s) is 1:
                assert lookup_ascii(s).is_printable

                many.append(s)
            else:
                assert (length(s) is 3) and (s[1] is '-')

                a0 = lookup_ascii(s[0])
                a2 = lookup_ascii(s[2])

                if not a0.is_printable:
                    raise_runtime_error('invalid character <%s> passed to ANY(%s)', portray_string(s[0]), portray_string(s))

                if not a2.is_printable:
                    raise_runtime_error('invalid character <%s> passed to ANY(%s)', portray_string(s[2]), portray_string(s))

                many.append(a0.pattern + '-' + a2.pattern)

        many.append(']')

        return TremoliteAnyOf(
                   intern_string(''.join(many)),
                   intern_arrange('ANY(%s)', ', '.join(portray_string(s)   for s in arguments)),
                   Tuple(intern_string(s)   for s in arguments)
               )


    @export
    def EXACT(s):
        assert length(s) >= 1

        return (TremoliteMultiple   if length(s) > 1 else   TremoliteSingular)(
                   create_exact(s), intern_arrange('EXACT(%s)', portray_string(s)), intern_string(s),
               )


    @export
    def GROUP(group_name, inside):
        if type(inside) is String:
            inside = wrap_string(inside)

        return TremoliteGroup(
                   intern_arrange('(?P<%s>%s)', group_name, inside.pattern),
                   arrange('GROUP(%s, %s)', portray_string(group_name), inside),
                   group_name,
                   inside,
               )


    @export
    def ONE_OR_MORE(inside):
        return create_repeat('ONE_OR_MORE', inside, '+')


    @export
    def OPTIONAL(inside):
        return create_repeat('OPTIONAL', inside, '?')


    @export
    def ZERO_OR_MORE(inside):
        return create_repeat('ZERO_OR_MORE', inside, '*')


    export(
        'EMPTY',            TremoliteEmpty(),
        'END_OF_STRING',    TremoliteSpecialSingular(r'\Z', 'END_OF_STRING', false),
    )
