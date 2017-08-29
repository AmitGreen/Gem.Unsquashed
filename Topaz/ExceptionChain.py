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

    from Gem import catch_FileNotFoundError, Exception
    from Gem import print_exception_chain, rename_path


    class Context(Object):
        __slots__ = (())


        def __enter__(t):
            return t


        def __exit__(t, e_type, e, e_traceback):
            with exit_clause(e_type, e, e_traceback):
                from_path = 'd.d.d.d'
                to_path   = 'd.d.d.d.d'

                with catch_FileNotFoundError(from_path, to_path) as e:
                    rename_path(from_path, to_path)

                if e.caught:
                    with e.handle_exception():
                        try:
                            e = Exception('e')

                            raising_exception(e)

                            raise e
                        except Exception as e:
                            with except_clause(e):
                                e = Exception('f')

                                raising_exception(e)

                                raise e


    def test_b(previous):
        e = Exception('b')

        raising_exception_from(e, previous)

        raise e


    def test_abcd():
        try:
            e = Exception('a')

            raising_exception(e)

            raise e
        except Exception as e:
            with except_clause(e):
                try:
                    test_b(e)
                except:
                    with except_any_clause():
                        with Context():
                            e = Exception('c')

                            #raising_exception(e)       #   Test with this missing

                            raise e


    @share
    def test_exception_chain():
        try:
            test_abcd()
        except:
            with except_any_clause() as e:
                print_exception_chain(e)
