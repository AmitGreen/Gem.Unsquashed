#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Marble.ConjureDual')
def gem():
    def create_conjure(f, prefix, suffix, k1, k2):
        name = arrange('%s_%s', prefix, suffix)

        f.blank2()

        f.line('@share')
        with f.indent(arrange('def produce_%s(name, Meta, cache):', name)):
            f.line('lookup = cache.get')
            f.line('store  = cache.__setitem__')

            f.blank2()

            f.line('@rename(%r, name)', arrange('%s_%%s', prefix))
            with f.indent(arrange('def %s(k1, k2):', name)):
                f.line('a = lookup(%s, absent)', k1)

                f.blank()

                with f.indent(arrange('if a.%s is %s:', k2, k2)):
                    f.line('return a')

                f.blank()

                with f.indent('if not a.is_herd:'):
                    f.line('r = Meta(k1, k2)')

                    f.blank()

                    f.line('store(%s, (r   if a is absent else   create_herd_2(a.%s, %s, a, r)))',
                           k1, k2, k2)

                    f.blank()

                    f.line('return r')

                f.blank()

                f.line('r = a.glimpse(%s)', k2)

                f.blank()

                with f.indent('if r is not none:'):
                    f.line('assert r.%s is %s', k2, k2)

                    f.blank()

                    f.line('return r')

                f.blank()

                f.line('r = Meta(k1, k2)')

                f.blank()

                f.line('a_ = a.insert(%s, r)', k2)

                f.blank()

                with f.indent('if a is not a_:'):
                    f.line('store(%s, a_)', k1)

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
                f.blank_suppress()

                #create_conjure(f, 'simplified_conjure', 'dual',     'k1', 'k2')
                #create_conjure(f, 'simplified_conjure', 'dual__21', 'k2', 'k1')

            data = f.finish()

        partial(data)
