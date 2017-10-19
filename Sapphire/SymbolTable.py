#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.SymbolTable')
def gem():
    require_gem('Sapphire.Cache')


    function_parameter_cache = {}
    global_variable_cache    = {}
    local_variable_cache     = {}


    def construct__index_name(t, index, name):
        t.index = index
        t.name  = name


    def portray__index_name(t):
        return arrange('<%s#%d %s>', t.display_name, t.index, t.name.s)



    class FunctionParameter(Object):
        __slots__ = ((
            'index',                    #   Integer
            'name',                     #   Identifier
        ))


        display_name = 'parameter'


        __init__      = construct__index_name
        __repr__      = portray__index_name
        display_token = portray__index_name


    class GlobalVariable(Object):
        __slots__ = ((
            'index',                    #   Integer
            'name',                     #   Identifier
        ))


        display_name = 'global'


        __init__      = construct__index_name
        __repr__      = portray__index_name
        display_token = portray__index_name


    class LocalVariable(Object):
        __slots__ = ((
            'index',                    #   Integer
            'name',                     #   Identifier
        ))


        display_name = 'local'


        __init__      = construct__index_name
        __repr__      = portray__index_name
        display_token = portray__index_name


    @privileged
    def produce_add_variable(name, conjure):
        def add_variable(t, name):
            variable_map = t.variable_map

            if variable_map is 0:
                t.variable_map      = variable_map = { name : conjure(0, name) }
                t.contains_variable = variable_map.__contains__
                t.store_variable    = variable_map.__setitem__
                return

            if t.contains_variable(name):
                return

            t.store_variable(name, conjure(length(t.variable_map), name))


        if __debug__:
            add_variable.__name__ = intern_string(name)

        return add_variable



    class BaseSymbolTable(Object):
        __slots__ = ((
            'function_map',             #   Zero | Map { FunctionDefinition } of Something
            'variable_map',             #   Zero | Map { Name } of ( FunctionParameter | LocalVariable )
            'contains_variable',        #   Vacant | Method
            'store_variable',           #   Vacant | Method
        ))


        def __init__(t):
            t.function_map = 0
            t.variable_map = 0


        def add_function(t, definition):
            function_map = t.function_map

            if function_map is 0:
                t.function_map = { definition : 0 }
            else:
                function_map[definition] = 0

            t.add_variable(definition.a.name.find_identifier())


        def dump_variables(t, name):
            line('===  %s %s  ===', t.display_name, name)

            function_map = t.function_map

            if function_map is not 0:
                for k in iterate_values_sorted_by_key({ k.a.name.find_identifier().s : k    for k in function_map }):
                    dump_token(k.a.name.find_identifier().s, k)
                    line('  : %r', function_map[k])

            variable_map = t.variable_map

            if variable_map is not 0:
                line('===  variables ===')
                for k in iterate_values_sorted_by_key({ k.s : k   for k in variable_map }):
                    line('  %s: %s', k.s, variable_map[k])


    class FunctionSymbolTable(BaseSymbolTable):
        __slots__ = ((
            'parent',                   #   GlobalSymbolTable
        ))


        display_name = 'function-symbol-table'


        def __init__(t, parent):
            t.parent       = parent
            t.function_map = 0
            t.variable_map = 0


        
    class GlobalSymbolTable(BaseSymbolTable):
        __slots__ = (())


        display_name = 'global-symbol-table'


    conjure_function_parameter = produce_conjure_dual('function_parameter', FunctionParameter, function_parameter_cache)
    conjure_global_variable    = produce_conjure_dual('global_variable',    GlobalVariable,    global_variable_cache)
    conjure_local_variable     = produce_conjure_dual('local_variable',     LocalVariable,     local_variable_cache)


    append_cache('function_parameter', function_parameter_cache)
    append_cache('global_variable',    global_variable_cache)
    append_cache('local_variable',     local_variable_cache)


    FunctionSymbolTable.add_parameter = produce_add_variable('add_parameter', conjure_function_parameter)
    FunctionSymbolTable.add_variable  = produce_add_variable('add_variable',  conjure_local_variable)
    GlobalSymbolTable  .add_variable  = produce_add_variable('add_variable',  conjure_global_variable)


    @share
    def create_global_symbol_table():
        return GlobalSymbolTable()


    @share
    def create_function_symbol_table(parent):
        return FunctionSymbolTable(parent)
