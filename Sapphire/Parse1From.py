#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1From')
def gem():
    require_gem('Sapphire.Elemental')
    require_gem('Sapphire.Expression')
    require_gem('Sapphire.Match')
    require_gem('Sapphire.Statement')


    @share
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

        keyword = m2.group('keyword')
        #</as>

        if keyword is none:
            return (( imported, TokenNewline(m2.group()), m2.end() ))

        if keyword is ',':
            return (( imported, OperatorComma(m2.group()), m2.end() ))

        as_keyword = KeywordAs(m2.group())

        #
        #<name2>
        #
        m3 = name_match(s, m2.end())

        if m3 is none:
            line('parse1_statement_from_as: incomplete#3')
            return tuple_of_3_nones

        imported = AsFragment(imported, as_keyword, Symbol(m3.group()))
        #</name2>

        #
        #<comma>
        #
        m4 = from1_comma_match(s, m3.end())

        if m4 is none:
            line('parse1_statement_from_as: incomplete#4')
            return tuple_of_3_nones
        #</comma>

        if m4.start('comma') is -1:
            return (( imported, TokenNewline(m4.group()), m4.end() ))

        return (( imported, OperatorComma(m4.group()), m4.end() ))


    @share
    def parse1_statement_from(m1, s):
        keyword_from = KeywordDefine(m1.group())

        #
        #<name1>
        #
        m2 = name_match(s, m1.end())

        if m2 is none:
            line('parse1_statement_from: incomplete#1')
            return UnknownLine(s)

        module = Symbol(m2.group())
        #</name1>

        #
        #<import>
        #   ['.' name] ... 'import'
        #
        while true:
            m3       = from1_module_match(s, m2.end())
            operator = m3.group('operator')

            if operator is not '.':
                break

            operator_dot = OperatorDot(m3.group())

            #
            #<name2>
            #
            m2 = name_match(s, m3.end())

            if m2 is none:
                line('parse1_statement_from: incomplete#2')
                return UnknownLine(s)
            #</name2>

            module = ExpressionDot(module, operator_dot, m2.group())

        keyword_import = KeywordImport(m3.group())
        #<import>

        #
        #<imported: name [as name] ... (, | newline)>
        #
        [imported, operator, index] = parse1_statement_from_as(s, m3.end())

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
        #<imported: name [as name] ... (, | newline)>
        #
        [imported_2, operator_2, index] = parse1_statement_from_as(s, index)

        if imported is none:
            return UnknownLine(s)
        #<imported/>

        if operator_2.is_token_newline:
            return StatementFromImport(
                       keyword_from,
                       module,
                       keyword_import,
                       ExpressionComma(imported, operator, imported_2),
                       operator_2,
                   )

        line('parse1_statement_from: incomplete#3')
        return UnknownLine(s)
