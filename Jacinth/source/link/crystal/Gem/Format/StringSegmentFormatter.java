//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.RuntimeException;
import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.SegmentFormattable;


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
        String                              interned_s = intern_permenant_string(s);

        return new StringSegmentFormatter(interned_s);
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


    public String                       select_3(String a, String b, String c)
    {
        return this.s;
    }


    public String                       select_4(String a, String b, String c, String d)
    {
        return this.s;
    }


    public String                       select_5(String a, String b, String c, String d, String e)
    {
        return this.s;
    }


    public String                       select_many(String[] arguments)
    {
        return this.s;
    }


    public String                       portray()
    {
        return "<StringSegmentFormatter " + portray_string(this.s) + ">";
    }


    public String                       s()
    {
        return this.s;
    }
}
