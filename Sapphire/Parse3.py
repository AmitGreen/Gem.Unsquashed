#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse3')
def gem():
    show = 0


    @share
    def parse3_python(data, data_lines, many):
        if "test identical output":
            with create_StringOutput() as f:
                w = f.write

                for v in many:
                    v.write(w)

            if data != f.result:
                with create_DelayedFileOutput('oops.txt') as oops:
                    oops.write(f.result)

                raise_runtime_error('mismatch on %r: output saved in %r', path, 'oops.txt')

            line('Passed#1: Identical dump from parse tree.  Total: %d line%s',
                 length(many), (''   if length(many) is 0 else   's'))

        if "test count newlines":
            total = 0

            for v in many:
                total += v.count_newlines()

            if total != length(data_lines):
                raise_runtime_error('mismatch on counted lines (counted: %d; expected: %d)',
                                    total, length(parse_context.data_lines))
                                
            line('Passed#2: Total counted lines %d matches input', total)

        if show:
            for v in many:
                line('+%d %s', v.indentation.total, v.display_token())
