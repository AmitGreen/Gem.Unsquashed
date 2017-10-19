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


    #FunctionParameter.k1 = FunctionParameter.index
    FunctionParameter.k2 = FunctionParameter.name


    class GlobalVariable(Object):
        __slots__ = ((
            'index',                    #   Integer
            'name',                     #   Identifier
        ))


        display_name = 'global'


        __init__      = construct__index_name
        __repr__      = portray__index_name
        display_token = portray__index_name


    #GlobalVariable.k1 = GlobalVariable.index
    GlobalVariable.k2 = GlobalVariable.name


    class LocalVariable(Object):
        __slots__ = ((
            'index',                    #   Integer
            'name',                     #   Identifier
        ))


        display_name = 'local'


        __init__      = construct__index_name
        __repr__      = portray__index_name
        display_token = portray__index_name


    #LocalVariable.k1 = LocalVariable.index
    LocalVariable.k2 = LocalVariable.name


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
            'function_many',            #   Zero | FunctionDefinition | List of FunctionDefinition
            'append_function',          #   Vacant | Method

            'function_map',             #   Vacant | FunctionSymbolTable | Map { FunctionDefinition } of FunctionSymbolTable
            'contains_function',        #   Vacant | Method
            'store_function',           #   Vacant | Method

            'variable_map',             #   Zero | Map { Name } of ( FunctionParameter | LocalVariable )
            'contains_variable',        #   Vacant | Method
            'store_variable',           #   Vacant | Method
        ))


        def __init__(t):
            t.function_many   = 0
           #t.append_function = vacant

           #t.function_map     = vacant
           #t.contains_funtion = vacant
           #t.store_function   = vacant

            t.variable_map      = 0
           #t.contains_variable = vacant
           #t.store_variable    = vacant


        def add_function(t, definition):
            function_many = t.function_many

            if function_many is 0:
                t.function_many = definition
                t.function_map  = 0
            elif type(function_many) is not List:
                if function_many is definition:
                    return

                t.function_many   = many = [function_many, definition]
                t.append_function = many.append

                t.function_map      = map = { function_many : 0, definition : 0 }
                t.contains_function = map.__contains__
                t.store_function    = map.__setitem__
            else:
                if t.contains_function(definition):
                    return

                t.store_function(definition)
                t.append_function(definition)

            t.add_variable(definition.a.name.find_identifier())


        def dump_variables(t, name):
            line('===  %s %s  ===', t.display_name, name)

            function_many = t.function_many

            if function_many is not 0:
                if type(function_many) is not List:
                    s = function_many.a.name.find_identifier().s

                    dump_token(arrange('Only function: %s.%s', name, s), function_many)

                    if t.function_map is not 0:
                        t.function_map.dump_variables(arrange('%s.%s', name, s))
                else:
                    for [i, v] in enumerate(function_many):
                        s = v.a.name.find_identifier().s
                        dump_token(arrange('function #%d: %s.%s', i, name, s), v)

                        t.function_map[v].dump_variables(arrange('%s.%s', name, s))

            variable_map = t.variable_map

            if variable_map is not 0:
                line('===  variables %s  ===', name)

                for k in iterate_values_sorted_by_key({ k.s : k   for k in variable_map }):
                    line('  %s: %s', k.s, variable_map[k])


        def scan_functions(t):
            function_many = t.function_many

            if function_many is 0:
                return

            if type(function_many) is not List:
                t.function_map = art = create_function_symbol_table(t)

                function_many.a.parameters.scan_parameters(art)
                function_many.b           .scan_variables(art)

                art.scan_functions()

                return

            for v in function_many:
                art = create_function_symbol_table(t)

                t.function_map[v] = art

                v.a.parameters.scan_parameters(art)
                v.b           .scan_variables(art)

                art.scan_functions()


    construct_BaseSymbolTable = BaseSymbolTable.__init__


    class FunctionSymbolTable(BaseSymbolTable):
        __slots__ = ((
            'parent',                   #   GlobalSymbolTable
        ))


        display_name = 'function-symbol-table'


        def __init__(t, parent):
            construct_BaseSymbolTable(t)

            t.parent = parent

        
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
