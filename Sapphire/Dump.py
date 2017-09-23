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

                    if w.__class__ is Map:
                        for [k3, x] in iterate_items_sorted_by_key(w):
                            line('    %s:', k3.display_token())

                            if x.__class__ is Map:
                                for [k4, y] in iterate_items_sorted_by_key(x):
                                    line('      %s:', k4.display_token())
                                    line('        %s', y.display_token())

                                continue

                            line('      %s', x.display_token())

                        continue

                    line('    %s', w.display_token())

                continue

            line('  %s', v.display_token())
