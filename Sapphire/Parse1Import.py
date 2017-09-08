#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1From')
def gem():
    require_gem('Sapphire.Core')
    require_gem('Sapphire.Elemental')
    require_gem('Sapphire.Match')
    require_gem('Sapphire.Statement')


    def parse1_statement_import_module(index):
        s = qs()

        #
        #<name>
        #
        m1 = name_match(s, index)

        if m1 is none:
            raise_unknown_line(1)

        module = conjure_identifier(m1.group())
        #</name>

        #
        #<module: name ||| ['.' name] ... ('as' | ',' | newline)
        #
        while true:
            m2 = import_module_match1(s, m1.end())

            if m2 is none:
                raise_unknown_line(2)

            operator = m2.group('operator')

            if operator is not '.':
                break

            operator_dot = conjure_dot(m2.group())

            #
            #<name>
            #
            m1 = name_match(s, m2.end())

            if m1 is none:
                raise_unknown_line(3)
            #</name>

            module = MemberExpression_1(module, operator_dot, conjure_identifier(m1.group()))

        if operator is none:
            wk(conjure_token_newline(m2.group()))

            return module

        if operator is ',':
            wj(m2.end())
            wk(conjure_comma(m2.group()))

            return module

        keyword_as = conjure_keyword_as(m2.group())
        #</module>

        #
        #<name>
        #
        m3 = name_match(s, m2.end())

        if m3 is none:
            raise_unknown_line(4)

        module = ModuleAsFragment(module, keyword_as, conjure_identifier(m3.group()))
        #</name>

        #
        #<comma-or-newline>
        #
        m4 = comma_or_newline_match1(s, m3.end())

        if m4 is none:
            raise_unknown_line(5)
        #</comma-or-newline>

        if m4.start('comma') is -1:
            wk(conjure_token_newline(m4.group()))

            return module

        wj(m4.end())
        wk(conjure_comma(m4.group()))

        return module


    @share
    def parse1_statement_import(m1):
        if m1.end('comment_newline') is not -1:
            raise_unknown_line(1)

        keyword_import = KeywordImport(m1.group())

        #
        #<module ... 'import'>
        #
        module   = parse1_statement_import_module(m1.end())
        operator = qk()

        wk(none)
        #</module>

        if operator.is_token_newline:
            return StatementImport(keyword_import, module, operator)

        raise_unknown_line(2)
