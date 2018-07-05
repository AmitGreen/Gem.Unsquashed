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
import link.crystal.Gem.Support.Storehouse_StringSegmentFormatter;


public class    StringSegmentFormatter
    extends     MessageFormatter_Base
//  extends     Gem_Object<Inspection>
//  extends     Object
    implements  MessageFormattable,
                SegmentFormattable,
                Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create("Gem.Format.StringSegmentFormatter");


    //
    //  Members
    //
    private int                         argument_index;


    //
    //  Constructor & Factory
    //
    private                             StringSegmentFormatter(int argument_index)
    {
        this.argument_index = argument_index;
    }


    static public StringSegmentFormatter    conjure(Zone z, int argument_index)
    {
        final Storehouse_StringSegmentFormatter     cache = Storehouse_StringSegmentFormatter.singleton;

        StringSegmentFormatter              r = cache.lookup(argument_index);

        if (r != null) {
            return r;
        }

        r = new StringSegmentFormatter(argument_index);

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
    @Override
    public void                         arrange(Gem_StringBuilder builder, int depth, Object v)
    {
        builder.append(v.toString());
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
            builder.append(v.toString());
            return;
        }

        z.RUNTIME("argument_index is {} (expected 0)", argument_index);
    }


    public void                         choose(Gem_StringBuilder builder, int depth, Object v, Object w)
    {
        final int                       argument_index = this.argument_index;

        final Zone                      z = builder.z;

        if (argument_index == 0) {
            builder.append(v.toString());
            return;
        }

        if (argument_index == 1) {
            builder.append(w.toString());
            return;
        }

        z.RUNTIME("argument_index is {} (expected 0 or 1)", argument_index);
    }


    public void                         choose(Gem_StringBuilder builder, int depth, Object v, Object w, Object x)
    {
        final int                       argument_index = this.argument_index;

        final Zone                      z = builder.z;

        if (argument_index == 0) {
            builder.append(v.toString());
            return;
        }

        if (argument_index == 1) {
            builder.append(w.toString());
            return;
        }

        if (argument_index == 2) {
            builder.append(x.toString());
            return;
        }

        z.RUNTIME("argument_index is {} (expected 0, 1, or 2)", argument_index);
    }


    public void                         choose(Gem_StringBuilder builder, int depth, Object v, Object w, Object x, Object y)
    {
        final int                       argument_index = this.argument_index;

        final Zone                      z = builder.z;

        if (argument_index == 0) {
            builder.append(v.toString());
            return;
        }

        if (argument_index == 1) {
            builder.append(w.toString());
            return;
        }

        if (argument_index == 2) {
            builder.append(x.toString());
            return;
        }

        if (argument_index == 3) {
            builder.append(y.toString());
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
            builder.append(v.toString());
            return;
        }

        if (argument_index == 1) {
            builder.append(w.toString());
            return;
        }

        if (argument_index == 2) {
            builder.append(x.toString());
            return;
        }

        if (argument_index == 3) {
            builder.append(y4.toString());
            return;
        }

        if (argument_index == 4) {
            builder.append(y5.toString());
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
            builder.append(v.toString());
            return;
        }

        if (argument_index == 1) {
            builder.append(w.toString());
            return;
        }

        if (argument_index == 2) {
            builder.append(x.toString());
            return;
        }

        if (argument_index == 3) {
            builder.append(y4.toString());
            return;
        }

        if (argument_index == 4) {
            builder.append(y5.toString());
            return;
        }

        if (argument_index == 5) {
            builder.append(y6.toString());
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
            builder.append(v.toString());
            return;
        }

        if (argument_index == 1) {
            builder.append(w.toString());
            return;
        }

        if (argument_index == 2) {
            builder.append(x.toString());
            return;
        }

        if (argument_index == 3) {
            builder.append(y4.toString());
            return;
        }

        if (argument_index == 4) {
            builder.append(y5.toString());
            return;
        }

        if (argument_index == 5) {
            builder.append(y6.toString());
            return;
        }

        if (argument_index == 6) {
            builder.append(y7.toString());
            return;
        }

        builder.append(other_arguments[argument_index - 7].toString());
    }


    public String                       portray(Zone z)
    {
        return "<StringSegmentFormatter " + Integer.toString(this.argument_index) + ">";
    }
}
