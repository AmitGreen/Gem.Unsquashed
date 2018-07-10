//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Interface;


import java.lang.String;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Format.SegmentFormatter_Inspection;
import link.crystal.Gem.Interface.Inspectable;


public interface    SegmentFormattable<INSPECTION extends SegmentFormatter_Inspection>
    extends         MessageFormattable,
                    Inspectable       <INSPECTION>//,
{
    //
    //  Interface Inspectable
    //
    @Override
    public INSPECTION                   inspect();                      //  NOTE: Different `INSPECTION`

    public void                         portray(Gem_StringBuilder builder);


    //
    //  Interface MessageFormattable
    //
    //
    //  TODO: Copy versions here
    //

    //
    //  Interface <me>
    //
    void                                choose(Gem_StringBuilder builder, int depth);
    void                                choose(Gem_StringBuilder builder, int depth, Object v);
    void                                choose(Gem_StringBuilder builder, int depth, Object v, Object w);
    void                                choose(Gem_StringBuilder builder, int depth, Object v, Object w, Object x);

    void                                choose(
            Gem_StringBuilder                   builder,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y//,
        );

    void                                choose(
            Gem_StringBuilder                   builder,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5//,
        );

    void                                choose(
            Gem_StringBuilder                   builder,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5,
            Object                              y6//,
        );

    void                                choose(
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
        );
}
