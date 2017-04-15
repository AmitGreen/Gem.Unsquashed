#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1From')
def gem():
    require_gem('Sapphire.Elemental')
    require_gem('Sapphire.Match')
    require_gem('Sapphire.Statement')
    require_gem('Sapphire.Token')


    def parse1_statement_from_module(s, index):
        #
        #<name1>
        #
        m1 = name_match(s, index)

        if m1 is none:
            line('parse1_statement_from_module: incomplete#1')
            return tuple_of_3_nones

        module = Symbol(m1.group())
        #</name1>

        #
        #<module: name ||| ['.' name] ... 'import'>
        #
        while true:
            m2 = from1_module_match(s, m1.end())

            if m2 is none:
                line('parse1_statement_from_module: incomplete#2')
                return tuple_of_3_nones

            operator = m2.group('operator')

            if operator is not '.':
                break

            operator_dot = OperatorDot(m2.group())

            #
            #<name2>
            #
            m1 = name_match(s, m2.end())

            if m1 is none:
                line('parse1_statement_from_module: incomplete#3')
                return tuple_of_3_nones
            #</name2>

            module = ExpressionDot(module, operator_dot, m1.group())

        return (( module, KeywordImport(m2.group()), m2.end() ))
        #</module>


    def parse1_statement_from_as(s, index):
        #
        #<name>
        #
        m1 = name_match(s, index)

        if m1 is none:
            line('parse1_statement_from_as: incomplete#1')
            return tuple_of_3_nones

        imported = Symbol(m1.group())
        #</name>

        #
        #<as>
        #
        m2 = from1_as_match(s, m1.end())

        if m2 is none:
            line('parse1_statement_from_as: incomplete#2')
            return tuple_of_3_nones

        operator = m2.group('operator')
        #</as>

        if operator is none:
            return (( imported, TokenNewline(m2.group()), m2.end() ))

        if operator is ',':
            return (( imported, OperatorComma(m2.group()), m2.end() ))

        keyword_as = KeywordAs(m2.group())

        #
        #<name2>
        #
        m3 = name_match(s, m2.end())

        if m3 is none:
            line('parse1_statement_from_as: incomplete#3')
            return tuple_of_3_nones

        imported = FromAsFragment(imported, keyword_as, Symbol(m3.group()))
        #</name2>

        #
        #<comma-or-newline>
        #
        m4 = comma1_or_newline_match(s, m3.end())

        if m4 is none:
            line('parse1_statement_from_as: incomplete#4')
            return tuple_of_3_nones
        #</comma-or-newline>

        if m4.start('comma') is -1:
            return (( imported, TokenNewline(m4.group()), m4.end() ))

        return (( imported, OperatorComma(m4.group()), m4.end() ))


    @share
    def parse1_statement_from(m1, s):
        keyword_from = KeywordFrom(m1.group())

        #
        #<module ... 'import'>
        #
        [module, keyword_import, index] = parse1_statement_from_module(s, m1.end())
        #</module>

        #
        #<imported ... (, | newline)>
        #
        [imported, operator, index] = parse1_statement_from_as(s, index)

        if imported is none:
            return UnknownLine(s)
        #<imported/>

        if operator.is_token_newline:
            assert length(s) == index

            return StatementFromImport(
                       keyword_from,
                       module,
                       keyword_import,
                       imported,
                       operator,
                   )

        #
        #<imported ... (, | newline)>
        #
        [imported_2, operator_2, index] = parse1_statement_from_as(s, index)

        if imported is none:
            return UnknownLine(s)
        #<imported/>

        if operator_2.is_token_newline:
            assert length(s) == index

            return StatementFromImport(
                       keyword_from,
                       module,
                       keyword_import,
                       ExpressionComma(imported, operator, imported_2),
                       operator_2,
                   )

        line('parse1_statement_from: incomplete#3')
        return UnknownLine(s)
