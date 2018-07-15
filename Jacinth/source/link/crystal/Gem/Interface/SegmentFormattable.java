//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Interface;


import java.lang.String;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Format.SegmentFormatter_Inspection;
import link.crystal.Gem.Interface.Inspectable;


public interface    SegmentFormattable<INSPECTION extends SegmentFormatter_Inspection>
    extends         MessageFormattable<INSPECTION>,
                    Inspectable       <INSPECTION>//,
{
    //
    //  Interface Inspectable
    //
    @Override
    public INSPECTION                   inspect();                      //  NOTE: Different `INSPECTION`

    public void                         portray(final Gem_StringBuilder builder);


    //
    //  Interface MessageFormattable
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


    //
    //  Interface <me>
    //
    void                                choose(final Gem_StringBuilder builder, final int depth);
    void                                choose(final Gem_StringBuilder builder, final int depth, final Object v);

    void                                choose(
            final Gem_StringBuilder             builder,
            final int                           depth,
            final Object                        v,
            final Object                        w//,
        );

    void                                choose(
            final Gem_StringBuilder             builder,
            final int                           depth,
            final Object                        v,
            final Object                        w,
            final Object                        x//,
        );

    void                                choose(
            final Gem_StringBuilder             builder,
            final int                           depth,
            final Object                        v,
            final Object                        w,
            final Object                        x,
            final Object                        y//,
        );

    void                                choose(
            final Gem_StringBuilder             builder,
            final int                           depth,
            final Object                        v,
            final Object                        w,
            final Object                        x,
            final Object                        y4,
            final Object                        y5//,
        );

    void                                choose(
            final Gem_StringBuilder             builder,
            final int                           depth,
            final Object                        v,
            final Object                        w,
            final Object                        x,
            final Object                        y4,
            final Object                        y5,
            final Object                        y6//,
        );

    void                                choose(
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
