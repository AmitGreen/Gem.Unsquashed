#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Quartz.Parse1')
def gem():
    require_gem('Quartz.Match')
    require_gem('Quartz.Core')


    show = true


    @share
    def parse1_mysql_from_path(path):
        data   = read_text_from_path(path)
        many   = []
        append = many.append

        iterate_lines = z_initialize(data)

        for s in iterate_lines:
            m1 = mysql_line_match(s)

            if m1 is none:
                append(create_UnknownLine(parse1_mysql_from_path, 1))
                continue

            comment = m1.group('comment')

            if comment is none:
                append(EmptyLine(s))
                continue

            comment_start = m1.start('comment')

            if comment_start is 1:
                append(PoundSignComment(comment, TokenNewline(s[m1.end('comment'):])))
                continue

            append(
                IndentedPoundSignComment(
                    TokenIndented(s[:comment_start - 1]),
                    comment,
                    TokenNewline(s[m1.end('comment'):]),
                ),
            )

            continue

        if show:
            for v in many:
                line('%r', v)

        with create_StringOutput() as f:
            w = f.write

            for v in many:
                v.write(w)

        if data != f.result:
            with create_DelayedFileOutput('oops.txt') as oops:
                oops.write(f.result)

            raise_runtime_error('mismatch on %r: output saved in %r', path, 'oops.txt')
