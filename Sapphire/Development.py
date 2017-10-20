#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Development')
def gem():
    adorn = 0
    dump  = 0
    show  = 7


    require_gem('Sapphire.Cache')
    require_gem('Sapphire.SymbolTable')


    @share
    def development():
        path = 'test.py'

        require_gem('Sapphire.Pattern')

        create_sapphire_match()

        require_gem('Sapphire.Parse')                       #   Must be after 'create_sapphire_match'

        tree = parse_python(path, test = 7, show = 0)

        if show is 7:
            for v in tree:
                dump_token('v', v)

        if adorn is 7:
            art = create_global_symbol_table()

            for s in ['__builtins__', '__doc__', '__file__', '__name__', '__package__']:
                art.write_variable(conjure_name(s))
                
            for v in tree:
                v.scout_variables(art)

            art.scout_functions()

            #first_2 = first.adorn(art)

            art.dump_variables('globals')

        if dump is 7:
            dump_caches('cell_function_parameter')
            dump_caches('cell_local')
            dump_caches('function_parameter')
            dump_caches('free_variable')
            dump_caches('local_variable')
            dump_caches('global_variable')
