#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse3')
def gem():
    tree = 7
    show = 7


    require_gem('Sapphire.DualStatement')
    require_gem('Sapphire.Suite')

    if __debug__:
        require_gem('Sapphire.DumpToken')


    @share
    def parse3_python(path, data, data_lines, data_many):
        data_many.append(end_of_data)

        data_iterator = iterate(data_many)
        next_line     = next_method(data_iterator)

        tree_many   = []
        append_twig = tree_many.append

        variables = [
                        0,                  #   0 = before
                        0,                  #   1 = comment
                        0,                  #   2 = v
                    ]

        query = variables.__getitem__
        write = variables.__setitem__

        qb  = Method(query, 0)
        qc  = Method(query, 1)
        qv  = Method(query, 2)

        wb  = Method(write, 0)
        wc  = Method(write, 1)
        wv  = Method(write, 2)

        wb0 = Method(wb, 0)
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

 
        #
        #   parse_blank_line:
        #
        #       This routine is "rolled-out" at least three times ... Hard to read the first time (and second time
        #       and third time!), but the code is actualy "simplier" due to the 'unrolling' ("simplier" in the sense
        #       less conditions per loop, if it was not "rolled-out")
        #
        def parse_blank_lines(v):
            assert qb() is qc() is qv() is 0

            #
            #   At this point:
            #       v:              first comment or empty line
            #
            #   Set soon:
            #       v_impression:   indentation if 'v' is a comment, or 0 if 'v' is an empty line
            #       w:              next line
            #       w_impression:   indentation if 'w' is a comment, or 0 if 'w' is an empty line
            #
            v_impression = v.impression
            w            = next_line()

            if not w.is_comment__or__empty_line:
                if v_impression is w.indentation:
                    assert (v.is_comment_line) and (not w.is_end_of_data)

                    add_comment = w.add_comment

                    if add_comment is not 0:
                        return add_comment(v)

                wb(v)
                return w

            w_impression = w.impression

            if v_impression is w_impression:
                if v_impression is 0:
                    assert (v.is_empty_line) and (w.is_empty_line)

                    empty_line_many = [v, w]

                    while 7 is 7:
                        w = next_line()

                        if w.is_empty_line:
                            empty_line_many.append(w)
                            continue

                        if w.is_comment_line:
                            w_impression = w.impression
                            break

                        wb(conjure_empty_line_suite(empty_line_many))
                        return w

                    v = conjure_empty_line_suite(empty_line_many)
                else:
                    assert (v.is_comment_line) and (w.is_comment_line)

                    comment_many = [v, w]

                    while 7 is 7:
                        w = next_line()

                        if w.is_comment__or__empty_line:
                            w_impression = w.impression

                            if v_impression is w_impression:
                                comment_many.append(w)
                                continue

                            break

                        if v_impression is w.indentation:
                            add_comment = w.add_comment

                            if add_comment is not 0:
                                return add_comment(conjure_comment_suite(comment_many))

                        wb(conjure_comment_suite(comment_many))
                        return w

                    v = conjure_comment_suite(comment_many)

            #
            #   At this point:
            #       v:              first comment, empty line, suite of comments, or suite of empty lines
            #       w:              current comment or empty line
            #       w_impression:   indentation if 'w' is a comment, or 0 if 'w' is an empty line
            #
            #   Set soon:
            #       x:              next line
            #       x_impression:   indentation if 'x' is a comment, or 0 if 'x' is an empty line
            #
            x = next_line()

            if not x.is_comment__or__empty_line:
                if w_impression is x.indentation:
                    assert (w.is_comment_line) and (not x.is_end_of_data)

                    add_comment = x.add_comment

                    if add_comment is not 0:
                        wb(v)
                        return add_comment(w)

                wb(conjure_mixed_suite([v, w]))
                return x

            x_impression = x.impression

            if w_impression is not x_impression:
                mixed_many = [v, w]
            elif w_impression is 0:
                assert (w.is_empty_line) and (x.is_empty_line)

                empty_line_many = [w, x]

                while 7 is 7:
                    x = next_line()

                    if x.is_empty_line:
                        empty_line_many.append(x)
                        continue

                    if x.is_comment_line:
                        x_impression = x.impression
                        break

                    wb(conjure_mixed_suite([v, conjure_empty_line_suite(empty_line_many)]))
                    return x

                mixed_many = [v, conjure_empty_line_suite(empty_line_many)]
            else:
                assert (w.is_comment_line) and (x.is_comment_line)

                comment_many = [w, x]

                while 7 is 7:
                    x = next_line()

                    if x.is_comment__or__empty_line:
                        x_impression = x.impression

                        if w_impression is x_impression:
                            comment_many.append(x)
                            continue

                        break

                    if w_impression is x.indentation:
                        add_comment = x.add_comment

                        if add_comment is not 0:
                            wb(v)
                            return add_comment(conjure_comment_suite(comment_many))

                    wb(conjure_mixed_suite([v, conjure_comment_suite(comment_many)]))
                    return x

                mixed_many = [v, conjure_comment_suite(comment_many)]

            #
            #   At this point:
            #       v:              no longer used
            #       w:              no longer used
            #       mixed_many:     multiple mixed
            #       x:              current comment or empty line
            #       x_impression:   indentation if 'x' is a comment, or 0 if 'x' is an empty line
            #
            #   Set soon:
            #       y:              next line
            #       y_impression:   indentation if 'y' is a comment, or 0 if 'y' is an empty line
            #
            y = next_line()

            if not y.is_comment__or__empty_line:
                if x_impression is y.indentation:
                    assert (x.is_comment_line) and (not y.is_end_of_data)

                    add_comment = y.add_comment

                    if add_comment is not 0:
                        wb(conjure_mixed_suite(mixed_many))
                        return add_comment(x)

                mixed_many.append(x)
                wb(conjure_mixed_suite(mixed_many))
                return y

            y_impression = y.impression

            if x_impression is not y_impression:
                mixed_append = mixed_many.append

                mixed_append(x)
            elif x_impression is 0:
                assert (x.is_empty_line) and (y.is_empty_line)

                empty_line_many = [x, y]

                while 7 is 7:
                    y = next_line()

                    if y.is_empty_line:
                        empty_line_many.append(y)
                        continue

                    if y.is_comment_line:
                        y_impression = y.impression
                        break

                    mixed_many.append(conjure_empty_line_suite(empty_line_many))
                    wb(conjure_mixed_suite(mixed_many))
                    return y

                mixed_append = mixed_many.append

                mixed_append(conjure_empty_line_suite(empty_line_many))
            else:
                assert (x.is_comment_line) and (y.is_comment_line)

                comment_many = [x, y]

                while 7 is 7:
                    y = next_line()

                    if y.is_comment__or__empty_line:
                        y_impression = y.impression

                        if x_impression is y_impression:
                            comment_many.append(y)
                            continue

                        break

                    if x_impression is y.indentation:
                        add_comment = y.add_comment

                        if add_comment is not 0:
                            wb(conjure_mixed_suite(mixed_many))
                            return add_comment(conjure_comment_suite(comment_many))

                    mixed_many.append(conjure_comment_suite(comment_many))
                    wb(conjure_mixed_suite(mixed_many))
                    return y

                mixed_append = mixed_many.append

                mixed_append(conjure_comment_suite(comment_many))

            #
            #   At this point:
            #       v:              no longer used
            #       w:              no longer used
            #       x:              no longer used
            #       mixed_many:     multiple mixed
            #       mixed_append:   append to mixed_many
            #       y:              current comment or empty line
            #       y_impression:   indentation if 'y' is a comment, or 0 if 'y' is an empty line
            #
            #   Set soon:
            #       z:              next line
            #       z_impression:   indentation if 'z' is a comment, or 0 if 'z' is an empty line
            #
            while 7 is 7:
                z = next_line()

                if not z.is_comment__or__empty_line:
                    if y_impression is z.indentation:
                        assert (y.is_comment_line) and (not z.is_end_of_data)

                        add_comment = z.add_comment

                        if add_comment is not 0:
                            wb(conjure_mixed_suite(mixed_many))
                            return add_comment(y)

                    mixed_append(y)
                    wb(conjure_mixed_suite(mixed_many))
                    return z

                if y_impression is not z.impression:
                    mixed_append(y)

                    y            = z
                    y_impression = z.impression
                    continue

                if y_impression is 0:
                    assert (y.is_empty_line) and (z.is_empty_line)

                    empty_line_many = [y, z]

                    while 7 is 7:
                        y = next_line()

                        if y.is_empty_line:
                            empty_line_many.append(y)
                            continue

                        if y.is_comment_line:
                            y_impression = y.impression
                            break

                        mixed_append(conjure_empty_line_suite(empty_line_many))
                        wb(conjure_mixed_suite(mixed_many))
                        return y

                    mixed_append(conjure_empty_line_suite(empty_line_many))
                    continue

                assert (y.is_comment_line) and (z.is_comment_line)

                comment_many = [y, z]

                while 7 is 7:
                    y = next_line()

                    if y.is_comment__or__empty_line:
                        if y_impression is y.impression:
                            comment_many.append(y)
                            continue

                        y_impression = y.impression
                        break

                    if y_impression is y.indentation:
                        add_comment = y.add_comment

                        if add_comment is not 0:
                            wb(conjure_mixed_suite(mixed_many))
                            return add_comment(conjure_comment_suite(comment_many))

                    mixed_append(conjure_comment_suite(comment_many))
                    wb(conjure_mixed_suite(mixed_many))
                    return y

                mixed_append(conjure_comment_suite(comment_many))
                y_impression = y.impression


        def parse_class_header(header):
            return conjure_class_definition(header, parse_suite(header.indentation))


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


        def parse_function_header(header):
            return conjure_function_definition(header, parse_suite(header.indentation))


        def parse_if_header(v):
            indentation = v.indentation

            v = conjure_if_statement(v, parse_suite(indentation))

            w = qv()

            if w is not 0:
                if (not w.is_else_header) or (indentation is not w.indentation):
                    return v

                wv0()
                prefix = qc()

                if prefix is not 0:
                    wc0()

                    return conjure_dual_statement(
                               v,
                               conjure_prefixed_else_fragment(prefix, w, parse_suite(indentation)),
                           )
            else:
                w = next_line()

                if (not w.is_else_header) or (indentation is not w.indentation):
                    wv(v)
                    return v

            return conjure_dual_statement(v, conjure_else_fragment(w, parse_suite(indentation)))


        def parse_while_header(header):
            return conjure_while_statement(header, parse_suite(header.indentation))


        def parse_lines():
            if tree is 7:
                while 7 is 7:
                    v = qv()

                    if v is 0:
                        v = next_line()
                    else:
                        wv0()

                        comment = qc()

                        if comment is not 0:
                            wc0()

                            append_twig(comment)

                    if v.is_comment__or__empty_line:
                        v = parse_blank_lines(v)
                        
                        before = qb()

                        if before is not 0:
                            wc0()
                            append_twig(before)

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
                v = parse_blank_lines(v)

                assert (not v.is_comment__or__empty_line)

                before = qb()

                if before is not 0:
                    wb0()
            else:
                before = 0

            if v.is_end_of_data:
                raise_unknown_line()

            indentation = v.indentation

            if indentation.total <= previous_indentation.total:
                raise_runtime_error('missing indentation: %d (expected indentation greater than %d)',
                                    indentation.total, previous_indentation.total)

            if v.is_statement_header:
                v = v.parse_header()

            #
            #  Now look for 2nd part of suite
            #
            if before is not 0:
                suite_many = [before, v]
            else:
                w = qv()

                if w is not 0:
                    if indentation is not w.indentation:
                        return v

                    wv0()
                    comment = qc()
                else:
                    w = next_line()
                    comment = 0

                if comment is not 0:
                    wc0()

                    suite_many = [v, comment, (w.parse_header()   if w.is_statement_header else w)]
                else:
                    if w.is_comment__or__empty_line:
                        w = parse_blank_lines(w)

                        assert not w.is_comment__or__empty_line

                        before = qb()

                        if before is not 0:
                            wb0()

                            if indentation is not w.indentation:
                                wc(before)
                                wv(w)

                                return v

                            suite_many = [v, before, (w.parse_header()   if w.is_statement_header else w)]
                        else:
                            if indentation is not w.indentation:
                                wv(w)

                                return v

                            suite_many = [v, (w.parse_header()   if w.is_statement_header else w)]
                    else:
                        if indentation is not w.indentation:
                            wv(w)

                            return v
                    
                        suite_many = [v, (w.parse_header()   if w.is_statement_header else w)]

            #
            #   Handle 3rd part of suite -- set suite_append only if needed
            #
            x = qv()

            if x is not 0:
                if indentation is not x.indentation:
                    return conjure_statement_suite(suite_many)

                wv0()
                comment = qc()
            else:
                x       = next_line()
                comment = 0

            if comment is not 0:
                wc0()

                suite_append = suite_many.append
                suite_append(comment)

                assert indentation is x.indentation
            else:
                if x.is_comment__or__empty_line:
                    x = parse_blank_lines(x)

                    assert not x.is_comment__or__empty_line

                    before = qb()

                    if before is not 0:
                        wb0()
                        suite_append = suite_many.append
                        suite_append(before)

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

            suite_append(x.parse_header()   if x.is_statement_header else   x)


            #
            #   Handle 4th+ part of suite -- use suite_append
            #
            while 7 is 7:
                x = qv()

                if x is not 0:
                    if indentation is not x.indentation:
                        return conjure_statement_suite(suite_many)

                    wv0()
                    comment = qc()
                else:
                    x       = next_line()
                    comment = 0

                if comment is not 0:
                    wc0()

                    suite_append(comment)

                    assert indentation is x.indentation
                else:
                    if x.is_comment__or__empty_line:
                        x = parse_blank_lines(x)

                        assert not x.is_comment__or__empty_line

                        before = qb()

                        if before is not 0:
                            wb0()
                            suite_append(before)

                    if indentation is not x.indentation:
                        wv(x)

                        return conjure_statement_suite(suite_many)

                suite_append(x.parse_header()   if x.is_statement_header else   x)


        ClassHeader    .parse_header = parse_class_header
        DecoratorHeader.parse_header = parse_decorator_header
        FunctionHeader .parse_header = parse_function_header
        IfHeader       .parse_header = parse_if_header
        WhileHeader    .parse_header = parse_while_header


        #dump_newline_meta_cache()

        if show is 5:
            show_indentation()

        parse_lines()
        test_identical_output()
        test_count_newlines()

        if show is 7:
            show_tree()

        #dump_caches('dual-twig')
