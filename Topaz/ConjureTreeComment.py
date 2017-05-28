#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Topaz.ConjureTreeComment')
def gem():
    require_gem('Topaz.Core')
    require_gem('Pearl.Comment')


    from Pearl import conjure_tree_comment, tree_comment_cache


    def dump_tree_comment_cache():
        line('===  Dump of tree_comment_cache  ===')

        for [k1, v1] in iterate_items_sorted_by_key(tree_comment_cache):
            if type(v1) is not Map:
                line('%r: %r', k1, v1)
                continue

            line('%r:', k1)

            for [k2, v2] in iterate_items_sorted_by_key(v1):
                if type(v2) is not Map:
                    line('  %r: %r', k2, v2)
                    continue

                line('  %r:', k2)

                for [k3, v3] in iterate_items_sorted_by_key(v2):
                    line('    %r: %r', k3, v3)

    @share
    def test_conjure_tree_comment():
        conjure_tree_comment('#', '1', '\n')
        conjure_tree_comment('#', '2', '\n')
        conjure_tree_comment('#1', '2', '\n')
        conjure_tree_comment('#2', '2', '\n')
        conjure_tree_comment('#2', '2', '1\n')
        conjure_tree_comment('#2', '2', '2\n')
        conjure_tree_comment('#2', '2', '3\n')
        conjure_tree_comment('#', '3', '1\n')
        conjure_tree_comment('#', '3', '2\n')
        conjure_tree_comment('#', '3', '3\n')
        conjure_tree_comment('#', '3', '3\n')

        dump_tree_comment_cache()
