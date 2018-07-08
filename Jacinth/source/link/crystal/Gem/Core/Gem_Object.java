//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.io.PrintStream;
import java.lang.Class;
import java.lang.Integer;
import java.lang.Object;
import java.lang.String;
import java.lang.System;
import java.lang.System;
import java.lang.Thread;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Exception.ExceptionFunctions;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Support.Storehouse_MessageFormattable;
import link.crystal.Gem.Support.Storehouse_String;
import link.crystal.Gem.World.Inspection;


public abstract class   Gem_Object <INSPECTION extends Inspection>
    extends             Object
    implements          Inspectable<INSPECTION>//,
{
    //
    //  Public static
    //
    public static final PrintStream     standard_output = System.out;


    //
    //  Interface Inspectable
    //
    public abstract INSPECTION          inspect();


    public void                         portray(Gem_StringBuilder builder)
    {
        final INSPECTION                inspection = this.inspect();

        builder.append("<", inspection.simple_class_name, ">");
    }


    //
    //  Public (ASSERT)
    //
    public static boolean               fact(boolean condition, String format)
    {
        if (condition) {
            return true;
        }

        ExceptionFunctions.ASSERTION_FAILED(2, "assertion failed: {}", format);

        return false;
    }


    public static boolean               fact_between(int start, int v, int end)
    {
        if (start <= v && v <= end) {
            return true;
        }

        ExceptionFunctions.ASSERT(2, "{} is not between {} and {}", v, start, end);

        return false;
    }


    public static boolean               fact_null(Object p, String name)
    {
        if (p == null) {
            return true;
        }

        ExceptionFunctions.ASSERT(2, "`{}` is not null", name);

        return false;
    }


    public static boolean               fact_pointer(Object p, String name)
    {
        if (p != null) {
            return true;
        }

        ExceptionFunctions.ASSERT(2, "`{}` is null", name);

        return false;
    }


    //
    //  Public (ERRORS)
    //
    public void                         INVALID_ROUTINE()
    {
        ExceptionFunctions.RUNTIME(2, "invalid routine");
    }


    public void                         RUNTIME(String error_message, Object ... arguments)
    {
        ExceptionFunctions.RUNTIME(2, error_message, arguments);
    }


    //
    //  Public (arrange)
    //
    public String                       arrange(String format)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable        formattable = Storehouse_MessageFormattable.conjure(z, format);

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

        formattable.arrange(builder, 2);

        return builder.finish_AND_recycle();
    }


    public String                       arrange(String format, Object v)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable        formattable = Storehouse_MessageFormattable.conjure(z, format);

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

        formattable.arrange(builder, 2, v);

        return builder.finish_AND_recycle();
    }


    public String                       arrange(String format, Object v, Object w)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable        formattable = Storehouse_MessageFormattable.conjure(z, format);

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

        formattable.arrange(builder, 2, v, w);

        return builder.finish_AND_recycle();
    }


    public String                       arrange(String format, Object v, Object w, Object x)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable        formattable = Storehouse_MessageFormattable.conjure(z, format);

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

        formattable.arrange(builder, 2, v, w, x);

        return builder.finish_AND_recycle();
    }


    public String                       arrange(
            String                              format,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y//
        )
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable        formattable = Storehouse_MessageFormattable.conjure(z, format);

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

        formattable.arrange(builder, 2, v, w, x, y);

        return builder.finish_AND_recycle();
    }


    public String                       arrange(
            String                              format,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5//,
        )
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable        formattable = Storehouse_MessageFormattable.conjure(z, format);

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

        formattable.arrange(builder, 2, v, w, x, y4, y5);

        return builder.finish_AND_recycle();
    }


    public String                       arrange(
            String                              format,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5,
            Object                              y6//,
        )
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable        formattable = Storehouse_MessageFormattable.conjure(z, format);

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

        formattable.arrange(builder, 2, v, w, x, y4, y5, y6);

        return builder.finish_AND_recycle();
    }


    public String                       arrange(
            String                              format,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5,
            Object                              y6,
            Object                              y7,
            Object ...                          other_arguments//,
        )
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable        formattable = Storehouse_MessageFormattable.conjure(z, format);

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

        formattable.arrange(builder, 2, v, w, x, y4, y5, y6, y7, other_arguments);

        return builder.finish_AND_recycle();
    }


    //
    //  Public (line)
    //
    public void                         line()
    {
        standard_output.println();
    }


    public void                         line(String format)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable        formattable = Storehouse_MessageFormattable.conjure(z, format);

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

        formattable.arrange(builder, 2);

        standard_output.println(builder.finish_AND_recycle());
    }


    public void                         line(String format, Object v)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable        formattable = Storehouse_MessageFormattable.conjure(z, format);

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

        formattable.arrange(builder, 2, v);

        standard_output.println(builder.finish_AND_recycle());
    }


    public void                         line(String format, Object v, Object w)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable        formattable = Storehouse_MessageFormattable.conjure(z, format);

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

        formattable.arrange(builder, 2, v, w);

        standard_output.println(builder.finish_AND_recycle());
    }


    public void                         line(String format, Object v, Object w, Object x)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable        formattable = Storehouse_MessageFormattable.conjure(z, format);

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

        formattable.arrange(builder, 2, v, w, x);

        standard_output.println(builder.finish_AND_recycle());
    }


    public void                         line(String format, Object v, Object w, Object x, Object y)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable        formattable = Storehouse_MessageFormattable.conjure(z, format);

        Gem_StringBuilder               builder = z.summon_StringBuilder();

        formattable.arrange(builder, 2, v, w, x, y);

        standard_output.println(builder.finish_AND_recycle());
    }


    public void                         line(String format, Object v, Object w, Object x, Object y4, Object y5)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable        formattable = Storehouse_MessageFormattable.conjure(z, format);

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

        formattable.arrange(builder, 2, v, w, x, y4, y5);

        standard_output.println(builder.finish_AND_recycle());
    }


    public void                         line(
            String                              format,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5,
            Object                              y6//,
        )
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable        formattable = Storehouse_MessageFormattable.conjure(z, format);

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

        formattable.arrange(builder, 2, v, w, x, y4, y5, y6);

        standard_output.println(builder.finish_AND_recycle());
    }


    public void                         line(
            String                              format,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5,
            Object                              y6,
            Object                              y7,
            Object ...                          other_arguments//,
        )
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable        formattable = Storehouse_MessageFormattable.conjure(z, format);

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

        formattable.arrange(builder, 2, v, w, x, y4, y5, y6, y7, other_arguments);

        standard_output.println(builder.finish_AND_recycle());
    }


    //
    //  Public (other)
    //
    public static int                   limit_to_between(int minimum, int v, int maximum)
    {
        if (v < minimum) {
            return minimum;
        }

        if (v > maximum) {
            return maximum;
        }

        return v;
    }


    public static void                  output(String s)
    {
        standard_output.println(s);
    }
}
