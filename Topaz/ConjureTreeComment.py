#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Topaz.ConjureTreeComment')
def gem():
    require_gem('Topaz.Core')
    require_gem('Pearl.ConjureTreeComment')


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


    def test_conjure_tree_comment__first__comment_operator_different():
        conjure_tree_comment('#1', '1', '\n')
        conjure_tree_comment('#2', '1', '\n')
        conjure_tree_comment('#2', '1', '\n')

        assert length(tree_comment_cache) == 1

        first = tree_comment_cache['1']

        assert length(first) == 2

        assert first['#1'].comment_operator.s == '#1'
        assert first['#2'].comment_operator.s == '#2'

        tree_comment_cache.clear()


    def test_conjure_tree_comment__first__newline_different():
        conjure_tree_comment('#', '1', '1\n')
        conjure_tree_comment('#', '1', '2\n')
        conjure_tree_comment('#', '1', '2\n')

        assert length(tree_comment_cache) == 1

        first = tree_comment_cache['1']

        assert length(first) == 1

        second = first['#']

        assert length(second) == 2

        assert second['1\n'].newline.s == '1\n'
        assert second['2\n'].newline.s == '2\n'

        tree_comment_cache.clear()



    def test_conjure_tree_comment__other():
        conjure_tree_comment('#1', '1', '\n')
        conjure_tree_comment('#1', '1', '\n')
        conjure_tree_comment('#2', '1', '1\n')
        conjure_tree_comment('#2', '1', '2\n')
        conjure_tree_comment('#2', '1', '3\n')
        conjure_tree_comment('#', '2', '1\n')
        conjure_tree_comment('#', '2', '2\n')
        conjure_tree_comment('#', '2', '3\n')
        conjure_tree_comment('#', '2', '3\n')


        assert length(tree_comment_cache) == 2


        #
        #    '1':
        #      '#1': <comment '#1' '1' '\n'>
        #      '#2':
        #        '1\n': <comment '#2' '1' '1\n'>
        #        '2\n': <comment '#2' '1' '2\n'>
        #        '3\n': <comment '#2' '1' '3\n'>
        #
        first = tree_comment_cache['1']

        assert length(first) == 2

        assert first['#1'].comment_operator.s == '#1'

        second = first['#2']

        assert length(second) == 3

        assert second['1\n'].newline.s == '1\n'
        assert second['2\n'].newline.s == '2\n'
        assert second['3\n'].newline.s == '3\n'


        #
        #   '2':
        #     '#':
        #       '1\n': <comment '#' '2' '1\n'>
        #       '2\n': <comment '#' '2' '2\n'>
        #       '3\n': <comment '#' '2' '3\n'>
        #
        first = tree_comment_cache['2']

        assert length(first) == 1

        second = first['#']

        assert length(second) == 3

        assert second['1\n'].newline.s == '1\n'
        assert second['2\n'].newline.s == '2\n'
        assert second['3\n'].newline.s == '3\n'



    @share
    def test_conjure_tree_comment():
        test_conjure_tree_comment__first__comment_operator_different()
        test_conjure_tree_comment__first__newline_different()
        test_conjure_tree_comment__other()
