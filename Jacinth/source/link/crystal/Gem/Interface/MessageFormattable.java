//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Interface;


import java.lang.Object;
import java.lang.String;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;


public interface   MessageFormattable
{
    void                                arrange(Gem_StringBuilder builder, int depth);
    void                                arrange(Gem_StringBuilder builder, int depth, Object v);
    void                                arrange(Gem_StringBuilder builder, int depth, Object v, Object w);
    void                                arrange(Gem_StringBuilder builder, int depth, Object v, Object w, Object x);

    void                                arrange(
            Gem_StringBuilder                   builder,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y//,
        );

    void                                arrange(
            Gem_StringBuilder                   builder,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5//,
        );

    void                                arrange(
            Gem_StringBuilder                   builder,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5,
            Object                              y6//,
        );

    void                                arrange(
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

    String                              portray(Zone z);
}
