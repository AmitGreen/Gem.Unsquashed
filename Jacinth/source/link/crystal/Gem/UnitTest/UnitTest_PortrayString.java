
//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.UnitTest;


import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Inspection.Inspection;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Support.AnalyzeString;
import link.crystal.Mirror.Shape;


final class         PortrayStringData
    extends         Gem_Object <Inspection>
//  extends         Object
    implements      Inspectable<Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("PortrayStringData_2");


    //
    //  Members
    //
    public final String                 s;
    public final String                 raw_expected;
    public final String                 python_expected;


    //
    //  Constructor & Factory
    //
    private                             PortrayStringData(
            final String                        s,
            final String                        raw_expected,
            final String                        python_expected//,
        )
    {
        this.s               = s;
        this.raw_expected    = raw_expected;
        this.python_expected = python_expected;
    }


    public static final PortrayStringData   create_2(final String s, final String raw_expected)
    {
        final String                    python_expected = raw_expected;

        return new PortrayStringData(s, raw_expected, python_expected);
    }


    public static final PortrayStringData   create_3(
            final String                        s,
            final String                        raw_expected,
            final String                        python_expected//,
        )
    {
        return new PortrayStringData(s, raw_expected, python_expected);
    }


    //
    //  Interface Inspectable
    //
    @Override
    public final Inspection             inspect()
    {
        return /*static*/ this.inspection;
    }


    @Override
    public final void                   portray(final Gem_StringBuilder builder)
    {
        builder.append("<PortrayStringData_2 ");
        builder.java_quote(this.s);
        builder.append("; ", this.raw_expected, ">");
    }
}


public final class  UnitTest_PortrayString
    extends         Gem_Object <Inspection>
