//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.String;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import link.crystal.Gem.Core.ArrayFunctions;
import link.crystal.Gem.Core.Gem;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Format.AdornmentSegmentFormatter;
import link.crystal.Gem.Format.ArgumentSegmentFormatter_Inspection;
import link.crystal.Gem.Format.Map__String__ArgumentSegmentFormatter_Inspection;
import link.crystal.Gem.Format.MessageFormatter_1__Prefix;
import link.crystal.Gem.Format.MessageFormatter_2;
import link.crystal.Gem.Format.MessageFormatter_3;
import link.crystal.Gem.Format.MessageFormatter_4;
import link.crystal.Gem.Format.MessageFormatter_5;
import link.crystal.Gem.Format.MessageFormatter_Many;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Interface.SegmentFormattable;
import link.crystal.Gem.Support.Storehouse_MessageFormattable;
import link.crystal.Gem.World.Inspection;


public class   ParseFormat
    extends    Gem_Object <Inspection>
    implements Inspectable<Inspection>//,                               //  Via Gem_Object
{
    private static final Inspection     inspection = Inspection.create("ParseFormat");


    //
    //  Static members
    //
    //      Matching rules:
    //          Most likely match:          group 6                     //  Example: {}, {1}, {s} {3p}
    //          Second most likely match:   group 2                     //  Example: {{
    //          Third  most likely match:   group 7                     //  Example: }}
    //          Fourth most likely:         FAIL                        //  Example: {, or } by themselves
    //
    private static final Pattern        braces_pattern = Pattern.compile(
              "(?:[^{}]*)"
            + "(?:"
            +    "(\\{)"                                                //  Group 1 = '{'
            +    "(?:"
            +       "(\\{)"                                             //  Group 2 = '{'
            +      "|(?:(\\+)|(0|[1-9][0-9]*)?([ps]?))"                 //  Group 3 = '+', Group 4 = #, Group 5 = [ps]?
            +       "(\\})?"                                            //  Group 6 = '}'
            +    ")"
            +   "|\\}"
            +    "(\\})?"                                               //  Group 7 = '}'
            + ")"
        );


    //
    //  Members
    //
    private final Zone                  z;

    private       String                                            format;
    private final Matcher                                           braces_matcher;
    private final Map__String__ArgumentSegmentFormatter_Inspection  format_map;

    private       Gem_StringBuilder     builder;

    private       SegmentFormattable[]  segment_many;
    private       int                   segment_total;
    private       int                   segment_allocated;

    private       int[]                 used_index_many;
    private       int                   used_index_total;
    private       int                   used_index_allocated;

    private       int[]                 missing_many;
    private       int                   missing_total;
    private       int                   missing_allocated;


    //
    //  Constructor, Factory, & Recycle
    //
    private                             ParseFormat(
            Zone                                                z,
            String                                              format,
            Matcher                                             braces_matcher,
            Map__String__ArgumentSegmentFormatter_Inspection    format_map//,
        )
    {
        this.z = z;

        this.format         = format;
        this.braces_matcher = braces_matcher;
        this.format_map     = format_map;

        this.builder = null;

        this.segment_many      = null;
        this.segment_total     = 0;
        this.segment_allocated = 0;

        this.used_index_many      = null;
        this.used_index_total     = 0;
        this.used_index_allocated = 0;

        this.missing_many      = null;
        this.missing_total     = 0;
        this.missing_allocated = 0;
    }


    public static ParseFormat           create__ALLY__Zone(
            Zone                                                z,
            String                                              format,
            Map__String__ArgumentSegmentFormatter_Inspection    format_map//,
        )
    {
        final Matcher                   braces_matcher = ParseFormat.braces_pattern.matcher(format);

        return new ParseFormat(z, format, braces_matcher, format_map);
    }


    public ParseFormat                  recycle(String format)
    {
        this.format = format;
        this.braces_matcher.reset(format);

        this.segment_total = 0;

        this.used_index_total = 0;

        this.missing_total = 0;

        return this;
    }


    //
    //  Interface Inspectable
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }


    //
    //  Private
    //
    private void                        add_used_index(int argument_index)
    {
        if (false) {
            output("add_used_index(" + Integer.toString(argument_index) + ")");
        }

        int[]                           used_index_many      = this.used_index_many;
        final int                       used_index_total     = this.used_index_total;
        final int                       used_index_allocated = this.used_index_allocated;
        final int                       needed               = argument_index + 1;

        if (used_index_allocated < needed) {
            final int                   new_allocated = limit_to_between(20, needed * 2, 100);

            used_index_many = ArrayFunctions.grow_primitive_integer_array(
                    this.z,
                    used_index_many,
                    used_index_total,
                    new int[new_allocated],
                    new_allocated//,
                );

            this.used_index_many      = used_index_many;
            this.used_index_allocated = new_allocated;
        }

        for (int                    i = used_index_total; i <= argument_index; i ++) {
            used_index_many[i] = 0;
        }

        used_index_many[argument_index] += 1;

        if (used_index_total < needed) {
            this.used_index_total = needed;
        }
    }


    private void                        append_missing(int missing)
    {
        int[]                           missing_many      = this.missing_many;
        final int                       missing_total     = this.missing_total;
        final int                       missing_allocated = this.missing_allocated;
        final int                       needed            = missing_total + 1;

        if (missing_allocated < needed) {
            final int                   new_allocated = limit_to_between(20, needed * 2, 100);

            missing_many = ArrayFunctions.grow_primitive_integer_array(
                    this.z,
                    missing_many,
                    missing_total,
                    new int[new_allocated],
                    new_allocated//,
                );

            this.missing_many      = missing_many;
            this.missing_allocated = new_allocated;
        }

        missing_many[missing_total] = missing;

        this.missing_total = missing_total + 1;
    }


    private void                        append_segment(SegmentFormattable segment)
    {
        SegmentFormattable[]            segment_many      = this.segment_many;
        final int                       segment_total     = this.segment_total;
        final int                       segment_allocated = this.segment_allocated;
        final int                       needed            = segment_total + 1;

        if (segment_allocated < needed) {
            if (segment_allocated == 201) {
                RUNTIME("maximum of 100 '{#}' allowed");
            }

            final Zone                  z = this.z;

            final int                   new_allocated = limit_to_between(21, needed * 2, 201);

            segment_many = ArrayFunctions.<SegmentFormattable>grow_array(
                    z,
                    segment_many,
                    segment_total,
                    new SegmentFormattable[new_allocated],
                    new_allocated//,
                );

            this.segment_many      = segment_many;
            this.segment_allocated = new_allocated;
        }

        segment_many[segment_total] = segment;

        this.segment_total = segment_total + 1;
    }


    private void                        examine_missing()
    {
        final Zone                      z                = this.z;
        final int[]                     used_index_many  = this.used_index_many;
        final int                       used_index_total = this.used_index_total;

        for (int                        i = 0; i < used_index_total; i ++) {
            if (used_index_many[i] == 0) {
                this.append_missing(i);
            }
        }

        final int                       missing_total = this.missing_total;

        if (missing_total == 0) {
            return;
        }

        final int[]                     missing_many = this.missing_many;

        if (missing_total == 1) {
            RUNTIME("format string is missing {{{}}}: {p}", missing_many[0], this.format);
        }

        if (missing_total == 2) {
            RUNTIME("format string is missing {{{}}} and {{{}}}: {p}", missing_many[0], missing_many[1], this.format);
        }

        final Gem_StringBuilder         builder = this.summon_builder();

        for (int                        i = 0; i < missing_total; i ++) {
            if (i == missing_total - 1) {
                builder.append(", and ");
            } else if (i > 0) {
                builder.append(", ");
            }

            builder.append("{", missing_many[i], "}");
        }

        RUNTIME("format string is missing {s}: {p}", builder.finish_AND_keep(), this.format);
    }


    private MessageFormattable          parse_format__work()
    {
        final Zone                      z              = this.z;
        final String                    format         = this.format;
        final Matcher                   braces_matcher = this.braces_matcher;

        if ( ! braces_matcher.lookingAt()) {
            return z.conjure_AdornmentSegmentFormatter(format);
        }

        int                             argument_index    = -1;
        int                             automatic_index   = -1;
        Gem_StringBuilder               builder           = null;
        boolean                         has_prefix        = false;
        int                             format_total      = format.length();
        int                             start             = 0;
        String                          prefix_at_index_0 = null;

        for (;;) {
            //
            //  NOTE:
            //      See "matching" rules above, as to why this is done in the order:
            //
            //          6                                               //  Example: {}, {1}, {s} {3p}
            //          2 or 7                                          //  Example: {{ or }}
            //          FAIL                                            //  Example: {, or } by themselves
            //
            final int                   end_6 = braces_matcher.end(6);

            if (end_6 == -1) {
                int                     start_brace_pair = braces_matcher.start(2);

                if (start_brace_pair == -1) {
                    start_brace_pair = braces_matcher.start(7);

                    if (start_brace_pair == -1) {
                        RUNTIME("format string is malformed: {p}", format);
                    }
                }

                final String            prefix = format.substring(start, start_brace_pair);

                start = start_brace_pair + 1;

                if (start == format_total) {
                    if (has_prefix) {
                        builder.append(prefix);
                        break;
                    }

                    this.append_segment(z.conjure_AdornmentSegmentFormatter(prefix));
                    break;
                }

                if (builder == null) {
                    builder = summon_builder();
                }

                builder.append(prefix);
                has_prefix = true;

                braces_matcher.region(start, format_total);

                if ( ! braces_matcher.lookingAt()) {
                    break;
                }

                continue;
            }

            final int                   start_1 = braces_matcher.start(1);

            if (start < start_1) {
                String                  start_s = format.substring(start, start_1);

                if (has_prefix) {
                    builder.append(start_s);

                    start_s = builder.finish_AND_keep();

                    has_prefix = false;
                }

                if (this.segment_total == 0) {
                    prefix_at_index_0 = start_s;
                    this.append_segment(null);
                } else {
                    this.append_segment(z.conjure_AdornmentSegmentFormatter(start_s));
                }
            } else {
                if (has_prefix) {
                    final String        previous = builder.finish_AND_keep();

                    if (this.segment_total == 0) {
                        prefix_at_index_0 = previous;
                        this.append_segment(null);
                    } else {
                        this.append_segment(z.conjure_AdornmentSegmentFormatter(previous));
                    }

                    has_prefix = false;
                }
            }

            if (braces_matcher.start(3) != -1) {
                this.append_segment(Gem.conjure_MethodNameSegmentFormatter());
            } else {
                final String            group_4 = braces_matcher.group(4);

                if (group_4 == null) {
                    if (automatic_index == -6) {
                        this.raise_both_automatic_and_manual_field_number();
                    }

                    automatic_index += 1;
                    argument_index  = automatic_index;
                } else {
                    if (automatic_index >= 0) {
                        this.raise_both_automatic_and_manual_field_number();
                    }

                    argument_index = Integer.parseInt(group_4);
                }

                final ArgumentSegmentFormatter_Inspection   argument_inspection = (
                        this.format_map.find(braces_matcher.group(5))
                    );

                this.append_segment(argument_inspection.conjure_argument_segment(z, argument_index));

                add_used_index(argument_index);
            }

            start = end_6;

            braces_matcher.region(end_6, format_total);

            if ( ! braces_matcher.lookingAt()) {
                break;
            }
        }

        if (start < format_total) {
            final String                end_s = format.substring(start);

            if (has_prefix) {
                builder.append(end_s);

                this.append_segment(z.conjure_AdornmentSegmentFormatter(builder.finish_AND_keep()));
            } else {
                this.append_segment(z.conjure_AdornmentSegmentFormatter(end_s));
            }
        } else {
            if (has_prefix) {
                this.append_segment(z.conjure_AdornmentSegmentFormatter(builder.finish_AND_keep()));
            }
        }

        this.examine_missing();

        if (false) {
            final Gem_StringBuilder     b2 = z.summon_StringBuilder();

            b2.append("format: ");
            b2.quote(format);

            output(b2.finish_AND_recycle());

            for (int                    i = 0; i < segment_total; i ++) {
                final SegmentFormattable    segment = segment_many[i];
                final Gem_StringBuilder     b3      = z.summon_StringBuilder();

                b3.append(i, " :");
                b3.portray(segment);

                output(b3.finish_AND_recycle());
            }
        }

        final int                       expected = this.used_index_total;

        if (segment_total == 1) {
            assert fact_null(prefix_at_index_0, "prefix_at_index_0");

            return segment_many[0];
        }

        if (prefix_at_index_0 != null) {
            assert fact_null(segment_many[0], "segment_many[0]");

            if (segment_total == 2) {
                final SegmentFormattable    b = segment_many[1];

                if (b.inspect().is_portray_segment_formatter) {
                    return MessageFormatter_1__Prefix.create(z, prefix_at_index_0);
                }
            }

            segment_many[0] = z.conjure_AdornmentSegmentFormatter(prefix_at_index_0);
        } else {
            assert fact_pointer(segment_many[0], "segment_many[0]");
        }

        if (segment_total == 2) {
            return MessageFormatter_2.create(z, expected, segment_many[0], segment_many[1]);
        }

        if (segment_total == 3) {
            return MessageFormatter_3.create(z, expected, segment_many[0], segment_many[1], segment_many[2]);
        }

        if (segment_total == 4) {
            return MessageFormatter_4.create(
                    z,
                    expected,
                    segment_many[0],
                    segment_many[1],
                    segment_many[2],
                    segment_many[3]//,
                );
        }

        if (segment_total == 5) {
            return MessageFormatter_5.create(
                    z,
                    expected,
                    segment_many[0],
                    segment_many[1],
                    segment_many[2],
                    segment_many[3],
                    segment_many[4]//,
                );
        }

        SegmentFormattable[]        shrunk_many;
        final int                   shrunk_total = segment_total;

        if (segment_total < segment_allocated) {
            shrunk_many = ArrayFunctions.<SegmentFormattable>shrink_array(
                                 z,
                                 segment_many,
                                 segment_allocated,
                                 new SegmentFormattable[segment_total],
                                 segment_total//,
                             );
        } else {
            shrunk_many = this.steal_segments();
        }

        return MessageFormatter_Many.create(z, expected, shrunk_many);
    }


    private void                        raise_both_automatic_and_manual_field_number()
    {
        RUNTIME("format string has both automatic & manual field numbering: {p}", this.format);
    }


    //
    //  Null any references (for garbage collection purposes)
    //
    //  NOTE:
    //      Not really useful, since all the same data is saved elsewhere, and will never be garbage collectd ...
    //      ...  However, doing this just on principle anyway ...
    //
    private void                        scrub()
    {
        final int                       segment_total = this.segment_total;

        this.format = null;
        this.braces_matcher.reset();

        if (segment_total > 0) {
            SegmentFormattable[]        segment_many = this.segment_many;

            for (int                    i = 0; i < segment_total; i ++) {
                segment_many[i] = null;
            }

            this.segment_total = 0;
        }
    }


    private SegmentFormattable[]        steal_segments()
    {
        final SegmentFormattable[]      segment_many = this.segment_many;

        if (segment_many == null) {
            RUNTIME("no segments to steal");
        }

        this.segment_many      = null;
        this.segment_allocated = 0;
        this.segment_total     = 0;

        return segment_many;
    }


    private Gem_StringBuilder           summon_builder()
    {
        Gem_StringBuilder               builder = this.builder;

        if (builder != null) {
            return builder.recycle();
        }

        builder =
            this.builder = z.summon_StringBuilder();

        return builder;
    }


    //
    //  Public static
    //
    public static MessageFormattable    parse_format(Zone z, String format)
    {
        final Storehouse_MessageFormattable     cache = z.conjure__Storehouse_MessageFormattable();

        final MessageFormattable        previous = cache.get(format);

        if (previous != null) {
            return previous;
        }

        ParseFormat                     parse_format = z.summon_ParseFormat__ALLY__ParseFormat(format);

        final MessageFormattable        formattable = parse_format.parse_format__work();

        parse_format.scrub();
        z.recycle__ParseFormat__ALLY__ParseFormat(parse_format);

        cache.insert(z, format, formattable);

        return formattable;
    }
}
