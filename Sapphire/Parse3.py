#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse3')
def gem():
    show = 7


    require_gem('Sapphire.BodyStatement')
    require_gem('Sapphire.Suite')


    variables = [0]

    query = variables.__getitem__
    write = variables.__setitem__

    qv = Method(query, 0)
    wv = Method(write, 0)

    wv0 = Method(wv, 0)


    @share
    def parse3_python(path, data, data_lines, data_many):
        def show_indentation():
            for v in data_many:
                line('+%d %s', v.indentation.total, v.display_token())


        def show_all():
            with create_StringOutput() as f:
                f.line('===  show_all  ===')

                for v in many:
                    r = v.dump_token(f)

                    assert not r

            partial(f.result)


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
            v = qv()

            if v is 0:
                v = next_line()

                if not v.is_comment__or__empty_line:
                    return v.add_comment(first_comment)
            else:
                if not v.is_comment__or__empty_line:
                    return v.add_comment(first_comment)

                wv0()

            indentation = first_comment.indentation

            if v.is_comment_line:
                if indentation is not  v.indentation:
                    raise_unknown_line()

                comments = [first_comment, v]

                while 7 is 7:
                    v = qv()

                    if v is 0:
                        v = next_line()

                        if not v.is_comment__or__empty_line:
                            return v.add_comment(conjure_comment_suite(comments))
                    else:
                        if v.is_comment__or__empty_line:
                            return v.add_comment(conjure_comment_suite(comments))

                        wv0()

                    if (v.is_comment_line) and (indentation is v.indentation):
                        comments.append(v)
                        continue

                    wv(v)
                    break

            raise_unknown_line()


        def parse_decorator_header(decorator_header):
            indentation = decorator_header.indentation
            v           = next_line()

            if v.is_comment__or__empty_line:
                if v.is_comment_line:
                    v = parse_comments(v)

                    if v.is_end_of_data:
                        raise_unknown_line()

                    v = v.add_comment(comment)
                else:
                    raise_unknown_line()

            if not v.is_class_decorator_or_function_header:
                raise_runtime_error('decorator_header must be followed by class, decorator, or function header: %r',
                                    decorator_header)

            if indentation is not v.indentation:
                raise_runtime_error('decorator_header (with indentation %d) followed by'
                                        + ' class, decorator, or function header with different indentation: %d',
                                    indentation.total,
                                    v.indentation.total)

            return conjure_decorated_definition(decorator_header, v.parse_header())


        def parse_function_header(function_header):
            return conjure_function_definition(function_header, parse_suite(function_header.indentation))


        def parse_lines():
            while 7 is 7:
                v = qv()

                if v is 0:
                    v = next_line()

                    if v.is_comment__or__empty_line:
                        if v.is_comment_line:
                            v = parse_comments(v)
                        else:
                            raise_unknown_line()
                    else:
                        if v.is_end_of_data:
                            wv(v)
                            break
                else:
                    if v.is_comment__or__empty_line:
                        if v.is_comment_line:
                            wv(0)
                            v = parse_comments(v)
                        else:
                            raise_unknown_line()
                    else:
                        if v.is_end_of_data:
                            break


                if v.indentation.total != 0:
                    raise_runtime_error('unexpected indentation %d (expected 0): %r', v.indentation.total, v)

                if v.is_statement_header:
                    v = v.parse_header()
                else:
                    my_line('v: %r', v)
                    raise_unknown_line()

                #my_line('===  append  ===')
                #v.dump_token()

                append(v)
            else:
                raise_runtime_error('programming error: loop to parse lines did not exit on %r', end_of_data)

            while 7 is 7:
                v = qv()

                if v is 0:
                    v = next_line()
                else:
                    wv(0)

                if v.is_end_of_data:
                    break

                append(v)
            else:
                raise_runtime_error('programming error: SECOND loop to parse lines did not exit on %r', end_of_data)


        def parse_suite(indentation):
            v = next_line()

            if v.is_comment__or__empty_line:
                if v.is_comment_line:
                    v = parse_comments(v)
                else:
                    raise_unknown_line()

            if v.is_end_of_data:
                raise_unknown_line()

            if v.indentation.total <= indentation.total:
                raise_runtime_error('missing indentation: %d (expected indentation greater than %d)',
                                    v.indentation.total, indentation.total)

            if v.is_statement_header:
                v = v.parse_header(v)

            w = next_line()

            if w.is_comment__or__empty_line:
                if w.is_comment_line:
                    w = parse_comments(v)
                else:
                    raise_unknown_line()

            if w.is_end_of_data:
                wv(w)
                return v

            raise_unknown_line()


        DecoratorHeader.parse_header = parse_decorator_header
        FunctionHeader .parse_header = parse_function_header

        parse_lines()
        test_identical_output()
        test_count_newlines()

        if show is 7:
            show_all()

        #dump_caches('dual-twig')
