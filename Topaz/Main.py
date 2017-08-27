#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
def boot(module_name):
    def execute(f):
        return f()

    return execute


@boot('Boot')
def boot():
    from sys     import path    as module_path
    from os.path import abspath as path_absolute, join as path_join

    module_path.insert(1, path_absolute(path_join(module_path[0], '..')))


    import Gem


@gem('Topaz.Main')
def gem():
    require_gem('Topaz.ConjureTreeComment')
    require_gem('Topaz.Path')
    require_gem('Topaz.Pattern')
    require_gem('Topaz.PortrayString')
    require_gem('Topaz.StringOutput')
    require_gem('Gem.Exception')
    require_gem('Gem.Traceback')


    @share
    def main():
        from Gem import caught_any_exception, caught_exception, Exception, maybe_exit_exception, print_exception_chain
        from Gem import raising_exception_from


        try:
            test_conjure_tree_comment()
            test_pattern()
            test_portray_raw_string()
            test_remove_path()
            test_rename_path()
            test_string_output()


            if 1:
                def b(previous):
                    e = Exception('b')

                    raising_exception_from(e, previous)

                    raise e


                class D(Object):
                    __slots__ = (())

                    def __enter__(t):
                        return t

                    def __exit__(t, e_type, e, e_traceback):
                        with maybe_exit_exception(e_type, e, e_traceback):
                            assert 0, 'd'


                try:
                    assert 0, 'a'
                except AssertionError as e:
                    with caught_exception(e):
                        try:
                            b(e)
                        except:
                            with caught_any_exception():
                                with D():
                                    assert 0, 'c'
        except:
            with caught_any_exception() as e:
                print_exception_chain(e)
