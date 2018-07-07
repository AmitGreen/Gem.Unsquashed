//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.io.PrintStream;
import java.lang.System;
import java.util.HashMap;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Exception.ExceptionFunctions;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Support.Storehouse_MessageFormattable;
import link.crystal.Gem.World.Inspection;


public abstract class   Gem_Map     <INSPECTION extends Inspection, K, V>
    extends             HashMap                                    <K, V>
//  extends             AbstractHashMap                            <K, V>
//  extends             Object
    implements          Inspectable<INSPECTION>//,
{
    //
    //  Public static
    //
    public static final PrintStream     standard_output = System.out;


    //
    //  Members
    //
    protected final Zone                z;


    //
    //  Constructor
    //
    protected                           Gem_Map(Zone z, int initial_capacity)
    {
        super(initial_capacity);

        this.z = z;
    }


    //
    //  Interface Inspectable
    //
    public abstract INSPECTION          inspect();
    public abstract void                portray(Gem_StringBuilder builder);


    //
    //  Abstract
    //
    public abstract void                dump(String name);


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

        final Zone                      z = Zone.current_zone();

        ExceptionFunctions.ASSERT(2, "`{}` is null", name);

        return false;
    }


    //
    //  Public (ERRORS)
    //
    public void                         RUNTIME(String error_message, Object ... arguments)
    {
        ExceptionFunctions.RUNTIME(2, error_message, arguments);
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

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

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
    public V                            lookup(K k)
    {
        return this.get(k);
    }


    public void                         insert(Zone z, K k, V v)
    {
        assert fact(this.z == z, "this.z == z");

        final V                         previous = this.putIfAbsent(k, v);

        if (previous != null) {
            RUNTIME("previous value for {} already exists: {}", k, v);
        }
    }


    public static void                  output(String s)
    {
        standard_output.println(s);
    }
}
