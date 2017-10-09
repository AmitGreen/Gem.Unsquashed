#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Development')
def gem():
    require_gem('Sapphire.Parse')

    variables = [
                    0,                  #   0 = copyright
                ]

    query = variables.__getitem__
    write = variables.__setitem__

    qc = Method(query, 0)
    wc = Method(write, 0)

    wc0 = Method(wc, 0)


    #
    #   Tokens
    #
    LP = conjure_left_parenthesis ('(')
    RP = conjure_right_parenthesis(')')

    empty_indentation__function = conjure_indented_token( empty_indentation, conjure_keyword_function('def '))


    class Copyright(Object):
        __slots__ = ((
            'year',                     #   Integer
            'author',                   #   String+
        ))


        def __init__(t, year, author):
            t.year   = year
            t.author = author


        def write(t, f):
            copyright = qc()

            if t is not copyright:
                if copyright is not 0:
                    close_copyright()

                wc(t)

                f.blank2()
                f.line('#<Copyright (c) %d %s.  All rights reserved.>', t.year, t.author)


    Copyright.k1 = Copyright.year
    Copyright.k1 = Copyright.author


    create_copyright = produce_conjure_dual('copyright', Copyright)


    def close_copyright(f):
        if qc() is not 0:
            wc0()

            f.line('#</Copyright>')
            f.blank2()


    class TwigCode(Object):
        __slots__ = ((
            'path',                     #   String+
            'part',                     #   String
            'copyright',                #   Copyright
            'twig',                     #   Any
        ))


        def __init__(t, path, part, copyright, twig):
            t.path      = path
            t.part      = part
            t.copyright = copyright
            t.twig      = twig


        def write(t, f):
            t.copyright.write(f)

            f.line(arrange("#<source %r %s>", t.path, t.part))
            t.twig.write(f.write)
            f.line('#</source>')


    @share
    def extract_boot():
        main_path = '../Sapphire/Main.py'

        tree = parse_python(main_path)

        #
        #   [0]
        #
        boot_decorator = tree[0]

        #def boot(module_name):
        boot_decorator__function_header = conjure_function_header(
                                              empty_indentation__function,
                                              conjure_name('boot'),
                                              conjure_parameters_1(LP, conjure_name('module_name'), RP),
                                              colon__empty_line_marker,
                                          )

        assert boot_decorator.is_function_definition
        assert boot_decorator.a is boot_decorator__function_header
        assert boot_decorator.b.is_statement_suite

        copyright = boot_decorator.prefix

        assert copyright.is_comment_suite
        assert length(copyright) is 3
        assert copyright[0] == empty_comment_line
        assert copyright[1].is_comment_line
        assert copyright[2] == empty_comment_line

        m = copyright_match(copyright[1])

        if m is none:
            raise_runtime_error('failed to extract copyright from: %r', copyright[1])

        copyright = create_copyright(Integer(m.group('year')), m.group('author'))


        #
        #   [1]
        #
        assert tree[1].is_empty_line_suite


        #
        #   [2]
        #
        boot_code = tree[2]

        #@boot('Boot')
        boot_decorator_header = conjure_decorator_header(
                                    empty_indentation__at_sign,
                                    conjure_call_expression(
                                        boot_decorator.a.name,
                                        conjure_arguments_1(LP, conjure_single_quote("'Boot'"), RP),
                                    ),
                                    empty_line_marker,
                                )

        assert boot_code.is_decorated_definition
        assert boot_code.a is boot_decorator_header

        #dump_token('boot_code.b', boot_code.b)


        #
        #   Result
        #
        return TwigCode(main_path, '[0]', copyright, boot_decorator)


    @share
    def development():
        boot_decorator = extract_boot()

        output_path = '.pyxie/hma.py'

        with create_DelayedFileOutput(output_path) as f:
            boot_decorator.write(f)

            close_copyright(f)

        partial(read_text_from_path(output_path))
