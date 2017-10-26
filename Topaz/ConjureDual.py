#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Topaz.Cache')
def gem():
    require_gem('Topaz.CacheSupport')
    require_gem('Topaz.Core')


    show = 0


    #
    #   Specific instances
    #
    eight = conjure_number('eight', 8)
    five  = conjure_number('five',  5)
    four  = conjure_number('four',  4)
    nine  = conjure_number('nine',  9)
    one   = conjure_number('one',   1)
    seven = conjure_number('seven', 7)
    six   = conjure_number('six',   6)
    three = conjure_number('three', 3)
    two   = conjure_number('two',   2)
    zero  = conjure_number('zero',  0)

    circle    = conjure_shape('circle')
    ellipse   = conjure_shape('ellipse')
    moon      = conjure_shape('moon')
    pentagon  = conjure_shape('pentagon')
    oval      = conjure_shape('oval')
    square    = conjure_shape('square')
    polygon   = conjure_shape('polygon')
    star      = conjure_shape('star')
    trapazoid = conjure_shape('trapazoid')
    triangle  = conjure_shape('triangle')


    #
    #   dual_test_list
    #
    dual_test_list = ((
            ((   one,   circle       )),
            ((   three, circle       )),
            ((   two,   circle       )),

            ((   two,   ellipse      )),
            ((   one,   ellipse      )),
            ((   seven, ellipse      )),
            ((   six,   ellipse      )),
            ((   three, ellipse      )),
            ((   five,  ellipse      )),
            ((   four,  ellipse      )),

            ((   two,   moon         )),
            ((   five,  moon         )),
            ((   three, moon         )),
            ((   four,  moon         )),
            ((   one,   moon         )),

            ((   five,  pentagon     )),
            ((   four,  pentagon     )),
            ((   one,   pentagon     )),
            ((   six,   pentagon     )),
            ((   three, pentagon     )),
            ((   two,   pentagon     )),

            ((   one,  square        )),
            ((   two,  square        )),

            ((   four,  star         )),
            ((   three, star         )),
            ((   two,   star         )),
            ((   one,   star         )),

            ((   five,  trapazoid    )),
            ((   four,  trapazoid    )),
            ((   six,   trapazoid    )),
            ((   three, trapazoid    )),
            ((   nine,  trapazoid    )),
            ((   eight, trapazoid    )),
            ((   two,   trapazoid    )),
            ((   one,   trapazoid    )),        #   Herd_Many.scrub
            ((   seven, trapazoid    )),

            ((   one, triangle       )),
        ))


    #
    #   A simplified version of produce_conjure_unique_dual (and also produce_conjure_unique_dual__21)
    #
    #       The version in Gem/Cache2.py that uses multiple functions (for speed optimization).
    #
    #       This simplified version is writen as a single function (to do exactly the same thing) for testing
    #       that the speed optimization is identical to this version
    #
    #   NOTE:
    #       These use the 'produce' metaphor so they look like the origianl produce functions in Gem/Cache2.py;
    #       (rather than simplifying them -- since optimization is irrelevant for test code).
    #
    def produce_simplified_conjure_unique_dual(name, Meta, cache):
        lookup = cache.get
        store  = cache.__setitem__


        @rename('simplified_conjure_%s', name)
        def simplified_conjure_unique_dual(k1, k2):
            first = lookup(k1, absent)

            if first.k2 is k2:
                return first

            if not first.is_herd:
                r = Meta(k1, k2)

                store(k1, (r   if first is absent else   create_herd_2(first.k2, k2, first, r)))

                return r

            r = first.glimpse(k2)

            if r is not none:
                assert r.k2 is k2

                return r

            r = Meta(k1, k2)

            first__2 = first.insert(k2, r)

            if first is not first__2:
                store(k1, first__2)

            return r


        return simplified_conjure_unique_dual


    def produce_simplified_conjure_unique_dual__21(name, Meta, cache):
        lookup = cache.get
        store  = cache.__setitem__


        @rename('simplified_conjure_%s__21', name)
        def simplified_conjure_unique_dual__21(k1, k2):
            first = lookup(k2, absent)

            if first.k1 is k1:
                return first

            if not first.is_herd:
                r = Meta(k1, k2)

                store(k2, (r   if first is absent else   create_herd_2(first.k1, k1, first, r)))

                return r

            r = first.glimpse(k1)

            if r is not none:
                assert r.k1 is k1

                return r

            r = Meta(k1, k2)

            first__2 = first.insert(k1, r)

            if first is not first__2:
                store(k2, first__2)

            return r


        return simplified_conjure_unique_dual__21


    def test_final_scrub(cache):
        cache.scrub()

        assert cache.count_nested() is 0

        #my_line('scrubed cache %s', cache.name)


    def test_conjure_dual__X__scrub(cache, conjure_numbered_shape):
        keep_set = LiquidSet()
        add      = keep_set.add

        for loop in [7, 5, 3, 2, 1]:
            total = 0

            for [number, shape] in dual_test_list:
                v = conjure_numbered_shape(number, shape)
                total += 1

                if not (total % loop):
                    add(v)

            del v

            assert cache.count_nested() == length(dual_test_list)

            #if 7 is 7:
            #    my_line('BEFORE: (loop %d)', loop)
            #    for v in keep_set:
            #        my_line('keep_set:%r', v)
            #    v=0
            #    print_cache(cache.name)

            cache.scrub()

            #if 7 is 7:
            #    my_line('AFTER: (loop %d)', loop)
            #    for v in keep_set:
            #        my_line('keep_set:%r', v)
            #    v=0
            #    print_cache(cache.name)

            assert cache.count_nested() is length(keep_set)

            #if 7 is 7:
            #    my_line('keeping %d of %d', length(keep_set), length(dual_test_list))


    def test_conjure_dual__X__verify(cache, simplified_conjure_dual):
        cache_dump = dump_cache_to_string(cache)

        test_final_scrub(cache)

        for [number, shape] in dual_test_list:
            simplified_conjure_dual(number, shape)

        assert cache_dump == dump_cache_to_string(cache)

        if show is 7:
            partial(cache_dump)


    def test_conjure_unique_dual():
        numbered_shape_cache = create_cache('numbered_shape', nub = Number.value.__get__)

        test_conjure_dual__X__scrub(
            numbered_shape_cache,
            produce_conjure_unique_dual(
                'numbered_shape',
                NumberedShape,
                cache = numbered_shape_cache,
            ),
        )

        test_conjure_dual__X__verify(
            numbered_shape_cache,
            produce_simplified_conjure_unique_dual(
                'simplified_numbered_shape',
                NumberedShape,
                cache = numbered_shape_cache,
            ),
        )


    def test_conjure_unique_dual__21():
        shape_number_cache = create_cache('shape_number', nub = Shape.name.__get__)


        test_conjure_dual__X__scrub(
            shape_number_cache,
            produce_conjure_unique_dual__21(
                'shape_number',
                NumberedShape,
                cache = shape_number_cache,
            ),
        )


        #
        #   Verify that the dual test list is ordered as expected
        #
        for v in [circle, ellipse, moon, pentagon, square, star, trapazoid, triangle]:
            w = shape_number_cache[v]

            if w.is_herd:
                value = 1

                for [number, x] in w.items_sorted_by_key():
                    assert number.value is value
                    assert x.number is number
                    assert x.shape  is v

                    value += 1
            else:
                assert w.number.value is 1

        del v, w, x


        #
        #   Verify conjure_numbered_shape__21 & simplified_conjure_numbered_shape__21 produce the same cache structure.
        #
        test_conjure_dual__X__verify(
            shape_number_cache,
            produce_simplified_conjure_unique_dual__21(
                'simplified_shape_number',
                NumberedShape,
                cache = shape_number_cache,
            ),
        )


    @share
    def test_conjure_dual():
        test_conjure_unique_dual()
        test_conjure_unique_dual__21()

        line('PASSED: test_conjure_dual')
