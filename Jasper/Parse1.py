#
#   Copyright (c) 2017-2018 Amit Green.  All rights reserved.
#
@gem('Jasper.Parse1')
def gem():
    require_gem('Jasper.Core')
    require_gem('Jasper.Match')


    def parse_java_statement_import(m):
        if m.end('comment_newline') is not -1:
            raise_unknown_line()

        j = m.end()

        indented_keyword = evoke_indented_import(m.end('indented'), j)

        wi(j)
        wj(j)

        raise_unknown_line()


    lookup_parse_java_line = {
                                 'import' : parse_java_statement_import,
                             }.get


    @share
    def parse_java_from_path(path):
        data = read_text_from_path(path)

        parse_context = z_initialize(path, data)

        append        = parse_context.append
        many          = parse_context.many
        iterate_lines = parse_context.iterate_lines

        for LOOP in parse_context:
            with parse_context:
                for s in iterate_lines:
                    line('s: %s', s)

                    assert qd() is 0

                    m = line_match(s)

                    if m is none:
                        raise_unknown_line()

                    keyword_s = m.group('keyword')

                    if keyword_s is not none:
                        parse1_line = lookup_parse_java_line(keyword_s)

                        if parse1_line is not none:
                            append(parse1_line(m))

                            assert qd() is 0
                            continue

                        raise_unknown_line()

                    comment_end = m.end('comment')

                    if comment_end is not -1:
                        append(conjure_any_comment_line(m.end('indented'), comment_end))
                        continue

                    if m.end('newline') is -1:
                        raise_unknown_line()

                    append(conjure_empty_line(m.group()))

        return ((data, parse_context.data_lines, many))
