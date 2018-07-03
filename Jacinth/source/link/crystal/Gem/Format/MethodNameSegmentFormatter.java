//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.SegmentFormattable;


public class    MethodNameSegmentFormatter
    extends     Gem_Object<Inspection>
//  extends     Object
    implements  SegmentFormattable,
                Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create("Gem.Format.MethodNameSegmentFormatter");


    //
    //  Private static
    //
    private static MethodNameSegmentFormatter   singleton = null;



    //
    //  Constructor & Factory
    //
    private                             MethodNameSegmentFormatter()
    {
    }


    static public MethodNameSegmentFormatter    conjure(Zone z)
    {
        MethodNameSegmentFormatter      singleton = MethodNameSegmentFormatter.singleton;

        if (singleton != null) {
            return singleton;
        }

        singleton =
            MethodNameSegmentFormatter.singleton = new MethodNameSegmentFormatter();

        return singleton;
    }


    //
    //  Private
    //
    static String                       method_name(Zone z) {
        return "?";
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
    public String                       select_1(Zone z, String a)
    {
        return this.method_name(z);
    }


    public String                       select_2(Zone z, String a, String b)
    {
        return this.method_name(z);
    }


    public String                       select_3(Zone z, String a, String b, String c)
    {
        return this.method_name(z);
    }


    public String                       select_4(Zone z, String a, String b, String c, String d)
    {
        return this.method_name(z);
    }


    public String                       select_5(Zone z, String a, String b, String c, String d, String e)
    {
        return this.method_name(z);
    }


    public String                       select_many(Zone z, String[] arguments)
    {
        return this.method_name(z);
    }


    public String                       portray(Zone z)
    {
        return "<MethodNameSegmentFormatter>";
    }
}
