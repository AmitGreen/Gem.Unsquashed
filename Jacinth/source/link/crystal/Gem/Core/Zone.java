//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.io.PrintStream;
import java.lang.RuntimeException;
import java.lang.System;
import java.lang.Thread;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.ParseFormat;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Support.ExceptionFunctions;
import link.crystal.Gem.Support.PortrayFunctions;
import link.crystal.Gem.Support.Storehouse_MessageFormattable;
import link.crystal.Gem.Support.Storehouse_String;
import link.crystal.Gem.Format.Map__String__ArgumentSegmentFormatter_Inspection;


public class    Zone
    extends     Gem_Object<Inspection>
//  extends     Object
    implements  Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create_with_portrait("Zone");


    //
    //  Static members
    //
    private static Thread               first_thread          = null;
    private static Zone                 first_zone            = null;
    private static final int            gem_builder_allocated = 10;
    public static final PrintStream     standard_output = System.out;


    //
    //  Members
    //
    public final Thread                 zone_thread;
    private      ParseFormat            parse_format;

    private final Gem_StringBuilder[]   gem_builder_many;
    private       int                   gem_builder_total;

    private final Map__String__ArgumentSegmentFormatter_Inspection  format_map;


    //
    //  Constructor & Factory
    //
    private                             Zone(Thread zone_thread, Gem_StringBuilder[] gem_builder_many)
    {
        this.zone_thread       = zone_thread;
        this.parse_format      = null;

        this.gem_builder_many  = gem_builder_many;
        this.gem_builder_total = 0;

        this.format_map = Map__String__ArgumentSegmentFormatter_Inspection.CREATE_AND_POPULATE(this);
    }


    public static Zone                  create(Thread zone_thread)
    {
        final Gem_StringBuilder[]       gem_builder_many = new Gem_StringBuilder[Zone.gem_builder_allocated];

        return new Zone(zone_thread, gem_builder_many);
    }


    //
    //  Interface Inspectable
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }


    //
    //  Public (gem_builder)
    //
    public Gem_StringBuilder            conjure__StringBuilder()
    {
        int                             gem_builder_total = this.gem_builder_total;

        if (gem_builder_total > 0) {
            gem_builder_total -= 1;

            this.gem_builder_total = gem_builder_total;

            return this.gem_builder_many[gem_builder_total].recycle();
        }

        return Gem_StringBuilder.create__ALLY__Gem_Zone(this);
    }


    public void                         recycle__StringBuilder(Gem_StringBuilder builder)
    {
        final int                       gem_builder_total = this.gem_builder_total;

        if (gem_builder_total < Zone.gem_builder_allocated) {
            this.gem_builder_many[gem_builder_total] = builder;

            this.gem_builder_total = gem_builder_total + 1;
        }
    }


    //
    //  Public (parse_format)
    //
    //  NOTE:
    //      Due to possible nested called in a single thread, we might need multiple copies of the 'parse_format'.
    //
    //      The `store_parse_format` routine *ONLY* saves the last version of `pares_format`; any previous
    //      version is discarded, as we only bother to "cache" a single value per thread.
    //
    public ParseFormat                  pop__parse_format__OR__null()
    {
        ParseFormat                     parse_format = this.parse_format;

        this.parse_format = null;

        return parse_format;
    }


    public void                         store_parse_format(ParseFormat parse_format)
    {
        this.parse_format = parse_format;                       //  Overwrite any previously saved copy of parse_format
    }


    //
    //  Public
    //
    public String                       arrange(String format)
    {
        MessageFormattable              formattable = Storehouse_MessageFormattable.lookup(this, format);

        if (formattable == null) {
            formattable = ParseFormat.parse_format(this, format);

            Storehouse_MessageFormattable.insert(this, format, formattable);
        }

        Gem_StringBuilder               builder = this.conjure__StringBuilder();

        formattable.arrange(builder, 2);

        return builder.finish__AND__recycle();
    }


    public String                       arrange(String format, Object v)
    {
        MessageFormattable              formattable = Storehouse_MessageFormattable.lookup(this, format);

        if (formattable == null) {
            formattable = ParseFormat.parse_format(this, format);

            Storehouse_MessageFormattable.insert(this, format, formattable);
        }

        Gem_StringBuilder               builder = this.conjure__StringBuilder();

        formattable.arrange(builder, 2, v);

        return builder.finish__AND__recycle();
    }


    public String                       arrange(String format, Object v, Object w)
    {
        MessageFormattable              formattable = Storehouse_MessageFormattable.lookup(this, format);

        if (formattable == null) {
            formattable = ParseFormat.parse_format(this, format);

            Storehouse_MessageFormattable.insert(this, format, formattable);
        }

        Gem_StringBuilder               builder = this.conjure__StringBuilder();

        formattable.arrange(builder, 2, v, w);

        return builder.finish__AND__recycle();
    }


    public String                       arrange(String format, Object v, Object w, Object x)
    {
        MessageFormattable              formattable = Storehouse_MessageFormattable.lookup(this, format);

        if (formattable == null) {
            formattable = ParseFormat.parse_format(this, format);

            Storehouse_MessageFormattable.insert(this, format, formattable);
        }

        Gem_StringBuilder               builder = this.conjure__StringBuilder();

        formattable.arrange(builder, 2, v, w, x);

        return builder.finish__AND__recycle();
    }


    public String                       arrange(
            String                              format,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y//
        )
    {
        MessageFormattable              formattable = Storehouse_MessageFormattable.lookup(this, format);

        if (formattable == null) {
            formattable = ParseFormat.parse_format(this, format);

            Storehouse_MessageFormattable.insert(this, format, formattable);
        }

        Gem_StringBuilder               builder = this.conjure__StringBuilder();

        formattable.arrange(builder, 2, v, w, x, y);

        return builder.finish__AND__recycle();
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
        MessageFormattable              formattable = Storehouse_MessageFormattable.lookup(this, format);

        if (formattable == null) {
            formattable = ParseFormat.parse_format(this, format);

            Storehouse_MessageFormattable.insert(this, format, formattable);
        }

        Gem_StringBuilder               builder = this.conjure__StringBuilder();

        formattable.arrange(builder, 2, v, w, x, y4, y5);

        return builder.finish__AND__recycle();
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
        MessageFormattable              formattable = Storehouse_MessageFormattable.lookup(this, format);

        if (formattable == null) {
            formattable = ParseFormat.parse_format(this, format);

            Storehouse_MessageFormattable.insert(this, format, formattable);
        }

        Gem_StringBuilder               builder = this.conjure__StringBuilder();

        formattable.arrange(builder, 2, v, w, x, y4, y5, y6);

        return builder.finish__AND__recycle();
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
        MessageFormattable              formattable = Storehouse_MessageFormattable.lookup(this, format);

        if (formattable == null) {
            formattable = ParseFormat.parse_format(this, format);

            Storehouse_MessageFormattable.insert(this, format, formattable);
        }

        Gem_StringBuilder               builder = this.conjure__StringBuilder();

        formattable.arrange(builder, 2, v, w, x, y4, y5, y6, y7, other_arguments);

        return builder.finish__AND__recycle();
    }


    public static Zone                  current_zone()
    {
        Thread                          thread = Thread.currentThread();

        if (Zone.first_thread == thread) {
            return Zone.first_zone;
        }

        if (Zone.first_thread != null) {
            //
            //  NOTE:
            //
            //      throw `RuntimeException` directly here, to avoid recursive calls
            //
            //      (since calling `.RUNTIME` might internally call this routine, leading to recursive calls)
            //
            throw new RuntimeException("Zone.current_zone: only single threaded currently supported");
        }

        Zone                            first_zone = Zone.create(thread);

        Zone.first_thread = thread;
        Zone.first_zone   = first_zone;

        return first_zone;
    }


    public void                         dump(Zone z)
    {
        final Gem_StringBuilder[]       gem_builder_many  = this.gem_builder_many;
        final int                       gem_builder_total = this.gem_builder_total;

        z.line("Dump of Gem_Zone");
        z.line("          zone_thread: {}", this.zone_thread);
        z.line("         parse_format: {}", this.parse_format);
        z.line("---");
        z.line("     gem_builder_many: {}", gem_builder_many);
        z.line("    gem_builder_total: {}", gem_builder_total);
        z.line("---");
        z.line("           format_map: {}", this.format_map);

        for (int                        i = 0; i < gem_builder_total; i ++) {
            z.line("  gem_builder_many[{}]: {}", i, gem_builder_many[i]);
        }

        z.line("End of dump of GemZone");
    }


    public String                       intern_permenant_string(String s)
    {
        return Storehouse_String.intern_permenant_string(this, s);
    }


    public String                       intern_permenant_string_0(String s)
    {
        if (s == null) {
            return null;
        }

        return Storehouse_String.intern_permenant_string(this, s);
    }


    public void                         line()
    {
        standard_output.println();
    }


    public void                         line(String format)
    {
        MessageFormattable              formattable = Storehouse_MessageFormattable.lookup(this, format);

        if (formattable == null) {
            formattable = ParseFormat.parse_format(this, format);

            Storehouse_MessageFormattable.insert(this, format, formattable);
        }

        Gem_StringBuilder               builder = this.conjure__StringBuilder();

        formattable.arrange(builder, 2);

        standard_output.println(builder.finish__AND__recycle());
    }


    public void                         line(String format, Object v)
    {
        MessageFormattable              formattable = Storehouse_MessageFormattable.lookup(this, format);

        if (formattable == null) {
            formattable = ParseFormat.parse_format(this, format);

            Storehouse_MessageFormattable.insert(this, format, formattable);
        }

        Gem_StringBuilder               builder = this.conjure__StringBuilder();

        formattable.arrange(builder, 2, v);

        standard_output.println(builder.finish__AND__recycle());
    }


    public void                         line(String format, Object v, Object w)
    {
        MessageFormattable              formattable = Storehouse_MessageFormattable.lookup(this, format);

        if (formattable == null) {
            formattable = ParseFormat.parse_format(this, format);

            Storehouse_MessageFormattable.insert(this, format, formattable);
        }

        Gem_StringBuilder               builder = this.conjure__StringBuilder();

        formattable.arrange(builder, 2, v, w);

        standard_output.println(builder.finish__AND__recycle());
    }


    public void                         line(String format, Object v, Object w, Object x)
    {
        MessageFormattable              formattable = Storehouse_MessageFormattable.lookup(this, format);

        if (formattable == null) {
            formattable = ParseFormat.parse_format(this, format);

            Storehouse_MessageFormattable.insert(this, format, formattable);
        }

        Gem_StringBuilder               builder = this.conjure__StringBuilder();

        formattable.arrange(builder, 2, v, w, x);

        standard_output.println(builder.finish__AND__recycle());
    }


    public void                         line(String format, Object v, Object w, Object x, Object y)
    {
        MessageFormattable              formattable = Storehouse_MessageFormattable.lookup(this, format);

        if (formattable == null) {
            formattable = ParseFormat.parse_format(this, format);

            Storehouse_MessageFormattable.insert(this, format, formattable);
        }

        Gem_StringBuilder               builder = this.conjure__StringBuilder();

        formattable.arrange(builder, 2, v, w, x, y);

        standard_output.println(builder.finish__AND__recycle());
    }


    public void                         line(String format, Object v, Object w, Object x, Object y4, Object y5)
    {
        MessageFormattable              formattable = Storehouse_MessageFormattable.lookup(this, format);

        if (formattable == null) {
            formattable = ParseFormat.parse_format(this, format);

            Storehouse_MessageFormattable.insert(this, format, formattable);
        }

        Gem_StringBuilder               builder = this.conjure__StringBuilder();

        formattable.arrange(builder, 2, v, w, x, y4, y5);

        standard_output.println(builder.finish__AND__recycle());
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
        MessageFormattable              formattable = Storehouse_MessageFormattable.lookup(this, format);

        if (formattable == null) {
            formattable = ParseFormat.parse_format(this, format);

            Storehouse_MessageFormattable.insert(this, format, formattable);
        }

        Gem_StringBuilder               builder = this.conjure__StringBuilder();

        formattable.arrange(builder, 2, v, w, x, y4, y5, y6);

        standard_output.println(builder.finish__AND__recycle());
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
        MessageFormattable              formattable = Storehouse_MessageFormattable.lookup(this, format);

        if (formattable == null) {
            formattable = ParseFormat.parse_format(this, format);

            Storehouse_MessageFormattable.insert(this, format, formattable);
        }

        Gem_StringBuilder               builder = this.conjure__StringBuilder();

        formattable.arrange(builder, 2, v, w, x, y4, y5, y6, y7, other_arguments);

        standard_output.println(builder.finish__AND__recycle());
    }


    public String                       portray(Object v)
    {
        return PortrayFunctions.portray(this, v);
    }


    public String                       quote_string(String s)
    {
        return PortrayFunctions.quote_string(this, s);
    }


    public void                         INVALID_ROUTINE()
    {
        ExceptionFunctions.RUNTIME(this, "invalid routine");
    }


    public void                         RUNTIME(String error_message)
    {
        ExceptionFunctions.RUNTIME(this, error_message);
    }


    public void                         RUNTIME(
            String                              format,
            Object                              v,
            Object ...                          other_arguments//,
        )
    {
        ExceptionFunctions.RUNTIME(this, format, v, other_arguments);
    }
}
