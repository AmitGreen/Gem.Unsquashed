//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.String;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Format.ArgumentSegmentFormatter;
import link.crystal.Gem.Format.ArgumentSegmentFormatter_Inspection;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Interface.SegmentFormattable;
import link.crystal.Gem.Support.Storehouse_PortraySegmentFormatter;
import link.crystal.Gem.World.World_Inspection;


public class    PortraySegmentFormatter
    extends     ArgumentSegmentFormatter<PortraySegmentFormatter_Inspection>
//  extends     MessageFormatter_Base   <PortraySegmentFormatter_Inspection>
//  extends     Gem_Object              <PortraySegmentFormatter_Inspection>
//  extends     Object
    implements  MessageFormattable,
                SegmentFormattable      <PortraySegmentFormatter_Inspection>,
                Inspectable             <PortraySegmentFormatter_Inspection>//, //  Via Gem_Object
{
    public static final PortraySegmentFormatter_Inspection  inspection = (
            PortraySegmentFormatter_Inspection.create("PortraySegmentFormatter")
        );


    //
    //  Constructor & Factory
    //
    private                             PortraySegmentFormatter(int argument_index)
    {
        super(argument_index);
    }


    static public PortraySegmentFormatter   conjure__ALLY__PortraySegmentFormatter_Inspection(
            Zone                                z,
            int                                 argument_index//,
        )
    {
        final Storehouse_PortraySegmentFormatter    cache = Storehouse_PortraySegmentFormatter.singleton;

        final PortraySegmentFormatter       previous = cache.lookup(argument_index);

        if (previous != null) {
            return previous;
        }

        final PortraySegmentFormatter       r = new PortraySegmentFormatter(argument_index);

        cache.insert(z, argument_index, r);

        return r;
    }


    //
    //  Interface Inspectable
    //
    public PortraySegmentFormatter_Inspection   inspect()
    {
        return /*static*/ this.inspection;
    }


    //
    //  Interface MessageFormattable
    //
    @Override
    public void                         arrange(Gem_StringBuilder builder, int depth, Object v)
    {
        builder.portray(v);
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

        if (argument_index == 0) {
            builder.portray(v);
            return;
        }

        RUNTIME("argument_index is {} (expected 0)", argument_index);
    }


    public void                         choose(Gem_StringBuilder builder, int depth, Object v, Object w)
    {
        final int                       argument_index = this.argument_index;

        if (argument_index == 0) {
            builder.portray(v);
            return;
        }

        if (argument_index == 1) {
            builder.portray(w);
            return;
        }

        RUNTIME("argument_index is {} (expected 0 or 1)", argument_index);
    }


    public void                         choose(Gem_StringBuilder builder, int depth, Object v, Object w, Object x)
    {
        final int                       argument_index = this.argument_index;

        if (argument_index == 0) {
            builder.portray(v);
            return;
        }

        if (argument_index == 1) {
            builder.portray(w);
            return;
        }

        if (argument_index == 2) {
            builder.portray(x);
            return;
        }

        RUNTIME("argument_index is {} (expected 0, 1, or 2)", argument_index);
    }


    public void                         choose(Gem_StringBuilder builder, int depth, Object v, Object w, Object x, Object y)
    {
        final int                       argument_index = this.argument_index;

        if (argument_index == 0) {
            builder.portray(v);
            return;
        }

        if (argument_index == 1) {
            builder.portray(w);
            return;
        }

        if (argument_index == 2) {
            builder.portray(x);
            return;
        }

        if (argument_index == 3) {
            builder.portray(y);
            return;
        }

        RUNTIME("argument_index is {} (expected number between 0 and 3)", argument_index);
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

        if (argument_index == 0) {
            builder.portray(v);
            return;
        }

        if (argument_index == 1) {
            builder.portray(w);
            return;
        }

        if (argument_index == 2) {
            builder.portray(x);
            return;
        }

        if (argument_index == 3) {
            builder.portray(y4);
            return;
        }

        if (argument_index == 4) {
            builder.portray(y5);
            return;
        }

        RUNTIME("argument_index is {} (expected number between 0 and 4)", argument_index);
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

        if (argument_index == 0) {
            builder.portray(v);
            return;
        }

        if (argument_index == 1) {
            builder.portray(w);
            return;
        }

        if (argument_index == 2) {
            builder.portray(x);
            return;
        }

        if (argument_index == 3) {
            builder.portray(y4);
            return;
        }

        if (argument_index == 4) {
            builder.portray(y5);
            return;
        }

        if (argument_index == 5) {
            builder.portray(y6);
            return;
        }

        RUNTIME("argument_index is {} (expected number between 0 and 5)", argument_index);
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

        if (argument_index == 0) {
            builder.portray(v);
            return;
        }

        if (argument_index == 1) {
            builder.portray(w);
            return;
        }

        if (argument_index == 2) {
            builder.portray(x);
            return;
        }

        if (argument_index == 3) {
            builder.portray(y4);
            return;
        }

        if (argument_index == 4) {
            builder.portray(y5);
            return;
        }

        if (argument_index == 5) {
            builder.portray(y6);
            return;
        }

        if (argument_index == 6) {
            builder.portray(y7);
            return;
        }

        builder.portray(other_arguments[argument_index - 7]);
    }
}


class           PortraySegmentFormatter_Inspection
    extends     ArgumentSegmentFormatter_Inspection<PortraySegmentFormatter>
//  extends     Inspection
//  extends     Gem_Object <World_Inspection>
//  extends     Object
    implements  Inspectable<World_Inspection>//,                        //  Via Gem_Object
{
    private static final World_Inspection   inspection = (
            World_Inspection.create("PortraySegmentFormatter_Inspection", 3)
        );


    //
    //  Constructor & Factory
    //
    protected                           PortraySegmentFormatter_Inspection(String simple_class_name)
    {
        super(simple_class_name);
    }


    public static PortraySegmentFormatter_Inspection    create(String simple_class_name)
    {
        final Zone                      z = Zone.current_zone();

        final String                    interned__simple_class_name = z.intern_permenant_string(simple_class_name);

        return new PortraySegmentFormatter_Inspection(interned__simple_class_name);
    }


    //
    //  Abstract ArgumentSegmentFormatter_Inspection
    //
    public PortraySegmentFormatter     conjure_argument_segment(Zone z, int argument_index)
    {
        return PortraySegmentFormatter.conjure__ALLY__PortraySegmentFormatter_Inspection(z, argument_index);
    }


    //
    //  Interface Inspectable
    //
    public World_Inspection             inspect()
    {
        return /*static*/ this.inspection;
    }
}
