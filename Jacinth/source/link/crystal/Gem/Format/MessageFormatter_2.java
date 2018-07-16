//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.String;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Format.MessageFormatter_Base;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Interface.SegmentFormattable;
import link.crystal.Gem.Inspection.Inspection;


public final class  MessageFormatter_2
    extends         MessageFormatter_Base<Inspection>
//  extends         Gem_Object           <Inspection>
//  extends         Object
    implements      MessageFormattable   <Inspection>,
                    Inspectable          <Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("MessageFormatter_2");


    //
    //  Members
    //
    private final int                   expected;
    private final SegmentFormattable    a;
    private final SegmentFormattable    b;


    //
    //  Constructor & Factory
    //
    private                             MessageFormatter_2(
            final int                           expected,
            final SegmentFormattable            a,
            final SegmentFormattable            b//,
        )
    {
        this.expected = expected;
        this.a        = a;
        this.b        = b;
    }


    public static final MessageFormatter_2  create(
            final Zone                          z,
            final int                           expected,
            final SegmentFormattable            a,
            final SegmentFormattable            b//,
        )
    {
        return new MessageFormatter_2(expected, a, b);
    }


    //
    //  Interface Inspectable
    //
    @Override
    public final Inspection             inspect()
    {
        return /*static*/ this.inspection;
    }


    @Override
    public final void                   portray(final Gem_StringBuilder builder)
    {
        builder.append("<MessageFormatter_2 ");
        builder.portray(this.a);
        builder.append(" ");
        builder.portray(this.b);
        builder.append(">");
    }


    //
    //  Interface MessageFormattable
    //
    @Override
    public final void                   augment(final Gem_StringBuilder builder, int depth)
    {
        if (this.expected != 0) {
            RUNTIME("0 arguments given (expected {})", this.expected);
        }

        depth += 1;

        this.a.choose(builder, depth);
        this.b.choose(builder, depth);
    }


    @Override
    public final void                   augment(final Gem_StringBuilder builder, /*:*/ int depth, final Object v)
    {
        if (this.expected != 1) {
            RUNTIME("1 argument given (expected {})", this.expected);
        }

        depth += 1;

        this.a.choose(builder, depth, v);
        this.b.choose(builder, depth, v);
    }


    @Override
    public final void                   augment(
            final Gem_StringBuilder             builder,
            /*:*/ int                           depth,
            final Object                        v,
            final Object                        w//,
        )
    {
        if (this.expected != 2) {
            RUNTIME("2 arguments given (expected {})", this.expected);
        }

        depth += 1;

        this.a.choose(builder, depth, v, w);
        this.b.choose(builder, depth, v, w);
    }


    @Override
    public final void                   augment_1_plus(
            final Gem_StringBuilder             builder,
            /*:*/ int                           depth,
            final Object                        v,
            final Object ...                    other_arguments//,
        )
    {
        final int                       actual = 1 + other_arguments.length;

        if (this.expected != actual) {
            RUNTIME("{} argument{} given (expected {})",
                    actual,
                    (actual == 1 ? "" : "s"),
                    this.expected);
        }

        depth += 1;

        if (actual == 1) {
            this.a.choose(builder, depth, v);
            this.b.choose(builder, depth, v);
            return;
        }

        assert fact(actual == 2, "actual == 2");

        final Object                    w = other_arguments[0];

        this.a.choose(builder, depth, v, w);
        this.b.choose(builder, depth, v, w);
    }
}
