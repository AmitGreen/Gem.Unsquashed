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
            'number',                   #   Integer
            'copyright',                #   Copyright
            'twig',                     #   Any
        ))


        def __init__(t, path, number, copyright, twig):
            t.path      = path
            t.number    = number
            t.copyright = copyright
            t.twig      = twig


        def write(t, f):
            t.copyright.write(f)

            f.line(arrange("#<source %r #%d>", t.path, t.number))
            t.twig.write(f.write)
            f.line('#</source>')


    @share
    def development():
        main_path = '../Sapphire/Main.py'

        tree = parse_python(main_path)

        boot = tree[0]

        assert boot.is_function_definition
        assert boot.a.is_function_header
        assert boot.a.name.s == 'boot'

        copyright = boot.prefix

        assert copyright.is_comment_suite
        assert length(copyright) is 3
        assert copyright[0] == empty_comment_line
        assert copyright[1].is_comment_line
        assert copyright[2] == empty_comment_line

        m = copyright_match(copyright[1])

        if m is none:
            raise_runtime_error('failed to extract copyright from: %r', copyright[1])

        copyright = create_copyright(Integer(m.group('year')), m.group('author'))

        boot_twig = TwigCode(main_path, 0, copyright, boot)

        with create_DelayedFileOutput('.pyxie/hma.py') as f:
            boot_twig.write(f)
            close_copyright(f)
