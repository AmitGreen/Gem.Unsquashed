#
#   Copyright (c) 2018 Amit Green.  All rights reserved.
#
@gem('Marble.GenerateAscii')
def gem():
    require_gem('Marble.Core')


    ascii_list = [0] * 128


    store_ascii = ascii_list.__setitem__


    class Ascii(Object):
        __slots__ = ((
            'c',                        #   String
            'ordinal',                  #   String
            'portray',                  #   String
            'is_apostrophe',            #   Boolean
            'is_backslash',             #   Boolean
            'is_boring_printable',      #   Boolean
            'is_printable',             #   Boolean
            'is_quotation_mark',        #   Boolean
        ))


        def __init__(
                t, c, ordinal, portray,

                is_apostrophe     = false,
                is_backslash      = false,
                is_printable      = false,
                is_quotation_mark = false,
        ):
            t.c       = c
            t.ordinal = ordinal
            t.portray = portray

            t.is_apostrophe = is_apostrophe
            t.is_backslash  = is_backslash

            t.is_boring_printable = not (
                                               is_backslash
                                            or is_quotation_mark
                                            or not is_printable
                                        )

            t.is_printable      = is_printable
            t.is_quotation_mark = is_quotation_mark


        def __repr__(t):
            other = ''

            if t.is_apostrophe:        other += '; is_apostrophe'
            if t.is_backslash:         other += '; is_backslash'

            if t.is_boring_printable:
                other += '; is_boring'

                assert t.printable
            elif t.is_printable:
                other += '; is_printable'

            if t.is_quotation_mark:    other += '; is_quotation_mark'

            return arrange('<Ascii %r %d %r%s>', t.c, t.ordinal, t.portray, other)


    def create_ascii(
            c, ordinal, portray,

            is_apostrophe     = false,
            is_backslash      = false,
            is_printable      = false,
            is_quotation_mark = false,
    ):
        c = character(ordinal)

        ascii = Ascii(
                c, ordinal, portray,

                is_apostrophe     = is_apostrophe,
                is_backslash      = is_backslash,
                is_printable      = is_printable,
                is_quotation_mark = is_quotation_mark,
            )

        store_ascii(ordinal, ascii)


    def java_portray(s):
        if s == '"':
            return r'"\""';

        return '"' + portray(s)[1:-1] + '"'


    @execute
    def populate_ascii_list():
        for i in iterate_range(0, 128):
            c = character(i)

            if not (32 <= i <= 126):
                c_portray = intern_string(portray(c)[1:-1])

                create_ascii(c, i, c_portray)
                continue

            if c == '"':
                create_ascii(c, i, c, is_quotation_mark = true, is_printable = true)
                continue

            if c == '\\':
                portay_backslash = intern_string(r'\\')

                create_ascii(c, i, portay_backslash, is_backslash = true, is_printable = true)
                continue

            create_ascii(c, i, c, is_printable = true)


    @share
    def generate_ascii():
        comment = []

        append_comment = comment.append
        zap_comment    = Method(comment.__delitem__, slice_all)
        length_comment = comment.__len__

        line('    static final AsciiTable[]       ascii_list = new AsciiTable[] {');

        for [i, v] in enumerate(ascii_list):
            if v is 0:
                continue

            if v.is_apostrophe:        append_comment('apostrophe')
            if v.is_backslash:         append_comment('backslash')

            if v.is_boring_printable:
                append_comment('boring_printable')

                assert v.is_printable
            elif v.is_printable:
                append_comment('printable')

            if v.is_quotation_mark:    append_comment('quotation_mark')

            line('        AsciiTable.create(%7s, %#04x),%s',
                 java_portray(v.portray),
                 (
                      (0x01   if v.is_boring_printable  else   0)
                    | (0x02   if v.is_printable         else   0)
                 ),
                 (('  //  ' + ', '.join(comment))   if comment else   ''));

            zap_comment()

        line('    };');
