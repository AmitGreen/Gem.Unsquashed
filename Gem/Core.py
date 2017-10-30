#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.Core')
def gem():
    PythonTypes = __import__('types')


    @export
    def execute(f):
        f()

        return execute


    #
    #   intern_arrange & intern_integer
    #
    @built_in
    def intern_arrange(format, *arguments):
        return intern_string(format % arguments)


    provide_integer = {}.setdefault


    @built_in
    def intern_integer(v):
        assert type(v) is Integer

        return provide_integer(v, v)


    #
    #   line & partial
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


    @built_in
    def partial(format, *arguments):
        write_standard_output(format % arguments   if arguments else   format)
        flush_standard_output()


    #
    #   method_is_function
    #
    if is_python_2:
        @built_in
        @privileged
        def method_is_function(method, f):
            return method.im_func is f
    else:
        @built_in
        def method_is_function(method, f):
            return method is f


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


    built_in(
        #
        #   Types
        #
        'Boolean',          PythonBuiltIn.bool,
        'Bytes',            PythonBuiltIn.bytes,
        'Integer',          PythonBuiltIn.int,
        'FrozenSet',        PythonBuiltIn.frozenset,
        'List',             PythonBuiltIn.list,
        'Long',             (PythonBuiltIn.long    if is_python_2 else   PythonBuiltIn.int),
        'Map',              PythonBuiltIn.dict,
        'Method',           PythonTypes.MethodType,
        'Object',           PythonBuiltIn.object,
        'Slice',            PythonBuiltIn.slice,
        'Tuple',            PythonBuiltIn.tuple,
        'Type',             PythonBuiltIn.type,


        #
        #   Functions
        #
        'address_of',       PythonBuiltIn.id,
        'attribute',        PythonBuiltIn.getattr,
        'character',        PythonBuiltIn.chr,
        'enumerate',        PythonBuiltIn.enumerate,
        'globals',          PythonBuiltIn.globals,
        'introspection',    PythonBuiltIn.dir,
        'iterate',          PythonBuiltIn.iter,
        'iterate_range',    PythonBuiltIn.range,
        'maximum',          PythonBuiltIn.max,
        'ordinal',          PythonBuiltIn.ord,
        'portray',          PythonBuiltIn.repr,
        'property',         PythonBuiltIn.property,
        'sorted_list',      PythonBuiltIn.sorted,
        'static_method',    PythonBuiltIn.staticmethod,
        'sum',              PythonBuiltIn.sum,
        'type',             PythonBuiltIn.type,

        #
        #   Values
        #
        '__debug__',        PythonBuiltIn.__debug__,
    )


    if __debug__:
        built_in(PythonException.AssertionError)
