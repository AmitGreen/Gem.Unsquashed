#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Tremolite.Build')
def gem():
    require_gem('Tremolite.Core')


    class TremoliteBase(Object):
        __slots__ = ((
            'pattern',          #   String
            'portray',          #   String
        ))


        is_tremolite     = true
        is_tremolite_add = false


        #def __init__(t, pattern, portray):
        #    t.pattern = pattern
        #    t.portray = portray


        def __add__(t, that):
            that = WRAP(that)

            if t.is_tremolite_add:
                return TremoliteAdd(t.pattern + that.pattern, t.portray + ' + ' + that.portray, t.many + ((that,)) )

            return TremoliteAdd(t.pattern + that.pattern, t.portray + ' + ' + that.portray, ((t, that)) )


        def __radd__(t, that):
            return WRAP(that) + t


        def __str__(t):
            return t.portray


    class TremoliteAdd(TremoliteBase):
        __slots__ = ((
            'many',             #   Tuple of TremoliteBase+
        ))


        is_tremolite_add = true
        singular         = false


        def __init__(t, pattern, portray, many):
            t.pattern = pattern
            t.portray = portray
            t.many    = many

        def __repr__(t):

            return arrange('<TremoliteAdd %s %s>',
                           portray_string(t.pattern),
                           ' '.join((portray_string(v)   if v.__class__ is String else   portray(v))  for v in t.many))


    class TremoliteGroup(TremoliteBase):
        __slots__ = ((
            'group_name',       #   String
            'inside',           #   String
        ))


        singular = true


        def __init__(t, pattern, portray, group_name, inside):
            t.pattern    = pattern
            t.portray    = portray
            t.group_name = group_name
            t.inside     = inside


        def __repr__(t):
            return arrange('<TremoliteGroup %s %s>',
                           t.group_name,
                           portray_string(t.inside)   if t.inside.__class__ is String else   portray(t.inside))



    class TremoliteMultiple(TremoliteBase):
        __slots__ = ((
            'exact',            #   String
        ))


        singular = false


        def __init__(t, pattern, portray, exact):
            t.pattern  = intern_string(pattern)
            t.portray  = portray
            t.exact    = intern_string(exact)


        def __repr__(t):
            return arrange('<TremolitMultiple %s %s>', portray_string(t.pattern), portray_string(t.exact))


    class TremoliteSingular(TremoliteBase):
        __slots__ = ((
            'exact',            #   String
        ))


        singular = true


        def __init__(t, pattern, portray, exact):
            t.pattern  = intern_string(pattern)
            t.portray  = portray
            t.exact    = intern_string(exact)


        def __repr__(t):
            return arrange('<TremolitSingular %s %s>', portray_string(t.pattern), portray_string(t.exact))


    class TremoliteSpecialSingular(TremoliteBase):
        __slots__ = (())


        singular = true


        def __init__(t, pattern, portray):
            t.pattern  = intern_string(pattern)
            t.portray  = intern_string(portray)


        def __repr__(t):
            return arrange('<TremoliteSpecialSingular %s %s>', portray_string(t.pattern), t.portray)


    END_OF_STRING = TremoliteSpecialSingular(r'\Z', 'END_OF_STRING')


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

        return (TremoliteMultiple   if length(s) > 1 else   TremoliteSingular)(
                   create_exact(s), intern_arrange('EXACT(%s)', portray_string(s)), intern_string(s),
               )


    @export
    def GROUP(group_name, inside):
        inside = WRAP(inside)

        return TremoliteGroup(
                   intern_arrange('(?P<%s>%s)', group_name, inside.pattern),
                   arrange('GROUP(%s, %s)', portray_string(group_name), inside),
                   group_name,
                   inside,
               )



    def WRAP(s):
        if type(s) is String:
            assert length(s) >= 1

            return (TremoliteMultiple   if length(s) > 1 else   TremoliteSingular)(
                       create_exact(s), intern_string(portray_string(s)), intern_string(s),
                   )

        assert s.is_tremolite

        return s


    export(
        'END_OF_STRING',    END_OF_STRING,
    )


    test = r'fake: \r' + GROUP('abc', '(abc)') + 'end' + END_OF_STRING

    line('%s', test)
    line('%r', test)
