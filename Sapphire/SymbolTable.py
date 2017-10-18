#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.SymbolTable')
def gem():
    require_gem('Sapphire.Cache')


    function_parameter_cache = {}
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


    class LocalVariable(Object):
        __slots__ = ((
            'index',                    #   Integer
            'name',                     #   Identifier
        ))


        display_name = 'local'


        __init__      = construct__index_name
        __repr__      = portray__index_name
        display_token = portray__index_name


    class FunctionSymbolTable(Object):
        __slots__ = ((
            'parent',                   #   GlobalSymbolTable
            'phase_function',           #   Boolean
            'variable_index',           #   Integer
            'parameter_many',           #   None | FunctionParameter | List of FunctionParameter
#           'definitions_many',         #   None | FunctionDefinition+ | List of FunctionDefinition+
            'variable_many',            #   None | LocalVariable | List of LocalVariable
        ))


        def __init__(t, parent):
            t.parent           = parent
            t.phase_function   = true
            t.variable_index   = 0
            t.parameter_many   = none
#           t.definitions_many = none
            t.variable_many    = 0


        def add_parameter(t, name):
            variable_index = t.variable_index

            t.variable_index = variable_index + 1

            function_parameter = conjure_function_parameter(variable_index, name)

            if variable_index is 0:
                t.parameter_many = function_parameter
                return

            if variable_index is 1:
                t.parameter_many = [t.parameter_many, function_parameter]
                return

            t.parameter_many.append(function_parameter)


        def add_variable(t, name):
            variable_index = t.variable_index
            variable_many  = t.variable_many

            t.variable_index = variable_index + 1

            local_variable = conjure_local_variable(variable_index, name)

            if variable_many is 0:
                t.variable_many = local_variable
                return

            if type(variable_many) is not List:
                t.variable_many = [variable_many, local_variable]
                return

            t.variable_many.append(local_variable)


        if 0:
            def add_function_definition(t, definition):
                definitions_many = t.definitions_many

                if definitions_many is 0:
                    t.definitions_many = definition
                    return

                if type(definitions_many) is not List:
                    t.definitions_many = [definitions_many, definition]
                    return

                definitions_many.append(definition)


        def dump_variables(t, name):
            line('===  FunctionSymbolTable %s  ===', name)

            parameter_many = t.parameter_many

            if parameter_many is not 0:
                if type(parameter_many) is List:
                    for v in parameter_many:
                        line('  %r', v)
                else:
                    line('  %r', parameter_many)

            variable_many = t.variable_many

            if variable_many is not 0:
                if type(variable_many) is List:
                    for v in variable_many:
                        line('  %r', v)
                else:
                    line('  %r', variable_many)

        
    class GlobalSymbolTable(Object):
        __slots__ = ((
            'variable_map',                 #   None | Variable | Map { Symbol } of Variable
            '_store_variable',              #   Method
        ))


        def __init__(t, variable_map):
            t.variable_map    = variable_map
            t._store_variable = variable_map.__setitem__


        def add_variable(t, symbol):
            t._store_variable(symbol.s, symbol)


        def dump_variables(t, name):
            line('===  GlobalSymbolTable %s  ===', name)

            for [k, v] in iterate_items_sorted_by_key(t.variable_map):
                line('  %s: %r', k, v)
            


    conjure_function_parameter = produce_conjure_dual('function_parameter', FunctionParameter, function_parameter_cache)
    conjure_local_variable     = produce_conjure_dual('local_variable',     LocalVariable,     local_variable_cache)


    append_cache('function_parameter', function_parameter_cache)
    append_cache('local_variable',     local_variable_cache)


    @share
    def create_global_symbol_table(variable_map):
        return GlobalSymbolTable(variable_map)


    @share
    def create_function_symbol_table(parent):
        return FunctionSymbolTable(parent)
