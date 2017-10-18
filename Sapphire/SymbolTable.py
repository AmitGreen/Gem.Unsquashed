#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.SymbolTable')
def gem():
    require_gem('Sapphire.Cache')


    function_parameter_cache = {}


    class FunctionParameter(Object):
        __slots__ = ((
            'index',                    #   Integer
            'name',                     #   Identifier
        ))


        def __init__(t, index, name):
            t.index = index
            t.name  = name


        def display_token(t):
            return arrange('<parameter #%d %s>', t.index, t.name.s)


    class FunctionSymbolTable(Object):
        __slots__ = ((
            'parent',                   #   GlobalSymbolTable
            'phase_function',           #   Boolean
            'parameter_many',           #   None | List of FunctionParameter
            'definitions_many',         #   None | FunctionDefinition+ | List of FunctionDefinition+
            'symbols',                  #   Map { Name } of Any
        ))


        def __init__(t, parent):
            t.parent           = parent
            t.phase_function   = true
            t.parameter_many   = none
            t.definitions_many = none


        def add_parameter(t, parameter):
            name           = parameter.find_identifier()
            parameter_many = t.parameter_many

            if parameter_many is none:
                parameter_many = conjure_function_parameter(0, name)
                return

            if type(parameter_many) is not List:
                parameter_many = [parameter_many, conjure_function_parameter(1, name)]
                return

            parameter_many.append(conjure_function_parameter(length(parameter_many), name))


        def add_function_definition(t, definition):
            definitions_many = t.definitions_many

            if definitions_many is none:
                t.definitions_many = definition
                return

            if type(definitions_many) is not List:
                t.definitions_many = [definitions_many, definition]
                return

            definitions_many.append(definition)

        
    class GlobalSymbolTable(Object):
        __slots__ = ((
        ))


        parent         = none
        phase_function = false


    conjure_function_parameter = produce_conjure_dual('function_parameter', FunctionParameter, function_parameter_cache)


    append_cache('function_parameter', function_parameter_cache)


    @share
    def create_global_symbol_table():
        return GlobalSymbolTable()


    @share
    def create_function_symbol_table(parent):
        return FunctionSymbolTable(parent)
