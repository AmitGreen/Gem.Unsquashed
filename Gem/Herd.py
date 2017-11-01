#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Gem.Herd')
def gem():
    #
    #   Herd:
    #
    #       Liquid (modifiable)
    #       Map (Associative Array)
    #       Unordered
    #       Key must not include absent
    #
    #   .inject
    #   .lookup
    #   .provide
    #       Use == for comparing keys
    #
    #       All the verbs here do NOT have an 'is' inside them.
    #
    #   .glimpse
    #   .insert
    #   .provision
    #       Unique Keys: Use 'is' for comparing keys
    #
    #       NOTE: All the verbs here have an 'is' inside them.
    #


    require_gem('Gem.Herd_2')
    require_gem('Gem.Herd_3')
    require_gem('Gem.Herd_4567')
    require_gem('Gem.HerdMany')


    def item_0(pair):
        return pair[0]


    class Herd_0(Object):
        __slots__ = (())


        is_herd      = true
        is_herd_many = false
        is_horde     = false
        k1           = absent
        k2           = absent
        k3           = absent
        k4           = absent
        skip         = 0


        @static_method
        def items_sorted_by_key():
            return (())


    class Herd_1(Object):
        __slots__ = ((
            'a',                        #   Any
            'v',                        #   Any
        ))


        is_herd      = true
        is_herd_many = false
        is_horde     = false
        k1           = absent
        k2           = absent
        k3           = absent
        k4           = absent
        skip         = 0


        def __init__(t, a, v):
            assert (a is not absent) and (v is not absent)

            t.a = a
            t.v = v


        def displace(t, k, v):
            assert (t.a is k) and (v is not absent)

            t.v = v


        def glimpse(t, k, d = none):
            if t.a is k: return t.v

            assert k is not absent

            return d


        def insert(t, b, w):
            assert (b is not absent) and (t.a is not b) and (w is not absent)

            return create_herd_2(t.a, b, t.v, w)


        def items_sorted_by_key(t):
            return (( ((t.a, t.v)), ))


        def provision(t, b, w):
            a = t.a
            if a is b: return t

            return create_herd_2(a, b, t.v, w)


        if 0:
            def provision_triple(t, displace, Meta, k1, k2, k3):
                a = t.a
                if a is k2:
                    v = t.v
                    if v.k3 is k3:  return v

                    if not v.is_herd:
                        r   = Meta(k1, k2, k3)
                        t.v = create_herd_2(v.k3, k3, v, r)
                        return r

                    return v.provision_triple_step2(displace_1v, t, Meta, k1, k2, k3)

                r = Meta(k1, k2, k3)

                displace(k1, create_herd_2(a, k2, t.v, r))

                return r


        if 0:
            def provision_triple__312(t, displace, Meta, k1, k2, k3):
                a = t.a
                if a is k1:
                    v = t.v
                    if v.k2 is k2:  return v

                    if not v.is_herd:
                        r   = Meta(k1, k2, k3)
                        t.v = create_herd_2(v.k2, k2, v, r)
                        return r

                    return v.provision_triple_step2__312(displace_1v, t, Meta, k1, k2, k3)

                r = Meta(k1, k2, k3)

                displace(k3, create_herd_2(a, k1, t.v, r))

                return r


        if 0:
            def provision_triple_step2(t, displace, parent, Meta, k1, k2, k3):
                a = t.a
                if a is k3:     return t.v

                r = Meta(k1, k2, k3)

                if parent.is_herd_many:
                    displace(parent, k2, create_herd_2(a, k3, t.v, r))
                    return r

                displace(parent, create_herd_2(a, k3, t.v, r))
                return r


    empty_herd = Herd_0()


    new_Herd_1 = Method(Object.__new__, Herd_1)


    @export
    def create_herd_1(a, v):
        assert (a is not absent) and (v is not absent)

        t = new_Herd_1()

        t.a = a
        t.v = v

        return t


    displace_1v = Herd_1.v.__set__


    Herd_0.provision = Herd_0.provide = Herd_0.inject = HerHerdrt = static_method(create_herd_1)


    export(
        'empty_herd',      empty_herd
    )
