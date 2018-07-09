//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.lang.RuntimeException;
import java.lang.Thread;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Format.AdornmentSegmentFormatter;
import link.crystal.Gem.Format.Map__String__ArgumentSegmentFormatter_Inspection;
import link.crystal.Gem.Format.NormalSegmentFormatter;
import link.crystal.Gem.Format.ParseFormat;
import link.crystal.Gem.Format.PortraySegmentFormatter;
import link.crystal.Gem.Format.StringSegmentFormatter;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Support.Storehouse_AdornmentSegmentFormatter;
import link.crystal.Gem.Support.Storehouse_MessageFormattable;
import link.crystal.Gem.Support.Storehouse_NormalSegmentFormatter;
import link.crystal.Gem.Support.Storehouse_PortraySegmentFormatter;
import link.crystal.Gem.Support.Storehouse_String;
import link.crystal.Gem.Support.Storehouse_StringSegmentFormatter;
import link.crystal.Gem.World.Inspection;


public class    Zone
    extends     Gem_Object <Inspection>
//  extends     Object
    implements  Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static final Inspection     inspection = Inspection.create("Zone");


    //
    //  Static members
    //
    private static Thread               first_thread             = null;
    private static Zone                 first_zone               = null;
    private static final int            parse_format_allocated   = 10;
    private static final int            string_builder_allocated = 10;


    //
    //  Members
    //
    public  final Thread                zone_thread;
    private       ParseFormat           parse_format;

    private final ParseFormat[]         parse_format_many;
    private       int                   parse_format_total;

    private final Gem_StringBuilder[]   string_builder_many;
    private       int                   string_builder_total;

    private       Map__String__ArgumentSegmentFormatter_Inspection  format_map;
    private       Storehouse_AdornmentSegmentFormatter              storehouse_adornment_segment_formatter;
    private       Storehouse_MessageFormattable                     storehouse_message_formattable;
    private       Storehouse_NormalSegmentFormatter                 storehouse_normal_segment_formatter;
    private       Storehouse_PortraySegmentFormatter                storehouse_portray_segment_formatter;
    private       Storehouse_StringSegmentFormatter                 storehouse_string_segment_formatter;
    private       Storehouse_String                                 storehouse_string;



    //
    //  Constructor & Factory
    //
    private                             Zone(
            Thread                              zone_thread,
            ParseFormat[]                       parse_format_many,
            Gem_StringBuilder[]                 string_builder_many//,
        )
    {
        this.zone_thread       = zone_thread;
        this.parse_format      = null;

        this.parse_format_many  = parse_format_many;
        this.parse_format_total = 0;

        this.string_builder_many  = string_builder_many;
        this.string_builder_total = 0;

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
        this.format_map                             = null;
        this.storehouse_adornment_segment_formatter = null;
        this.storehouse_message_formattable         = null;
        this.storehouse_normal_segment_formatter    = null;
        this.storehouse_portray_segment_formatter   = null;
        this.storehouse_string                      = null;
        this.storehouse_string_segment_formatter    = null;
    }


    public static Zone                  create(Thread zone_thread)
    {
        //
        //  NOTE:
        //      See comment in `.current_zone` that says these two calls are apparently "safe" & ok to do during class
        //      initialization.
        //
        final ParseFormat[]             parse_format_many   = new ParseFormat      [Zone.parse_format_allocated];
        final Gem_StringBuilder[]       string_builder_many = new Gem_StringBuilder[Zone.string_builder_allocated];

        return new Zone(zone_thread, parse_format_many, string_builder_many);
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
        builder.augment("<Zone zone_thread{p} ... string_builder_total{p} ...>",
                        this.zone_thread,
                        this.string_builder_total);
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
    public ParseFormat                  summon_ParseFormat__ALLY__ParseFormat(String format)
    {
        int                             parse_format_total = this.parse_format_total;

        if (parse_format_total > 0) {
            parse_format_total -= 1;

            this.parse_format_total = parse_format_total;

            return this.parse_format_many[parse_format_total].recycle(format);
        }


        //
        //  NOTE:
        //      Must allocate `format_map` after initialization -- trying this during class initialization causes
        //      nasty loops.
        //
        Map__String__ArgumentSegmentFormatter_Inspection    format_map = this.format_map;

        if (format_map == null) {
            format_map =
                this.format_map = Map__String__ArgumentSegmentFormatter_Inspection.CREATE_AND_POPULATE(this);
        }


        return ParseFormat.create__ALLY__Zone(this, format, format_map);
    }


    public void                         recycle__ParseFormat__ALLY__ParseFormat(ParseFormat parse_format)
    {
        final int                       parse_format_total = this.parse_format_total;

        if (parse_format_total < Zone.parse_format_allocated) {
            this.parse_format_many[parse_format_total] = parse_format;

            this.parse_format_total = parse_format_total + 1;
        }
    }


    //
    //  Public (string_builder)
    //
    public Gem_StringBuilder            summon_StringBuilder()
    {
        int                             string_builder_total = this.string_builder_total;

        if (string_builder_total > 0) {
            string_builder_total -= 1;

            this.string_builder_total = string_builder_total;

            return this.string_builder_many[string_builder_total].recycle();
        }

        return Gem_StringBuilder.create__ALLY__Zone(this);
    }


    public void                         recycle__StringBuilder__ALLY__Gem_StringBuilder(Gem_StringBuilder builder)
    {
        final int                       string_builder_total = this.string_builder_total;

        if (string_builder_total < Zone.string_builder_allocated) {
            this.string_builder_many[string_builder_total] = builder;

            this.string_builder_total = string_builder_total + 1;
        }
    }


    //
    //  Public (debug)
    //
    public void                         dump()
    {
        final Gem_StringBuilder[]       string_builder_many  = this.string_builder_many;
        final int                       string_builder_total = this.string_builder_total;

        line("Dump of Zone: {}", this);
        line("          zone_thread: {}", this.zone_thread);
        line("         parse_format: {}", this.parse_format);
        line("---");
        line("     string_builder_many: {}", string_builder_many);
        line("    string_builder_total: {}", string_builder_total);

        for (int                        i = 0; i < string_builder_total; i ++) {
            line("  string_builder_many[{}]: {}", i, string_builder_many[i]);
        }

        line("---");
        line("           format_map: {}", this.format_map);

        this.format_map.dump("Zone.format_map");

        line("End of dump of Zone");
    }


    //
    //  Public (current_zone)
    //
    //  NOTE:
    //      Since this is called during class initializatoin, this routine must be very careful not to do much
    //      (in particular, this routiine & the routines it calls `.create` & the constructor) must not do much.
    //
    //  NOTE:
    //      "not do much" includes ... not even looking at another class, as it might cause that class to call
    //      it's class initialization functions, leading to loops ...
    //
    //  NOTE:
    //      Apparently the calls to `new ParseFormat[]` & `new Gem_StringBuilder` in the `.create` function
    //      are safe -- and do not cause loops.
    //
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


    //
    //  Public (other)
    //
    public AdornmentSegmentFormatter    conjure_AdornmentSegmentFormatter(String s)
    {
        Storehouse_AdornmentSegmentFormatter    storehouse_adornment_segment_formatter = (
                this.storehouse_adornment_segment_formatter
            );

        if (storehouse_adornment_segment_formatter == null) {
            storehouse_adornment_segment_formatter =
                this.storehouse_adornment_segment_formatter = (
                        Storehouse_AdornmentSegmentFormatter.create__ALLY__Zone(this)
                    );
        }

        final AdornmentSegmentFormatter     previous = storehouse_adornment_segment_formatter.lookup(this, s);

        if (previous != null) {
            return previous;
        }

        final AdornmentSegmentFormatter     r = AdornmentSegmentFormatter.create__ALLY__Zone(this, s);

        storehouse_adornment_segment_formatter.insert(this, r.s, r);

        return r;
    }


    public NormalSegmentFormatter       conjure_NormalSegmentFormatter(int argument_index)
    {
        Storehouse_NormalSegmentFormatter   storehouse_normal_segment_formatter = (
                this.storehouse_normal_segment_formatter
            );

        if (storehouse_normal_segment_formatter == null) {
            storehouse_normal_segment_formatter =
                this.storehouse_normal_segment_formatter = (
                        Storehouse_NormalSegmentFormatter.create__ALLY__Zone(this)
                    );
        }

        final NormalSegmentFormatter    previous = storehouse_normal_segment_formatter.lookup(this, argument_index);

        if (previous != null) {
            return previous;
        }

        final NormalSegmentFormatter    r = NormalSegmentFormatter.create__ALLY__Zone(this, argument_index);

        storehouse_normal_segment_formatter.insert(this, argument_index, r);

        return r;
    }


    public PortraySegmentFormatter      conjure_PortraySegmentFormatter(int argument_index)
    {
        Storehouse_PortraySegmentFormatter  storehouse_portray_segment_formatter = (
                this.storehouse_portray_segment_formatter
            );

        if (storehouse_portray_segment_formatter == null) {
            storehouse_portray_segment_formatter =
                this.storehouse_portray_segment_formatter = (
                        Storehouse_PortraySegmentFormatter.create__ALLY__Zone(this)
                    );
        }

        final PortraySegmentFormatter   previous = storehouse_portray_segment_formatter.lookup(this, argument_index);

        if (previous != null) {
            return previous;
        }

        final PortraySegmentFormatter   r = PortraySegmentFormatter.create__ALLY__Zone(this, argument_index);

        storehouse_portray_segment_formatter.insert(this, argument_index, r);

        return r;
    }


    public Storehouse_MessageFormattable    conjure__Storehouse_MessageFormattable()
    {
        Storehouse_MessageFormattable   previous = this.storehouse_message_formattable;

        if (previous != null) {
            return previous;
        }

        storehouse_message_formattable =
            this.storehouse_message_formattable = Storehouse_MessageFormattable.create__ALLY__Zone(this);

        return storehouse_message_formattable;
    }


    public StringSegmentFormatter       conjure_StringSegmentFormatter(int argument_index)
    {
        Storehouse_StringSegmentFormatter   storehouse_string_segment_formatter = (
                this.storehouse_string_segment_formatter
            );

        if (storehouse_string_segment_formatter == null) {
            storehouse_string_segment_formatter =
                this.storehouse_string_segment_formatter = (
                        Storehouse_StringSegmentFormatter.create__ALLY__Zone(this)
                    );
        }

        final StringSegmentFormatter    previous = storehouse_string_segment_formatter.lookup(this, argument_index);

        if (previous != null) {
            return previous;
        }

        final StringSegmentFormatter    r = StringSegmentFormatter.create__ALLY__Zone(this, argument_index);

        storehouse_string_segment_formatter.insert(this, argument_index, r);

        return r;
    }


    public String                       intern_permenant_string(String s)
    {
        //
        //  NOTE:
        //      Must allocate `storehouse_string` after initialization -- trying this during class initialization
        //      causes nasty loops.
        //
        Storehouse_String               storehouse_string = this.storehouse_string;

        if (storehouse_string == null) {
            storehouse_string =
                this.storehouse_string = Storehouse_String.create__ALLY__Zone(this);
        }

        return storehouse_string.intern_permenant_string(this, s);
    }


    public String                       quote_string(String s)
    {
        final Gem_StringBuilder         builder = this.summon_StringBuilder();

        builder.quote(s);

        return builder.finish_AND_recycle();
    }
}
