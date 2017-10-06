#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse3')
def gem():
    tree = 7
    show = 7


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
                        0,                  #   0 = comment
                        0,                  #   1 = v
                    ]

        query = variables.__getitem__
        write = variables.__setitem__

        qc  = Method(query, 0)
        qv  = Method(query, 1)

        wc  = Method(write, 0)
        wv  = Method(write, 1)

        wc0 = Method(wc, 0)
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
                 length(tree_many), (''   if length(data_many) is 0 else   's'))


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

 
        def parse_comments_or_empty_lines(v):
            assert qc() is qv() is 0

            w = next_line()

            if not w.is_comment__or__empty_line:
                if (v.is_comment_line) and (v.impression is w.indentation):
                    return w.add_comment(v)

                wc(v)
                return w

            #
            #   mixed:          first element of mixed_many
            #   mixed_many:     multiple mixed
            #   impression:     impression of comments (or 0 if processing blank lines)
            #
            if w.is_comment_line:
                impression = w.impression

                if (v.is_comment_line) and (v.impression is impression):
                    comment_many = [v, w]

                    while 7 is 7:
                        w = next_line()

                        if w.is_comment_line:
                            if impression is w.impression:
                                comment_many.append(w)
                                continue

                            impression = w.impression
                            break

                        if w.is_empty_line:
                            impression = 0
                            break

                        if w.is_end_of_data:
                            wc(conjure_comment_suite(comment_many))
                            return w

                        return w.add_comment(conjure_comment_suite(comment_many))

                    mixed = conjure_comment_suite(comment_many)
                else:
                    mixed = v
            else:
                impression = 0

                if v.is_comment_line:
                    mixed = v
                else:
                    empty_line_many = [v, w]

                    while 7 is 7:
                        w = next_line()

                        if w.is_empty_line:
                            empty_line_many.append(w)
                            continue

                        if w.is_comment_line:
                            impression = w.impression
                            break

                        wc(conjure_empty_line_suite(empty_line_many))
                        return w

                    mixed = conjure_empty_line_suite(empty_line_many)

            mixed_many = none

            #
            #   At this point:
            #       v:              no longer used
            #       mixed:          first element of mixed_many, or 0 if no longer used
            #       mixed_many:     multiple mixed
            #       w:              current comment or empty line
            #       indentation:    indentation if comment, or 0 if empty line
            #
            if 0:
                my_line('=== 1 ===')
                my_line('mixed: %r', mixed)
                my_line('mixed_many: %r', mixed_many)
                my_line('w: %r', w)
                my_line('impression: %r', impression)

            if impression is 0:
                assert w.is_empty_line
            else:
                assert impression is w.impression

            while 7 is 7:
                x = next_line()

                if not x.is_comment__or__empty_line:
                    if impression is x.indentation:
                        if mixed is 0:
                            wc(conjure_mixed_suite(mixed_many))
                        else:
                            wc(mixed)

                        return x.add_comment(w)

                    if mixed is 0:
                        mixed_many.append(w)
                    else:
                        mixed_many = [mixed, w]

                    wc(conjure_mixed_suite(mixed_many))
                    return x

                if 0:
                    my_line('===')
                    my_line('x: %r', x)
                    my_line('impression: %r', impression)
                    my_line('x.impression: %r', x.impression)

                if impression is 0:
                    if x.is_empty_line:
                        empty_line_many = [w, x]

                        while 7 is 7:
                            x = next_line()

                            if x.is_empty_line:
                                empty_line_many.append(x)
                                continue

                            if x.is_comment_line:
                                impression = x.impression
                                break

                            if mixed is 0:
                                mixed_many.append(conjure_empty_line_suite(empty_line_many))
                                wc(conjure_mixed_suite(mixed_many))
                                return x

                            wc(conjure_mixed_suite([mixed, conjure_empty_line_suite(empty_line_many)]))
                            return x

                        w = x

                        if mixed is 0:
                            mixed_many.append(conjure_empty_line_suite(empty_line_many))
                            continue

                        mixed_many = [mixed, conjure_empty_line_suite(empty_line_many)]
                        mixed      = 0
                        continue

                elif impression is x.impression:
                    comment_many = [w, x]

                    while 7 is 7:
                        x = next_line()

                        if x.is_comment_line:
                            if impression is x.impression:
                                comment_many.append(x)
                                continue

                            impression = x.impression
                            break

                        if x.is_empty_line:
                            impression = 0
                            break

                        if x.is_end_of_data:
                            if mixed is not 0:
                                mixed_many = [mixed]

                            mixed_many.append(conjure_comment_suite(comment_many))
                            wc(conjure_mixed_suite(mixed_many))
                            return x

                        wc(conjure_mixed_suite(mixed_many)   if mixed is 0 else   mixed)
                        return x.add_comment(conjure_comment_suite(comment_many))

                    w = x

                    if mixed is 0:
                        mixed_many.append(conjure_comment_suite(comment_many))
                        continue

                    mixed_many = [mixed, conjure_comment_suite(comment_many)]
                    mixed      = 0
                    continue

                if mixed is 0:
                    mixed_many.append(w)
                else:
                    mixed_many = [mixed, w]
                    mixed      = 0

                impression = x.impression
                w          = x


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

                    comment = qc()

                    if comment is not none:
                        raise_unknown_line()

                    if v.is_end_of_data:
                        raise_unknown_line()
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
                        
                        comment = qc()

                        if comment is not 0:
                            wc0()
                            append_twig(comment)

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

                assert (not v.is_comment__or__empty_line)

                comment = qc()

                if comment is not 0:
                    wc0()
            else:
                comment = 0

            if v.is_end_of_data:
                raise_unknown_line()

            indentation = v.indentation

            if indentation.total <= previous_indentation.total:
                raise_runtime_error('missing indentation: %d (expected indentation greater than %d)',
                                    indentation.total, previous_indentation.total)

            if v.is_statement_header:
                v = v.parse_header()

            if comment is 0:
                w = qv()

                if w is 0:
                    w = next_line()
                else:
                    wv0()

                if w.is_comment__or__empty_line:
                    w = parse_comments_or_empty_lines(w)

                    assert not w.is_comment__or__empty_line

                    comment = qc()

                    if comment is not 0:
                        wc0()

                        if indentation is not w.indentation:
                            wv(w)

                            return conjure_statement_suite([v, comment])

                        suite_many = [v, comment, w]
                    else:
                        if indentation is not w.indentation:
                            wv(w)

                            return v

                        suite_many = [v, w]
                else:
                    if indentation is not w.indentation:
                        wv(w)

                        return v
                
                    suite_many = [v, w]
            else:
                suite_many = [comment, v]

            #
            #   Handle 3rd part of suite -- set suite_append only if needed
            #
            x = qv()

            if x is 0:
                x = next_line()
            else:
                wv0()

            if x.is_comment__or__empty_line:
                x = parse_comments_or_empty_lines(x)

                assert not x.is_comment__or__empty_line

                comment = qc()

                if comment is not 0:
                    wc0()
                    suite_append = suite_many.append
                    suite_append(comment)

                    if indentation is not x.indentation:
                        wv(x)

                        return conjure_statement_suite(suite_many)
                else:
                    if indentation is not x.indentation:
                        wv(x)

                        return conjure_statement_suite(suite_many)

                    suite_append = suite_many.append
            else:
                if indentation is not x.indentation:
                    wv(x)

                    return conjure_statement_suite(suite_many)

                suite_append = suite_many.append

            suite_append(x)

            #
            #   Handle 4th+ part of suite -- use suite_append
            #
            while 7 is 7:
                x = qv()

                if x is 0:
                    x = next_line()
                else:
                    wv0()

                if x.is_comment__or__empty_line:
                    x = parse_comments_or_empty_lines(x)

                    assert not x.is_comment__or__empty_line

                    comment = qc()

                    if comment is not 0:
                        wc0()
                        suite_append(comment)

                if indentation is not x.indentation:
                    wv(x)

                    return conjure_statement_suite(suite_many)

                suite_append(x)


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
