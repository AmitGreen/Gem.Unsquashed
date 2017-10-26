#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Topaz.Cache')
def gem():
    require_gem('Gem.Cache2')
    require_gem('Topaz.Core')
    require_gem('Topaz.CacheSupport')


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


    def test_conjure_again():
        assert one   is conjure_number('one',  1)
        assert two   is conjure_number('two',  2)
        assert zero  is conjure_number('zero', 0)
        assert three is conjure_number('three', 3)
        assert four  is conjure_number('four',  4)
        assert five  is conjure_number('five',  5)
        assert six   is conjure_number('six',   6)
        assert seven is conjure_number('seven', 7)
        assert eight is conjure_number('eight', 8)
        assert nine  is conjure_number('nine',  9)

        assert black  is conjure_color('black')
        assert blue   is conjure_color('blue')
        assert cyan   is conjure_color('cyan')
        assert green  is conjure_color('green')
        assert purple is conjure_color('purple')
        assert red    is conjure_color('red')
        assert silver is conjure_color('silver')
        assert white  is conjure_color('white')
        assert yellow is conjure_color('yellow')

        assert circle    is conjure_shape('circle')
        assert ellipse   is conjure_shape('ellipse')
        assert moon      is conjure_shape('moon')
        assert oval      is conjure_shape('oval')
        assert pentagon  is conjure_shape('pentagon')
        assert polygon   is conjure_shape('polygon')
        assert square    is conjure_shape('square')
        assert star      is conjure_shape('star')
        assert trapazoid is conjure_shape('trapazoid')
        assert triangle  is conjure_shape('triangle')


    @share
    def test_conjure_single():
        test_conjure_again()
        line('PASSED: test_conjure_single')
