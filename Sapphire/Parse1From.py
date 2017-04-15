#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1From')
def gem():
    require_gem('Sapphire.Elemental')
    require_gem('Sapphire.Match')
    require_gem('Sapphire.Statement')
    require_gem('Sapphire.Token')


    def parse1_statement_from_module(index):
        s = qs()

        #
        #<name1>
        #
        m1 = name_match(s, index)

        if m1 is none:
            return parse_incomplete(parse1_statement_from_module, 1)

        module = Symbol(m1.group())
        #</name1>

        #
        #<module: name ||| ['.' name] ... 'import'>
        #
        while true:
            m2 = from1_module_match(s, m1.end())

            if m2 is none:
                return parse_incomplete(parse1_statement_from_module, 2)

            operator = m2.group('operator')

            if operator is not '.':
                break

            operator_dot = OperatorDot(m2.group())

            #
            #<name2>
            #
            m1 = name_match(s, m2.end())

            if m1 is none:
                return parse_incomplete(parse1_statement_from_module, 2)
            #</name2>

            module = ExpressionDot(module, operator_dot, m1.group())

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

        imported = Symbol(m1.group())
        #</name>

        #
        #<as>
        #
        m2 = from1_as_match(s, m1.end())

        if m2 is none:
            line('parse1_statement_from_as: incomplete#2')
            return none

        operator = m2.group('operator')
        #</as>

        if operator is none:
            wk(TokenNewline(m2.group()))

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

        imported = FromAsFragment(imported, keyword_as, Symbol(m3.group()))
        #</name2>

        #
        #<comma-or-newline>
        #
        m4 = comma1_or_newline_match(s, m3.end())

        if m4 is none:
            line('parse1_statement_from_as: incomplete#4')
            return none
        #</comma-or-newline>

        if m4.start('comma') is -1:
            wk(TokenNewline(m4.group()))

            return imported

        wj(m4.end())
        wk(OperatorComma(m4.group()))

        return imported


    @share
    def parse1_statement_from(m1):
        keyword_from = KeywordFrom(m1.group())

        #
        #<module ... 'import'>
        #
        module = parse1_statement_from_module(m1.end())

        if module is none:
            return create_UnknownLine()

        keyword_import = qk()
        #</module>

        #
        #<imported ... (, | newline)>
        #
        imported = parse1_statement_from_as()

        if imported is none:
            return create_UnknownLine()

        operator = qk()
        #<imported/>

        if operator.is_token_newline:
            return StatementFromImport(keyword_from, module, keyword_import, imported, operator)

        #
        #<imported ... (, | newline)>
        #
        imported_2 = parse1_statement_from_as()

        if imported_2 is none:
            return create_UnknownLine()

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

        return create_UnknownLine(parse1_statement_from, 1)
