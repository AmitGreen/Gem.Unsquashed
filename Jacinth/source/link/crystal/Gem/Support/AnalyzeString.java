//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.Character;
import link.crystal.Gem.Core.Gem_Object;


public abstract class   AnalyzeString
    extends             Gem_Object//<Inspection>
{
    //
    //  Public
    //
    public static final void            analyze_string(final String s)
    {
        final int                       total = s.length();

        for (int                        i = 0; i < total; i ++) {
            final int                   code_point = s.codePointAt(i);

            line("{}", code_point);

            i += Character.charCount(code_point);
        }
    }
}
