#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse3')
def gem():
    show = 0


    @share
    def parse3_python(path, data, data_lines, data_many):
        def show_indentation():
            for v in data_many:
                line('+%d %s', v.indentation.total, v.display_token())


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
                total += v.count_newlines()

            if total != length(data_lines):
                raise_runtime_error('mismatch on counted lines (counted: %d; expected: %d)',
                                    total, length(parse_context.data_lines))
                                
            line('Passed#2: Total counted lines %d matches input', total)


        if show is 7:
            show_indentation()


        #
        #   Line parser
        #
        data_many.append(end_of_data)

        data_iterator = iterate(data_many)
        next_line     = next_method(data_iterator)

        many   = []
        append = many.append


        def parse_lines():
            for v in data_iterator:
                if v.is_comment__or__empty_line:
                    if v.is_comment_line:
                        w = next_line()

                        if w.is_comment__or__empty_line:
                            if w.is_comment_line:
                                comments = [v, w]

                                while 7 is 7:
                                    v = next_line()

                                    if v.is_comment__or__empty_line:
                                        if v.is_comment_line:
                                            comments.append(v)
                                            continue

                                    break

                                for x in comments:
                                    append(x)
                            else:
                                append(v)
                                append(w)
                                continue
                        else:
                            append(v)
                            append(w)
                            continue

                if v.is_end_of_data:
                    break

                append(v)
            else:
                raise_runtime_error('programming error: loop to parse lines did not exit on %r', end_of_data)

        parse_lines()
        test_identical_output()
        test_count_newlines()
