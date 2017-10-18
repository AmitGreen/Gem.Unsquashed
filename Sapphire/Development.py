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
        path = 'test.py'

        require_gem('Sapphire.Pattern')

        create_sapphire_match()

        require_gem('Sapphire.Parse')                       #   Must be after 'create_sapphire_match'

        tree = parse_python(path, test = 7, show = 0)

        assert length(tree) == 1

        first = tree[0]

        if show is 7:
            dump_token('development', first)

        if adorn is 7:
            global_scope = {
                '__builtins__' : 1,
                '__doc__'      : none,
                '__file__'     : path,
                '__name__'     : '__main__',
                '__package__'  : none,
            }

            art = create_global_symbol_table(global_scope)

            first.scan_variables(art)

            first_2 = first.adorn(art)

            art.dump_variables()

        dump_caches('function_parameter')
