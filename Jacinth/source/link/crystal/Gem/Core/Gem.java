//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.io.PrintStream;
import java.lang.Object;
import java.lang.System;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Support.Storehouse_MessageFormattable;


public abstract class   Gem
    extends             Object
{
    //
    //  Public static
    //
    public static final PrintStream     standard_output = System.out;


    //
    //  Static types
    //
    public static final Class<Gem_StringBuilder[]>  Gem_StringBuilder$array$class = Gem_StringBuilder[].class;
    public static final Class<Integer>              Integer$class                 = Integer.class;
    public static final Class<String>               String$class                  = String.class;
    public static final Class<Thread>               Thread$class                  = Thread.class;


    //
    //  Public (arrange)
    //
    public static String                arrange(int depth, String format)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable        formattable = Storehouse_MessageFormattable.conjure(z, format);

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

        formattable.augment(builder, depth + 1);

        return builder.finish_AND_recycle();
    }


    public static String                arrange(int depth, String format, Object v)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable        formattable = Storehouse_MessageFormattable.conjure(z, format);

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

        formattable.augment(builder, depth + 1, v);

        return builder.finish_AND_recycle();
    }


    public static String                arrange(int depth, String format, Object v, Object w)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable        formattable = Storehouse_MessageFormattable.conjure(z, format);

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

        formattable.augment(builder, depth + 1, v, w);

        return builder.finish_AND_recycle();
    }


    public static String                arrange(int depth, String format, Object v, Object w, Object x)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable        formattable = Storehouse_MessageFormattable.conjure(z, format);

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

        formattable.augment(builder, depth + 1, v, w, x);

        return builder.finish_AND_recycle();
    }


    public static String                arrange(
            int                                 depth,
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

        formattable.augment(builder, depth + 1, v, w, x, y);

        return builder.finish_AND_recycle();
    }


    public static String                arrange(
            int                                 depth,
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

        formattable.augment(builder, depth + 1, v, w, x, y4, y5);

        return builder.finish_AND_recycle();
    }


    public static String                arrange(
            int                                 depth,
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

        formattable.augment(builder, depth + 1, v, w, x, y4, y5, y6);

        return builder.finish_AND_recycle();
    }


    public static String                arrange(
            int                                 depth,
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

        formattable.augment(builder, depth + 1, v, w, x, y4, y5, y6, y7, other_arguments);

        return builder.finish_AND_recycle();
    }


    //
    //  Public (line)
    //
    public static void                  line()
    {
        standard_output.println();
    }


    public static void                  line(int depth, String format)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable        formattable = Storehouse_MessageFormattable.conjure(z, format);

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

        formattable.augment(builder, depth + 1);

        standard_output.println(builder.finish_AND_recycle());
    }


    public static void                  line(int depth, String format, Object v)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable        formattable = Storehouse_MessageFormattable.conjure(z, format);

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

        formattable.augment(builder, depth + 1, v);

        standard_output.println(builder.finish_AND_recycle());
    }


    public static void                  line(int depth, String format, Object v, Object w)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable        formattable = Storehouse_MessageFormattable.conjure(z, format);

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

        formattable.augment(builder, depth + 1, v, w);

        standard_output.println(builder.finish_AND_recycle());
    }


    public static void                  line(int depth, String format, Object v, Object w, Object x)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable        formattable = Storehouse_MessageFormattable.conjure(z, format);

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

        formattable.augment(builder, depth + 1, v, w, x);

        standard_output.println(builder.finish_AND_recycle());
    }


    public static void                  line(int depth, String format, Object v, Object w, Object x, Object y)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable        formattable = Storehouse_MessageFormattable.conjure(z, format);

        Gem_StringBuilder               builder = z.summon_StringBuilder();

        formattable.augment(builder, depth + 1, v, w, x, y);

        standard_output.println(builder.finish_AND_recycle());
    }


    public static void                  line(int depth, String format, Object v, Object w, Object x, Object y4, Object y5)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable        formattable = Storehouse_MessageFormattable.conjure(z, format);

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

        formattable.augment(builder, depth + 1, v, w, x, y4, y5);

        standard_output.println(builder.finish_AND_recycle());
    }


    public static void                  line(
            int                                 depth,
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

        formattable.augment(builder, depth + 1, v, w, x, y4, y5, y6);

        standard_output.println(builder.finish_AND_recycle());
    }


    public static void                  line(
            int                                 depth,
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

        formattable.augment(builder, depth + 1, v, w, x, y4, y5, y6, y7, other_arguments);

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
