//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.lang.Integer;
import java.lang.Object;
import java.lang.RuntimeException;
import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;


public abstract class   ArrayFunctions
    extends             Gem_Object//<Inspection>
//  extends             Object
{
    //
    //  Public Static
    //
    public static<T> T[]                shrink_array(T[] previous, int previous_total, T[] current, int new_total)
    {
        if (previous_total < 1) {
            throw new RuntimeException("ArrayFunctions.grow_array: previous_total < 1 (actual: " + portray(previous_total) + ")");
        }

        if (previous_total < new_total) {
            throw new RuntimeException(
                    (
                          "ArrayFunctions.grow_array: previous_total<"
                        + portray(previous_total)
                        + "> < new_total<"
                        + portray(new_total)
                    )
                );
        }

        for (int                        i = 0; i < new_total; i ++) {
            current[i] = previous[i];
        }

        return current;
    }


    public static<T> T[]                grow_array(T[] previous, int previous_total, T[] current, int new_total)
    {
        if (previous_total == 0) {
            if (previous != null) {
                throw new RuntimeException("ArrayFunctions.grow_array: previous_total == 0 && previous != null");
            }
        } else {
            if (previous_total < 0) {
                throw new RuntimeException("ArrayFunctions.grow_array: previous_total < 0 (actual: " + portray(previous_total) + ")");
            }

            if (previous_total >= new_total) {
                throw new RuntimeException(
                        (
                              "ArrayFunctions.grow_array: previous_total<"
                            + portray(previous_total)
                            + "> >= new_total<"
                            + portray(new_total)
                        )
                    );
            }
        }

        if (previous_total > 0) {
            for (int                    i = 0; i < previous_total; i ++) {
                current[i] = previous[i];
            }
        }

        return current;
    }
}
