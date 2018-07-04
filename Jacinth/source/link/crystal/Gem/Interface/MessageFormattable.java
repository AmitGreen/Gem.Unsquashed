//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Interface;


import java.lang.Object;
import java.lang.String;
import link.crystal.Gem.Core.Zone;


public interface   MessageFormattable
{
    String                              arrange(Zone z, int depth, Object v);
    String                              arrange(Zone z, int depth, Object v, Object w);
    String                              arrange(Zone z, int depth, Object v, Object w, Object x);
    String                              arrange(Zone z, int depth, Object v, Object w, Object x, Object y);
    String                              arrange(Zone z, int depth, Object v, Object w, Object x, Object y4, Object y5);

    String                              arrange(
            Zone                                z,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5,
            Object                              y6//,
        );

    String                              arrange(
            Zone                                z,
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

    void                                line(Zone z, int depth, Object v);
    void                                line(Zone z, int depth, Object v, Object w);
    void                                line(Zone z, int depth, Object v, Object w, Object x);
    void                                line(Zone z, int depth, Object v, Object w, Object x, Object y);
    void                                line(Zone z, int depth, Object v, Object w, Object x, Object y4, Object y5);

    void                                line(
            Zone                                z,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5,
            Object                              y6//,
        );

    void                                line(
            Zone                                z,
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
