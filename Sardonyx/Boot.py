#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@boot('Boot')
def boot():
    #
    #   This really belongs in Gem.Core, but is here since we need it during Boot
    #
    PythonSystem = __import__('sys')
    PythonTypes  = __import__('types')
    PythonPath   = __import__('os.path').path


    is_python_2     = (PythonSystem.version_info.major is 2)
    is_python_3     = (PythonSystem.version_info.major is 3)


    PythonBuiltIn = __import__('__builtin__'  if is_python_2 else   'builtins')


    #
    #   Python keywords
    #
    false = False
    none  = None
    true  = True


    #
    #   Python functions
    #
    intern_string = (PythonBuiltIn   if is_python_2 else   PythonSystem).intern
    module_path   = PythonSystem.path
    path_absolute = PythonPath.abspath
    path_join     = PythonPath.join


    #
    #   python_modules (also lookup_python_module & store_python_module)
    #
    python_modules       = PythonSystem.modules
    lookup_python_module = python_modules.get
    store_python_module  = python_modules.__setitem__


    #
    #   Gem_name
    #
    Gem_name = intern_string('Gem')


    #
    #   Calculate root & Gem paths
    #
    root_path = intern_string(path_absolute(path_join(module_path[0], '../..')))
    Gem_path  = intern_string(path_join(root_path, Gem_name))


    #
    #   Store root path
    #
    module_path[0] = root_path


    #
    #   Create Gem Module
    #
    ModuleType = type(PythonSystem)

    Gem = ModuleType(Gem_name)

    Gem.__file__ = intern_string(path_join(Gem_path, '__init__.py'))
    Gem.__path__ = [Gem_path]


    store_python_module(Gem_name, Gem)


    #
    #   Set flag to indicate using fast loading mode
    #
    Gem.fast_cache = fast_cache = {}

    find_fast  = fast_cache.get
    store_fast = fast_cache.__setitem__


    def gem(module_name):
        def execute(f):
            store_fast(module_name, f)

            return gem


        return execute


    __import__(__name__).gem = gem


    def boot():
        fast_cache['Gem.Boot']()

        f        = find_fast('Sapphire.Main')
        gem_main = __import__('__main__').gem('Sapphire.Main')

        gem_main(f)


    return boot
