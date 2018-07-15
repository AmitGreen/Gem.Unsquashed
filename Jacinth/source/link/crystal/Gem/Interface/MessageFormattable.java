//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Interface;


import java.lang.Object;
import java.lang.String;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Inspection.Inspection;


public interface    MessageFormattable<INSPECTION extends Inspection>
    extends         Inspectable       <INSPECTION>//,
{
    //
    //  Interface Inspectable
    //
    public INSPECTION                   inspect();
    public void                         portray(final Gem_StringBuilder builder);


    //
    //  Interface <me>
    //
    String                              augment(final int depth);
    String                              augment(final int depth, final Object v);

    void                                augment(final Gem_StringBuilder builder, final int depth);
    void                                augment(final Gem_StringBuilder builder, final int depth, final Object v);

    void                                augment(
            final Gem_StringBuilder             builder,
            final int                           depth,
            final Object                        v,
            final Object                        w//,
        );

    void                                augment(
            final Gem_StringBuilder             builder,
            final int                           depth,
            final Object                        v,
            final Object                        w,
            final Object                        x//,
        );

    void                                augment(
            final Gem_StringBuilder             builder,
            final int                           depth,
            final Object                        v,
            final Object                        w,
            final Object                        x,
            final Object                        y//,
        );

    void                                augment(
            final Gem_StringBuilder             builder,
            final int                           depth,
            final Object                        v,
            final Object                        w,
            final Object                        x,
            final Object                        y4,
            final Object                        y5//,
        );

    void                                augment(
            final Gem_StringBuilder             builder,
            final int                           depth,
            final Object                        v,
            final Object                        w,
            final Object                        x,
            final Object                        y4,
            final Object                        y5,
            final Object                        y6//,
        );

    void                                augment(
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
        );
}
