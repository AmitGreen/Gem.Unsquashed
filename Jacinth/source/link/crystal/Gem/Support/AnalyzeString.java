//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.util.regex.Matcher;
import java.util.regex.Pattern;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Inspection.Inspection;
import link.crystal.Gem.Interface.Inspectable;


public final class  AnalyzeString
    extends         Gem_Object <Inspection>
    implements      Inspectable<Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("AnalyzeString");


    //
    //  Static members
    //
    //      Matching rules:
    //          Most likely match:          group 1                     //  Example: First.Middle77.Last@gmail.com
    //          Second most likely match:   group 2                     //  Example: Can't!
    //
    private static final Pattern        string_pattern = Pattern.compile(
                "([-$%+,./0-9:@A-Z_a-z~]+)?"                            //  Example: First.Middle77.Last@gmail.com
              + "([^\"'\\\\]+)?"                                        //  Example: Can't!
        );
        

    //
    //  Members
    //
    public  final Zone                  z;
    private       String                s;
    public  final Matcher               matcher;


    //
    //  Constructor, Factory, & Recycle
    //
    private                             AnalyzeString(final Zone z, final String s, final Matcher matcher)
    {
        this.z       = z;
        this.s       = s;
        this.matcher = matcher;
    }


    static public AnalyzeString         create__ALLY__Zone(Zone z, String s)
    {
        final Matcher                   matcher = AnalyzeString.string_pattern.matcher(s);

        return new AnalyzeString(z, s, matcher);
    }


    public AnalyzeString                recycle(String s)
    {
        this.s = s;
        this.matcher.reset(s);

        return this;
    }


    //
    //  Interface Inspectable
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }


    //inherited public void             Portray(String_Builder builder);


    //
    //  Private
    //
    private final void                  analyze_string__work()
    {
        final String                    s       = this.s;
        final Matcher                   matcher = this.matcher;

        if ( ! matcher.matches()) {
            line("analyze_string: {p} - no match", s);
            return;
        }

        final int                       start_2 = matcher.start(2);

        if (start_2 != -1) {
            line("analyze_string: {p} - sentence", s);
            return;
        }

        final int                   start_1 = matcher.start(1);

        if (start_1 != -1) {
            line("analyze_string: {p} - word", s);
            return;
        }

        line("analyze_string: {p} - empty", s);
    }


    //
    //  Public
    //
    public static final void            analyze_string(final Zone z, final String s)
    {
        final AnalyzeString             analyze_string = z.summon_AnalyzeString__ALLY__AnalyzeString(s);

        analyze_string.analyze_string__work();

        z.recycle__AnalyzeString__ALLY__AnalyzeString(analyze_string);
    }
}
