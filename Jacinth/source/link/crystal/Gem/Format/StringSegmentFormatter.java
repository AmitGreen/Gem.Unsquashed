//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.RuntimeException;
import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.SegmentFormattable;
import link.crystal.Gem.Support.PortrayFunctions;


public class    StringSegmentFormatter
    extends     Gem_Object<Inspection>
//  extends     Object
    implements  SegmentFormattable,
                Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create("Gem.Format.StringSegmentFormatter");


    //
    //  Members
    //
    private String                      s;


    //
    //  Constructor & Factory
    //
    private                             StringSegmentFormatter(String s)
    {
        this.s = s;
    }


    static public StringSegmentFormatter    create__ALLY__Storehouse_StringSegmentFormatter(String s)
    {
        return new StringSegmentFormatter(s);
    }


    //
    //  Interface Inspectable
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }


    //
    //  Interface SegmentFormattable
    //
    public String                       select_2(String a, String b)
    {
        return this.s;
    }


    public String                       portray()
    {
        return "<StringSegmentFormatter " + PortrayFunctions.portray_string(this.s) + ">";
    }
}
