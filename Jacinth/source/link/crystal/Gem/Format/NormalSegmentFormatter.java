//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.String;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Format.ArgumentSegmentFormatter;
import link.crystal.Gem.Format.ArgumentSegmentFormatter_Inspection;
import link.crystal.Gem.Inspection.World_Inspection;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Interface.SegmentFormattable;


public final class  NormalSegmentFormatter
    extends         ArgumentSegmentFormatter<ArgumentSegmentFormatter_Inspection>
//  extends         MessageFormatter_Base   <ArgumentSegmentFormatter_Inspection>
//  extends         Gem_Object              <ArgumentSegmentFormatter_Inspection>
//  extends         Object
    implements      MessageFormattable      <ArgumentSegmentFormatter_Inspection>,
                    SegmentFormattable      <ArgumentSegmentFormatter_Inspection>,
                    Inspectable             <ArgumentSegmentFormatter_Inspection>//,
{
    public static final NormalSegmentFormatter_Inspection   inspection = (
            NormalSegmentFormatter_Inspection.create("NormalSegmentFormatter")
        );


    //
    //  Constructor & Factory
    //
    private                             NormalSegmentFormatter(final int argument_index)
    {
        super(argument_index);
    }


    public static final NormalSegmentFormatter  create__ALLY__Zone(final Zone z, final int argument_index)
    {
        return new NormalSegmentFormatter(argument_index);
    }


    //
    //  Interface Inspectable
    //
    @Override
    public final NormalSegmentFormatter_Inspection  inspect()
    {
        return /*static*/ this.inspection;
    }


    //
    //  Interface MessageFormattable
    //
    @Override
    public final void                   augment(final Gem_StringBuilder builder, int depth, final Object v)
    {
        builder.format(v);
    }


    @Override
    public final void                   augment_1_plus(
            final Gem_StringBuilder             builder,
            final int                           depth,
            final Object                        v,
            final Object ...                    other_arguments//,
        )
    {
        if (other_arguments.length != 0) {
            RUNTIME("{p} argument{} given (expected 0)",
                    other_arguments.length,
                    (other_arguments.length == 1 ? "" : "s"));
        }

        builder.format(v);
    }


    //
    //  Interface SegmentFormattable
    //
    @Override
    public final void                   choose(final Gem_StringBuilder builder, int depth)
    {
        INVALID_ROUTINE();
    }


    @Override
    public final void                   choose(final Gem_StringBuilder builder, int depth, final Object v)
    {
        final int                       argument_index = this.argument_index;

        if (argument_index == 0) {
            builder.format(v);
            return;
        }

        RUNTIME("argument_index is {} (expected 0)", argument_index);
    }


    @Override
    public final void                   choose(
            final Gem_StringBuilder             builder,
            final int                           depth,
            final Object                        v,
            final Object                        w//,
        )
    {
        final int                       argument_index = this.argument_index;

        if (argument_index == 0) {
            builder.format(v);
            return;
        }

        if (argument_index == 1) {
            builder.format(w);
            return;
        }

        RUNTIME("argument_index is {} (expected 0 or 1)", argument_index);
    }


    @Override
    public final void                   choose(
            final Gem_StringBuilder             builder,
            final int                           depth,
            final Object                        v,
            final Object                        w,
            final Object                        x//,
        )
    {
        final int                       argument_index = this.argument_index;

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

        RUNTIME("argument_index is {} (expected 0, 1, or 2)", argument_index);
    }


    @Override
    public final void                   choose(
            final Gem_StringBuilder             builder,
            final int                           depth,
            final Object                        v,
            final Object                        w,
            final Object                        x,
            final Object                        y//,
        )
    {
        final int                       argument_index = this.argument_index;

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

        RUNTIME("argument_index is {} (expected number between 0 and 3)", argument_index);
    }


    @Override
    public final void                   choose(
            final Gem_StringBuilder             builder,
            final int                           depth,
            final Object                        v,
            final Object                        w,
            final Object                        x,
            final Object                        y4,
            final Object                        y5//,
        )
    {
        final int                       argument_index = this.argument_index;

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

        RUNTIME("argument_index is {} (expected number between 0 and 4)", argument_index);
    }


    @Override
    public final void                   choose(
            final Gem_StringBuilder             builder,
            final int                           depth,
            final Object                        v,
            final Object                        w,
            final Object                        x,
            final Object                        y4,
            final Object                        y5,
            final Object                        y6//,
        )
    {
        final int                       argument_index = this.argument_index;

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

        RUNTIME("argument_index is {} (expected number between 0 and 5)", argument_index);
    }


    @Override
    public final void                   choose(
            final Gem_StringBuilder             builder,
            final int                           depth,
            final Object                        v,
            final Object                        w,
            final Object                        x,
            final Object                        y4,
            final Object                        y5,
            final Object                        y6,
            final Object                        y7,
            final Object ...                    other_arguments//,
        )
    {
        final int                       argument_index = this.argument_index;

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
//  extends     Gem_Object <World_Inspection>
//  extends     Object
    implements  Inspectable<World_Inspection>//,
{
    private static final World_Inspection   inspection = World_Inspection.create("NormalSegmentFormatter_Inspection");


    //
    //  Constructor & Factory
    //
    protected                           NormalSegmentFormatter_Inspection(final String simple_class_name)
    {
        super(simple_class_name);
    }


    public static NormalSegmentFormatter_Inspection     create(final String simple_class_name)
    {
        final Zone                      z = Zone.current_zone();

        final String                    interned__simple_class_name = z.intern_permenant_string(simple_class_name);

        return new NormalSegmentFormatter_Inspection(interned__simple_class_name);
    }


    //
    //  Abstract ArgumentSegmentFormatter_Inspection
    //
    @Override
    public final NormalSegmentFormatter     conjure_argument_segment(final Zone z, final int argument_index)
    {
        return z.conjure_NormalSegmentFormatter(argument_index);
    }


    //
    //  Interface Inspectable
    //
    @Override
    public final World_Inspection       inspect()
    {
        return /*static*/ this.inspection;
    }
}
