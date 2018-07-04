//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.RuntimeException;
import java.lang.Object;
import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.ParseFormat;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Support.Storehouse_MessageFormattable;


public abstract class   ExceptionFunctions
    extends             Gem_Object//<Inspection>
//  extends             Object
{
    //
    //  Public
    //
    public static void                  RAISE_runtime_exception(Zone z, String error_message)
    {
        throw new RuntimeException(error_message);
    }


    public static void                  RAISE_runtime_exception(Zone z, String format, Object v)
    {
        MessageFormattable              formattable = Storehouse_MessageFormattable.lookup(z, format);

        if (formattable == null) {
            formattable = ParseFormat.parse_format(z, format);

            Storehouse_MessageFormattable.insert(z, format, formattable);
        }

        String                          error_message = formattable.arrange(z, 2, v);

        throw new RuntimeException(error_message);
    }


    public static void                  RAISE_runtime_exception(Zone z, String format, Object v, Object w)
    {
        MessageFormattable              formattable = Storehouse_MessageFormattable.lookup(z, format);

        if (formattable == null) {
            formattable = ParseFormat.parse_format(z, format);

            Storehouse_MessageFormattable.insert(z, format, formattable);
        }

        String                          error_message = formattable.arrange(z, 2, v, w);

        throw new RuntimeException(error_message);
    }


    public static void                  RAISE_runtime_exception(
            Zone                                z,
            String                              format,
            Object                              v,
            Object                              w,
            Object                              x,
            Object ...                          other_arguments//,
        )
    {
        MessageFormattable              formattable = Storehouse_MessageFormattable.lookup(z, format);

        if (formattable == null) {
            formattable = ParseFormat.parse_format(z, format);

            Storehouse_MessageFormattable.insert(z, format, formattable);
        }

        int                             other_arguments_total = other_arguments.length;

        if (other_arguments_total == 0) {
            String                      error_message = formattable.arrange(z, 2, v, w, x);

            throw new RuntimeException(error_message);
        }

        Object                              y4 = other_arguments[0];

        if (other_arguments_total == 1) {
            String                      error_message = formattable.arrange(z, 2, v, w, x, y4);

            throw new RuntimeException(error_message);
        }

        Object                              y5 = other_arguments[1];

        if (other_arguments_total == 2) {
            String                      error_message = formattable.arrange(z, 2, v, w, x, y4, y5);

            throw new RuntimeException(error_message);
        }

        Object                              y6 = other_arguments[2];

        if (other_arguments_total == 3) {
            String                      error_message = formattable.arrange(z, 2, v, w, x, y4, y5, y6);

            throw new RuntimeException(error_message);
        }

        Object                              y7             = other_arguments[3];
        Object []                           adjusted       = null;
        int                                 adjusted_total = other_arguments_total - 4;

        if (adjusted_total > 0) {
            adjusted = new Object[adjusted_total];

            for (int                            i = 0; i < adjusted_total; i ++) {
                adjusted[i] = other_arguments[i + 4];
            }
        }
            
        String                      error_message = formattable.arrange(z, 2, v, w, x, y4, y5, y6, y7, adjusted);

        throw new RuntimeException(error_message);
    }
}
