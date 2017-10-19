#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.SymbolTable')
def gem():
    require_gem('Sapphire.Cache')


    cell_function_parameter_cache = {}
    cell_local_cache              = {}
    free_variable_cache           = {}
    function_parameter_cache      = {}
    global_variable_cache         = {}
    local_variable_cache          = {}


    def construct__index_name(t, index, name):
        t.index = index
        t.name  = name


    def construct__index_name__cell_index(t, index, name, cell_index):
        t.index      = index
        t.name       = name
        t.cell_index = cell_index


    def portray__index_name(t):
        return arrange('<%s#%d %s>', t.display_name, t.index, t.name.s)


    def portray__index_name__cell_index(t):
        return arrange('<%s#%d %s; cell#%d>', t.display_name, t.index, t.name.s, t.cell_index)


    class CellFunctionParameter(Object):
        __slots__ = ((
            'index',                    #   Integer
            'name',                     #   Identifier
            'cell_index',               #   Integer
        ))


        display_name       = 'cell-parameter'
        is_cell_variable   = true
        is_global_variable = false


        __init__      = construct__index_name__cell_index
        __repr__      = portray__index_name__cell_index
        display_token = portray__index_name__cell_index


    CellFunctionParameter.k1  = CellFunctionParameter.index
    CellFunctionParameter.k2  = CellFunctionParameter.name
    #CellFunctionParameter.k3 = CellFunctionParameter.cell_index


    class CellLocal(Object):
        __slots__ = ((
            'index',                    #   Integer
            'name',                     #   Identifier
            'cell_index',               #   Integer
        ))


        display_name       = 'cell-local'
        is_cell_variable   = true
        is_global_variable = false


        __init__      = construct__index_name__cell_index
        __repr__      = portray__index_name__cell_index
        display_token = portray__index_name__cell_index


    CellLocal.k1  = CellLocal.index
    CellLocal.k2  = CellLocal.name
    #CellLocal.k3 = CellLocal.cell_index


    class FreeVariable(Object):
        __slots__ = ((
            'index',                    #   Integer
            'name',                     #   Identifier
        ))


        display_name       = 'free-variable'
        is_cell_variable   = true
        is_global_variable = false


        __init__      = construct__index_name
        __repr__      = portray__index_name
        display_token = portray__index_name


    #FreeVariable.k1 = FreeVariable.index
    FreeVariable.k2 = FreeVariable.name


    class FunctionParameter(Object):
        __slots__ = ((
            'index',                    #   Integer
            'name',                     #   Identifier
        ))


        display_name       = 'parameter'
        is_global_variable = false


        __init__      = construct__index_name
        __repr__      = portray__index_name
        display_token = portray__index_name


    #FunctionParameter.k1 = FunctionParameter.index
    FunctionParameter.k2 = FunctionParameter.name


    class GlobalVariable(Object):
        __slots__ = ((
            'name',                     #   Identifier
        ))


        is_global_variable = true


        def __init__(t, name):
            t.name = name


        def __repr__(t):
            return arrange('<global %s>', t.name.s)


        display_token = __repr__


    class LocalVariable(Object):
        __slots__ = ((
            'index',                    #   Integer
            'name',                     #   Identifier
        ))


        display_name       = 'local'
        is_cell_variable   = false
        is_global_variable = false


        __init__      = construct__index_name
        __repr__      = portray__index_name
        display_token = portray__index_name


    #LocalVariable.k1 = LocalVariable.index
    LocalVariable.k2 = LocalVariable.name


    @privileged
    def produce_write_variable(name, conjure):
        def write_variable(t, name):
            variable_map = t.variable_map

            if variable_map is 0:
                t.variable_map     = variable_map = { name : conjure(0, name) }
                t.variable_index   = 1
                t.lookup_variable  = variable_map.get
                t.provide_variable = variable_map.setdefault
                t.store_variable   = variable_map.__setitem__
                return

            if t.lookup_variable(name):
                return

            index = t.variable_index

            t.store_variable(name, conjure(index, name))

            t.variable_index = index + 1


        if __debug__:
           write_variable.__name__ = intern_string(name)

        return write_variable


    class BaseSymbolTable(Object):
        __slots__ = ((
            'function_many',            #   Zero | FunctionDefinition | List of FunctionDefinition
            'append_function',          #   Vacant | Method

            'function_map',             #   Vacant | FunctionSymbolTable | Map { FunctionDefinition } of FunctionSymbolTable
            'contains_function',        #   Vacant | Method
            'store_function',           #   Vacant | Method

            'variable_map',             #   Zero | Map { Name } of ( FunctionParameter | LocalVariable )
            'variable_index',           #   Integer
            'lookup_variable',          #   Vacant | Method
            'provide_variable',         #   Vacant | Method
            'store_variable',           #   Vacant | Method

            'cell_index',               #   Integer
        ))


        def __init__(t):
            t.function_many   = 0
           #t.append_function = vacant

           #t.function_map     = vacant
           #t.contains_funtion = vacant
           #t.store_function   = vacant

            t.variable_index   = t.variable_map = 0
           #t.lookup_variable  = vacant
           #t.provide_variable = vacant
           #t.store_variable   = vacant

            t.cell_index = 0


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

            t.write_variable(definition.a.name.find_identifier())


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


        def scout_functions(t):
            function_many = t.function_many

            if function_many is 0:
                return

            if type(function_many) is not List:
                t.function_map = art = create_function_symbol_table(t)

                function_many.a.parameters.scout_parameters(art)
                function_many.b           .scout_variables(art)

                art.finalize_variables()
                art.scout_functions()

                return

            for v in function_many:
                art = create_function_symbol_table(t)

                t.function_map[v] = art

                v.a.parameters.scout_parameters(art)
                v.b           .scout_variables(art)

                art.finalize_variables()
                art.scout_functions()


        def fetch_variable(t, name):
            variable_map = t.variable_map

            if variable_map is 0:
                t.variable_map     = variable_map = { name : 0 }
                t.lookup_variable  = variable_map.get
                t.provide_variable = variable_map.setdefault
                t.store_variable   = variable_map.__setitem__
                return

            t.provide_variable(name, 0)


        def write_variable(t, name):
            variable_map = t.variable_map

            if variable_map is 0:
                t.variable_map     = variable_map = { name : conjure_global_variable(name) }
                t.lookup_variable  = variable_map.get
                t.provide_variable = variable_map.setdefault
                t.store_variable   = variable_map.__setitem__
                return

            if t.lookup_variable(name):
                return

            t.store_variable(name, conjure_global_variable(name))


    construct_BaseSymbolTable = BaseSymbolTable.__init__


    class FunctionSymbolTable(BaseSymbolTable):
        __slots__ = ((
            'parent',                   #   GlobalSymbolTable
        ))


        display_name = 'function-symbol-table'


        def __init__(t, parent):
            construct_BaseSymbolTable(t)

            t.parent = parent


        def finalize_variables(t):
            variable_map = t.variable_map

            if variable_map is 0:
                return

            parent              = t.parent
            parent_variable_map = parent.variable_map

            for [k, v] in view_items(variable_map):
                if v is not 0:
                    continue

                if parent_variable_map is not 0:
                    w = parent_variable_map.get(k)

                    if w is not none:
                        if w.is_global_variable:
                            variable_map[k] = conjure_global_variable(k)
                            continue

                        if not w.is_cell_variable:
                            parent_variable_map[k] = w.conjure_cell(w.index, k, parent.cell_index)
                            parent.cell_index += 1

                        variable_map[k] = conjure_free_variable(t.cell_index, k)
                        t.cell_index += 1
                        continue

                line('need to adjust %s', k)
                assert 0, 'incomplete#3'


    class GlobalSymbolTable(BaseSymbolTable):
        __slots__ = (())


        display_name = 'global-symbol-table'


    conjure_cell_function_parameter = produce_conjure_triple__312(
                                          'cell_function_parameter',
                                          CellFunctionParameter,
                                          cell_function_parameter_cache,
                                      )

    conjure_cell_local = produce_conjure_triple__312('cell_local', CellLocal, cell_local_cache)

    conjure_free_variable = produce_conjure_dual('free_variable', FreeVariable, free_variable_cache)

    conjure_function_parameter = produce_conjure_dual(
                                     'function_parameter',
                                     FunctionParameter,
                                     function_parameter_cache,
                                 )

    conjure_global_variable = produce_conjure_single('global_variable', GlobalVariable, global_variable_cache)
    conjure_local_variable  = produce_conjure_dual  ('local_variable',  LocalVariable,  local_variable_cache)


    append_cache('cell_function_parameter', cell_function_parameter_cache)
    append_cache('cell_local',              cell_local_cache)
    append_cache('function_parameter',      function_parameter_cache)
    append_cache('global_variable',         global_variable_cache)
    append_cache('local_variable',          local_variable_cache)


    FunctionSymbolTable.add_parameter  = produce_write_variable('add_parameter',  conjure_function_parameter)
    FunctionSymbolTable.write_variable = produce_write_variable('write_variable', conjure_local_variable)


    #
    #   .conjure_cell
    #
    FunctionParameter.conjure_cell = static_method(conjure_cell_function_parameter)
    LocalVariable    .conjure_cell = static_method(conjure_cell_local)


    @share
    def create_global_symbol_table():
        return GlobalSymbolTable()


    @share
    def create_function_symbol_table(parent):
        return FunctionSymbolTable(parent)
