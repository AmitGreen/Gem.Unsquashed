//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.String;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Format.MessageFormatter_Base;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Interface.SegmentFormattable;
import link.crystal.Gem.Support.Storehouse_AdornmentSegmentFormatter;
import link.crystal.Gem.Format.SegmentFormatter_Inspection;


public class    AdornmentSegmentFormatter
    extends     MessageFormatter_Base<SegmentFormatter_Inspection>
//  extends     Gem_Object           <SegmentFormatter_Inspection>
//  extends     Object
    implements  MessageFormattable,
                SegmentFormattable   <SegmentFormatter_Inspection>,
                Inspectable          <SegmentFormatter_Inspection>//,   //  Via Gem_Object
{
    private static SegmentFormatter_Inspection  inspection = (
            SegmentFormatter_Inspection.create("AdornmentSegmentFormatter")
        );


    //
    //  Members
    //
    public final String                 s;


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

        AdornmentSegmentFormatter       r = cache.lookup(z, s);

        if (r != null) {
            return r;
        }

        String                          interned_s = z.intern_permenant_string(s);

        r = new AdornmentSegmentFormatter(interned_s);

        cache.insert(z, interned_s, r);

        return r;
    }


    //
    //  Interface Inspectable
    //
    public SegmentFormatter_Inspection  inspect()
    {
        return /*static*/ this.inspection;
    }


    //
    //  Interface MessageFormattable
    //
    @Override
    public void                         augment(Gem_StringBuilder builder, int depth)
    {
        builder.append(this.s);
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


    public void                         portray(Gem_StringBuilder builder)
    {
        builder.append("<AdornmentSegmentFormatter ");
        builder.quote(this.s);
        builder.append(">");
    }


    public String                       s()
    {
        return this.s;
    }
}
