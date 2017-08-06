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
            return parse_incomplete(parse1_statement_import_module, 1)

        module = conjure_identifier(m1.group())
        #</name>

        #
        #<module: name ||| ['.' name] ... ('as' | ',' | newline)
        #
        while true:
            m2 = import_module_match1(s, m1.end())

            if m2 is none:
                return parse_incomplete(parse1_statement_import_module, 2)

            operator = m2.group('operator')

            if operator is not '.':
                break

            operator_dot = OperatorDot(m2.group())

            #
            #<name>
            #
            m1 = name_match(s, m2.end())

            if m1 is none:
                return parse_incomplete(parse1_statement_import_module, 3)
            #</name>

            module = ExpressionDot(module, operator_dot, conjure_identifier(m1.group()))

        if operator is none:
            wk(conjure_token_newline(m2.group()))

            return module

        if operator is ',':
            wj(m2.end())
            wk(OperatorComma(m2.group()))

            return module

        keyword_as = KeywordAs(m2.group())
        #</module>

        #
        #<name>
        #
        m3 = name_match(s, m2.end())

        if m3 is none:
            return parse_incomplete(parse1_statement_import_module, 4)

        module = ModuleAsFragment(module, keyword_as, conjure_identifier(m3.group()))
        #</name>

        #
        #<comma-or-newline>
        #
        m4 = comma_or_newline_match1(s, m3.end())

        if m4 is none:
            return parse_incomplete(parse1_statement_import_module, 5)
        #</comma-or-newline>

        if m4.start('comma') is -1:
            wk(conjure_token_newline(m4.group()))

            return module

        wj(m4.end())
        wk(OperatorComma(m4.group()))

        return module


    @share
    def parse1_statement_import(m1):
        if m1.end('newline') is not -1:
            return create_UnknownLine(parse1_statement_import, 1)

        keyword_import = KeywordImport(m1.group())

        #
        #<module ... 'import'>
        #
        module = parse1_statement_import_module(m1.end())

        if module is none:
            return create_UnknownLine()

        operator = qk()
        #</module>

        if operator.is_token_newline:
            return StatementImport(keyword_import, module, operator)

        return create_UnknownLine(parse1_statement_import, 2)
