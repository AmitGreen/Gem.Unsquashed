//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.Zone;
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


    static public StringSegmentFormatter    create__ALLY__Storehouse_StringSegmentFormatter(Zone z, String s)
    {
        String                              interned_s = z.intern_permenant_string(s);

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
    public void                         select_1(Gem_StringBuilder builder, Object a)
    {
        builder.append(this.s);
    }


    public void                         select_2(Gem_StringBuilder builder, Object a, Object b)
    {
        builder.append(this.s);
    }


    public void                         select_3(Gem_StringBuilder builder, Object a, Object b, Object c)
    {
        builder.append(this.s);
    }


    public void                         select_4(Gem_StringBuilder builder, Object a, Object b, Object c, Object d)
    {
        builder.append(this.s);
    }


    public void                         select_5(
            Gem_StringBuilder                   builder,
            Object                              a,
            Object                              b,
            Object                              c,
            Object                              d,
            Object                              e//,
        )
    {
        builder.append(this.s);
    }


    public void                         select_many(
            Gem_StringBuilder                   builder,
            Object                              a,
            Object                              b,
            Object                              c,
            Object                              d,
            Object                              e,
            Object ...                          other_arguments//,
        )
    {
        builder.append(this.s);
    }


    public String                       portray(Zone z)
    {
        return "<StringSegmentFormatter " + z.quote_string(this.s) + ">";
    }


    public String                       s()
    {
        return this.s;
    }
}
