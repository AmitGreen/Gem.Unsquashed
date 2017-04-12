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
    def parse1_statement_from(m1, s):
        keyword_from = KeywordDefine(m1.group())

        #
        #<name1>
        #
        m2 = name_match(s, m1.end())

        if m2 is none:
            line('parse1_statement_from: incomplete#1A')
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
        #<name>
        #
        m4 = name_match(s, m3.end())

        if m4 is none:
            line('parse1_statement_from: incomplete#3')
            return UnknownLine(s)

        imported = Symbol(m4.group())
        #</name>

        #
        #<as>
        #
        m5 = from1_as_match(s, m4.end())

        if m5 is none:
            line('parse1_statement_from: incomplete#4')
            return UnknownLine(s)

        keyword = m5.group('keyword')
        #</as>

        if keyword is none:
            return StatementFromImport(
                       keyword_from,
                       module,
                       keyword_import,
                       imported,
                       m5.group(),
                   )

        if keyword is ',':
            operator_comma = OperatorComma(m5.group())
        else:
            as_keyword = KeywordAs(m5.group())

            #
            #<name2>
            #
            m6 = name_match(s, m5.end())

            if m6 is none:
                line('parse1_statement_from: incomplete#5')
                return UnknownLine(s)

            imported = AsFragment(imported, as_keyword, Symbol(m6.group()))
            #</name2>

            #
            #<comma>
            #
            m5 = from1_comma_match(s, m6.end())

            if m5 is none:
                line('parse1_statement_from: incomplete#6')
                return UnknownLine(s)
            #</comma>

            if m5.start('comma') is -1:
                return StatementFromImport(
                           keyword_from,
                           module,
                           keyword_import,
                           imported,
                           m5.group(),
                       )

            operator_comma = OperatorComma(m5.group())

        #
        #<name>
        #
        m4 = name_match(s, m5.end())

        if m4 is none:
            line('parse1_statement_from: incomplete#7')
            return UnknownLine(s)

        imported_2 = Symbol(m4.group())
        #</name>

        #
        #<as>
        #
        m5 = from1_as_match(s, m4.end())

        if m5 is none:
            line('parse1_statement_from: incomplete#8')
            return UnknownLine(s)

        keyword = m5.group('keyword')
        #</as>

        if keyword is none:
            return StatementFromImport(
                       keyword_from,
                       module,
                       keyword_import,
                       ExpressionComma(imported, operator_comma, imported_2),
                       m5.group(),
                   )

        if keyword is ',':
            operator_comma = OperatorComma(m5.group())
        else:
            as_keyword = KeywordAs(m5.group())

            #
            #<name2>
            #
            m6 = name_match(s, m5.end())

            if m6 is none:
                line('parse1_statement_from: incomplete#9')
                return UnknownLine(s)

            imported_2 = AsFragment(imported_2, as_keyword, Symbol(m6.group()))
            #</name2>

            #
            #<comma>
            #
            m5 = from1_comma_match(s, m6.end())

            if m5 is none:
                line('parse1_statement_from: incomplete#10')
                return UnknownLine(s)
            #</comma>

            if m5.start('comma') is -1:
                return StatementFromImport(
                           keyword_from,
                           module,
                           keyword_import,
                           ExpressionComma(imported, operator_comma, imported_2),
                           m5.group(),
                       )

            operator_comma = OperatorComma(m5.group())

        line('parse1_statement_from: incomplete#11')
        return UnknownLine(s)
