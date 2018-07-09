//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.io.PrintStream;
import java.lang.Object;
import java.lang.System;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Format.MethodNameSegmentFormatter;
import link.crystal.Gem.Format.ParseFormat;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Support.Gem_ReferenceQueue;
import link.crystal.Gem.Support.World_Integer_Cache;
import link.crystal.Gem.Support.World_Integer_Key;
import link.crystal.Gem.World.World_Integer;
import link.crystal.Gem.Support.World_Integer_WeakReference;


public abstract class   Gem
    extends             Gem_Object//<Inspection>
//  extends             Object
{
    //
    //  Static types
    //
    public static final Class<Gem_StringBuilder[]>  Gem_StringBuilder$array$class = Gem_StringBuilder[].class;
    public static final Class<Integer>              Integer$class                 = Integer.class;
    public static final Class<String>               String$class                  = String.class;
    public static final Class<Thread>               Thread$class                  = Thread.class;


    //
    //  Public static
    //
    public static final PrintStream                 standard_output = System.out;


    //
    //  NOTE:
    //      To avoid class initialization loops all the following CANNOT be initialized here.
    //
    //      Each of the following must be initializated when first used
    //      (i.e.: after other class initializations have run)
    //
    //  HENCE:
    //      None of the following can be declared as `final` either ...
    //
    public static       World_Integer_Cache         integer_cache                  = null;
    public static       World_Integer_Key           integer_key                    = null;
    public static       MethodNameSegmentFormatter  message_name_segment_formatter = null;
    public static       Gem_ReferenceQueue          reference_queue                = null;


    //
    //  Public (arrange)
    //
    public static String                arrange(int depth, String format)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable        formattable = ParseFormat.parse_format(z, format);

        return formattable.augment(depth + 1);
    }


    public static String                arrange(int depth, String format, Object v)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable        formattable = ParseFormat.parse_format(z, format);

        return formattable.augment(depth + 1, v);
    }


    public static String                arrange(int depth, String format, Object v, Object w)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable        formattable = ParseFormat.parse_format(z, format);

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

        formattable.augment(builder, depth + 1, v, w);

        return builder.finish_AND_recycle();
    }


    public static String                arrange(int depth, String format, Object v, Object w, Object x)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable        formattable = ParseFormat.parse_format(z, format);

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

        final MessageFormattable        formattable = ParseFormat.parse_format(z, format);

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

        final MessageFormattable        formattable = ParseFormat.parse_format(z, format);

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

        final MessageFormattable        formattable = ParseFormat.parse_format(z, format);

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

        final MessageFormattable        formattable = ParseFormat.parse_format(z, format);

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

        final MessageFormattable        formattable = ParseFormat.parse_format(z, format);

        standard_output.println(formattable.augment(depth + 1));
    }


    public static void                  line(int depth, String format, Object v)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable        formattable = ParseFormat.parse_format(z, format);

        standard_output.println(formattable.augment(depth + 1, v));
    }


    public static void                  line(int depth, String format, Object v, Object w)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable        formattable = ParseFormat.parse_format(z, format);

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

        formattable.augment(builder, depth + 1, v, w);

        standard_output.println(builder.finish_AND_recycle());
    }


    public static void                  line(int depth, String format, Object v, Object w, Object x)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable        formattable = ParseFormat.parse_format(z, format);

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

        formattable.augment(builder, depth + 1, v, w, x);

        standard_output.println(builder.finish_AND_recycle());
    }


    public static void                  line(int depth, String format, Object v, Object w, Object x, Object y)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable        formattable = ParseFormat.parse_format(z, format);

        Gem_StringBuilder               builder = z.summon_StringBuilder();

        formattable.augment(builder, depth + 1, v, w, x, y);

        standard_output.println(builder.finish_AND_recycle());
    }


    public static void                  line(int depth, String format, Object v, Object w, Object x, Object y4, Object y5)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable        formattable = ParseFormat.parse_format(z, format);

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

        final MessageFormattable        formattable = ParseFormat.parse_format(z, format);

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

        final MessageFormattable        formattable = ParseFormat.parse_format(z, format);

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

        formattable.augment(builder, depth + 1, v, w, x, y4, y5, y6, y7, other_arguments);

        standard_output.println(builder.finish_AND_recycle());
    }


    //
    //  Public (dump)
    //
    public static void                  dump()
    {
        final PrintStream                   standard_output                = Gem.standard_output;

        final MethodNameSegmentFormatter    message_name_segment_formatter = Gem.message_name_segment_formatter;
        final Gem_ReferenceQueue            reference_queue                = Gem.reference_queue;

        line("Dump of Gem");
        line("  standard_output: {p}", standard_output);
        line("---");
        line("  message_name_segment_formatter: {p}", message_name_segment_formatter);
        line("                 reference_queue: {p}", reference_queue);
        line("End of dump of Gem");
    }


    //
    //  Public (other)
    //
    public static MethodNameSegmentFormatter    conjure_MethodNameSegmentFormatter()
    {
        final MethodNameSegmentFormatter        previous = Gem.message_name_segment_formatter;

        if (previous != null) {
            return previous;
        }

        //
        //  NOTE:
        //      Must allocate `message_name_segment_formatter` after initialization -- trying this during class
        //      initialization causes nasty loops.
        //
        final MethodNameSegmentFormatter        message_name_segment_formatter = (
                MethodNameSegmentFormatter.create__ALLY__Gem()
            );

        Gem.message_name_segment_formatter = message_name_segment_formatter;

        return message_name_segment_formatter;
    }


    public static Gem_ReferenceQueue    conjure__Gem_ReferenceQueue()
    {
        final Gem_ReferenceQueue        previous = Gem.reference_queue;

        if (previous != null) {
            return previous;
        }

        //
        //  NOTE:
        //      Must allocate `reference_queue` after initialization -- trying this during class
        //      initialization causes nasty loops.
        //
        final Gem_ReferenceQueue        reference_queue = Gem_ReferenceQueue.create__ALLY__Gem();

        Gem.reference_queue = reference_queue;

        return reference_queue;
    }


    public static World_Integer                 conjure__World_Integer(int value)
    {
        final World_Integer_Cache               integer_cache = Gem.conjure__World_Integer_Cache();

        World_Integer_Key                       key = Gem.integer_key;

        if (key == null) {
            //
            //  NOTE:
            //      Must allocate `integer_key` after initialization -- trying this during class
            //      initialization causes nasty loops.
            //
            key =
                Gem.integer_key = World_Integer_Key.create(value);
        } else {
            key.recycle(value);
        }

        final Gem_ReferenceQueue                reference_queue = Gem.conjure__Gem_ReferenceQueue();

        World_Integer_WeakReference             previous = integer_cache.get(key);

        if (previous != null) {
            World_Integer                       client = previous.get();

            if (client != null) {
                assert value == client.value;

                return client;
            }


            reference_queue.cleanup();

            assert fact(integer_cache.get(key) == null, "world_integer_cache.get({}) == null", key);
        }

        final World_Integer                     r = World_Integer.create__ALLY__Gem(value);

        final World_Integer_WeakReference       weak_reference = (
                World_Integer_WeakReference.create__ALLY__Gem(r, reference_queue)
            );

        integer_cache.put(weak_reference, weak_reference);

        return r;
    }


    public static World_Integer_Cache           conjure__World_Integer_Cache()
    {
        World_Integer_Cache                     previous = Gem.integer_cache;

        if (previous != null) {
            return previous;
        }


        //
        //  NOTE:
        //      Must allocate `integer_cache` after initialization -- trying this during class
        //      initialization causes nasty loops.
        //
        World_Integer_Cache                     integer_cache = World_Integer_Cache.create__ALLY__Gem();

        Gem.integer_cache = integer_cache;

        return integer_cache;
    }



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
