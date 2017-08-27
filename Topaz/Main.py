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
        test_conjure_tree_comment()
        test_pattern()
        test_portray_raw_string()
        test_remove_path()
        test_rename_path()
        test_string_output()


        if 0:
            from Gem import caught_any_exception, caught_exception, Exception, print_exception_chain
            from Gem import raising_exception_from


            def b(previous):
                e = Exception('b')

                raising_exception_from(e, previous)

                raise e


            try:
                try:
                    assert 0, 'a'
                except AssertionError as e:
                    with caught_exception(e):
                        try:
                            b(e)
                        except:
                            with caught_any_exception():
                                assert 0, 'c'
            except:
                with caught_any_exception() as e:
                    print_exception_chain(e)
