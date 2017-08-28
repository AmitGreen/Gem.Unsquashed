#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Topaz.ExceptionChain')
def gem():
    require_gem('Gem.Exception')
    require_gem('Gem.Traceback')
    require_gem('Topaz.Core')

    from Gem import caught_any_exception, caught_exception, Exception, maybe_exit_exception, print_exception_chain
    from Gem import raising_exception_from


    class Context(Object):
        __slots__ = (())

        def __enter__(t):
            return t

        def __exit__(t, e_type, e, e_traceback):
            with maybe_exit_exception(e_type, e, e_traceback):
                assert 0, 'd'


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
                    with caught_any_exception():
                        with Context():
                            assert 0, 'c'

    @share
    def test_exception_chain():
        try:
            test_abcd()
        except:
            with caught_any_exception() as e:
                print_exception_chain(e)
