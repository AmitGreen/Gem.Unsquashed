//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Interface;


import java.lang.Object;
import java.lang.String;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Inspection.Inspection;


//
//  TODO: Make this extends Inspectable
//
public interface    MessageFormattable<INSPECTION extends Inspection>
    extends         Inspectable       <INSPECTION>//,
{
    //
    //  Interface Inspectable
    //
    public INSPECTION                   inspect();
    public void                         portray(Gem_StringBuilder builder);


    //
    //  Interface <me>
    //
    String                              augment(int depth);
    String                              augment(int depth, Object v);

    void                                augment(Gem_StringBuilder builder, int depth);
    void                                augment(Gem_StringBuilder builder, int depth, Object v);
    void                                augment(Gem_StringBuilder builder, int depth, Object v, Object w);
    void                                augment(Gem_StringBuilder builder, int depth, Object v, Object w, Object x);

    void                                augment(
            Gem_StringBuilder                   builder,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y//,
        );

    void                                augment(
            Gem_StringBuilder                   builder,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5//,
        );

    void                                augment(
            Gem_StringBuilder                   builder,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5,
            Object                              y6//,
        );

    void                                augment(
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
