#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Tremolite.Build')
def gem():
    require_gem('Tremolite.Core')


    class TremoliteBase(Object):
        __slots__ = ((
            'pattern',          #   String
        ))


        is_tremolite     = true
        is_tremolite_add = false


        #def __init__(t, pattern):
        #    t.pattern = pattern


        def __add__(t, that):
            if that.__class__ is String:
                that_pattern = create_exact(that)
            else:
                that_pattern = that.pattern

            if t.is_tremolite_add:
                return TremoliteAdd(t.pattern + that_pattern, t.many + ((that,)) )

            return TremoliteAdd(t.pattern + that_pattern, ((t, that)) )


        def __radd__(t, that):
            assert that.__class__ is String

            return TremoliteAdd(create_exact(that) + t.pattern, ((that, t)) )


    class TremoliteAdd(TremoliteBase):
        __slots__ = ((
            'many',             #   Tuple of TremoliteBase+
        ))


        is_tremolite_add = true
        singular         = false


        def __init__(t, pattern, many):
            t.pattern = pattern
            t.many    = many

        def __repr__(t):
            return arrange('<TremoliteAdd %s %s>',
                           portray_string(t.pattern),
                           ' '.join((portray_string(v)   if v.__class__ is String else   portray(v))  for v in t.many))


        def __str__(t):
            return ' + '.join((portray_string(v)   if v.__class__  is String else   String(v))   for v in t.many)


    class TremoliteGroup(TremoliteBase):
        __slots__ = ((
            'group_name',       #   String
            'inside',           #   String
        ))


        singular = true


        def __init__(t, pattern, group_name, inside):
            t.pattern    = pattern
            t.group_name = group_name
            t.inside     = inside


        def __repr__(t):
            return arrange('<TremoliteGroup %s %s>',
                           t.group_name,
                           portray_string(t.inside)   if t.inside.__class__ is String else   portray(t.inside))


        def __str__(t):
            return arrange('GROUP(%s, %s)',
                           t.group_name,
                           portray_string(t.inside)   if t.inside.__class__ is String else   t.inside)


    class TremoliteMultiple(TremoliteBase):
        __slots__ = ((
            'exact',            #   String
        ))


        singular = false


        def __init__(t, pattern, exact):
            t.pattern  = intern_string(pattern)
            t.exact    = intern_string(exact)


        def __repr__(t):
            return arrange('<TremoliteMultiple %s %s>',
                           portray_string(t.pattern), portray_string(t.exact))


        def __str__(t):
            return arrange('EXACT(%s)', portray_string(t.exact))


    class TremoliteSpecial(TremoliteBase):
        __slots__ = ((
            'singular',         #   Boolean
            'original',         #   String
        ))


        is_right_side_pattern = true


        def __init__(t, pattern, singular, original):
            t.pattern  = intern_string(pattern)
            t.singular = singular
            t.original = intern_string(original)


        def __repr__(t):
            return arrange('<TremoliteSpecial %s %s %s>', portray_string(t.pattern), t.singular, t.original)


        def __str__(t):
            return t.original

            
    class TremoliteSingular(TremoliteBase):
        __slots__ = ((
            'exact',            #   String
        ))


        singular     = true


        def __init__(t, pattern, exact):
            t.pattern  = intern_string(pattern)
            t.exact    = intern_string(exact)


        def __repr__(t):
            return arrange('<TremoliteSingular %s %s>',
                           portray_string(t.pattern), portray_string(t.exact))


        def __str__(t):
            return arrange('EXACT(%s)', portray_string(t.exact))


    END_OF_STRING = TremoliteSpecial(r'\Z', true, 'END_OF_STRING')


    def find_pattern_exact(c, s):
        a = lookup_ascii(c)

        if not a.is_printable:
            raise_runtime_error('Invalid character <%s> passed to EXACT(%s)', portray_string(c), portray_string(s))

        return a.pattern


    def create_exact(s):
        assert length(s) >= 1

        return intern_string(''.join(find_pattern_exact(c, s)   for c in s))


    @export
    def EXACT(s):
        assert length(s) >= 1

        if length(s) == 1:
            return TremoliteSingular(create_exact(s), intern_string(s))

        return TremoliteMultiple(create_exact(s), intern_string(s))


    @export
    def GROUP(group_name, inside):
        if type(inside) is String:
            pattern = create_exact(inside)
        else:
            pattern = inside.pattern

        return TremoliteGroup(intern_string('(?P<' + group_name + '>' + pattern + ')'), group_name, inside)


    export(
        'END_OF_STRING',    END_OF_STRING,
    )


    test = r'fake: \r' + GROUP('abc', '(abc)') + 'end' + END_OF_STRING

    line('%s', test)
    line('%r', test)
