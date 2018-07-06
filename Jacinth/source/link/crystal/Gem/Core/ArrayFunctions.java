//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.lang.Integer;
import java.lang.Object;
import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Zone;


public abstract class   ArrayFunctions
    extends             Gem_Object//<Inspection>
//  extends             Object
{
    //
    //  Public Static
    //
    public static<T> T[]                shrink_array(
            Zone                                z,
            T[]                                 previous,
            int                                 previous_total,
            T[]                                 current,
            int                                 new_total//,
        )
    {
        assert fact_pointer(previous,                   "previous");
        assert fact        (1 < previous_total,         "1 < previous_total");
        assert fact_pointer(current,                    "current");
        assert fact        (1 < new_total,              "1 < new_total");
        assert fact        (new_total < previous_total, "new_total < previous_total");

        for (int                        i = 0; i < new_total; i ++) {
            current[i] = previous[i];
        }

        return current;
    }


    public static<T> T[]                grow_array(
            Zone                                z,
            T[]                                 previous,
            int                                 previous_total,
            T[]                                 current,
            int                                 new_total//,
        )
    {
        if (previous_total == 0) {
            assert fact_null(previous, "previous");
        } else {
            assert fact_pointer(previous,           "previous");
            assert fact        (1 < previous_total, "1 < previous_total");
        }

        assert fact_pointer(current,                    "current");
        assert fact        (1 < new_total,              "1 < new_total");
        assert fact        (previous_total < new_total, "previous_total < new_total");

        for (int                    i = 0; i < previous_total; i ++) {
            current[i] = previous[i];
        }

        return current;
    }


    public static int[]                 grow_primitive_integer_array(
            Zone                                z,
            int[]                               previous,
            int                                 previous_total,
            int[]                               current,
            int                                 new_total//,
        )
    {
        if (previous_total == 0) {
            assert fact_null(previous, "previous");
        } else {
            assert fact_pointer(previous,           "previous");
            assert fact        (1 < previous_total, "1 < previous_total");
        }

        assert fact_pointer(current,                    "current");
        assert fact        (1 < new_total,              "1 < new_total");
        assert fact        (previous_total < new_total, "previous_total < new_total");

        for (int                    i = 0; i < previous_total; i ++) {
            current[i] = previous[i];
        }

        return current;
    }
}
