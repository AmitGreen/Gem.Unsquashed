#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.Core')
def gem():
    #
    #   line
    #
    flush_standard_output = PythonSystem.stdout.flush
    write_standard_output = PythonSystem.stdout.write


    @built_in
    def line(format = none, *arguments):
        if format is none:
            assert length(arguments) is 0

            write_standard_output('\n')
        else:
            write_standard_output((format % arguments   if arguments else   format) + '\n')

        flush_standard_output()


    #
    #   privileged_2
    #
    if is_python_2:
        export(
            'privileged_2',     rename_function('privileged_2', privileged)
        )
    else:
        @export
        def privileged_2(f):
            return f


    #
    #   raise_value_error
    #
    ValueError = PythonException.ValueError


    @export
    def raise_value_error(format, *arguments):
        value_error = format % arguments

        #
        #   Since the next line will appear in stack traces, make it look prettier by using 'value_error'
        #   (to make the line shorter & more readable)
        #
        raise ValueError(value_error)


    built_in(
        #
        #   Functions
        #
        'globals',          PythonBuiltIn.globals,
        'introspection',    PythonBuiltIn.dir,
        'iterate',          PythonBuiltIn.iter,
        'iterate_range',    PythonBuiltIn.range,
        'property',         PythonBuiltIn.property,
        'type',             PythonBuiltIn.type,

        #
        #   Types
        #
        'Integer',          PythonBuiltIn.int,
        'FrozenSet',        PythonBuiltIn.frozenset,
        'Map',              PythonBuiltIn.dict,
        'Object',           PythonBuiltIn.object,
        'Tuple',            PythonBuiltIn.tuple,
    )


    if __debug__:
        built_in(PythonException.AssertionError)
