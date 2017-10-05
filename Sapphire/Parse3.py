#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse3')
def gem():
    tree = 0
    show = 0


    require_gem('Sapphire.BodyStatement')
    require_gem('Sapphire.DumpToken')
    require_gem('Sapphire.Suite')


    @share
    def parse3_python(path, data, data_lines, data_many):
        data_many.append(end_of_data)

        data_iterator = iterate(data_many)
        next_line     = next_method(data_iterator)

        tree_many   = []
        append_twig = tree_many.append

        variables = [
                        0,                  #   0 = v
                    ]

        query = variables.__getitem__
        write = variables.__setitem__

        qv  = Method(query, 0)
        wv  = Method(write, 0)

        wv0 = Method(wv, 0)


        def show_indentation():
            for v in data_many:
                line('+%d %s', v.indentation.total, v.display_token())


        def show_tree():
            with create_StringOutput() as f:
                f.line('===  show_tree  ===')

                for v in tree_many:
                    r = v.dump_token(f)

                    assert not r

            partial(f.result)


        def test_identical_output():
            with create_StringOutput() as f:
                w = f.write

                for v in tree_many:
                    v.write(w)

            if data != f.result:
                with create_DelayedFileOutput('oops.txt') as oops:
                    oops.write(f.result)

                raise_runtime_error('mismatch on %r: output saved in %r', path, 'oops.txt')

            line('Passed#1: Identical dump from parse tree.  Total: %d line%s',
                 length(data_many), (''   if length(data_many) is 0 else   's'))


        def test_count_newlines():
            total = 0

            for v in tree_many:
                v.is_statement                  #   Test this exists
                v.is_statement_header           #   Test this exists

                total += v.count_newlines()

            if total != length(data_lines):
                raise_runtime_error('mismatch on counted lines (counted: %d; expected: %d)',
                                    total, length(parse_context.data_lines))
                                
            line('Passed#2: Total counted lines %d matches input', total)


        def create_append():
            element = q_element()

            if element is none:
                many = []
            else:
                w_element_0()
                many = [element]

            append = many.append

            w_append(many)
            w_many(many)

            return append

 
        def parse_comments_or_empty_lines(first):
            assert qv() is 0

            v = next_line()

            if not v.is_comment__or__empty_line:
                if (first.is_comment_line) and (first.indentation is v.indentation):
                    return v.add_comment(first)

                wv(v)
                return first


            #
            #   mixed:        first element of mixed_many
            #   mixed_many:   multiple mixed
            #   indentation:  indentation of comments (or none if processing blank lines)
            #
            if v.is_comment_line:
                indentation = v.indentation

                if (first.is_comment_line) and (first.indentation is indentation):
                    comment_many = [first, v]

                    while 7 is 7:
                        v = next_line()

                        if v.is_comment_line:
                            if indentation is v.indentation:
                                comment_many.append(v)
                                continue

                            indentation = v.indentation
                            break

                        if v.is_empty_line:
                            indentation = none
                            break

                        if v.is_end_of_data:
                            raise_unknown_line()

                            (q_append() or create_append())(conjure_comment_suite(comment_many))
                            return v

                        return v.add_comment(conjure_comment_suite(comment_many))

                    raise_unknown_line()

                    mixed = conjure_comment_suite(comment_many)
                else:
                    raise_unknown_line()

                    mixed = first
            else:
                raise_unknown_line()

                indentation = none

                if first.is_comment_line:
                    mixed = first
                else:
                    blank_many = [first, v]

                    while 7 is 7:
                        v = next_line()

                        if v.is_empty_line:
                            blank_many.append(v)
                            continue

                        if v.is_comment_line:
                            indentation = v.indentation
                            break

                        (q_append() or create_append())(conjure_empty_line_suite(empty_line_many))
                        return v

                    mixed = conjure_empty_line_suite(empty_line_many)

            mixed_many = none

            while 7 is 7:
                w = next_line()

                if not w.is_comment__or__empty_line:
                    if w.indentation is indentation:
                        if mixed_many is none:
                            (q_append() or create_append())(mixed)




        def parse_decorator_header(decorator_header):
            indentation = decorator_header.indentation

            v = qv()

            if v is 0:
                v = next_line()
            else:
                wv0()

            if v.is_comment__or__empty_line:
                if v.is_comment_line:
                    v = parse_comments_or_empty_lines(v)

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
            if tree is 7:
                while 7 is 7:
                    v = qv()

                    if v is 0:
                        v = next_line()
                    else:
                        wv0()

                    if v.is_comment__or__empty_line:
                        v = parse_comments_or_empty_lines(v)

                        if v.is_comment__or__empty_line:
                            append_twig(v)

                            v = qv()
                            wv0()

                    if v.is_end_of_data:
                        wv(v)
                        break

                    if v.indentation.total != 0:
                        raise_runtime_error('unexpected indentation %d (expected 0): %r', v.indentation.total, v)

                    if v.is_statement_header:
                        v = v.parse_header()

                    append_twig(v)
                else:
                    raise_runtime_error('programming error: loop to parse lines did not exit on %r', end_of_data)

            while 7 is 7:
                v = qv()

                if v is 0:
                    v = next_line()
                else:
                    wv0()

                if v.is_end_of_data:
                    break

                append_twig(v)
            else:
                raise_runtime_error('programming error: SECOND loop to parse lines did not exit on %r', end_of_data)


        def parse_suite(previous_indentation):
            v = qv()

            if v is 0:
                v = next_line()
            else:
                assert 0

                wv0()

            if v.is_comment__or__empty_line:
                v = parse_comments_or_empty_lines(v)

                if v.is_comment__or__empty_line:
                    suite_many   = [v]
                    suite_append = suite_many.append

                    v = qv()

                    wv0()

                    assert (v is not 0) and (not v.is_comment__or__empty_line)
                else:
                    suite_append = suite_many = 0
            else:
                suite_append = suite_many = 0

            if v.is_end_of_data:
                raise_unknown_line()

            indentation = v.indentation

            if indentation.total <= previous_indentation.total:
                raise_runtime_error('missing indentation: %d (expected indentation greater than %d)',
                                    indentation.total, previous_indentation.total)

            if v.is_statement_header:
                v = v.parse_header()

            if suite_append is not 0:
                suite_append(v)

                v = 0

            w = qv()

            if w is 0:
                w = next_line()
            else:
                wv0()

            if w.is_comment__or__empty_line:
                w = parse_comments_or_empty_lines(w)

                if w.is_comment__or__empty_line:
                    if suite_append is 0:
                        assert v is not 0 

                        suite_many   = [v, w]
                        suite_append = suite_many.append
                    else:
                        assert v is 0

                        suite_append(w)

                    w = qv()

                    wv0()

                    assert (w is not 0) and (not w.is_comment__or__empty_line)

            if w.is_end_of_data:
                wv(w)

                if suite_append is 0:
                    return v

                return conjure_statement_suite(suite_many)


            if suite_append is 0:
                suite_many   = [v, w]
                suite_append = suite_many.append

                v = 0
            else:
                suite_append(w)


        DecoratorHeader.parse_header = parse_decorator_header
        FunctionHeader .parse_header = parse_function_header


        #dump_newline_meta_cache()

        if show is 5:
            show_indentation()

        parse_lines()
        test_identical_output()
        test_count_newlines()

        if show is 7:
            show_tree()

        #dump_caches('dual-twig')
