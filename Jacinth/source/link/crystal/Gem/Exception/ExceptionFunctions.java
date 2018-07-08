//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Exception;


import java.lang.Object;
import java.lang.RuntimeException;
import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Exception.AssertionError;
import link.crystal.Gem.Format.MethodNameSegmentFormatter;
import link.crystal.Gem.Format.ParseFormat;
import link.crystal.Gem.Interface.MessageFormattable;


public abstract class   ExceptionFunctions
    extends             Gem_Object//<Inspection>
//  extends             Object
{
    //
    //  Private
    //
    private static String               method_name(
            Zone                                z,
            int                                 depth,
            String                              extra,
            String                              format,
            Object ...                          arguments//,
        )
    {
        final MessageFormattable        formattable = ParseFormat.parse_format(z, format);

        depth += 1;

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

        MethodNameSegmentFormatter.method_name(builder, depth);

        builder.append(": ");

        if (extra != null) {
            builder.append(extra);
        }

        final int                       arguments_total = arguments.length;

        if (arguments_total == 0) {
            formattable.augment(builder, depth);

            return builder.finish_AND_recycle();
        }

        final Object                    v = arguments[0];

        if (arguments_total == 1) {
            formattable.augment(builder, depth, v);

            return builder.finish_AND_recycle();
        }

        final Object                    w = arguments[1];

        if (arguments_total == 2) {
            formattable.augment(builder, depth, v, w);

            return builder.finish_AND_recycle();
        }

        final Object                    x = arguments[2];

        if (arguments_total == 3) {
            formattable.augment(builder, depth, v, w, x);

            return builder.finish_AND_recycle();
        }

        final Object                    y4 = arguments[3];

        if (arguments_total == 4) {
            formattable.augment(builder, depth, v, w, x, y4);

            return builder.finish_AND_recycle();
        }

        final Object                    y5 = arguments[4];

        if (arguments_total == 5) {
            formattable.augment(builder, depth, v, w, x, y4, y5);

            return builder.finish_AND_recycle();
        }

        final Object                    y6 = arguments[5];

        if (arguments_total == 6) {
            formattable.augment(builder, depth, v, w, x, y4, y5, y6);

            return builder.finish_AND_recycle();
        }

        final Object                    y7             = arguments[6];
        Object []                       adjusted       = null;
        final int                       adjusted_total = arguments_total - 6;

        if (adjusted_total > 0) {
            adjusted = new Object[adjusted_total];

            for (int                    i = 0; i < adjusted_total; i ++) {
                adjusted[i] = arguments[i + 6];
            }
        }

        formattable.augment(builder, depth, v, w, x, y4, y5, y6, y7, adjusted);

        return builder.finish_AND_recycle();
    }


    //
    //  Public
    //
    public static void                  ASSERT(int depth, String format, Object ... arguments)
    {
        final Zone                      z = Zone.current_zone();

        final String                    error_message = (
                ExceptionFunctions.method_name(z, depth + 1, null, format, arguments)
            );

        final AssertionError            assertion_error = AssertionError.create(z, error_message);

        throw assertion_error;
    }


    public static void                  ASSERTION_FAILED(int depth, String format, Object ... arguments)
    {
        final Zone                      z = Zone.current_zone();

        final String                    error_message = (
                ExceptionFunctions.method_name(z, depth + 1, "assertion failed: ", format, arguments)
            );

        final AssertionError            assertion_error = AssertionError.create(z, error_message);

        throw assertion_error;
    }


    public static void                  RUNTIME(int depth, String format, Object ... arguments)
    {
        final Zone                      z = Zone.current_zone();

        final String                    error_message = (
                ExceptionFunctions.method_name(z, depth + 1, null, format, arguments)
            );

        final RuntimeException          runtime_exception = new RuntimeException(error_message);

        throw runtime_exception;
    }
}
