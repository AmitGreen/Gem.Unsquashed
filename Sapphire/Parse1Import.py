#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
@gem('Sapphire.Parse1From')
def gem():
    require_gem('Sapphire.Elemental')
    require_gem('Sapphire.Match')
    require_gem('Sapphire.Statement')
    require_gem('Sapphire.Token')


    def parse1_statement_import_module(s, index):
        #
        #<name>
        #
        m1 = name_match(s, index)

        if m1 is none:
            line('parse1_statement_import_module: incomplete#1')
            return tuple_of_3_nones

        module = Symbol(m1.group())
        #</name>

        #
        #<module: name ||| ['.' name] ... ('as' | ',' | newline)
        #
        while true:
            m2 = import1_module_match(s, m1.end())

            if m2 is none:
                line('parse1_statement_import_module: incomplete#2')
                return tuple_of_3_nones

            operator = m2.group('operator')

            if operator is not '.':
                break

            operator_dot = OperatorDot(m2.group())

            #
            #<name>
            #
            m1 = name_match(s, m2.end())

            if m1 is none:
                line('parse1_statement_import_module: incomplete#3')
                return tuple_of_3_nones
            #</name>

            module = ExpressionDot(module, operator_dot, m1.group())

        if operator is none:
            return (( module, TokenNewline(m2.group()), m2.end() ))
            
        if operator is ',':
            return (( module, OperatorComma(m2.group()), m2.end() ))

        keyword_as = KeywordAs(m2.group())
        #</module>

        #
        #<name>
        #
        m3 = name_match(s, m2.end())

        if m3 is none:
            line('parse1_statement_import_module: incomplete#4')
            return tuple_of_3_nones

        module = ModuleAsFragment(module, keyword_as, Symbol(m3.group()))
        #</name>

        #
        #<comma-or-newline>
        #
        m4 = comma1_or_newline_match(s, m3.end())

        if m4 is none:
            line('parse1_statement_import_module: incomplete#5')
            return tuple_of_3_nones
        #</comma-or-newline>

        if m4.start('comma') is -1:
            return (( module, TokenNewline(m4.group()), m4.end() ))

        return (( module, OperatorComma(m4.group()), m4.end() ))


    @share
    def parse1_statement_import(m1, s):
        keyword_import = KeywordImport(m1.group())

        #
        #<module ... 'import'>
        #
        [module, operator, index] = parse1_statement_import_module(s, m1.end())
        #</module>

        if module is none:
            return UnknownLine(s)

        if operator.is_token_newline:
            assert length(s) == index

            return StatementImport(
                       keyword_import,
                       module,
                       operator,
                   )

        line('parse1_statement_import: incomplete#1: %r %r %r %r', keyword_import, module, operator, index)
        return UnknownLine(s)
