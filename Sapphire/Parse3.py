#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse3')
def gem():
    show = 0


    require_gem('Sapphire.Suite')


    @share
    def parse3_python(path, data, data_lines, data_many):
        def show_indentation():
            for v in data_many:
                line('+%d %s', v.indentation.total, v.display_token())


        def show_all():
            for v in many:
                r = v.dump_token()

                assert not r


        def test_identical_output():
            with create_StringOutput() as f:
                w = f.write

                for v in many:
                    v.write(w)

            if data != f.result:
                with create_DelayedFileOutput('oops.txt') as oops:
                    oops.write(f.result)

                raise_runtime_error('mismatch on %r: output saved in %r', path, 'oops.txt')

            line('Passed#1: Identical dump from parse tree.  Total: %d line%s',
                 length(data_many), (''   if length(data_many) is 0 else   's'))


        def test_count_newlines():
            total = 0

            for v in many:
                v.is_statement                  #   Test this exists
                v.is_statement_header           #   Test this exists

                total += v.count_newlines()

            if total != length(data_lines):
                raise_runtime_error('mismatch on counted lines (counted: %d; expected: %d)',
                                    total, length(parse_context.data_lines))
                                
            line('Passed#2: Total counted lines %d matches input', total)


        if show is 5:
            show_indentation()


        #
        #   Line parser
        #
        data_many.append(end_of_data)

        data_iterator = iterate(data_many)
        next_line     = next_method(data_iterator)

        many   = []
        append = many.append


        def parse_comments(a):
            indentation = a.indentation
            v           = next_line()

            if v.is_comment__or__empty_line:
                if (v.is_comment_line) and (indentation is v.indentation):
                    comments = [a, v]

                    while 7 is 7:
                        v = next_line()

                        if v.is_comment__or__empty_line:
                            if (v.is_comment_line) and (indentation is v.indentation):
                                comments.append(v)
                                continue

                        break

                    append(conjure_comment_suite(comments))
                else:
                    append(a)
            else:
                append(a)

            return v


        def parse_lines():
            for v in data_iterator:
                if v.is_comment__or__empty_line:
                    if v.is_comment_line:
                        v = parse_comments(v)

                if v.is_end_of_data:
                    break

                if 0:
                    if v.indentation.total != 0:
                        raise_runtime_error('unexpected indentation %d (expected 0): %r', v.indentation.total, v)

                if v.is_statement_header:
                    pass

                append(v)
            else:
                raise_runtime_error('programming error: loop to parse lines did not exit on %r', end_of_data)

        parse_lines()
        test_identical_output()
        test_count_newlines()

        if show is 7:
            show_all()

        #dump_caches()
