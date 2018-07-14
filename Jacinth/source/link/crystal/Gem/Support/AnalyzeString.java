//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.Character;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Support.AsciiTable;


public abstract class   AnalyzeString
    extends             Gem_Object//<Inspection>
{
    //
    //  Class Order magic values
    //
    public static final int ANALYZE_STRING__EMPTY            = 0;
    public static final int ANALYZE_STRING__WORD             = 1;
    public static final int ANALYZE_STRING__BORING_PRINTABLE = 2;
    public static final int ANALYZE_STRING__PRINTABLE        = 3;
    public static final int ANALYZE_STRING__UNPRINTABLE      = 4;

    public static final String          analysis_name[] = new String[] {
            "empty",
            "word",
            "boring-printable",
            "printable",
            "unprintable",
        };


    //
    //  Public (debug)
    //
    public static final void            show_analyze_string(final String s)
    {
        final int                       analysis = AnalyzeString.analyze_string(s);

        line("analysis of {p}: {}", s, AnalyzeString.analysis_name[analysis]);
    }


    //
    //  Public
    //
    public static final int             analyze_string(final String s)
    {
        final AsciiTable[]              table = AsciiTable.table;

        final int                       total = s.length();

        boolean                         is_word             = true;
        boolean                         is_boring_printable = true;
        AsciiTable                      glyph               = null;

        int                             code_point;

        for (int                        i = 0; i < total; /*  i is incremented in the loop by 1 or 2  */) {
            code_point = s.codePointAt(i);

            if (code_point < 128) {
                glyph = table[code_point];

                if (glyph.is_word) {
                    continue;
                }

                is_word = false;

                if (glyph.is_boring_printable) {
                    continue;
                }

                break;
            }

            glyph = AsciiTable.unknown;

            i += Character.charCount(code_point);

            is_boring_printable =
                is_printable =
                is_word = false;
        }

        if (length == total) {
            if (is_word) {
                if (total == 0) {
                    return AnalyzeString.ANALYZE_STRING__EMPTY;
                }

                return AnalyzeString.ANALYZE_STRING__WORD;
            }

            return AnalyzeString.ANALYZE_STRING__BORING_PRINTABLE;
        }

        boolean                         is_printable;

        if (glyph.is_printable) {
        }

        return AnalyzeString.ANALYZE_STRING__UNPRINTABLE;
    }
}
