#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Marble.ConjureDual')
def gem():
    def create_conjure(f, prefix, suffix):
        name = arrange('%s_%s', prefix, suffix)

        f.line('@share')
        with f.indent(arrange('def produce_%s(name, Meta, cache):', name)):
            f.line('lookup = cache.get')
            f.line('store  = cache.__setitem__')

            f.blank2()

            f.line('@rename(%r, name)', arrange('%s_%%s', prefix))
            with f.indent(arrange('def %s(k1, k2):', name)):
                f.line('first = lookup(k1, absent)')

                f.blank()

                with f.indent('if first.k2 is k2:'):
                    f.line('return first')

                f.blank()

                with f.indent('if not first.is_herd:'):
                    f.line('r = Meta(k1, k2)')

                    f.blank()

                    f.line('store(k1, (r   if first is absent else   create_herd_2(first.k2, k2, first, r)))')

                    f.blank()

                    f.line('return r')

                f.blank()

                f.line('r = first.glimpse(k2)')

                f.blank()

                with f.indent('if r is not none:'):
                    f.line('assert r.k2 is k2')

                    f.blank()

                    f.line('return r')

                f.blank()

                f.line('r = Meta(k1, k2)')

                f.blank()

                f.line('first__2 = first.insert(k2, r)')

                f.blank()

                with f.indent('if first is not first__2:'):
                    f.line('store(k1, first__2)')

                f.blank()

                f.line('return r')

            f.blank2()

            f.line('return %s', name)


    @export
    def create_conjure_dual(path, year, author, module_name):
        with create_DelayedFileOutput(path) as f:
            f.line('#')
            f.line('#   Copyright (c) %s %s.  All rights reserved.', year, author)
            f.line('#')
            f.line('@gem(%r)', module_name)

            with f.indent('def gem():'):
                create_conjure(f, 'simplified_conjure', 'dual_v3')

            data = f.finish()

        partial(data)
