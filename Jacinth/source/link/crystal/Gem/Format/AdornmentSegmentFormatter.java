//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Format.MessageFormatter_Base;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Interface.SegmentFormattable;
import link.crystal.Gem.Support.Storehouse_AdornmentSegmentFormatter;


public class    AdornmentSegmentFormatter
    extends     MessageFormatter_Base
//  extends     Gem_Object<Inspection>
//  extends     Object
    implements  MessageFormattable,
                SegmentFormattable,
                Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create("Gem.Format.AdornmentSegmentFormatter");


    //
    //  Members
    //
    private String                      s;


    //
    //  Constructor & Factory
    //
    private                             AdornmentSegmentFormatter(String s)
    {
        this.s = s;
    }


    static public AdornmentSegmentFormatter     conjure(Zone z, String s)
    {
        Storehouse_AdornmentSegmentFormatter    cache = Storehouse_AdornmentSegmentFormatter.singleton;

        AdornmentSegmentFormatter       r = cache.lookup(s);

        if (r != null) {
            return r;
        }

        String                          interned_s = z.intern_permenant_string(s);

        r = new AdornmentSegmentFormatter(interned_s);

        cache.insert(interned_s, r);

        return r;
    }


    //
    //  Interface Inspectable
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }


    //
    //  Interface MessageFormattable
    //
    public String                       arrange(Zone z, int depth)
    {
        return this.s;
    }


    //
    //  Interface SegmentFormattable
    //
    public void                         choose(Gem_StringBuilder builder, int depth)
    {
        builder.append(this.s);
    }


    public void                         choose(Gem_StringBuilder builder, int depth, Object v)
    {
        builder.append(this.s);
    }


    public void                         choose(Gem_StringBuilder builder, int depth, Object v, Object w)
    {
        builder.append(this.s);
    }


    public void                         choose(Gem_StringBuilder builder, int depth, Object v, Object w, Object x)
    {
        builder.append(this.s);
    }


    public void                         choose(
            Gem_StringBuilder                   builder,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y//,
        )
    {
        builder.append(this.s);
    }


    public void                         choose(
            Gem_StringBuilder                   builder,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5//,
        )
    {
        builder.append(this.s);
    }


    public void                         choose(
            Gem_StringBuilder                   builder,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5,
            Object                              y6//,
        )
    {
        builder.append(this.s);
    }


    public void                         choose(
            Gem_StringBuilder                   builder,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5,
            Object                              y6,
            Object                              y7,
            Object ...                          other_arguments//,
        )
    {
        builder.append(this.s);
    }


    public String                       portray(Zone z)
    {
        return "<AdornmentSegmentFormatter " + z.quote_string(this.s) + ">";
    }


    public String                       s()
    {
        return this.s;
    }
}
