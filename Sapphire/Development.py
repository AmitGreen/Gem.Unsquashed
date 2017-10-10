#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Development')
def gem():
    adorn = 7
    dump  = 0
    show  = 0


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
            [art, tree] = build_global_symbol_table(tree)

            f = create_TokenOutput()
            art.dump_global_symbol_table(f)

            partial(f.finish())


        if dump is 7:
            dump_caches('cell_function_parameter')
            dump_caches('cell_local')
            dump_caches('function_parameter')
            dump_caches('free_variable')
            dump_caches('local_variable')
            dump_caches('global_variable')
