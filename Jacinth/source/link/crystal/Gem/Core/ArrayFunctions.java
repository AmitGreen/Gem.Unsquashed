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
        if (previous_total == 0) {
            if (previous != null) {
                z.RAISE_runtime_exception("ArrayFunctions.shrink_array: previous_total == 0 && previous != null");
            }
        } else {
            if (previous_total < 1) {
                z.RAISE_runtime_exception("ArrayFunctions.shrink_array: previous_total < 1 (actual: {0})",
                                          previous_total);
            }

            if (previous_total <= new_total) {
                z.RAISE_runtime_exception("ArrayFunctions.shrink_array: previous_total<{0}> <= new_total<{1}>",
                                          previous_total,
                                          new_total);
            }
        }

        if (previous_total < new_total) {
            z.RAISE_runtime_exception("ArrayFunctions.shrink_array: previous_total<{0}> < new_total<{1}>",
                                      previous_total,
                                      new_total);
        }

        if (current == null) {
            z.RAISE_runtime_exception("ArrayFunctions.shrink_array: `current` == null");
        }

        if (new_total <= 0) {
            z.RAISE_runtime_exception("ArrayFunctions.shrink_array: `new_total`<{0}>", previous_total);
        }

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
            if (previous != null) {
                z.RAISE_runtime_exception("ArrayFunctions.grow_array: previous_total == 0 && previous != null");
            }
        } else {
            if (previous_total < 0) {
                z.RAISE_runtime_exception("ArrayFunctions.grow_array: previous_total < 0 (actual: {0})", previous_total);
            }

            if (previous_total >= new_total) {
                z.RAISE_runtime_exception("ArrayFunctions.grow_array: previous_total<{0}> >= new_total<{1}>",
                                        previous_total,
                                        new_total);
            }
        }

        if (current == null) {
            z.RAISE_runtime_exception("ArrayFunctions.grow_array: `current` == null");
        }

        if (new_total <= 0) {
            z.RAISE_runtime_exception("ArrayFunctions.grow_array: `new_total`<{0}>", previous_total);
        }

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
            if (previous != null) {
                z.RAISE_runtime_exception(
                        "ArrayFunctions.grow_primitive_integer_array: `previous_total`<0> && `previous` != null"//,
                    );
            }
        } else {
            if (previous_total < 0) {
                z.RAISE_runtime_exception("ArrayFunctions.grow_primitive_integer_array: `previous_total`<{0}> < 0",
                                          previous_total);
            }

            if (previous_total >= new_total) {
                z.RAISE_runtime_exception("{0} `previous_total`<{1}> >= `new_total`<{2}>",
                                          "ArrayFunctions.grow_primitive_integer_array",
                                          previous_total,
                                          new_total);
            }
        }

        if (current == null) {
            z.RAISE_runtime_exception("ArrayFunctions.grow_primitive_integer_array: `current` == null");
        }

        if (new_total <= 0) {
            z.RAISE_runtime_exception("ArrayFunctions.grow_primitive_integer_array: `new_total`<{0}> <= 0",
                                    previous_total);
        }

        for (int                    i = 0; i < previous_total; i ++) {
            current[i] = previous[i];
        }

        return current;
    }
}