//  extends         Object
    implements      Inspectable<Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("UnitTest_PortrayString");


    //
    //  Members
    //
    public final Zone                   z;


    //
    //  Static Members (Unit Test Data)
    //
    static public final PortrayStringData[]   portray_string_many = new PortrayStringData[] {
            PortrayStringData.create_2(
              "wink \\\"\\\"'",
              "r\"wink \\\"\\\"'\""//,
            ),
            PortrayStringData.create_3(
              "ending single quote '",
              "r\"ending single quote '\"",
              "\"ending single quote '\""//,
            ),
            PortrayStringData.create_3(
              "'",
              "r\"'\"",
              "\"'\""//,
            ),
            PortrayStringData.create_2(
              "wi\nk \\\"\\\"'",
              "\"\"\"wi\\nk \\\\\"\\\\\"'\"\"\""//,
            ),
            PortrayStringData.create_2(
              "\\\"two apostrophe\\\": ''",
              "r\"\\\"two apostrophe\\\": ''\""//,
            ),
            PortrayStringData.create_3(
              "quoted: ''",
              "r\"quoted: ''\"",
              "\"quoted: ''\""//,
            ),
            PortrayStringData.create_2(
              "wo\nk \\\"\\\"''",
              "\"\"\"wo\\nk \\\\\"\\\\\"''\"\"\""//,
            ),
            PortrayStringData.create_2(
              "le'mo\n\\",
              "\"le'mo\\n\\\\\""//,
            ),
            PortrayStringData.create_2(
              "apostrophe & backlash: '\\",
              "\"apostrophe & backlash: '\\\\\""//,
            ),
            PortrayStringData.create_2(
              "\\\"'\\\"",
              "r\"\\\"'\\\"\""//,
            ),
            PortrayStringData.create_3(
              "can't",
              "r\"can't\"",
              "\"can't\""//,
            ),
            PortrayStringData.create_2(
              "ca\n't",
              "\"ca\\n't\""//,
            ),
            PortrayStringData.create_3(
              "End with \"'\": \"'",
              "r\"\"\"End with \"'\": \"'\"\"\"",
              "\"\"\"End with \"'\": \"'\"\"\""//,
            ),
            PortrayStringData.create_3(
              "other way: '\"' & '",
              "r\"\"\"other way: '\"' & '\"\"\"",
              "\"\"\"other way: '\"' & '\"\"\""//,
            ),
            PortrayStringData.create_2(
              "\"lemo\n's\"'",
              "\"\"\"\\\"lemo\\n's\"'\"\"\""//,
            ),
            PortrayStringData.create_3(
              "prefer \", \"\", ', or ''",
              "r\"\"\"prefer \", \"\", ', or ''\"\"\"",
              "\"\"\"prefer \", \"\", ', or ''\"\"\""//,
            ),
            PortrayStringData.create_3(
              "prefer ', '', \", or ''",
              "r\"\"\"prefer ', '', \", or ''\"\"\"",
              "\"\"\"prefer ', '', \", or ''\"\"\""//,
            ),
            PortrayStringData.create_2(
              "\"more lemo\n''s\"'",
              "\"\"\"\\\"more lemo\\n''s\"'\"\"\""//,
            ),
            PortrayStringData.create_2(
              "le'\"mo\"\n\\",
              "'''le'\"mo\"\\n\\\\'''"//,
            ),
            PortrayStringData.create_2(
              "all \", ', & \\",
              "'''all \", ', & \\\\'''"//,
            ),
            PortrayStringData.create_2(
              "'triple' is: \"\"\\\".",
              "r\"\"\"'triple' is: \"\"\\\".\"\"\""//,
            ),
            PortrayStringData.create_3(
              "'\"\" \"\"'2",
              "r\"\"\"'\"\" \"\"'2\"\"\"",
              "\"\"\"'\"\" \"\"'2\"\"\""//,
            ),
            PortrayStringData.create_2(
              "\"triple\" is: ''\\'.",
              "r'''\"triple\" is: ''\\'.'''"//,
            ),
            PortrayStringData.create_3(
              "\"'' ''\"!",
              "r'''\"'' ''\"!'''",
              "'''\"'' ''\"!'''"//,
            ),
            PortrayStringData.create_3(
              "single: ', '' .vs. \"?",
              "r\"\"\"single: ', '' .vs. \"?\"\"\"",
              "\"\"\"single: ', '' .vs. \"?\"\"\""//,
            ),
            PortrayStringData.create_2(
              "lemo\n''s \"yet\" again",
              "'''lemo\\n''s \"yet\" again'''"//,
            ),
            PortrayStringData.create_3(
              "singles \"'\" & \"''\"",
              "r'''singles \"'\" & \"''\"'''",
              "'''singles \"'\" & \"''\"'''"//,
            ),
            PortrayStringData.create_3(
              "the quotes: ' & \"",
              "r'''the quotes: ' & \"'''",
              "'''the quotes: ' & \"'''"//,
            ),
            PortrayStringData.create_3(
              "Wow: ''\"",
              "r'''Wow: ''\"'''",
              "'''Wow: ''\"'''"//,
            ),
            PortrayStringData.create_2(
              "lemo\n's are \"sour\"",
              "'''lemo\\n's are \"sour\"'''"//,
            ),
            PortrayStringData.create_3(
              "more quotes: '' & \"\"",
              "r'''more quotes: '' & \"\"'''",
              "'''more quotes: '' & \"\"'''"//,
            ),
            PortrayStringData.create_3(
              "compare: ''+'' .vs. \"\"",
              "r'''compare: ''+'' .vs. \"\"'''",
              "'''compare: ''+'' .vs. \"\"'''"//,
            ),
            PortrayStringData.create_2(
              "yep - lemo\n's \"\"sour\"\"",
              "'''yep - lemo\\n's \"\"sour\"\"'''"//,
            ),
            PortrayStringData.create_2(
              "\"\"\"\tab'",
              "\"\"\"\\\"\"\\\"\\tab'\"\"\""//,
            ),
            PortrayStringData.create_2(
              "\"\"\"\\non-tab'",
              "\"\"\"\\\"\"\\\"\\\\non-tab'\"\"\""//,
            ),
            PortrayStringData.create_2(
              "': '\"\"\"\".'",
              "\"\"\"': '\"\"\\\"\".'\"\"\""//,
            ),
            PortrayStringData.create_2(
              "3: '\"\"\".'",
              "\"\"\"3: '\"\"\\\".'\"\"\""//,
            ),
            PortrayStringData.create_2(
              "\"\"\"AS_B\n''",
              "\"\"\"\\\"\"\\\"AS_B\\n''\"\"\""//,
            ),
            PortrayStringData.create_2(
              "\"\"\"\\AS_B''",
              "\"\"\"\\\"\"\\\"\\\\AS_B''\"\"\""//,
            ),
            PortrayStringData.create_2(
              "\"\"\"\"\"\".''",
              "\"\"\"\\\"\"\\\"\"\\\"\".''\"\"\""//,
            ),
            PortrayStringData.create_2(
              "le'\"\"\"mo\"\"\"\n\\",
              "'''le'\"\"\"mo\"\"\"\\n\\\\'''"//,
            ),
            PortrayStringData.create_2(
              "all \"\"\", ', & \\",
              "'''all \"\"\", ', & \\\\'''"//,
            ),
            PortrayStringData.create_3(
              "more \"\"\"\" than '!",
              "r'''more \"\"\"\" than '!'''",
              "'''more \"\"\"\" than '!'''"//,
            ),
            PortrayStringData.create_3(
              "l''s \"\"\"\" t''n '!",
              "r'''l''s \"\"\"\" t''n '!'''",
              "'''l''s \"\"\"\" t''n '!'''"//,
            ),
            PortrayStringData.create_2(
              "\"\"\"'now' AS_\n",
              "'''\"\"\"'now' AS_\\n'''"//,
            ),
            PortrayStringData.create_3(
              "lots of ''''' - more'",
              "r\"lots of ''''' - more'\"",
              "\"lots of ''''' - more'\""//,
            ),
            PortrayStringData.create_2(
              "'''@C_N + e\nding '",
              "\"'''@C_N + e\\nding '\""//,
            ),
            PortrayStringData.create_3(
              "lots of ''''' - extra''",
              "r\"lots of ''''' - extra''\"",
              "\"lots of ''''' - extra''\""//,
            ),
            PortrayStringData.create_2(
              "'''@C_N + 2x e\nding ''",
              "\"'''@C_N + 2x e\\nding ''\""//,
            ),
            PortrayStringData.create_3(
              "abundance of '''''''",
              "r\"abundance of '''''''\"",
              "\"abundance of '''''''\""//,
            ),
            PortrayStringData.create_2(
              "'''C_C is a pali\ndrome'''",
              "\"'''C_C is a pali\\ndrome'''\""//,
            ),
            PortrayStringData.create_2(
              "''''Super\n?'''\\",
              "\"''''Super\\n?'''\\\\\""//,
            ),
            PortrayStringData.create_2(
              "''''supercalifragilisticexpialidocious?'''\\",
              "\"''''supercalifragilisticexpialidocious?'''\\\\\""//,
            ),
            PortrayStringData.create_3(
              "lots of ''''' - lots!",
              "r\"lots of ''''' - lots!\"",
              "\"lots of ''''' - lots!\""//,
            ),
            PortrayStringData.create_2(
              "'''@C_\n",
              "\"'''@C_\\n\""//,
            ),
            PortrayStringData.create_2(
              "\\",
              "'\\\\'"//,
            ),
            PortrayStringData.create_3(
              "End '''with \"'\": \"'",
              "r\"\"\"End '''with \"'\": \"'\"\"\"",
              "\"\"\"End '''with \"'\": \"'\"\"\""//,
            ),
            PortrayStringData.create_2(
              "\"lemo\n'''s\"'",
              "\"\"\"\\\"lemo\\n'''s\"'\"\"\""//,
            ),
            PortrayStringData.create_3(
              "More \"quotes\" ''' & ''",
              "r\"\"\"More \"quotes\" ''' & ''\"\"\"",
              "\"\"\"More \"quotes\" ''' & ''\"\"\""//,
            ),
            PortrayStringData.create_2(
              "\"lemo\n\"ade'''s''",
              "\"\"\"\\\"lemo\\n\"ade'''s''\"\"\""//,
            ),
            PortrayStringData.create_3(
              "End with 3x \"'\": \"'''",
              "r\"\"\"End with 3x \"'\": \"'''\"\"\"",
              "\"\"\"End with 3x \"'\": \"'''\"\"\""//,
            ),
            PortrayStringData.create_2(
              "'''\"\tables\"'''",
              "\"\"\"'''\"\\tables\"'''\"\"\""//,
            ),
            PortrayStringData.create_2(
              "le'''\"mo\"\n\\",
              "\"\"\"le'''\"mo\"\\n\\\\\"\"\""//,
            ),
            PortrayStringData.create_2(
              "deja vu: \", ''', & \\",
              "\"\"\"deja vu: \", ''', & \\\\\"\"\""//,
            ),
            PortrayStringData.create_3(
              "l\"\"s '''' t\"\"n \"!",
              "r\"\"\"l\"\"s '''' t\"\"n \"!\"\"\"",
              "\"\"\"l\"\"s '''' t\"\"n \"!\"\"\""//,
            ),
            PortrayStringData.create_3(
              "more '''' than \"!",
              "r\"\"\"more '''' than \"!\"\"\"",
              "\"\"\"more '''' than \"!\"\"\""//,
            ),
            PortrayStringData.create_2(
              "'''\"\rake\"''' leaves",
              "\"\"\"'''\"\\rake\"''' leaves\"\"\""//,
            ),
            PortrayStringData.create_2(
              "been \"there\", '''done that'''\\",
              "\"\"\"been \"there\", '''done that'''\\\\\"\"\""//,
            ),
            PortrayStringData.create_2(
              "'''\t\"",
              "'''\\''\\'\\t\"'''"//,
            ),
            PortrayStringData.create_2(
              "'333: \"'''.\"",
              "'''\\'333: \"''\\'.\"'''"//,
            ),
            PortrayStringData.create_2(
              "almos\t done: '''\"\"",
              "'''almos\\t done: ''\\'\"\"'''"//,
            ),
            PortrayStringData.create_2(
              "three: \"''''''.\"\"",
              "'''three: \"''\\''\\''.\"\"'''"//,
            ),
            PortrayStringData.create_2(
              "more lemo\ns\\",
              "'more lemo\\ns\\\\'"//,
            ),
            PortrayStringData.create_2(
              "not a real lemon\\",
              "'not a real lemon\\\\'"//,
            ),
            PortrayStringData.create_3(
              "",
              "r''",
              "''"//,
            ),
            PortrayStringData.create_3(
              "test#2",
              "r'test#2'",
              "'test#2'"//,
            ),
            PortrayStringData.create_2(
              "double backslash: \\\\",
              "r'double backslash: \\\\'"//,
            ),
            PortrayStringData.create_2(
              "\\'",
              "r\"\\'\""//,
            ),
            PortrayStringData.create_2(
              "A \normal lemo\n",
              "'A \\normal lemo\\n'"//,
            ),
            PortrayStringData.create_2(
              "backslash: \\",
              "'backslash: \\\\'"//,
            ),
            PortrayStringData.create_2(
              "le\"mo\"\nade\\",
              "'le\"mo\"\\nade\\\\'"//,
            ),
            PortrayStringData.create_2(
              "just \" & \\",
              "'just \" & \\\\'"//,
            ),
            PortrayStringData.create_3(
              "\" is a quotation mark",
              "r'\" is a quotation mark'",
              "'\" is a quotation mark'"//,
            ),
            PortrayStringData.create_2(
              "\\'\"\\'",
              "r'\\'\"\\''"//,
            ),
            PortrayStringData.create_2(
              "A \"\normal\" lemo\n",
              "'A \"\\normal\" lemo\\n'"//,
            ),
            PortrayStringData.create_2(
              "\"backslash\": \\",
              "'\"backslash\": \\\\'"//,
            ),
            PortrayStringData.create_3(
              "\"",
              "r'\"'",
              "'\"'"//,
            ),
            PortrayStringData.create_2(
              "She \\'said\\' \\'hello\"",
              "r'She \\'said\\' \\'hello\"'"//,
            ),
            PortrayStringData.create_2(
              "lemo\n \"orchard\"",
              "'lemo\\n \"orchard\"'"//,
            ),
            PortrayStringData.create_3(
              "double quoted: \"\"",
              "r'double quoted: \"\"'",
              "'double quoted: \"\"'"//,
            ),
            PortrayStringData.create_2(
              "More \\'\\'\\' than \"\"",
              "r'More \\'\\'\\' than \"\"'"//,
            ),
            PortrayStringData.create_2(
              "lemo\n\"s and quotes\"\"",
              "'lemo\\n\"s and quotes\"\"'"//,
            ),
            PortrayStringData.create_2(
              "\"\"\"S\nakes\"\"\" \\",
              "'\"\"\"S\\nakes\"\"\" \\\\'"//,
            ),
            PortrayStringData.create_2(
              "\"\"\"Snakes\"\"\" & backslash: \\",
              "'\"\"\"Snakes\"\"\" & backslash: \\\\'"//,
            ),
            PortrayStringData.create_3(
              "lots of \"\"\"\"\" - lots!",
              "r'lots of \"\"\"\"\" - lots!'",
              "'lots of \"\"\"\"\" - lots!'"//,
            ),
            PortrayStringData.create_2(
              "Prefer \\'\\'\\'\\' or \"\"\"?",
              "r'Prefer \\'\\'\\'\\' or \"\"\"?'"//,
            ),
            PortrayStringData.create_2(
              "Yet again \"\"\" & \\",
              "'Yet again \"\"\" & \\\\'"//,
            ),
            PortrayStringData.create_3(
              "Three \"\"\" is more than 1 \"",
              "r'Three \"\"\" is more than 1 \"'",
              "'Three \"\"\" is more than 1 \"'"//,
            ),
            PortrayStringData.create_2(
              "\"\"\"\\'\\'hi\\'\\' & \\'hello\"",
              "r'\"\"\"\\'\\'hi\\'\\' & \\'hello\"'"//,
            ),
            PortrayStringData.create_2(
              "\"\"\"Quotatio\n\"",
              "'\"\"\"Quotatio\\n\"'"//,
            ),
            PortrayStringData.create_3(
              "Three \"\"\" > 2 \"\"",
              "r'Three \"\"\" > 2 \"\"'",
              "'Three \"\"\" > 2 \"\"'"//,
            ),
            PortrayStringData.create_2(
              "\"\"\"\\'\\'hello\\'\\' & \\'bye\"\"",
              "r'\"\"\"\\'\\'hello\\'\\' & \\'bye\"\"'"//,
            ),
            PortrayStringData.create_2(
              "\"\"\"5 Quotatio\n marks\"\"",
              "'\"\"\"5 Quotatio\\n marks\"\"'"//,
            ),
            PortrayStringData.create_3(
              "\"\"\"",
              "r'\"\"\"'",
              "'\"\"\"'"//,
            ),
            PortrayStringData.create_2(
              "\"\"\"\\'\\'\\'\\'\\'\\'\\'\"\"\"",
              "r'\"\"\"\\'\\'\\'\\'\\'\\'\\'\"\"\"'"//,
            ),
            PortrayStringData.create_2(
              "\"\"\"And \now six!\"\"\"",
              "'\"\"\"And \\now six!\"\"\"'"//,
            ),
            PortrayStringData.create_2(
              "\"lots of ''''' - lots!\"",
              "'''\"lots of ''\\''\\' - lots!\"'''"//,
            )//,
        };


    //
    //  Constructor & Factory
    //
    private                             UnitTest_PortrayString(final Zone z)
    {
        this.z = z;
    }


    public static final UnitTest_PortrayString  create(final Zone z)
    {
        return new UnitTest_PortrayString(z);
    }


    //
    //  Interface Inspectable
    //
    @Override
    public final Inspection             inspect()
    {
        return /*static*/ this.inspection;
    }


    //
    //  Public (Unit tests)
    //
    public final boolean                test_portray_string()
    {
        line("===   Unit Test:  Portray String   ===");

        final PortrayStringData[]       portray_string_many = UnitTest_PortrayString.portray_string_many;

        final int                       portray_string_total = portray_string_many.length;

        /*:*/ int                       i;

        for (i = 0; i < portray_string_total; i ++) {
            final PortrayStringData     portray_string_data = portray_string_many[i];
            
            final String                s               = portray_string_data.s;
            final String                raw_expected    = portray_string_data.raw_expected;
            final String                python_expected = portray_string_data.python_expected;

            final String                raw_actual = AnalyzeString.analyze_raw_string(s);

            if ( ! raw_actual.equals(raw_expected)) {
                line("portray_raw_string({p})", s);
                line("  actual:   {}", raw_actual);
                line("  expected: {}", raw_expected);

            //  RUNTIME("portray_raw_string({p}) failed", s);
                break;
            }

            final String                python_actual   = AnalyzeString.analyze_python_string(s);

            if ( ! python_actual.equals(python_expected)) {
                line("portray_python_string({p})", s);
                line("  actual:   {}", python_actual);
                line("  expected: {}", python_expected);

            //  RUNTIME("portray_python_string({p}) failed", s);
                break;
            }
        }

        if (i < portray_string_total) {
            line("INCOMPLETE:   Unit Test:  Portray String");
        } else {
            line("PASSED:  Portray String");
        }
        
        return true;
    }
}
