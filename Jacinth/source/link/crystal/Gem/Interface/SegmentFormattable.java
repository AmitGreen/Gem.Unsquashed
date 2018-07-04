//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Interface;


import java.lang.String;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;


public interface   SegmentFormattable
{
    String                              portray (Zone z);
    void                                choose(Gem_StringBuilder builder, int depth, Object v);
    void                                choose(Gem_StringBuilder builder, Object v, Object w);
    void                                choose(Gem_StringBuilder builder, Object v, Object w, Object x);
    void                                choose(Gem_StringBuilder builder, Object v, Object w, Object x, Object y);

    void                                choose(
            Gem_StringBuilder                   builder,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5//,
        );

    void                                select_many(
            Gem_StringBuilder                   builder,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5,
            Object ...                          other_arguments//,
        );
}
