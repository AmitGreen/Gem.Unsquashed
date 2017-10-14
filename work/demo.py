#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
#   MIT License
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#   of this software and associated documentation files (the "Software"), to deal
#   in the Software without restriction, including without limitation the rights
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#   copies of the Software, and to permit persons to whom the Software is
#   furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in all
#   copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#   SOFTWARE.
#
def emulate_context(path):
    #
    #   These are our 'context' variables, that can be shared deep in routines
    #
    current_path  = None
    current_line  = None
    line_number   = 0
    line_position = 0
    append_line   = None

    #
    #  This allows us to emulate a stack of contexts, allowing us to nest contexts.
    #
    #       This makes it easy to emulate a 'import' statement, to import a file,
    #       and when done, to pop back to the previous file.
    #
    #  Henceforth, accessing any of the four context variables:
    #
    #       current_path
    #       current_line
    #       line_number
    #       line_position
    #       append_line
    #
    #  Accesses its value on last pushed context on the context stack.
    #
    class Context(object):
        __slots__ = ((
            'current_path',     #   Previous path
            'current_line',     #   Previous current line
            'line_number',      #   Previous line number
            'line_position',    #   Previous line position
            'append_line',      #   Previous append method
        ))

        #
        #   Push a new context, start the variables at their default values
        #
        def __init__(self, next_append_line):
            nonlocal current_path, current_line, line_number, line_position, append_line

            self.current_path  = current_path
            self.current_line  = current_line
            self.line_number   = line_number
            self.line_position = line_position
            self.append_line   = append_line

            current_path  = None
            current_line  = None
            line_number   = 0
            line_position = 0
            append_line   = next_append_line


        def __enter__(self):
            return self

        #
        #   Pop the current context, and restore previous context state
        #
        def __exit__(self, e_type, e, e_traceback):
            nonlocal current_path, current_line, line_number, line_position, append_line

            current_path  = self.current_path
            current_line  = self.current_line
            line_number   = self.line_number
            line_position = self.line_position
            append_line   = self.append_line


    #
    #   Support code:
    #
    #       line - print a line of text
    #
    def line(format = None, *arguments):
        if format == None:
            print()
            return

        if arguments:
            print(format % arguments)
            return

        print(format)


    #
    #   Support code:
    #
    #       UnknownLineException - An error fo an unknown line of code
    #
    class UnknownLineException(Exception):
        __slots__ = (())


        def __init__(self, format, *arguments):
            super(Exception, self).__init__(format % arguments)

    #
    #   Loop over a generator, catch UnknownLineException, & restart loop until end of file
    #
    class LoopAndCatchUnknownLines(object):
        __slots__ = ((
            'finished',                     #   Boolean
            'loop',                         #   Integer
        ))


        def __init__(self, append):
            self.finished = False
            self.loop     = 0


        def __enter__(self):
            return self


        def __exit__(self, e_type, e, e_traceback):
            if e is None:
               self.finished = True
               return

            if e_type is not UnknownLineException:
                return

            #
            #   Eat the exception & append it to the lines parsed
            #
            append_evaluated_line(e.args[0])
            return True


        def __iter__(self):
            while not self.finished:
                self.loop += 1

                yield self


    #
    #   Here is our generator to walk over a file.
    #
    #   This generator has three sections:
    #
    #       generator_start     - Always run when the generator is started.
    #                             This opens the file & reads it.
    #
    #       generator_next      - Run each time the generator needs to retrieve
    #                             The next value.
    #
    #       generator_stop      - Called when the generator is going to stop.
    #
    def iterate_lines(path):
        data_lines = None


        def generator_startup(path):
            nonlocal current_path, data_lines

            with open(path) as f:
                current_path = path
                data         = f.read()

            data_lines = tuple(data.splitlines())


        def generator_next():
            nonlocal current_line, line_number

            for current_line in data_lines:
                line_number += 1
                line_position = 0

                yield current_line

            generator_stop()


        def generator_stop():
            current_path  = None
            line_number   = 0
            line_position = 0


        generator_startup(path)

        return generator_next()


    class EvaluatedLine(object):
        __slots__ = ((
            'path',                     #   String
            'line_number',              #   Integer
            'result',                   #   String
        ))


        def __init__(self, path, line_number, result):
            self.path        = path
            self.line_number = line_number
            self.result      = result


    def append_evaluated_line(format, *arguments):
        append_line(
            EvaluatedLine(current_path, line_number, format % arguments)
        )



    import re


    print_match    = re.compile('print ').match
    import_match   = re.compile('import (?P<module>[a-z0-9]+)\Z').match
    atom_match     = re.compile(' *(?:(?P<number>[0-9]+)|(?P<operator>\())').match
    operator_match = re.compile(' *(?P<operator>[-+*/)])?').match


    left_parenthesis = object()
    right_parenthesis = object()


    def tokenize_atom():
        nonlocal line_position

        m = atom_match(current_line, line_position)

        if m is None:
            raise UnknownLineException('UNKNOWN ATOM: %r', current_line[line_position : ])

        line_position = m.end()

        number = m.group('number')

        if number is not None:
            return int(number)

        return left_parenthesis


    def tokenize_operator():
        nonlocal line_position

        m = operator_match(current_line, line_position)

        if m is None:
            raise UnknownLineException('UNKNOWN OPERATOR: %r', current_line[line_position : ])

        line_position = m.end()

        result = m.group('operator')

        if result == ')':
            return right_parenthesis

        return result
        

    def parse_atom():
        atom = tokenize_atom()

        if type(atom) is int:
            return atom

        assert atom is left_parenthesis

        [v, operator] = parse_expression()

        assert operator is right_parenthesis

        return v


    def parse_add(v):
        w        = parse_atom()
        operator = tokenize_operator()

        if operator == '*':
            [w, operator] = parse_multiply(w)

        result = v + w

        if operator == '-':
            [result, operator] = parse_subtract(result)

        if (operator is None) or (operator is right_parenthesis):
            return [result, operator]

        raise UnknownLineException('parse_add: unimplemented: %r', operator)


    def parse_subtract(v):
        w        = parse_atom()
        operator = tokenize_operator()

        if operator == '*':
            [w, operator] = parse_multiply(w)

        if (operator is None) or (operator is right_parenthesis):
            return [v - w, operator]

        raise UnknownLineException('parse_subtract: unimplemented: %r', operator)


    def parse_divide(v):
        w        = parse_atom()
        operator = tokenize_operator()

        if operator is None:
            return [v // w, operator]

        raise UnknownLineException('parse_divide: operator: %r', operator)


    def parse_multiply(v):
        w        = parse_atom()
        operator = tokenize_operator()

        if operator == '*':
            [v, operator] = parse_multiply(v)

        if (operator is None) or (operator is right_parenthesis) or (operator == '-') or (operator == '+'):
            return [v * w, operator]

        raise UnknownLineException('parse_multiply: operator: %r', operator)


    def parse_expression():
        v        = parse_atom()
        operator = tokenize_operator()

        if operator == '*':
            [v, operator] = parse_multiply(v)

        if operator == '/':
            [v, operator] = parse_divide(v)

        if operator == '-':
            [v, operator] = parse_subtract(v)

        if operator == '+':
            [v, operator] = parse_add(v)

        if (operator is None) or (operator == right_parenthesis):
            return [v, operator]

        raise UnknownLineException('parse_expression: incomplete: %r', operator)


    def parse_full_expression():
        [v, operator] = parse_expression()

        if operator is None:
            return v

        raise UnknownLineException('parse_full_expression: incomplete: %r', operator)


    def import_file(path):
        nonlocal line_position

        with Context(append_line):
            iterator = iterate_lines(path)
            result   = []

            for LOOP in LoopAndCatchUnknownLines(result.append):
                with LOOP:
                    for s in iterator:
                        m = import_match(s)

                        if m:
                            module = m.group('module')

                            append_evaluated_line('importing module %s', module)

                            import_file(module + '.py')
                            continue

                        m = print_match(s)

                        if m:
                            line_position = m.end()
                            expression    = current_line[line_position : ]

                            [result, operator] = parse_expression()

                            assert operator is None

                            append_evaluated_line('expression %r evaluates to %s', expression, result)
                            continue

                        raise UnknownLineException('UNKNOWN STATEMENT: %r', current_line)


    def parse_file(path):
        nonlocal append_line

        result_list = []
        append_line = result_list.append

        import_file(path)

        for v in result_list:
            line('%s#%d: %s', v.path, v.line_number, v.result)


    parse_file(path)


if __name__ == '__main__':
    open('demo1.py', 'w').write("""
print 1
print 8 - 2 * 3
import demo2
print 9 - sqrt(16)
print 10 / (8 - 2 * 3)
import demo2
print 2 * 2 * 2 + 3 - 4
"""[1:-1]
    )

    open('demo2.py', 'w').write("""
print 3 * (3 - 2)
error
print 4
"""[1:-1]
    )

    emulate_context('demo1.py')
