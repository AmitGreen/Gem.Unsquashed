//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.io.PrintStream;
import java.lang.Object;
import java.lang.System;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Format.MethodNameSegmentFormatter;
import link.crystal.Gem.Format.ParseFormat;
import link.crystal.Gem.Inspection.Comparable_Inspection;
import link.crystal.Gem.Inspection.Gem_Reference_Inspection;
import link.crystal.Gem.Interface.Gem_ComparableReference_Interface;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Support.Gem_ReferenceQueue;
import link.crystal.Gem.Support.Map_String_Inspection;
import link.crystal.Gem.Support.World_Integer_Cache;
import link.crystal.Gem.Support.World_Integer_Key;
import link.crystal.Gem.Support.World_Integer_WeakReference;
import link.crystal.Gem.Support.World_String_Cache;
import link.crystal.Gem.Support.World_String_EnduringReference;
import link.crystal.Gem.Support.World_String_Key;
import link.crystal.Gem.Support.World_String_WeakReference;
import link.crystal.Gem.World.World_Integer;
import link.crystal.Gem.World.World_String;
import link.crystal.Silver.UnitTest.UnitTest;
import link.crystal.Gem.UnitTest.World_String_WeakReference_PhantomReference;


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
    public static /*boot-final*/    World_Integer_Cache         integer_cache                  /* = null */ ;
    public static /*boot-final*/    World_String_Cache          string_cache                   /* = null */ ;
    public static /*boot-final*/    Map_String_Inspection       map_string_inspection          /* = null */ ;
    public static /*boot-final*/    MethodNameSegmentFormatter  message_name_segment_formatter /* = null */ ;
    public static /*boot-final*/    Gem_ReferenceQueue          reference_queue                /* = null */ ;


    //
    //  Public Statis (Unit Test)
    //
    private static UnitTest             unit_test = null;


    //
    //  Ally
    //
    public static void                  boot__ALLY__Zone(Zone z)
    {
        assert fact_null(Gem.integer_cache,                  "Gem.integer_cache");
        assert fact_null(Gem.string_cache,                   "Gem.string_cache");
        assert fact_null(Gem.map_string_inspection,          "Gem.map_string_inspection");
        assert fact_null(Gem.message_name_segment_formatter, "Gem.message_name_segment_formatter");
        assert fact_null(Gem.reference_queue,                "Gem.reference_queue");

        final Map_String_Inspection         map_string_inspection = Map_String_Inspection.create__ALLY__Gem(z);

        Gem.integer_cache                  = World_Integer_Cache.create__ALLY__Gem();
        Gem.string_cache                   = World_String_Cache .create__ALLY__Gem();
        Gem.map_string_inspection          = map_string_inspection;
        Gem.message_name_segment_formatter = MethodNameSegmentFormatter.create__ALLY__Gem();
        Gem.reference_queue                = Gem_ReferenceQueue        .create__ALLY__Gem();

        map_string_inspection.boot__ALLY__Zone(z);
    }


    public static final void                store_unit_test__ALLY__UnitTest(UnitTest unit_test)
    {
        assert fact_null   (Gem.unit_test, "Gem.unit_test");
        assert fact_pointer(unit_test,     "unit_test");

        Gem.unit_test = unit_test;
    }


    //
    //  Public (arrange)
    //
    public static String                arrange(int depth, String format)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable<?>     formattable = ParseFormat.parse_format(z, format);

        return formattable.augment(depth + 1);
    }


    public static String                arrange(int depth, String format, Object v)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable<?>     formattable = ParseFormat.parse_format(z, format);

        return formattable.augment(depth + 1, v);
    }


    public static String                arrange(int depth, String format, Object v, Object w)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable<?>     formattable = ParseFormat.parse_format(z, format);

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

        formattable.augment(builder, depth + 1, v, w);

        return builder.finish_AND_recycle();
    }


    public static String                arrange(int depth, String format, Object v, Object w, Object x)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable<?>     formattable = ParseFormat.parse_format(z, format);

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

        final MessageFormattable<?>     formattable = ParseFormat.parse_format(z, format);

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

        final MessageFormattable<?>     formattable = ParseFormat.parse_format(z, format);

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

        final MessageFormattable<?>     formattable = ParseFormat.parse_format(z, format);

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

        final MessageFormattable<?>     formattable = ParseFormat.parse_format(z, format);

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

        final MessageFormattable<?>     formattable = ParseFormat.parse_format(z, format);

        standard_output.println(formattable.augment(depth + 1));
    }


    public static void                  line(int depth, String format, Object v)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable<?>     formattable = ParseFormat.parse_format(z, format);

        standard_output.println(formattable.augment(depth + 1, v));
    }


    public static void                  line(int depth, String format, Object v, Object w)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable<?>     formattable = ParseFormat.parse_format(z, format);

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

        formattable.augment(builder, depth + 1, v, w);

        standard_output.println(builder.finish_AND_recycle());
    }


    public static void                  line(int depth, String format, Object v, Object w, Object x)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable<?>     formattable = ParseFormat.parse_format(z, format);

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

        formattable.augment(builder, depth + 1, v, w, x);

        standard_output.println(builder.finish_AND_recycle());
    }


    public static void                  line(int depth, String format, Object v, Object w, Object x, Object y)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable<?>     formattable = ParseFormat.parse_format(z, format);

        Gem_StringBuilder               builder = z.summon_StringBuilder();

        formattable.augment(builder, depth + 1, v, w, x, y);

        standard_output.println(builder.finish_AND_recycle());
    }


    public static void                  line(int depth, String format, Object v, Object w, Object x, Object y4, Object y5)
    {
        final Zone                      z = Zone.current_zone();

        final MessageFormattable<?>     formattable = ParseFormat.parse_format(z, format);

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

        final MessageFormattable<?>     formattable = ParseFormat.parse_format(z, format);

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

        final MessageFormattable<?>     formattable = ParseFormat.parse_format(z, format);

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

        formattable.augment(builder, depth + 1, v, w, x, y4, y5, y6, y7, other_arguments);

        standard_output.println(builder.finish_AND_recycle());
    }


    //
    //  Public (dump)
    //
    public static void                  dump()
    {
        line("Dump of Gem");
        line("  standard_output: {p}", Gem.standard_output);
        line("---");
        line("                   integer_cache: {p}", Gem.integer_cache);
        line("                    string_cache: {p}", Gem.string_cache);
        line("           map_string_inspection: {p}", Gem.map_string_inspection);
        line("  message_name_segment_formatter: {p}", Gem.message_name_segment_formatter);
        line("                 reference_queue: {p}", Gem.reference_queue);
        line("End of dump of Gem");
    }


    //
    //  Public (other)
    //
    public static World_String                  conjure_enduring_string(String s)
    {
        final Zone                              z = Zone.current_zone();

        final World_String_Cache                string_cache    = Gem.string_cache;

        final World_String_Key                  key = z.string_key;

        key.recycle(s);

        final Gem_ComparableReference_Interface<
                  ? extends Gem_Reference_Inspection,
                  World_String,
                  Comparable_Inspection
              >                                 previous = string_cache.get(key);

        World_String                            client;

        if (previous == null) {
            client = World_String.create__ALLY__Gem(s);
        } else {
            client = previous.client_OR_enqueue();

            if (client == null) {
                Gem.reference_queue.cleanup();

                assert fact(string_cache.get(key) == null, "world_string_cache.get({}) == null", key);

                client = World_String.create__ALLY__Gem(s);
            } else {
                assert fact(s.equals(client.s), "s.equals(client.s)");

                if (previous.inspect().is_enduring_reference) {
                    return client;
                }


                final UnitTest          unit_test = Gem.unit_test;

                if (unit_test != null) {
                    final World_String_WeakReference_PhantomReference   phantom_reference = (
                            World_String_WeakReference_PhantomReference.create__ALLY__Gem(
                                (World_String_WeakReference) previous,
                                Gem.reference_queue//,
                            )
                        );

                    unit_test.store_phantom(phantom_reference);
                }

                //
                //  NOTE:
                //      Have to remove the 'previous' key (the weak reference), so that a new key (and new value) can
                //      be `put`.
                //
                //      Be default `put` *ONLY* replaces the value, and not the key; hence the need to remove the key
                //      first.
                //
                string_cache.remove(previous);
            }
        }

        final World_String_EnduringReference    enduring_reference = (
                World_String_EnduringReference.create__ALLY__Gem(client)
            );

        string_cache.put(enduring_reference, enduring_reference);

        return client;
    }


    public static World_Integer                 conjure_integer(int value)
    {
        final Zone                              z = Zone.current_zone();

        final World_Integer_Cache               integer_cache   = Gem.integer_cache;
        final Gem_ReferenceQueue                reference_queue = Gem.reference_queue;

        final World_Integer_Key                 key = z.integer_key;

        key.recycle(value);

        Gem_ComparableReference_Interface<
            ? extends Gem_Reference_Inspection,
            World_Integer,
            Comparable_Inspection
        >                                       previous = integer_cache.get(key);

        if (previous != null) {
            World_Integer                       client = previous.client_OR_enqueue();

            if (client != null) {
                assert fact(value == client.value, "value == client.value");

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


    public static MethodNameSegmentFormatter    conjure_MethodNameSegmentFormatter()
    {
        final MethodNameSegmentFormatter        message_name_segment_formatter = Gem.message_name_segment_formatter;

        assert fact_pointer(message_name_segment_formatter, "message_name_segment_formatter");

        return message_name_segment_formatter;
    }


    public static World_String                  conjure_string(String s)
    {
        final Zone                              z = Zone.current_zone();

        final World_String_Cache                string_cache    = Gem.string_cache;
        final Gem_ReferenceQueue                reference_queue = Gem.reference_queue;

        final World_String_Key                  key = z.string_key;

        key.recycle(s);

        Gem_ComparableReference_Interface<
            ? extends Gem_Reference_Inspection,
            World_String,
            Comparable_Inspection
        >                                       previous = string_cache.get(key);

        if (previous != null) {
            World_String                        client = previous.client_OR_enqueue();

            if (client != null) {
                assert fact(s.equals(client.s), "s.equals(client.s)");

                return client;
            }

            reference_queue.cleanup();

            assert fact(string_cache.get(key) == null, "world_string_cache.get({}) == null", key);
        }

        final World_String                      r = World_String.create__ALLY__Gem(s);

        final World_String_WeakReference        weak_reference = (
                World_String_WeakReference.create__ALLY__Gem(r, reference_queue)
            );

        string_cache.put(weak_reference, weak_reference);

        return r;
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
