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
    //  Members
    //
    public final Zone                   z;


    //
    //  Constructor & Factory
    //
    private                             AnalyzeString(Zone z)
    {
        this.z = z;
    }


    static public AnalyzeString         create__ALLY__Zone(Zone z)
    {
        return new AnalyzeString(z);
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
    //  Public
    //
    public final void                   analyze_string(final String s)
    {
        line("analyze_string: {p}", s);
    }
}
