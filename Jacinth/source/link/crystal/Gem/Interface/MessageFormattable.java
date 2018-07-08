//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Interface;


import java.lang.Object;
import java.lang.String;
import link.crystal.Gem.Core.Gem_StringBuilder;


public interface   MessageFormattable
{
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

    void                                portray(Gem_StringBuilder builder);
}
