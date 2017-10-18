#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Development')
def gem():
    adorn = 7
    show  = 0


    require_gem('Sapphire.Cache')
    require_gem('Sapphire.SymbolTable')


    @share
    def development():
        require_gem('Sapphire.Pattern')

        create_sapphire_match()

        require_gem('Sapphire.Parse')                       #   Must be after 'create_sapphire_match'

        tree = parse_python('test.py', test = 7, show = 0)

        assert length(tree) == 1

        first = tree[0]

        if show is 7:
            dump_token('development', first)

        if adorn is 7:
            art = create_global_symbol_table()

            first__2 = first.adorn(art)

        dump_caches('function_parameter')
