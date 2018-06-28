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


public final class  MessageFormatter_Many
    extends         MessageFormatter_Base<Inspection>
//  extends         Gem_Object           <Inspection>
//  extends         Object
    implements      MessageFormattable   <Inspection>,
                    Inspectable          <Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("MessageFormatter_Many");


    //
    //  Members
    //
    private final int                   expected;
    private final SegmentFormattable[]  segment_many;


    //
    //  Constructor & Factory
    //
    private                             MessageFormatter_Many(
            final int                           expected,
            final SegmentFormattable[]          segment_many//,
        )
    {
        this.expected     = expected;
        this.segment_many = segment_many;
    }


    public static final MessageFormatter_Many   create(
            final Zone                          z,
            final int                           expected,
            final SegmentFormattable[]          segment_many//,
        )
    {
        assert fact_between(2, expected, segment_many.length);

        return new MessageFormatter_Many(expected, segment_many);
    }


    //
    //  Interface Inspectable
    //
    @Override
    public final Inspection             inspect()
    {
        return /*static*/ this.inspection;
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

        final SegmentFormattable[]      segment_many = this.segment_many;

        final int                       segment_total = segment_many.length;

        depth += 1;

        for (/*:*/ int                  i       = 0; i < segment_total; i ++) {
            final SegmentFormattable    segment = segment_many[i];

            segment.choose(builder, depth);
        }
    }


    @Override
    public final void                   augment(final Gem_StringBuilder builder, int depth, final Object v)
    {
        if (this.expected != 1) {
            RUNTIME("1 argument given (expected {})", this.expected);
        }

        final SegmentFormattable[]      segment_many = this.segment_many;

        final int                       segment_total = segment_many.length;

        depth += 1;

        for (/*:*/ int                  i       = 0; i < segment_total; i ++) {
            final SegmentFormattable    segment = segment_many[i];

            segment.choose(builder, depth, v);
        }
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

        final SegmentFormattable[]      segment_many = this.segment_many;

        final int                       segment_total = segment_many.length;

        depth += 1;

        for (/*:*/ int                  i       = 0; i < segment_total; i ++) {
            final SegmentFormattable    segment = segment_many[i];

            segment.choose(builder, depth, v, w);
        }
    }


    @Override
    public final void                   augment(
            final Gem_StringBuilder             builder,
            /*:*/ int                           depth,
            final Object                        v,
            final Object                        w,
            final Object                        x//,
        )
    {
        if (this.expected != 3) {
            RUNTIME("3 arguments given (expected {})", this.expected);
        }

        final SegmentFormattable[]      segment_many = this.segment_many;

        final int                       segment_total = segment_many.length;

        depth += 1;

        for (/*:*/ int                  i       = 0; i < segment_total; i ++) {
            final SegmentFormattable    segment = segment_many[i];

            segment.choose(builder, depth, v, w, x);
        }
    }


    @Override
    public final void                   augment(
            final Gem_StringBuilder             builder,
            /*:*/ int                           depth,
            final Object                        v,
            final Object                        w,
            final Object                        x,
            final Object                        y//,
        )
    {
        if (this.expected != 4) {
            RUNTIME("4 arguments given (expected {})", this.expected);
        }

        final SegmentFormattable[]      segment_many = this.segment_many;

        final int                       segment_total = segment_many.length;

        depth += 1;

        for (/*:*/ int                  i       = 0; i < segment_total; i ++) {
            final SegmentFormattable    segment = segment_many[i];

            segment.choose(builder, depth, v, w, x, y);
        }
    }


    @Override
    public final void                   augment(
            final Gem_StringBuilder             builder,
            /*:*/ int                           depth,
            final Object                        v,
            final Object                        w,
            final Object                        x,
            final Object                        y4,
            final Object                        y5//,
        )
    {
        if (this.expected != 5) {
            RUNTIME("5 arguments given (expected {})", this.expected);
        }

        final SegmentFormattable[]      segment_many = this.segment_many;

        final int                       segment_total = segment_many.length;

        depth += 1;

        for (/*:*/ int                  i       = 0; i < segment_total; i ++) {
            final SegmentFormattable    segment = segment_many[i];

            segment.choose(builder, depth, v, w, x, y4, y5);
        }
    }


    @Override
    public final void                   augment(
            final Gem_StringBuilder             builder,
            /*:*/ int                           depth,
            final Object                        v,
            final Object                        w,
            final Object                        x,
            final Object                        y4,
            final Object                        y5,
            final Object                        y6//,
        )
    {
        if (this.expected != 6) {
            RUNTIME("6 arguments given (expected {})", this.expected);
        }

        final SegmentFormattable[]      segment_many = this.segment_many;

        final int                       segment_total = segment_many.length;

        depth += 1;

        for (/*:*/ int                  i       = 0; i < segment_total; i ++) {
            final SegmentFormattable    segment = segment_many[i];

            segment.choose(builder, depth, v, w, x, y4, y5, y6);
        }
    }


    @Override
    public final void                   augment(
            final Gem_StringBuilder             builder,
            /*:*/ int                           depth,
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
        final int                       actual = 7 + other_arguments.length;

        if (this.expected != actual) {
            RUNTIME("{} arguments given (expected {})", actual, this.expected);
        }

        final SegmentFormattable[]      segment_many = this.segment_many;

        final int                       segment_total = segment_many.length;

        depth += 1;

        for (/*:*/ int                  i       = 0; i < segment_total; i ++) {
            final SegmentFormattable    segment = segment_many[i];

            segment.choose(builder, depth, v, w, x, y4, y5, y6, y7, other_arguments);
        }
    }


    @Override
    public final void                   augment_1_plus(
            final Gem_StringBuilder             builder,
            /*:*/ int                           depth,
            final Object                        v,
            final Object ...                    other_arguments//,
        )
    {
        final int                       total_other_arguments = other_arguments.length;

        final int                       actual = 1 + total_other_arguments;

        if (this.expected != actual) {
            RUNTIME("{} argument{} given (expected {})",
                    actual,
                    (actual == 1 ? "" : "s"),
                    this.expected);
        }

        final SegmentFormattable[]      segment_many = this.segment_many;

        final int                       segment_total = segment_many.length;

        depth += 1;

        if (actual == 1) {
            for (/*:*/ int              i = 0; i < segment_total; i ++) {
                final SegmentFormattable    segment = segment_many[i];

                segment.choose(builder, depth, v);
            }

            return;
        }

        final Object                    w = other_arguments[0];

        if (actual == 2) {
            for (/*:*/ int              i = 0; i < segment_total; i ++) {
                final SegmentFormattable    segment = segment_many[i];

                segment.choose(builder, depth, v, w);
            }

            return;
        }

        final Object                    x = other_arguments[1];

        if (actual == 3) {
            for (/*:*/ int              i = 0; i < segment_total; i ++) {
                final SegmentFormattable    segment = segment_many[i];

                segment.choose(builder, depth, v, w, x);
            }

            return;
        }

        final Object                    y4 = other_arguments[2];

        if (actual == 4) {
            for (/*:*/ int              i = 0; i < segment_total; i ++) {
                final SegmentFormattable    segment = segment_many[i];

                segment.choose(builder, depth, v, w, x, y4);
            }

            return;
        }

        final Object                    y5 = other_arguments[3];

        if (actual == 5) {
            for (/*:*/ int              i = 0; i < segment_total; i ++) {
                final SegmentFormattable    segment = segment_many[i];

                segment.choose(builder, depth, v, w, x, y4, y5);
            }

            return;
        }

        final Object                    y6 = other_arguments[4];

        if (actual == 6) {
            for (/*:*/ int              i = 0; i < segment_total; i ++) {
                final SegmentFormattable    segment = segment_many[i];

                segment.choose(builder, depth, v, w, x, y4, y5, y6);
            }

            return;
        }

        final Object                    y7 = other_arguments[5];

        if (actual == 7) {
            for (/*:*/ int              i = 0; i < segment_total; i ++) {
                final SegmentFormattable    segment = segment_many[i];

                segment.choose(builder, depth, v, w, x, y4, y5, y6, y7);
            }

            return;
        }

        final Object[]                  adjusted_arguments = new Object[total_other_arguments - 6];

        for (/*:*/ int                  i = 6; i < total_other_arguments; i ++) {
            adjusted_arguments[i - 6] = other_arguments[i];
        }

        for (/*:*/ int              i = 0; i < segment_total; i ++) {
            final SegmentFormattable    segment = segment_many[i];

            segment.choose(builder, depth, v, w, x, y4, y5, y6, y7, adjusted_arguments);
        }
    }


    @Override
    public final void                   portray(final Gem_StringBuilder builder)
    {
        final int                       expected     = this.expected;
        final SegmentFormattable[]      segment_many = this.segment_many;

        final int                       segment_total = segment_many.length;

        builder.append("<MessageFormatter_Many expected<", expected, "> total<", segment_total, ">;");

        for (/*:*/ int                  i       = 0; i < segment_total; i ++) {
            final SegmentFormattable    segment = segment_many[i];

            builder.append(" ");
            builder.portray(segment);
        }

        builder.append(">");
    }
}
