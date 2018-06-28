//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Inspection.Inspection;


public abstract class   MessageFormatter_Base<INSPECTION extends Inspection>
    extends             Gem_Object           <INSPECTION>
//  extends             Object
    implements          MessageFormattable   <INSPECTION>,
                        Inspectable          <INSPECTION>//,
{
    //
    //  Interface MessageFormattable
    //
    @Override
    public /*overrideable*/ String      augment(final int depth)
    {
        final Zone                      z = Zone.current_zone();

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

        this.augment(builder, depth + 1);

        return builder.finish_AND_recycle();
    }


    @Override
    public /*overrideable*/ String      augment(final int depth, final Object v)
    {
        final Zone                      z = Zone.current_zone();

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

        this.augment(builder, depth + 1, v);

        return builder.finish_AND_recycle();
    }


    @Override
    public /*overrideable*/ void        augment(final Gem_StringBuilder builder, int depth)
    {
        final INSPECTION                inspection = this.inspect();

        RUNTIME("invalid routine (derived class: {})", inspection.simple_class_name);
    }


    @Override
    public /*overrideable*/ void        augment(final Gem_StringBuilder builder, int depth, final Object v)
    {
        final INSPECTION                inspection = this.inspect();

        RUNTIME("invalid routine (derived class: {})", inspection.simple_class_name);
    }


    @Override
    public /*overrideable*/ void        augment(
            final Gem_StringBuilder             builder,
            final int                           depth,
            final Object                        v,
            final Object                        w//,
        )
    {
        INVALID_ROUTINE();
    }


    @Override
    public /*overrideable*/ void        augment(
            final Gem_StringBuilder             builder,
            final int                           depth,
            final Object                        v,
            final Object                        w,
            final Object                        x//,
        )
    {
        INVALID_ROUTINE();
    }


    @Override
    public /*overrideable*/ void        augment(
            final Gem_StringBuilder             builder,
            final int                           depth,
            final Object                        v,
            final Object                        w,
            final Object                        x,
            final Object                        y//,
        )
    {
        INVALID_ROUTINE();
    }


    @Override
    public /*overrideable*/ void        augment(
            final Gem_StringBuilder             builder,
            final int                           depth,
            final Object                        v,
            final Object                        w,
            final Object                        x,
            final Object                        y4,
            final Object                        y5//,
        )
    {
        INVALID_ROUTINE();
    }


    @Override
    public /*overrideable*/ void        augment(
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
        INVALID_ROUTINE();
    }


    @Override
    public /*overrideable*/ void        augment(
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
        INVALID_ROUTINE();
    }


    @Override
    public /*overrideable*/ void        augment_1_plus(
            final Gem_StringBuilder             builder,
            final int                           depth,
            final Object                        v,
            final Object ...                    other_arguments//,
        )
    {
        INVALID_ROUTINE();
    }
}
