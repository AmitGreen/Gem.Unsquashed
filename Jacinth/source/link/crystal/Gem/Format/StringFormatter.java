//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.RuntimeException;
import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.PortrayFunctions;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.SegmentFormattable;


public class    StringFormatter
    extends     Gem_Object<Inspection>
//  extends     Object
    implements  SegmentFormattable,
                Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create("Gem.Format.StringFormatter");


    //
    //  Members
    //
    private String                      s;


    //
    //  Constructor & Factory
    //
    private                             StringFormatter(String s)
    {
        this.s = s;
    }


    static public StringFormatter       create__ALLY__PermenantStringFormatter(String s)
    {
        return new StringFormatter(s);
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
        return "<StringFormatter " + PortrayFunctions.portray_string(this.s) + ">";
    }
}
