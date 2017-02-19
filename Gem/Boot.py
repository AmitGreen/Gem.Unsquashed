#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#


def gem(module_name):
    def execute(f):
        return f()

    return execute


@gem('Gem.Boot')
def gem():
    #
    #   This really belongs in Gem.Core, but is here since we need it during Boot
    #
    PythonSystem = __import__('sys')
    is_python_2   = PythonSystem.version_info.major is 2
    is_python_3   = PythonSystem.version_info.major is 3
    PythonCore    = __import__('__builtin__'  if is_python_2 else   'builtins')


    #
    #   Python keywords
    #
    none = None

    #
    #   Python Functions
    #
    intern_string = (PythonCore   if is_python_2 else   PythonSystem).intern
    iterate       = PythonCore.iter
    length        = PythonCore.len


    #
    #   Python types
    #
    Module    = PythonCore.__class__
    LiquidSet = PythonCore.set
    String    = PythonCore.str


    #
    #   Python methods
    #
    python_modules      = PythonSystem.modules
    store_python_module = python_modules.__setitem__


    #
    #   Gem
    #       Replace the index in python_modules & also Gem.__name__ with an intern'ed copy of 'Gem'.
    #
    Gem       = python_modules['Gem']
    Gem_name  = Gem.__name__ = intern_string(Gem.__name__)
    gem_scope = Gem.__dict__

    store_python_module(Gem_name, Gem)


    #
    #   Gem{Builtin,Privileged,Shared}_scope
    #
    special_builtins_name = intern_string('__builtins__')
    special_name          = intern_string('__name__')
    GemBuiltIn_scope      = { special_name : intern_string('Gem.BuiltIn') }
    GemPrivileged_scope   = {
                                special_builtins_name : PythonCore.__dict__,
                                special_name          : intern_string('Gem.Privileged'),
                            }
    GemShared_scope       = {
                              special_builtins_name : GemBuiltIn_scope,
                              special_name          : intern_string('Gem.Shared'),
                            }

    #
    #   boot
    #
    def boot():
        del Gem.Boot
        del python_modules['Gem.Boot']


    #
    #   Function
    #
    Function = boot.__class__

    if is_python_2:
        function_closure  = Function.func_closure .__get__
        function_code     = Function.func_code    .__get__
        function_defaults = Function.func_defaults.__get__
        function_globals  = Function.func_globals .__get__
    else:
        function_closure  = Function.__closure__ .__get__
        function_code     = Function.__code__    .__get__
        function_defaults = Function.__defaults__.__get__
        function_globals  = Function.__globals__ .__get__

    function_name = Function.__dict__['__name__'].__get__


    #
    #   localize, privilege, & localize3_or_privileged2
    #
    #       Strickly speaking:
    #
    #           We don't really need to localize ourselves ...
    #           (since is never exported or referenced once this function finishes)
    #
    #       However ... might as well ... hence: 'localize = localize(localize)'
    #
    def produce_change_scope(scope):
        def change_scope(f):
            return Function(
                       function_code(f),
                       scope,
                       function_name(f),
                       function_defaults(f),
                       function_closure(f),
                   )

        return change_scope


    privileged = produce_change_scope(GemPrivileged_scope)
    privileged = privileged(privileged)                     #   Make ourselves privileged ;)
    localize   = privileged(produce_change_scope(GemShared_scope))

    localize3_or_privileged2 = (privileged   if is_python_2 else   localize)


    #
    #   next_method
    #       Access the .next method of an iterator
    #
    #       (Deals with the annoyance of .next method named .next in python 2.0, but .__next__ in python 3.0)
    #
    if is_python_2:
        @localize
        def next_method(iterator):
            return iterator.next
    else:
        @localize
        def next_method(iterator):
            return iterator.__next__


    #
    #   export
    #       Exports a function to Gem (Global Execution Module); also the actual function exported
    #       is a copy of the original function -- but with its global scope replaced to be Gem's scope.
    #
    #       Can also be used with multiple arguments to export a list of values (no replacement of
    #       global scope's is done in this case).
    #
    @localize3_or_privileged2
    def produce_actual_export(scope, insert):
        def export(f, *arguments):
            if length(arguments) is 0:
                if (f.__class__ is Function) and (function_globals(f) is not GemPrivileged_scope):
                    name = intern_string(function_name(f))

                    return insert(
                               name,
                               Function(
                                   function_code(f),
                                   scope,                   #   Replace global scope with module's scope
                                   name,
                                   function_defaults(f),
                                   function_closure(f),
                               ),
                           )

                return insert(intern_string(f.__name__), f)

            argument_iterator = iterate(arguments)
            next_argument     = next_method(argument_iterator)

            assert f.__class__ is String

            insert(f, next_argument())

            for name in argument_iterator:
                assert name.__class__ is String

                insert(intern_string(name), next_argument())


        return export


    #
    #   share_code
    #
    if __debug__:
        #
        #   Code
        #
        Code = function_code(boot).__class__


        code_argument_count    = Code.co_argcount   .__get__
        code_cell_vars         = Code.co_cellvars   .__get__
        code_constants         = Code.co_consts     .__get__
        code_filename          = Code.co_filename   .__get__
        code_first_line_number = Code.co_firstlineno.__get__
        code_flags             = Code.co_flags      .__get__
        code_free_variables    = Code.co_freevars   .__get__
        code_global_names      = Code.co_names      .__get__
        code_line_number_table = Code.co_lnotab     .__get__
        code_name              = Code.co_name       .__get__
        code_number_locals     = Code.co_nlocals    .__get__
        code_stack_size        = Code.co_stacksize  .__get__
        code_variable_names    = Code.co_varnames   .__get__
        code_virtual_code      = Code.co_code       .__get__

        if not is_python_2:
            code_keyword_only_argument_count = Code.co_kwonlyargcount.__get__


        #
        #   rename_export_code
        #
        if is_python_2:
            def rename_code(code, interned_name):
                return Code(
                           code_argument_count   (code),
                           code_number_locals    (code),
                           code_stack_size       (code),
                           code_flags            (code),
                           code_virtual_code     (code),
                           code_constants        (code),
                           code_global_names     (code),
                           code_variable_names   (code),
                           code_filename         (code),
                           intern_string(interned_name),                #   Rename to 'name'
                           code_first_line_number(code),
                           code_line_number_table(code),
                           code_free_variables   (code),
                           code_cell_vars        (code),
                      )
        else:
            def rename_code(code, interned_name):
                return Code(
                           code_argument_count             (code),
                           code_keyword_only_argument_count(code),
                           code_number_locals              (code),
                           code_stack_size                 (code),
                           code_flags                      (code),
                           code_virtual_code               (code),
                           code_constants                  (code),
                           code_global_names               (code),
                           code_variable_names             (code),
                           code_filename                   (code),
                           intern_string(interned_name),                #   Rename to 'name'
                           code_first_line_number          (code),
                           code_line_number_table          (code),
                           code_free_variables             (code),
                           code_cell_vars                  (code),
                      )


    #
    #
    #
    if __debug__:
        def rename_function(name, f, code = none):
            name = intern_string(name)

            return Function(
                       (code) or (rename_code(function_code(f), name)),
                       function_globals(f),
                       name,
                       function_defaults(f),
                       function_closure(f),
                   )
    else:
        def rename_function(name, f, code = none):
            return f


    #
    #   Rename
    #
    if __debug__:
        def rename(name):
            def rename(f):
                return rename_function(name, f)

            return rename

                        
    #
    #   share_code
    #
    if __debug__:
        share_code = rename_code(function_code(produce_actual_export(0, 0)), 'share')


    #
    #   arrange
    #
    @localize
    def arrange(format, *arguments):
        return format % arguments


    #
    #   raise_already_exists
    #
    if __debug__:
        PythonException = (__import__('exceptions')   if is_python_2 else  PythonCore)
        NameError       = PythonException.NameError


        @localize
        def raise_already_exists(module_name, name, previous, exporting):
            name_error = arrange("%s.%s already exists (value: %r): can't export %r also",
                                 module_name, name, previous, exporting)

            raise NameError(name_error)


    #
    #   produce_dual_insert
    #
    if __debug__:
        @localize
        def produce_dual_insert(function_name, single_insert, provide, module_name):
            module_name = intern_string(module_name)


            @rename(function_name)
            def dual_insert(name, exporting):
                previous = provide(name, single_insert(name, exporting))

                if previous is exporting:
                    return exporting

                raise_already_exists(module_name, name, previous, exporting)


            return dual_insert
    else:
        @localize
        def produce_dual_insert(function_name, single_insert, provide, module_name):
            def dual_insert(name, exporting):
                return provide(name, single_insert(name, exporting))


            return dual_insert


    #
    #   produce_single_insert
    #
    if __debug__:
        @localize
        def produce_single_insert(function_name, provide, module_name):
            module_name = intern_string(module_name)


            @rename(function_name)
            def single_insert(name, exporting):
                previous = provide(name, exporting)

                if previous is exporting:
                    return previous

                raise_already_exists(module_name, name, previous, exporting)


            return single_insert
    else:
        @localize
        def produce_single_insert(function_name, provide, module_name):
            return provide


    #
    #   built_in & restricted
    #
    insert_privileged = produce_single_insert(
                            'insert_privileged',
                            GemPrivileged_scope.setdefault,
                             GemPrivileged_scope[special_name],
                        )

    insert__built_in = produce_dual_insert(
                           'insert__built_in',
                           insert_privileged,
                           GemBuiltIn_scope.setdefault,
                           GemBuiltIn_scope[special_name],
                       )

    built_in   = produce_actual_export(GemShared_scope, insert__built_in)
    restricted = produce_actual_export(GemShared_scope, insert_privileged)


    if __debug__:
        built_in   = rename_function('built_in',   built_in,   code = share_code)
        restricted = rename_function('restricted', restricted, code = share_code)


    #
    #   produce_export_and_share
    #
    if __debug__:
        share_name = intern_string('share')


    @localize
    def produce_export_and_share(module, shared_scope = none):
        module_name  = module.__name__ = intern_string(module.__name__)
        module_scope = module.__dict__

        if shared_scope is none:
            shared_scope = {}

        insert_share = produce_single_insert(
                           'insert_share',
                           shared_scope.setdefault,
                           arrange('%s.Shared', module_name),
                       )

        insert_export = produce_dual_insert(
                            'insert_export',
                            insert_share,
                            module_scope.setdefault,
                            module_name,
                        )


        export = produce_actual_export(shared_scope, insert_export)
        share  = produce_actual_export(shared_scope, insert_share)

        if __debug__:
            share = rename_function(share_name, share, code = share_code)

        export('Shared', shared_scope)

        return ((export, share))


    #
    #   export & share
    #
    [export, share] = produce_export_and_share(Gem, shared_scope = GemShared_scope)


    #
    #   Initial built-in's
    #
    built_in(
        #
        #   Keywords
        #       implemented as keywords in Python 3.0 --so can't use an expression like 'PythonCore.None'.
        #
        'false',    False,
        'none',     None,
        'true',     True,


        #
        #   Functions
        #
        'arrange',      arrange,
        'privileged',   privileged,
    )


    #
    #   Only put in GemBuiltin_scope: __build__class & __import__
    #
    #       (not needed in GemPrivileged_scope, since it is found in GemPrivileged_scope['__builtins__'])
    #
    if is_python_3:
        GemBuiltIn_scope[intern_string(PythonCore.__build_class__.__name__)] = PythonCore.__build_class__


    GemBuiltIn_scope[intern_string(PythonCore.__import__.__name__)] = PythonCore.__import__


    #
    #   Initial shares's
    #
    share(
        'built_in',     built_in,
        'export',       export,
        'share',        share,
        'restricted',   restricted,
        'Privileged',   GemPrivileged_scope
    )


    #
    #   gem
    #
    gem_name = intern_string('gem')


    @export
    @privileged
    def gem(module_gem):
        def execute(f):
            assert f.__name__ == gem_name

            Function(
                function_code(f),
                GemShared_scope,         #   Replace global scope with Gem' shared scope
                gem_name,
                function_defaults(f),
                function_closure(f),
            )(
            )

            return gem

        return execute


    #
    #   require_gem
    #
    gem_modules    = LiquidSet()
    add_gem_module = gem_modules.add
    has_gem_module = gem_modules.__contains__

    if is_python_2:
        #
        #   Python 2.0 method of loading a module with 'gem' pre-initialized
        #
        #       This is messy -- see below for the Python 3.0 method which is much cleaner.
        #
        PythonOldImport = __import__('imp')
        find_module     = PythonOldImport.find_module
        load_module     = PythonOldImport.load_module


        @export
        @privileged
        def require_gem(module_name):
            if has_gem_module(module_name):
                return

            module_name = intern_string(module_name)

            add_gem_module(module_name)

            module     = Module(module_name)
            module.gem = gem

            #
            #   Temporarily store our module in 'python_modules[module_name]'.
            #
            #   This is needed in python 2.0, as the way to pass the 'pre-initialized' module to 'load_module'
            #
            #       (In the cleaner python 3.0 version below, we pass the modules directly to 'exec_module'
            #       and thus do not need to store the module in 'python_modules[module_name]').
            #
            #   NOTE:
            #       If this was real import implementation we would need to cleanup
            #       'python_modules[module_name]' When an exception is thrown.
            #
            #       However, this is not a true import mechanism.  If it fails, our program will simply
            #       exit.
            #
            #       Therefore, there is no 'try' clause below to cleanup if 'load_module' throws ImportError
            #
            store_python_module(module_name, module)

            dot_index = module_name.rfind('.')

            if dot_index is -1:
                [f, pathname, description] = find_module(module_name)
            else:
                [f, pathname, description] = find_module(
                                                 module_name[dot_index + 1:],
                                                 python_modules[module_name[:dot_index]].__path__,
                                             )

            #
            #   CAREFUL here:
            #       We *MUST* close 'f' if any exception is thrown.
            #
            #       So ASAP use 'f' within a 'with' clause (this ensures 'f' is always closed, whether
            #       an exception is thrown or not)
            #
            if f is not none:
                with f:
                    load_module(module_name, f, pathname, description)
            else:
                load_module(module_name, f, pathname, description)

            #
            #   discard the module, it is no longer needed
            #
            del python_modules[module_name]


    else:
        #
        #   Python 3.0 method of loading a module with 'gem' pre-initialized
        #
        PythonImportUtility          = __import__('importlib.util').util
        ImportError                  = PythonCore.ImportError
        lookup_module_blueprint      = PythonImportUtility.find_spec
        create_module_from_blueprint = PythonImportUtility.module_from_spec


        @export
        def require_gem(module_name):
            if has_gem_module(module_name):
                return

            module_name = intern_string(module_name)

            add_gem_module(module_name)

            blueprint = lookup_module_blueprint(module_name)

            if blueprint is none:
                raise ImportError("Can't find module %s" % module_name)

            module     = create_module_from_blueprint(blueprint)
            module.gem = gem

            blueprint.loader.exec_module(module)



    require_gem('Gem.Core')


    #
    #   main
    #
    Main = python_modules['__main__']


    @localize
    def main(module_name):
        assert module_name == 'Main'


        def export(f):
            assert f.__name__ == 'main'

            del Main.export

            return produce_export_and_share(Main)[0](f)


        def execute(f):
            assert f.__name__ == 'main'

            f()

            Main.main()


        del Main.boot
        del Main.main

        Main.export      = export
        Main.require_gem = require_gem

        return execute


    Gem.boot = boot


    Main.__builtins__ = GemBuiltIn_scope
    Main.main         = main

    del Gem.__builtins__
    del Gem.__package__


if 1:
    import Gem

    Gem_keys      = sorted(Gem.__dict__.keys())
    built_in_keys = sorted(Gem.Shared['__builtins__'].keys())

    print('Gem: ',        Gem_keys)
    print('Builtins: ',   built_in_keys)
    print('Shared: ',     sorted(k   for k in Gem.Shared.keys()   if k not in Gem_keys))
    print('Privileged: ', sorted(k   for k in Gem.Shared['Privileged'].keys()   if k not in built_in_keys))
