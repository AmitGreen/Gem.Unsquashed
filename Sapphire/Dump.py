#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Dump')
def gem():
    @share
    def dump_cache(name, cache):
        line('===  %s  ===', name)

        for [k, v] in iterate_items_sorted_by_key(cache):
            line('%s:', k.display_token())

            if v.__class__ is Map:
                for [k2, w] in iterate_items_sorted_by_key(v):
                    line('  %s:', k2.display_token())
                    line('    %s', w.display_token())

                continue

            line('  %s', v.display_token())
