#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.ManyFrill')
def gem():
    require_gem('Sapphire.QuadrupleFrill')
    require_gem('Sapphire.TokenTuple')


    many_frill_cache   = {}
    provide_many_frill = many_frill_cache.setdefault


    class ManyFrill(TokenTuple):
        __slots__    = (())
        display_name = 'frill-*'


        frill_estimate = 7


        def iterate_write(t, w):
            for v in t:
                w(v.s)
                yield


        def transform(t, vary):
            iterator = iterate(t)

            i = 0

            for v in iterator:
                v__2 = v.transform(vary)

                if v is not v__2:
                    break

                i += 1
            else:
                return t

            many__2 = (
                          []       if i is 0 else
                          [t[0]]   if i is 1 else
                          List(t[:i])
                      )

            append = many__2.append

            append(v__2)

            for v in iterator:
                append(v.transform(vary))

            return conjure_many_frill(many__2)


    @share
    def conjure_many_frill(many):
        if type(many) is not List:
            assert many.frill_estimate

            return many

        total = length(many)

        if total <= 4:
            if total is 1:
                assert many[0].frill_estimate is 1

                return many[0]

            if total is 2:
                return conjure_vw_frill(many[0], many[1])

            if total is 3:
                return conjure_vwx_frill(many[0], many[1], many[2])

            assert total is 4

            return conjure_vwxy_frill(many[0], many[1], many[2], many[3])

        r = ManyFrill(many)

        return provide_many_frill(r, r)


    append_cache('many-frill', many_frill_cache)
