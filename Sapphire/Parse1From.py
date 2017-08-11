#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1From')
def gem():
    require_gem('Sapphire.Core')
    require_gem('Sapphire.Elemental')
    require_gem('Sapphire.Match')
    require_gem('Sapphire.Statement')


    def parse1_statement_from_module(index):
        s = qs()

        #
        #<name1>
        #
        m1 = name_match(s, index)

        if m1 is none:
            return parse_incomplete(1)

        module = conjure_identifier(m1.group())
        #</name1>

        #
        #<module: name ||| ['.' name] ... 'import'>
        #
        while true:
            m2 = from_module_match1(s, m1.end())

            if m2 is none:
                return parse_incomplete(2)

            operator = m2.group('operator')

            if operator is not '.':
                break

            operator_dot = OperatorDot(m2.group())

            #
            #<name2>
            #
            m1 = name_match(s, m2.end())

            if m1 is none:
                return parse_incomplete(2)
            #</name2>

            module = ExpressionDot(module, operator_dot, conjure_identifier(m1.group()))

        wj(m2.end())
        wk(KeywordImport(m2.group()))

        return module
        #</module>


    def parse1_statement_from_as():
        s = qs()

        #
        #<name>
        #
        m1 = name_match(s, qj())

        if m1 is none:
            line('parse1_statement_from_as: incomplete#1')
            return none

        imported = conjure_identifier(m1.group())
        #</name>

        #
        #<as>
        #
        m2 = from_as_match1(s, m1.end())

        if m2 is none:
            line('parse1_statement_from_as: incomplete#2')
            return none

        operator = m2.group('operator')
        #</as>

        if operator is none:
            wk(conjure_token_newline(m2.group()))

            return imported

        if operator is ',':
            wj(m2.end())
            wk(OperatorComma(m2.group()))

            return imported

        keyword_as = KeywordAs(m2.group())

        #
        #<name2>
        #
        m3 = name_match(s, m2.end())

        if m3 is none:
            line('parse1_statement_from_as: incomplete#3')
            return none

        imported = FromAsFragment(imported, keyword_as, conjure_identifier(m3.group()))
        #</name2>

        #
        #<comma-or-newline>
        #
        m4 = comma_or_newline_match1(s, m3.end())

        if m4 is none:
            line('parse1_statement_from_as: incomplete#4')
            return none
        #</comma-or-newline>

        if m4.start('comma') is -1:
            wk(conjure_token_newline(m4.group()))

            return imported

        wj(m4.end())
        wk(OperatorComma(m4.group()))

        return imported


    @share
    def parse1_statement_from(m1):
        if m1.end('newline') is not -1:
            return create_UnknownLine(1)

        keyword_from = KeywordFrom(m1.group())

        #
        #<module ... 'import'>
        #
        module = parse1_statement_from_module(m1.end())

        if module is none:
            return create_UnknownLine_0()

        keyword_import = qk()
        #</module>

        #
        #<imported ... (, | newline)>
        #
        imported = parse1_statement_from_as()

        if imported is none:
            return create_UnknownLine_0()

        operator = qk()
        #<imported/>

        if operator.is_token_newline:
            return StatementFromImport(keyword_from, module, keyword_import, imported, operator)

        #
        #<imported ... (, | newline)>
        #
        imported_2 = parse1_statement_from_as()

        if imported_2 is none:
            return create_UnknownLine_0()

        operator_2 = qk()
        #<imported/>

        if operator_2.is_token_newline:
            return StatementFromImport(
                       keyword_from,
                       module,
                       keyword_import,
                       ExpressionComma(imported, operator, imported_2),
                       operator_2,
                   )

        return create_UnknownLine(2)
