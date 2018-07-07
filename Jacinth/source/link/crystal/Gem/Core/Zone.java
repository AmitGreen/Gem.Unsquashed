//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.lang.RuntimeException;
import java.lang.Thread;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.ParseFormat;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Support.Storehouse_MessageFormattable;
import link.crystal.Gem.Support.Storehouse_String;
import link.crystal.Gem.Format.Map__String__ArgumentSegmentFormatter_Inspection;


public class    Zone
    extends     Gem_Object<Inspection>
//  extends     Object
    implements  Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create("Zone");


    //
    //  Static members
    //
    private static Thread               first_thread          = null;
    private static Zone                 first_zone            = null;
    private static final int            gem_builder_allocated = 10;


    //
    //  Members
    //
    public  final Thread                zone_thread;
    private       ParseFormat           parse_format;

    private final Gem_StringBuilder[]   gem_builder_many;
    private       int                   gem_builder_total;

    public  final Map__String__ArgumentSegmentFormatter_Inspection  format_map;


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


    public void                         portray(Gem_StringBuilder builder)
    {
        builder.arrange("<Zone zone_thread{p} ... gem_builder_total{p} ...>",
                        this.zone_thread,
                        this.gem_builder_total);
    }


    //
    //  Public (gem_builder)
    //
    public Gem_StringBuilder            summon_StringBuilder()
    {
        int                             gem_builder_total = this.gem_builder_total;

        if (gem_builder_total > 0) {
            gem_builder_total -= 1;

            this.gem_builder_total = gem_builder_total;

            return this.gem_builder_many[gem_builder_total].recycle();
        }

        return Gem_StringBuilder.create__ALLY__Gem_Zone(this);
    }


    public void                         recycle__StringBuilder__ALLY__Gem_StringBuilder(Gem_StringBuilder builder)
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
        final ParseFormat               parse_format = this.parse_format;

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
        final MessageFormattable        formattable = Storehouse_MessageFormattable.conjure(this, format);

        final Gem_StringBuilder         builder = this.summon_StringBuilder();

        formattable.arrange(builder, 2);

        return builder.finish_AND_recycle();
    }


    public String                       arrange(String format, Object v)
    {
        final MessageFormattable        formattable = Storehouse_MessageFormattable.conjure(this, format);

        final Gem_StringBuilder         builder = this.summon_StringBuilder();

        formattable.arrange(builder, 2, v);

        return builder.finish_AND_recycle();
    }


    public String                       arrange(String format, Object v, Object w)
    {
        final MessageFormattable        formattable = Storehouse_MessageFormattable.conjure(this, format);

        final Gem_StringBuilder         builder = this.summon_StringBuilder();

        formattable.arrange(builder, 2, v, w);

        return builder.finish_AND_recycle();
    }


    public String                       arrange(String format, Object v, Object w, Object x)
    {
        final MessageFormattable        formattable = Storehouse_MessageFormattable.conjure(this, format);

        final Gem_StringBuilder         builder = this.summon_StringBuilder();

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
        final MessageFormattable        formattable = Storehouse_MessageFormattable.conjure(this, format);

        final Gem_StringBuilder         builder = this.summon_StringBuilder();

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
        final MessageFormattable        formattable = Storehouse_MessageFormattable.conjure(this, format);

        final Gem_StringBuilder         builder = this.summon_StringBuilder();

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
        final MessageFormattable        formattable = Storehouse_MessageFormattable.conjure(this, format);

        final Gem_StringBuilder         builder = this.summon_StringBuilder();

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
        final MessageFormattable        formattable = Storehouse_MessageFormattable.conjure(this, format);

        final Gem_StringBuilder         builder = this.summon_StringBuilder();

        formattable.arrange(builder, 2, v, w, x, y4, y5, y6, y7, other_arguments);

        return builder.finish_AND_recycle();
    }


    public static Zone                  current_zone()
    {
        final Thread                    thread = Thread.currentThread();

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

        final Zone                      first_zone = Zone.create(thread);

        Zone.first_thread = thread;
        Zone.first_zone   = first_zone;

        return first_zone;
    }


    public void                         dump()
    {
        final Gem_StringBuilder[]       gem_builder_many  = this.gem_builder_many;
        final int                       gem_builder_total = this.gem_builder_total;

        line("Dump of Gem_Zone: {}", this);
        line("          zone_thread: {}", this.zone_thread);
        line("         parse_format: {}", this.parse_format);
        line("---");
        line("     gem_builder_many: {}", gem_builder_many);
        line("    gem_builder_total: {}", gem_builder_total);

        for (int                        i = 0; i < gem_builder_total; i ++) {
            line("  gem_builder_many[{}]: {}", i, gem_builder_many[i]);
        }

        line("---");
        line("           format_map: {}", this.format_map);

        this.format_map.dump("Gem_Zone.format_map");

        line("End of dump of GemZone");
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


    public String                       quote_string(String s)
    {
        final Gem_StringBuilder         builder = this.summon_StringBuilder();

        builder.quote(s);

        return builder.finish_AND_recycle();
    }
}
