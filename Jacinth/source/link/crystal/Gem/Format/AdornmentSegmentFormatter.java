//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.String;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Format.MessageFormatter_Base;
import link.crystal.Gem.Format.SegmentFormatter_Inspection;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Interface.SegmentFormattable;
import link.crystal.Gem.Support.Storehouse_AdornmentSegmentFormatter;


public final class  AdornmentSegmentFormatter
    extends         MessageFormatter_Base<SegmentFormatter_Inspection>
//  extends         Gem_Object           <SegmentFormatter_Inspection>
//  extends         Object
    implements      MessageFormattable   <SegmentFormatter_Inspection>,
                    SegmentFormattable   <SegmentFormatter_Inspection>,
                    Inspectable          <SegmentFormatter_Inspection>//,
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
    private                             AdornmentSegmentFormatter(final String s)
    {
        this.s = s;
    }


    public static final AdornmentSegmentFormatter   create__ALLY__Zone(final Zone z, final String s)
    {
        final String                    interned_s = z.intern_permenant_string(s);

        return new AdornmentSegmentFormatter(interned_s);
    }


    //
    //  Interface Inspectable
    //
    @Override
    public final SegmentFormatter_Inspection    inspect()
    {
        return /*static*/ this.inspection;
    }


    //
    //  Interface MessageFormattable
    //
    @Override
    public final String                 augment(final int depth)
    {
        return this.s;
    }


    @Override
    public final void                   augment(final Gem_StringBuilder builder, final int depth)
    {
        builder.append(this.s);
    }


    //
    //  Interface SegmentFormattable
    //
    @Override
    public final void                   choose(final Gem_StringBuilder builder, final int depth)
    {
        builder.append(this.s);
    }


    @Override
    public final void                   choose(final Gem_StringBuilder builder, final int depth, final Object v)
    {
        builder.append(this.s);
    }


    @Override
    public final void                   choose(
            final Gem_StringBuilder             builder,
            final int                           depth,
            final Object                        v,
            final Object                        w//,
        )
    {
        builder.append(this.s);
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
        builder.append(this.s);
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
        builder.append(this.s);
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
        builder.append(this.s);
    }


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
        builder.append(this.s);
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
        builder.append(this.s);
    }


    @Override
    public final void                   portray(final Gem_StringBuilder builder)
    {
        builder.append("<AdornmentSegmentFormatter ");
        builder.quote(this.s);
        builder.append(">");
    }


    //
    //  Public
    //
    public final String                 s()
    {
        return this.s;
    }
}
