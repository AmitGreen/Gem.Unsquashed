#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Topaz.Cache')
def gem():
    require_gem('Topaz.Core')
    require_gem('Topaz.CacheSupport')


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

    red    = conjure_color('red')
    white  = conjure_color('white')
    purple = conjure_color('purple')
    green  = conjure_color('green')
    silver = conjure_color('silver')
    black  = conjure_color('black')
    blue   = conjure_color('blue')
    yellow = conjure_color('yellow')
    cyan   = conjure_color('cyan')

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


    triple_test_list = ((
            ((   one,   red,     circle       )),
            ((   one,   red,     ellipse      )),
            ((   one,   red,     moon         )),       #   .displace_v
            ((   one,   red,     oval         )),
            ((   one,   red,     pentagon     )),
            ((   one,   red,     square       )),
            ((   one,   red,     star         )),
            ((   one,   red,     trapazoid    )),
            ((   one,   red,     triangle     )),

            ((   two,   cyan,    oval         )),       #   Herd_2.distribute_triple__312
            ((   two,   cyan,    star         )),
            ((   two,   cyan,    triangle     )),
            ((   two,   cyan,    square       )),
            ((   two,   red,     star         )),       #   Horde_Many.distribute_triple_step2 ...
            #                                           #       ... & Herd2.distribute_triple_step2__312
            ((   two,   red,     square       )),       #   .displace_w
            ((   two,   green,   star         )),       #   .displace_x & Herd3.distribute_triple_step2__312
            ((   two,   green,   moon         )),
            ((   two,   blue,    star         )),       #   Herd_4567.distribute_triple_step2__312

            ((   three,  blue,   moon         )),       #   Herd_3.distribute_triple__312
            ((   three,  green,  moon         )),
            ((   three,  cyan,   star         )),
            ((   three,  red,    star         )),
            ((   three,  red,    moon         )),       #   .displace_y
            ((   three,  purple, moon         )),
            ((   three,  purple, oval         )),       #   .displace_z
            ((   three,  purple, triangle     )),
            ((   three,  purple, star         )),

            ((   four,   black,  circle      )),
            ((   four,   green,  circle      )),
            ((   four,   white,  oval        )),        #   Herd_4567.distribute_triple__312
            ((   four,   blue,   oval        )),
            ((   four,   red,    moon        )),
            ((   four,   purple, triangle    )),
            ((   four,   purple, star        )),        #   .displace_z6
            ((   four,   cyan,   square      )),
            ((   four,   cyan,   triangle    )),        #   .displace_z7
            ((   four,   yellow, ellipse     )),        #   Herd_Many.distribute_triple
            ((   four,   yellow, moon        )),
            ((   four,   silver, oval        )),

            ((   five,   silver, moon        )),
            ((   five,   silver, square      )),
            ((   five,   purple, oval        )),        #   Horde_23.distribute_triple_step2
            ((   five,   silver, oval        )),
            ((   five,   silver, circle      )),        #   Horde_23 (with skip 0) calls create_herd_4567

            ((   six,    green,  square      )),
            ((   six,    green,  circle      )),
            ((   six,    green,  triangle    )),

            #
            #   Additional tests for produce_conjure_unique_triple__312
            #
            ((   five,   purple, triangle    )),
            ((   seven,  black,  triangle    )),
            ((   eight,  white,  triangle    )),        #   Herd_Many.distribute_triple__312
            ((   nine,   blue,   triangle    )),

            ((   two,    black,  star        )),
            ((   two,    yellow, star        )),
            ((   two,    purple, star        )),
            ((   two,    silver, star        )),        #   Herd_Many.distribute_triple_step2__312
            ((   two,    white,  star        )),

            ((   one,    silver, pentagon    )),        #   Horde_23.distribute_triple__312, & ...
            #                                           #     ... Horde_Many.increment_skip
            ((   one,    black,  pentagon    )),
            ((   one,    purple, pentagon    )),        #   Horde_Many.distribute_triple__312
            ((   one,    green,  pentagon    )),

            ((   one,    green,  trapazoid   )),
            ((   two,    green,  trapazoid   )),        #   Horde_23.distribute_triple_step2__312

            ((   five,   white,  polygon     )),
            ((   five,   green,  polygon     )),
            ((   five,   silver, polygon     )),
            ((   five,   black,  polygon     )),
            ((   seven,  silver, polygon     )),        #   Horde_Many.distribute_triple_step2__312
        ))


    triple_test_list__2 = ((
            #
            #   Test herds turning into hordes.
            #
            ((   two,   red,     circle,    0   )),
            ((   two,   blue,    triangle,  7   )),
            ((   two,   blue,    moon,      7   )),     #   Herd_2.increment_skip

            ((   three, green,   pentagon,  0   )),
            ((   three, white,   square,    7   )),
            ((   three, white,   oval,      7   )),
            ((   three, white,   moon,      7   )),     #   Herd_3.increment_skip

            ((   four,  cyan,    moon,      0   )),
            ((   four,  purple,  triangle,  7   )),
            ((   four,  purple,  oval,      7   )),
            ((   four,  purple,  ellipse,   7   )),
            ((   four,  purple,  pentagon,  7   )),     #   Herd_4567.increment_skip (4 elements)

            ((   five,  cyan,    triangle,  0   )),
            ((   five,  yellow,  triangle,  7   )),
            ((   five,  yellow,  oval,      7   )),
            ((   five,  yellow,  square,    7   )),
            ((   five,  yellow,  pentagon,  7   )),
            ((   five,  yellow,  moon,      7   )),     #   Herd_4567.increment_skip (5 elements)

            ((   six,   black,   moon,      0   )),
            ((   six,   green,   square,    7   )),
            ((   six,   green,   pentagon,  7   )),
            ((   six,   green,   triangle,  7   )),
            ((   six,   green,   oval,      7   )),
            ((   six,   green,   moon,      7   )),
            ((   six,   green,   ellipse,   7   )),     #   Herd_4567.increment_skip (6 elements)

            ((   seven, black,   moon,      0   )),
            ((   seven, red,     moon,      7   )),
            ((   seven, red,     ellipse,   7   )),
            ((   seven, red,     square,    7   )),
            ((   seven, red,     pentagon,  7   )),
            ((   seven, red,     oval,      7   )),
            ((   seven, red,     star,      7   )),
            ((   seven, red,     triangle,  7   )),     #   Herd_4567.increment_skip (7 elements)

            #
            #   Test a horde restoring a sample in Horde_4567.scrub
            #
            ((  eight,  green,  moon,       0   )),
            ((  eight,  green,  ellipse,    7   )),
            ((  eight,  green,  oval,       7   )),
            ((  eight,  green,  star,       7   )),
            ((  eight,  green,  triangle,   7   )),
            ((  eight,  green,  square,     7   )),
        ))


    def test_final_scrub(cache):
        cache.scrub()

        assert cache.count_nested() is 0

        #my_line('scrubed cache %s', cache.name)


    def test_conjure_triple__X__scrub(cache, conjure_numbered_color_shape):
        keep_set = LiquidSet()
        add      = keep_set.add

        for loop in [7, 5, 3, 2, 1]:
            total = 0

            for [number, color, shape] in triple_test_list:
                v = conjure_numbered_color_shape(number, color, shape)
                total += 1

                if not (total % loop):
                    add(v)
                #else:
                #    if v not in keep_set:
                #        my_line('will discard: %r', v)
            del v

            assert cache.count_nested() == length(triple_test_list)

            #if 7 is 7:
            #    my_line('BEFORE: (loop %d)', loop)
            #    for v in keep_set:
            #        my_line('keep_set:%r', v)
            #    v=0
            #    print_cache(cache.name)

            cache.scrub()

            #if 7 is 7:
            #    my_line('AFTER: (loop %d)', loop)
            #    #for v in keep_set:
            #    #    my_line('keep_set:%r', v)
            #    v=0
            #    print_cache(cache.name)

            assert cache.count_nested() == length(keep_set)

            #if 7 is 7:
            #    my_line('keeping %d of %d', length(keep_set), length(triple_test_list))
            #    line()


    def test_conjure_triple__X__verify(cache, simplified_conjure_triple):
        cache_dump = dump_cache_to_string(cache, show_sample = false)

        test_final_scrub(cache)
        test_conjure_triple__X__scrub(cache, simplified_conjure_triple)

        simplified_cache_dump = dump_cache_to_string(cache, show_sample = false)

        test_final_scrub(cache)

        if cache_dump != simplified_cache_dump:
            write_binary_to_path('oops1.txt', cache_dump)
            write_binary_to_path('oops2.txt', simplified_cache_dump)
            raise_runtime_error('cache_dump != simplified_cache_dump (see oops1.txt & oops2.txt)')

        if show is 7:
            partial(cache_dump)


    def test_conjure_unique_triple():
        cache = create_cache('numbered_colored_shape', nub = Number.value.__get__)

        conjure_numbered_colored_shape = produce_conjure_unique_triple(
                                             'numbered_colored_shape',
                                             NumberedColoredShape,
                                             cache,
                                         )

        test_conjure_triple__X__scrub(cache, conjure_numbered_colored_shape)


        #
        #   Verify conjure_numbered_colored_shape & produce_simplified_conjure_triple produce the same cache structure.
        #
        test_conjure_triple__X__verify(
            cache,
            produce_simplified_conjure_triple(
                'simplified_numbered_colored_shape',
                NumberedColoredShape,
                cache,
            ),
        )

        #
        #   Extra test with 'triple__test_list__2' to test herds turning into hordes.
        #
        keep_set = LiquidSet()
        add      = keep_set.add

        for loop in [1, 2]:
            total = 0

            for [number, color, shape, keep] in triple_test_list__2:
                v = conjure_numbered_colored_shape(number, color, shape)
                total += 1

                if keep:
                    add(v)
            del v

            #if loop is 1:
            #    my_line('BEFORE:')
            #    print_cache(cache.name)

            cache.scrub()

            #my_line('AFTER:')
            #print_cache(cache.name)

            assert cache.count_nested() == length(keep_set)

        del keep_set, add


    def test_conjure_unique_triple__312():
        cache = create_cache('shape_number_color__312', nub = Shape.name.__get__)

        test_conjure_triple__X__scrub(
            cache,
            produce_conjure_unique_triple__312('shape_number_color__312', NumberedColoredShape, cache),
        )

        test_conjure_triple__X__verify(
            cache,
            produce_simplified_conjure_triple__312(
                'simplified_numbered_colored_shape__312',
                NumberedColoredShape,
                cache,
            ),
        )

        test_final_scrub(cache)


    @share
    def test_conjure_triple():
        test_conjure_unique_triple()
        test_conjure_unique_triple__312()

        line('PASSED: conjure_triple')

        #print_cache('numbered_colored_shape')
        #print_cache('shape_number_color__312')
