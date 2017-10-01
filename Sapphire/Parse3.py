#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse3')
def gem():
    show = 7


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


        def parse_comments(first_comment):
            v = next_line()

            if not v.is_comment__or__empty_line:
                return ((first_comment, v))

            indentation = first_comment.indentation

            if v.is_comment_line:
                if indentation is not  v.indentation:
                    raise_unknown_line()

                comments = [first_comment, v]

                while 7 is 7:
                    v = next_line()

                    if v.is_comment__or__empty_line:
                        if (v.is_comment_line) and (indentation is v.indentation):
                            comments.append(v)
                            continue

                    break

                return ((conjure_comment_suite(comments), v))

            raise_unknown_line()


        def parse_decorator(decorator_comment, decorator_header):
            indentation = decorator_header.indentation
            v           = next_line()

            if v.is_comment__or__empty_line:
                if v.is_comment_line:
                    [v_comment, v] = parse_comments(v)
                else:
                    raise_unknown_line()
            else:
                v_comment = no_comment

            if not v.is_class_or_function_header:
                raise_runtime_error('decorator_header must be followed by class or function header: %r',
                                    decorator_header)

            if indentation is not v.indentation:
                raise_runtime_error('decorator_header (with indentation %d) followed by'
                                        + ' class or function header with different indentation: %d',
                                    indentation.total,
                                    v.indentation.total)

            [body, next_comment] = parse_suite(indentation)

            my_line('decorator_comment: %r', decorator_comment)
            line('decorator_header: %r', decorator_header)
            line('v_comment: %r', v_comment)
            line('v: %r', v)
            line('body: %r', body)
            line('next_comment: %r', next_comment)

            raise_unknown_line()


        def parse_lines():
            for v in data_iterator:
                if v.is_comment__or__empty_line:
                    if v.is_comment_line:
                        [comment, v] = parse_comments(v)
                    else:
                        raise_unknown_line()
                else:
                    comment = no_comment

                if v.is_end_of_data:
                    if comment is not no_comment:
                        append(comment)

                    break

                if 0:
                    if v.indentation.total != 0:
                        raise_runtime_error('unexpected indentation %d (expected 0): %r', v.indentation.total, v)

                    if v.is_statement_header:
                        if v.is_decorator_header:
                            v = parse_decorator(comment, v)
                        else:
                            raise_unknown_line()
                    else:
                        raise_unknown_line()

                if comment is not no_comment:
                    #
                    #   Fix this later
                    #
                    append(comment)

                append(v)
            else:
                raise_runtime_error('programming error: loop to parse lines did not exit on %r', end_of_data)


        def parse_suite(indentation):
            v = next_line()

            if v.is_comment__or__empty_line:
                if v.is_comment_line:
                    [v_comment, v] = parse_comments(v)
                else:
                    raise_unknown_line()
            else:
                v_comment = no_comment

            if v.is_end_of_data:
                raise_unknown_line()

            if v.indentation.total <= indentation.total:
                raise_runtime_error('missing indentation: %d (expected indentation greater than %d)',
                                    v.indentation.total, indentation.total)

            if v.is_statement_header:
                if v.is_decorator_header:
                    v = parse_decorator(comment, v)
                else:
                    raise_unknown_line()
            else:
                if v_comment is not no_comment:
                    raise_unknown_line()

            w = next_line()

            if w.is_comment__or__empty_line:
                if w.is_comment_line:
                    [w_comment, w] = parse_comments(v)
                else:
                    raise_unknown_line()
            else:
                w_comment = no_comment

            if w.is_end_of_data:
                return ((v, w_comment))

            raise_unknown_line()


        parse_lines()
        test_identical_output()
        test_count_newlines()

        if show is 7:
            show_all()

        #dump_caches()
