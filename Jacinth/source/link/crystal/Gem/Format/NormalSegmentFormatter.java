//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Format.ArgumentSegmentFormatter;
import link.crystal.Gem.Format.ArgumentSegmentFormatter_Inspection;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Interface.SegmentFormattable;
import link.crystal.Gem.Support.Storehouse_NormalSegmentFormatter;


public class    NormalSegmentFormatter
    extends     ArgumentSegmentFormatter<ArgumentSegmentFormatter_Inspection>
//  extends     MessageFormatter_Base   <ArgumentSegmentFormatter_Inspection>
//  extends     Gem_Object              <ArgumentSegmentFormatter_Inspection>
//  extends     Object
    implements  MessageFormattable,
                SegmentFormattable,
                Inspectable<ArgumentSegmentFormatter_Inspection>//,     //  Via Gem_Object
{
    public static NormalSegmentFormatter_Inspection     inspection = (
            NormalSegmentFormatter_Inspection.create("NormalSegmentFormatter")
        );


    //
    //  Constructor & Factory
    //
    private                             NormalSegmentFormatter(int argument_index)
    {
        super(argument_index);
    }


    static public NormalSegmentFormatter    conjure__ALLY__NormalSegmentFormatter_Inspection(
            Zone                                z,
            int                                 argument_index//,
        )
    {
        final Storehouse_NormalSegmentFormatter     cache = Storehouse_NormalSegmentFormatter.singleton;

        NormalSegmentFormatter             r = cache.lookup(argument_index);

        if (r != null) {
            return r;
        }

        r = new NormalSegmentFormatter(argument_index);

        cache.insert(argument_index, r);

        return r;
    }


    //
    //  Interface Inspectable
    //
    public NormalSegmentFormatter_Inspection    inspect()
    {
        return /*static*/ this.inspection;
    }


    //
    //  Interface MessageFormattable
    //
    @Override
    public void                         arrange(Gem_StringBuilder builder, int depth, Object v)
    {
        builder.z.output("Hmm ... " + v);

        builder.format(v);
    }


    //
    //  Interface SegmentFormattable
    //
    public void                         choose(Gem_StringBuilder builder, int depth)
    {
        INVALID_ROUTINE();
    }

    public void                         choose(Gem_StringBuilder builder, int depth, Object v)
    {
        final int                       argument_index = this.argument_index;

        final Zone                      z = builder.z;

        if (argument_index == 0) {
            builder.format(v);
            return;
        }

        z.RUNTIME("argument_index is {} (expected 0)", argument_index);
    }


    public void                         choose(Gem_StringBuilder builder, int depth, Object v, Object w)
    {
        final int                       argument_index = this.argument_index;

        final Zone                      z = builder.z;

        if (argument_index == 0) {
            builder.format(v);
            return;
        }

        if (argument_index == 1) {
            builder.format(w);
            return;
        }

        z.RUNTIME("argument_index is {} (expected 0 or 1)", argument_index);
    }


    public void                         choose(Gem_StringBuilder builder, int depth, Object v, Object w, Object x)
    {
        final int                       argument_index = this.argument_index;

        final Zone                      z = builder.z;

        if (argument_index == 0) {
            builder.format(v);
            return;
        }

        if (argument_index == 1) {
            builder.format(w);
            return;
        }

        if (argument_index == 2) {
            builder.format(x);
            return;
        }

        z.RUNTIME("argument_index is {} (expected 0, 1, or 2)", argument_index);
    }


    public void                         choose(Gem_StringBuilder builder, int depth, Object v, Object w, Object x, Object y)
    {
        final int                       argument_index = this.argument_index;

        final Zone                      z = builder.z;

        if (argument_index == 0) {
            builder.format(v);
            return;
        }

        if (argument_index == 1) {
            builder.format(w);
            return;
        }

        if (argument_index == 2) {
            builder.format(x);
            return;
        }

        if (argument_index == 3) {
            builder.format(y);
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
            builder.format(v);
            return;
        }

        if (argument_index == 1) {
            builder.format(w);
            return;
        }

        if (argument_index == 2) {
            builder.format(x);
            return;
        }

        if (argument_index == 3) {
            builder.format(y4);
            return;
        }

        if (argument_index == 4) {
            builder.format(y5);
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
            builder.format(v);
            return;
        }

        if (argument_index == 1) {
            builder.format(w);
            return;
        }

        if (argument_index == 2) {
            builder.format(x);
            return;
        }

        if (argument_index == 3) {
            builder.format(y4);
            return;
        }

        if (argument_index == 4) {
            builder.format(y5);
            return;
        }

        if (argument_index == 5) {
            builder.format(y6);
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
            builder.format(v);
            return;
        }

        if (argument_index == 1) {
            builder.format(w);
            return;
        }

        if (argument_index == 2) {
            builder.format(x);
            return;
        }

        if (argument_index == 3) {
            builder.format(y4);
            return;
        }

        if (argument_index == 4) {
            builder.format(y5);
            return;
        }

        if (argument_index == 5) {
            builder.format(y6);
            return;
        }

        if (argument_index == 6) {
            builder.format(y7);
            return;
        }

        builder.format(other_arguments[argument_index - 7]);
    }
}


class           NormalSegmentFormatter_Inspection
    extends     ArgumentSegmentFormatter_Inspection<NormalSegmentFormatter>
//  extends     Inspection
//  extends     Gem_Object<Inspection>
//  extends     Object
    implements  Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create("NormalSegmentFormatter_Inspection");


    //
    //  Constructor & Factory
    //
    protected                           NormalSegmentFormatter_Inspection(String simple_class_name)
    {
        super(simple_class_name);
    }


    public static NormalSegmentFormatter_Inspection     create(String simple_class_name)
    {
        final Zone                      z = Zone.current_zone();

        final String                    interned__simple_class_name = z.intern_permenant_string(simple_class_name);

        return new NormalSegmentFormatter_Inspection(interned__simple_class_name);
    }


    //
    //  Abstract ArgumentSegmentFormatter_Inspection
    //
    public NormalSegmentFormatter       conjure_argument_segment(Zone z, int argument_index)
    {
        return NormalSegmentFormatter.conjure__ALLY__NormalSegmentFormatter_Inspection(z, argument_index);
    }


    //
    //  Interface Inspectable
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }
}
