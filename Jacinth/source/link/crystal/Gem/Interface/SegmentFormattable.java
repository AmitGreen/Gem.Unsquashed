//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Interface;


import java.lang.String;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;


public interface   SegmentFormattable
{
    String                              portray (Zone z);
    void                                select_1(Gem_StringBuilder builder, Object a);
    void                                select_2(Gem_StringBuilder builder, Object a, Object b);
    void                                select_3(Gem_StringBuilder builder, Object a, Object b, Object c);
    void                                select_4(Gem_StringBuilder builder, Object a, Object b, Object c, Object d);

    void                                select_5(
            Gem_StringBuilder                   builder,
            Object                              a,
            Object                              b,
            Object                              c,
            Object                              d,
            Object                              e//,
        );

    void                                select_many(
            Gem_StringBuilder                   builder,
            Object                              a,
            Object                              b,
            Object                              c,
            Object                              d,
            Object                              e,
            Object ...                          other_arguments//,
        );
}
