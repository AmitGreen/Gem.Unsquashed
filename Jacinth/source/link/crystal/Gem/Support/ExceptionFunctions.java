//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.RuntimeException;
import java.lang.Object;
import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
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
    public static void                  RUNTIME(Zone z, String format)
    {
        MessageFormattable              formattable = Storehouse_MessageFormattable.lookup(z, format);

        if (formattable == null) {
            formattable = ParseFormat.parse_format(z, format);

            Storehouse_MessageFormattable.insert(z, format, formattable);
        }

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        formattable.arrange(builder, 2);

        String                      error_message = builder.finish__AND__recycle();

        throw new RuntimeException(error_message);
    }


    public static void                  RUNTIME(Zone z, String format, Object v, Object ... other_arguments)
    {
        MessageFormattable              formattable = Storehouse_MessageFormattable.lookup(z, format);

        if (formattable == null) {
            formattable = ParseFormat.parse_format(z, format);

            Storehouse_MessageFormattable.insert(z, format, formattable);
        }

        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        int                             other_arguments_total = other_arguments.length;

        if (other_arguments_total == 0) {
            formattable.arrange(builder, 2, v);

            String                      error_message = builder.finish__AND__recycle();

            throw new RuntimeException(error_message);
        }

        Object                          w = other_arguments[0];

        if (other_arguments_total == 1) {
            formattable.arrange(builder, 2, v, w);

            String                      error_message = builder.finish__AND__recycle();

            throw new RuntimeException(error_message);
        }

        Object                          x = other_arguments[1];

        if (other_arguments_total == 2) {
            formattable.arrange(builder, 2, v, w, x);

            String                      error_message = builder.finish__AND__recycle();

            throw new RuntimeException(error_message);
        }

        Object                          y4 = other_arguments[2];

        if (other_arguments_total == 3) {
            formattable.arrange(builder, 2, v, w, x, y4);

            String                      error_message = builder.finish__AND__recycle();

            throw new RuntimeException(error_message);
        }

        Object                          y5 = other_arguments[3];

        if (other_arguments_total == 4) {
            formattable.arrange(builder, 2, v, w, x, y4, y5);

            String                      error_message = builder.finish__AND__recycle();

            throw new RuntimeException(error_message);
        }

        Object                          y6 = other_arguments[4];

        if (other_arguments_total == 5) {
            formattable.arrange(builder, 2, v, w, x, y4, y5, y6);

            String                      error_message = builder.finish__AND__recycle();

            throw new RuntimeException(error_message);
        }

        Object                          y7             = other_arguments[5];
        Object []                       adjusted       = null;
        int                             adjusted_total = other_arguments_total - 5;

        if (adjusted_total > 0) {
            adjusted = new Object[adjusted_total];

            for (int                    i = 0; i < adjusted_total; i ++) {
                adjusted[i] = other_arguments[i + 5];
            }
        }

        formattable.arrange(builder, 2, v, w, x, y4, y5, y6, y7, adjusted);

        String                          error_message = builder.finish__AND__recycle();

        throw new RuntimeException(error_message);
    }
}
