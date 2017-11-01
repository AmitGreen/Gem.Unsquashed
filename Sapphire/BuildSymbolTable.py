#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.BuildSymbolTable')
def gem():
    require_gem('Sapphire.Variable')


    def construct__build_nested_symbol_table(t, write_global_variable, parent):
        construct_BaseBuildSymbolTable(t)

        t.write_global_variable = write_global_variable
        t.parent                = parent


    def finalize_variables__build_nested_symbol_table(t):
        variable_map = t.variable_map

        if variable_map is 0:
            return

        parent = t.parent

        if parent.is_global_symbol_table:
            parent_variable_map = parent = 0
        else:
            parent_variable_map = parent.variable_map

        for [k, v] in view_items(variable_map):
            if v is not 0:
                continue

            if parent_variable_map is not 0:
                w = parent_variable_map.get(k)

                if w is not none:
                    if w.is_global_variable:
                        variable_map[k] = global_variable = conjure_global_variable(k)
                        t.write_global_variable(global_variable)
                        continue

                    if not w.is_cell_variable:
                        parent_variable_map[k] = w.conjure_cell(w.index, k, parent.cell_index)
                        parent.cell_index += 1

                    variable_map[k] = conjure_free_variable(t.cell_index, k)
                    t.cell_index += 1
                    continue

            if parent is not 0:
                ancestor = parent.parent

                while ancestor.is_function_symbol_table:
                    ancestor_variable_map = ancestor.variable_map

                    if ancestor_variable_map is not 0:
                        w = ancestor_variable_map.get(k)

                        if w is not none:
                            if w.is_global_variable:
                                break

                            if not w.is_cell_variable:
                                ancestor_variable_map[k] = w.conjure_cell(w.index, k, ancestor.cell_index)
                                ancestor.cell_index += 1

                            variable_map[k] = conjure_free_variable(t.cell_index, k)
                            t.cell_index += 1
                            break

                    ancestor = ancestor.parent
                else:
                    variable_map[k] = global_variable = conjure_global_variable(k)
                    t.write_global_variable(global_variable)
                    continue

                if not w.is_global_variable:
                    syncronize = parent

                    while syncronize is not ancestor:
                        syncronize_variable_map = syncronize.variable_map

                        free_variable = conjure_free_variable(syncronize.cell_index, k)

                        syncronize.cell_index += 1

                        if syncronize_variable_map is 0:
                            syncronize.variable_map     = variable_map = { k : free_variable }
                            syncronize.lookup_variable  = variable_map.get
                            syncronize.provide_variable = variable_map.setdefault
                            syncronize.store_variable   = variable_map.__setitem__
                        else:
                            syncronize_variable_map[k] = free_variable

                        syncronize = syncronize.parent

                    continue

            variable_map[k] = global_variable = conjure_global_variable(k)
            t.write_global_variable(global_variable)


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


    class BaseBuildSymbolTable(Object):
        __slots__ = ((
            'definition_many',          #   Zero | (ClassDefinition | FunctionDefinition)
                                        #       | List of (ClassDefinition | FunctionDefinition)
            'append_definition',        #   Vacant | Method

            'definition_map',           #   Vacant | BuildClassSymbolTable | BuildFunctionSymbolTable
                                        #       | Map { ClassDefinition | FunctionDefinition }
                                        #             of (BuildClassSymbolTable | BuildFunctionSymbolTable)
            'contains_definition',      #   Vacant | Method
            'store_definition',         #   Vacant | Method

            'variable_map',             #   Zero | Map { Name } of ( FunctionParameter | LocalVariable )
            'variable_index',           #   Integer
            'lookup_variable',          #   Vacant | Method
            'provide_variable',         #   Vacant | Method
            'store_variable',           #   Vacant | Method

            'cell_index',               #   Integer
        ))


        def __init__(t):
            t.definition_many   = 0
           #t.append_definition = vacant

           #t.definition_map      = vacant
           #t.contains_definition = vacant
           #t.store_definition    = vacant

            t.variable_index   = t.variable_map = 0
           #t.lookup_variable  = vacant
           #t.provide_variable = vacant
           #t.store_variable   = vacant

            t.cell_index = 0


        def add_definition(t, definition):
            definition_many = t.definition_many

            if definition_many is 0:
                t.definition_many = definition
                t.definition_map  = 0
            elif type(definition_many) is not List:
                if definition_many is definition:
                    return

                t.definition_many   = many = [definition_many, definition]
                t.append_definition = many.append

                t.definition_map      = map = { definition_many : 0, definition : 0 }
                t.contains_definition = map.__contains__
                t.store_definition    = map.__setitem__
            else:
                if t.contains_definition(definition):
                    return

                t.store_definition(definition, 0)
                t.append_definition(definition)

            t.write_variable(definition.a.name.find_identifier())


        def dump_variables(t, name):
            line('===  %s %s  ===', t.display_name, name)

            definition_many = t.definition_many

            if definition_many is not 0:
                if type(definition_many) is not List:
                    s = definition_many.a.name.find_identifier().s

                    dump_token(arrange('only function: %s.%s', name, s), definition_many)

                    if t.definition_map is not 0:
                        t.definition_map.dump_variables(arrange('%s.%s', name, s))
                else:
                    for [i, v] in enumerate(definition_many):
                        s = v.a.name.find_identifier().s
                        dump_token(arrange('function #%d: %s.%s', i, name, s), v)

                        t.definition_map[v].dump_variables(arrange('%s.%s', name, s))

            variable_map = t.variable_map

            if variable_map is not 0:
                line('===  variables %s  ===', name)

                for k in iterate_values_sorted_by_key({ k.s : k   for k in variable_map }):
                    line('  %s: %s', k.s, variable_map[k])


        def scout_definitions(t):
            def scout_nested_definition(v):
                #line('Scouting: %r', v.a.name)

                if v.is_function_definition:
                    art = BuildFunctionSymbolTable(
                              (t.write_global_variable   if t.is_global_symbol_table else   t.write_global_variable),
                              (t.parent                  if t.is_class_symbol_table  else   t),
                          )

                    v.a.parameters.add_parameters(art)
                else:
                    art = BuildClassSymbolTable(
                              (t.write_global_variable   if t.is_global_symbol_table else   t.write_global_variable),
                              BuildWrapperSymbolTable(
                                  (t.parent              if t.is_class_symbol_table  else   t),
                              ),
                          )

                v.b.scout_variables(art)

                art.finalize_variables()
                art.scout_definitions()

                return art


            definition_many = t.definition_many

            if definition_many is 0:
                return

            if type(definition_many) is not List:
                t.definition_map = scout_nested_definition(definition_many)

                return

            store_definition = t.store_definition

            for v in definition_many:
                store_definition(v, scout_nested_definition(v))


        def fetch_variable(t, name):
            variable_map = t.variable_map

            if variable_map is 0:
                t.variable_map     = variable_map = { name : 0 }
                t.lookup_variable  = variable_map.get
                t.provide_variable = variable_map.setdefault
                t.store_variable   = variable_map.__setitem__
                return

            t.provide_variable(name, 0)


    construct_BaseBuildSymbolTable = BaseBuildSymbolTable.__init__


    class BuildClassSymbolTable(BaseBuildSymbolTable):
        __slots__ = ((
            'write_global_variable',    #   Method
            'parent',                   #   BuildWrapperSymbolTable
        ))


        display_name             = 'class-symbol-table'
        is_class_symbol_table    = true
        is_function_symbol_table = false
        is_global_symbol_table   = false
        is_nested_symbol_table   = true


        __init__           = construct__build_nested_symbol_table
        finalize_variables = finalize_variables__build_nested_symbol_table


        def dump_variables(t, name):
            t.parent.dump_variables(arrange('wrapper for %s', name))
            BaseBuildSymbolTable.dump_variables(t, name)


    class BuildFunctionSymbolTable(BaseBuildSymbolTable):
        __slots__ = ((
            'write_global_variable',    #   Method
            'parent',                   #   BaseBuildSymbolTable+
            'local_variables',          #   Vacant | (FunctionParameter | FunctionLocal)
                                        #       | List of (FunctionParameter | FunctionLocal)
        ))


        display_name             = 'function-symbol-table'
        is_class_symbol_table    = false
        is_function_symbol_table = true
        is_global_symbol_table   = false
        is_nested_symbol_table   = true


        def __init__(t, write_global_variable, parent):
            construct_BaseBuildSymbolTable(t)

            t.write_global_variable = write_global_variable
            t.parent                = parent
            t.local_variables       = 0


        def add_parameter(t, name):
            variable_map = t.variable_map

            if variable_map is 0:
                t.local_variables = parameter = conjure_function_parameter(0, name)

                t.variable_map     = variable_map = { name : parameter }
                t.variable_index   = 1
                t.lookup_variable  = variable_map.get
                t.provide_variable = variable_map.setdefault
                t.store_variable   = variable_map.__setitem__
                return

            if t.lookup_variable(name):
                raise_runtime_error('parameter %s declared multiple times', name)

            parameter = conjure_function_parameter(t.variable_index, name)

            local_variables = t.local_variables

            if type(local_variable) is not List:
                t.local_variables = [local_variables, parameter]
            else:
                t.local_variables.append(parameter)

            t.variable_index = index + 1

            t.store_variable(name, parameter)


        finalize_variables = finalize_variables__build_nested_symbol_table


    class BuildGlobalSymbolTable(BaseBuildSymbolTable):
        __slots__ = (())


        display_name             = 'global-symbol-table'
        is_class_symbol_table    = false
        is_function_symbol_table = false
        is_global_symbol_table   = true
        is_nested_symbol_table   = false


        def write_global_variable(t, global_variable):
            variable_map = t.variable_map

            if variable_map is 0:
                t.variable_map     = variable_map = { global_variable.name : global_variable }
                t.lookup_variable  = variable_map.get
                t.provide_variable = variable_map.setdefault
                t.store_variable   = variable_map.__setitem__
                return

            t.store_variable(global_variable.name, global_variable)


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


    class BuildWrapperSymbolTable(BaseBuildSymbolTable):
        __slots__ = ((
            'parent',                   #   BaseBuildSymbolTable+
        ))


        display_name             = 'wrapper-symbol-table'
        is_class_symbol_table    = false
        is_function_symbol_table = false
        is_global_symbol_table   = false
        is_nested_symbol_table   = true


        def __init__(t, parent):
            construct_BaseBuildSymbolTable(t)

            t.parent = parent


        finalize_variables = finalize_variables__build_nested_symbol_table


    write_variable = produce_write_variable('write_variable', conjure_local_variable)

    BuildClassSymbolTable   .write_variable = write_variable
    BuildFunctionSymbolTable.add_parameter  = produce_write_variable('add_parameter', conjure_function_parameter)
    BuildFunctionSymbolTable.write_variable = write_variable


    #
    #   .conjure_cell
    #
    FunctionParameter.conjure_cell = static_method(conjure_cell_function_parameter)
    LocalVariable    .conjure_cell = static_method(conjure_cell_local)


    @share
    def create_build_global_symbol_table():
        return BuildGlobalSymbolTable()
