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
import link.crystal.Gem.Support.Storehouse_PortraySegmentFormatter;


public class    PortraySegmentFormatter
    extends     MessageFormatter_Base
//  extends     Gem_Object<Inspection>
//  extends     Object
    implements  MessageFormattable,
                SegmentFormattable,
                Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create("Gem.Format.PortraySegmentFormatter");


    //
    //  Members
    //
    private int                         argument_index;


    //
    //  Constructor & Factory
    //
    private                             PortraySegmentFormatter(int argument_index)
    {
        this.argument_index = argument_index;
    }


    static public PortraySegmentFormatter   conjure(Zone z, int argument_index)
    {
        final Storehouse_PortraySegmentFormatter    cache = Storehouse_PortraySegmentFormatter.singleton;

        PortraySegmentFormatter             r = cache.lookup(argument_index);

        if (r != null) {
            return r;
        }

        r = new PortraySegmentFormatter(argument_index);

        cache.insert(argument_index, r);

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
    public String                       arrange(Zone z, int depth, Object v)
    {
        return z.portray(v);
    }


    //
    //  Interface SegmentFormattable
    //
    public void                         choose(Gem_StringBuilder builder, int depth)
    {
        final Zone                      z = builder.z;

        z.INVALID_ROUTINE();
    }

    public void                         choose(Gem_StringBuilder builder, int depth, Object v)
    {
        final int                       argument_index = this.argument_index;

        final Zone                      z = builder.z;

        if (argument_index == 0) {
            builder.append(z.portray(v));
            return;
        }

        z.RUNTIME("argument_index is {} (expected 0)", argument_index);
    }


    public void                         choose(Gem_StringBuilder builder, int depth, Object v, Object w)
    {
        final int                       argument_index = this.argument_index;

        final Zone                      z = builder.z;

        if (argument_index == 0) {
            builder.append(z.portray(v));
            return;
        }

        if (argument_index == 1) {
            builder.append(z.portray(w));
            return;
        }

        z.RUNTIME("argument_index is {} (expected 0 or 1)", argument_index);
    }


    public void                         choose(Gem_StringBuilder builder, int depth, Object v, Object w, Object x)
    {
        final int                       argument_index = this.argument_index;

        final Zone                      z = builder.z;

        if (argument_index == 0) {
            builder.append(z.portray(v));
            return;
        }

        if (argument_index == 1) {
            builder.append(z.portray(w));
            return;
        }

        if (argument_index == 2) {
            builder.append(z.portray(x));
            return;
        }

        z.RUNTIME("argument_index is {} (expected 0, 1, or 2)", argument_index);
    }


    public void                         choose(Gem_StringBuilder builder, int depth, Object v, Object w, Object x, Object y)
    {
        final int                       argument_index = this.argument_index;

        final Zone                      z = builder.z;

        if (argument_index == 0) {
            builder.append(z.portray(v));
            return;
        }

        if (argument_index == 1) {
            builder.append(z.portray(w));
            return;
        }

        if (argument_index == 2) {
            builder.append(z.portray(x));
            return;
        }

        if (argument_index == 3) {
            builder.append(z.portray(y));
            return;
        }

        z.RUNTIME("argument_index is {} (expected number between 0 and 3)", argument_index);
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
        final int                       argument_index = this.argument_index;

        final Zone                      z = builder.z;

        if (argument_index == 0) {
            builder.append(z.portray(v));
            return;
        }

        if (argument_index == 1) {
            builder.append(z.portray(w));
            return;
        }

        if (argument_index == 2) {
            builder.append(z.portray(x));
            return;
        }

        if (argument_index == 3) {
            builder.append(z.portray(y4));
            return;
        }

        if (argument_index == 4) {
            builder.append(z.portray(y5));
            return;
        }

        z.RUNTIME("argument_index is {} (expected number between 0 and 4)", argument_index);
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
        final int                       argument_index = this.argument_index;

        final Zone                      z = builder.z;

        if (argument_index == 0) {
            builder.append(z.portray(v));
            return;
        }

        if (argument_index == 1) {
            builder.append(z.portray(w));
            return;
        }

        if (argument_index == 2) {
            builder.append(z.portray(x));
            return;
        }

        if (argument_index == 3) {
            builder.append(z.portray(y4));
            return;
        }

        if (argument_index == 4) {
            builder.append(z.portray(y5));
            return;
        }

        if (argument_index == 5) {
            builder.append(z.portray(y6));
            return;
        }

        z.RUNTIME("argument_index is {} (expected number between 0 and 5)", argument_index);
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
        final int                       argument_index = this.argument_index;

        final Zone                      z = builder.z;

        if (argument_index == 0) {
            builder.append(z.portray(v));
            return;
        }

        if (argument_index == 1) {
            builder.append(z.portray(w));
            return;
        }

        if (argument_index == 2) {
            builder.append(z.portray(x));
            return;
        }

        if (argument_index == 3) {
            builder.append(z.portray(y4));
            return;
        }

        if (argument_index == 4) {
            builder.append(z.portray(y5));
            return;
        }

        if (argument_index == 5) {
            builder.append(z.portray(y6));
            return;
        }

        if (argument_index == 6) {
            builder.append(z.portray(y7));
            return;
        }

        builder.append(z.portray(other_arguments[argument_index - 7]));
    }


    public String                       portray(Zone z)
    {
        return "<PortraySegmentFormatter " + Integer.toString(this.argument_index) + ">";
    }
}
