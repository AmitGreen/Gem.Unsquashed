#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Topaz.ExceptionChain')
def gem():
    require_gem('Gem.CatchException')
    require_gem('Gem.Exception')
    require_gem('Gem.Path')
    require_gem('Gem.Traceback')
    require_gem('Topaz.Core')

    from Gem import catch_FileNotFoundError, caught_exception, Exception
    from Gem import maybe_exit_exception, print_exception_chain, rename_path


    class Context(Object):
        __slots__ = (())


        def __enter__(t):
            return t


        def __exit__(t, e_type, e, e_traceback):
            with maybe_exit_exception(e_type, e, e_traceback):
                from_path = 'd.d.d.d'
                to_path   = 'd.d.d.d.d'

                with catch_FileNotFoundError(from_path, to_path) as e:
                    rename_path(from_path, to_path)

                if e.caught:
                    with e.handle_exception():
                        try:
                            assert 0, 'e'
                        except AssertionError as e:
                            with caught_exception(e):
                                assert 0, 'f'


    def test_b(previous):
        e = Exception('b')

        raising_exception_from(e, previous)

        raise e


    def test_abcd():
        try:
            assert 0, 'a'
        except AssertionError as e:
            with caught_exception(e):
                try:
                    test_b(e)
                except:
                    with except_any_clause():
                        with Context():
                            assert 0, 'c'

    @share
    def test_exception_chain():
        try:
            test_abcd()
        except:
            with except_any_clause() as e:
                print_exception_chain(e)
