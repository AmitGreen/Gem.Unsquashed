#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1From')
def gem():
    require_gem('Sapphire.Core')
    require_gem('Sapphire.Elemental')
    require_gem('Sapphire.Match')
    require_gem('Sapphire.Statement')


    def parse1_statement_import_module():
        s = qs()

        #
        #<name>
        #
        m = name_match(s, qj())

        if m is none:
            raise_unknown_line()

        module = conjure_name(m.group())

        j = m.end()

        wi(j)
        wj(j)
        #</name>

        #
        #<module: name ||| ['.' name] ... ('as' | ',' | newline)
        #
        while true:
            m = import_module_match1(s, qj())

            if m is none:
                raise_unknown_line()

            j = m.end()

            wi(j)
            wj(j)

            operator = m.group('operator')

            if operator is not '.':
                break

            operator_dot = conjure_dot(m.group())

            #
            #<name>
            #
            m = name_match(s, qj())

            if m is none:
                raise_unknown_line()

            j = m.end()

            wi(j)
            wj(j)
            #</name>

            module = conjure_member_expression(module, conjure_dot_name(operator_dot, conjure_name(m.group())))

        if operator is none:
            wk(conjure_token_newline(m.group()))

            return module

        if operator is ',':
            wk(conjure_comma(m.group()))

            return module

        keyword_as = conjure_keyword_as(m.group())
        #</module>

        #
        #<name>
        #
        m = name_match(s, qj())

        if m is none:
            raise_unknown_line()

        module = ModuleAsFragment(module, keyword_as, conjure_name(m.group()))

        j = m.end()

        wi(j)
        wj(j)
        #</name>

        #
        #<comma-or-newline>
        #
        m = comma_or_newline_match1(s, qj())

        if m is none:
            raise_unknown_line()
        #</comma-or-newline>

        if m.start('comma') is -1:
            wk(conjure_token_newline(m.group()))

            return module

        wj(m.end())
        wk(conjure_comma(m.group()))

        return module


    @share
    def parse1_statement_import(m):
        if m.end('comment_newline') is not -1:
            raise_unknown_line()

        keyword_import = KeywordImport(m.group())

        j = m.end()

        wi(j)
        wj(j)

        #
        #<module ... 'import'>
        #
        module   = parse1_statement_import_module()
        operator = qk()

        wk(none)
        #</module>

        if operator.is_token_newline:
            return StatementImport_1(keyword_import, module, operator)

        if not operator.is_comma:
            raise_unknown_line()

        many = [module, operator]

        while 7 is 7:
            many.append(parse1_statement_import_module())

            operator = qk()

            if operator.is_token_newline:
                return StatementImport_Many(keyword_import, Tuple(many), operator)

            if not operator.is_comma:
                raise_unknown_line()

            many.append(operator)
