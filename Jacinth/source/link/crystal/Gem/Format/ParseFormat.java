//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.lang.String;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import link.crystal.Gem.Core.ArrayFunctions;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Format.AdornmentSegmentFormatter;
import link.crystal.Gem.Format.MessageFormatter_1__Prefix;
import link.crystal.Gem.Format.MessageFormatter_1__Suffix;
import link.crystal.Gem.Format.MessageFormatter_2;
import link.crystal.Gem.Format.MessageFormatter_3;
import link.crystal.Gem.Format.MessageFormatter_4;
import link.crystal.Gem.Format.MessageFormatter_5;
import link.crystal.Gem.Format.MessageFormatter_Many;
import link.crystal.Gem.Format.MethodNameSegmentFormatter;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Interface.SegmentFormattable;
import link.crystal.Gem.Format.ArgumentSegmentFormatter_Inspection;


public class   ParseFormat
    extends    Gem_Object<Inspection>
    implements Inspectable<Inspection>//,                               //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create("Gem.Core.ParseFormat");


    //
    //  Static members
    //
    private static Pattern              braces_pattern = Pattern.compile(
            "(?:[^{}]|\\{\\{|\\}\\})*(\\{)(?:(\\+)|(0|[1-9][0-9]*)?([ps]?))(\\})?"//,
        );


    //
    //  Members
    //
    private final Zone                  z;

    private String                      format;
    private Matcher                     braces_matcher;

    private SegmentFormattable[]        segment_many;
    private int                         segment_total;
    private int                         segment_allocated;

    private int[]                       used_index_many;
    private int                         used_index_total;
    private int                         used_index_allocated;

    private int[]                       missing_many;
    private int                         missing_total;
    private int                         missing_allocated;


    //
    //  Constructor, Factory, & Recycle
    //
    private                             ParseFormat(Zone z, String format, Matcher braces_matcher)
    {
        this.z = z;

        this.format         = format;
        this.braces_matcher = braces_matcher;

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


    public static ParseFormat           create(Zone z, String format)
    {
        Matcher                         braces_matcher = ParseFormat.braces_pattern.matcher(format);

        return new ParseFormat(z, format, braces_matcher);
    }


    public void                         recycle(String format)
    {
        this.format = format;
        this.braces_matcher.reset(format);

        this.segment_total = 0;

        this.used_index_total = 0;

        this.missing_total = 0;
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
            final Zone                  z = this.z;

            z.line("add_used_index(" + Integer.toString(argument_index) + ")");
        }

        int[]                           used_index_many      = this.used_index_many;
        int                             used_index_total     = this.used_index_total;
        int                             used_index_allocated = this.used_index_allocated;
        int                             needed               = argument_index + 1;

        if (used_index_allocated < needed) {
            int                         new_allocated = limit_to_between(20, needed * 2, 100);

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
        int                             missing_total     = this.missing_total;
        int                             missing_allocated = this.missing_allocated;
        int                             needed            = missing_total + 1;

        if (missing_allocated < needed) {
            int                         new_allocated = limit_to_between(20, needed * 2, 100);

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
        int                             segment_total     = this.segment_total;
        int                             segment_allocated = this.segment_allocated;
        int                             needed            = segment_total + 1;

        if (segment_allocated < needed) {
            Zone                         z = this.z;

            if (segment_allocated == 201) {
                z.RUNTIME("maximum of 100 '{#}' allowed");
            }

            int                         new_allocated = limit_to_between(21, needed * 2, 201);

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
        Zone                            z                = this.z;
        int[]                           used_index_many  = this.used_index_many;
        int                             used_index_total = this.used_index_total;

        for (int                        i = 0; i < used_index_total; i ++) {
            if (used_index_many[i] == 0) {
                this.append_missing(i);
            }
        }

        int                             missing_total = this.missing_total;

        if (missing_total == 0) {
            return;
        }

        int[]                           missing_many = this.missing_many;

        if (missing_total == 1) {
            z.RUNTIME("format string is missing {{{}}}: {}", missing_many[0], z.quote_string(this.format));
        }

        if (missing_total == 2) {
            z.RUNTIME("format string is missing {{{}}} and {{{}}}: {}",
                      missing_many[0],
                      missing_many[1],
                      z.quote_string(this.format));
        }


        Gem_StringBuilder               builder = z.conjure__StringBuilder();

        for (int                        i = 0; i < missing_total; i ++) {
            if (i == missing_total - 1) {
                builder.append(", and ");
            } else if (i > 0) {
                builder.append(", ");
            }

            builder.append("{", missing_many[i], "}");
        }

        z.RUNTIME("format string is missing {}: {}", builder.finish__AND__recycle(), z.quote_string(this.format));
    }


    private void                        raise_both_automatic_and_manual_field_number()
    {
        Zone                            z      = this.z;
        String                          format = this.format;

        z.RUNTIME("format string has both automatic & manual field numbering: {}", format);
    }


    private SegmentFormattable[]        steal_segments()
    {
        SegmentFormattable[]            segment_many = this.segment_many;

        if (segment_many == null) {
            Zone                        z = this.z;

            z.RUNTIME("no segments to steal");
        }

        this.segment_many      = null;
        this.segment_allocated = 0;
        this.segment_total     = 0;

        return segment_many;
    }


    private MessageFormattable          parse_format__work()
    {
        Zone                            z              = this.z;
        String                          format         = this.format;
        Matcher                         braces_matcher = this.braces_matcher;

        if ( ! braces_matcher.lookingAt()) {
            return AdornmentSegmentFormatter.conjure(z, format);
        }


        int                             format_total = format.length();

        //
        //  First argument
        //
        int                             end_5 = braces_matcher.end(5);

        if (end_5 == -1) {
            z.RUNTIME("format string is malformed: {}", z.quote_string(format));
        }

        int                             start_1             = braces_matcher.start(1);
        boolean                         method_name_segment = (braces_matcher.start(2) != -1);

        ArgumentSegmentFormatter_Inspection     argument_inspection;

        int                             automatic_index;
        int                             argument_index;

        if (method_name_segment) {
            automatic_index = -1;
            argument_index  = -1;

            argument_inspection = null;
        } else {
            String                      group_3 = braces_matcher.group(3);

            if (group_3 == null) {
                automatic_index = 0;
                argument_index  = 0;
            } else {
                automatic_index = -6;
                argument_index  = Integer.parseInt(group_3);
            }

            argument_inspection = z.format_map.find(braces_matcher.group(4));
        }


        //
        //  Second segment?
        //
        boolean                         found;

        if (end_5 == format_total) {
            found = false;
        } else {
            braces_matcher.region(end_5, format_total);

            found = braces_matcher.lookingAt();
        }


        //
        //  First segment
        //
        String                          start_s;

        if (start_1 == 0) {
            start_s = null;
        } else {
            start_s = format.substring(0, start_1);
        }

        //
        //  First segment: Special cases:
        //
        //      1.  "{+}"                   becomes     MethodNameSegmentFormatter
        //      2.  "{}"                    becomes     PortraySegmentFormatter
        //      3.  "{p}"                   becomes     StringSegmentFormatter
        //      4.  "prefix: {p}"           becomes     MessageFormatter_1__Prefix
        //      5.  "prefix: {0} suffix"    becomes     MessageFormatter_1__Suffix
        //
        if ( ! found) {
            if (start_s == null) {
                if (end_5 == format_total) {
                    if (method_name_segment) {
                        return MethodNameSegmentFormatter.conjure(z);
                    }

                    return argument_inspection.conjure_argument_segment(z, 0);
                }
            } else {
                if (argument_index == 0) {
                    if (end_5 == format_total) {
                        return MessageFormatter_1__Prefix.create(z, start_s);
                    }

                    String              end_s = format.substring(end_5);

                    return MessageFormatter_1__Suffix.create(z, start_s, end_s);
                }
            }
        }


        //
        //  First segment: Normal cases
        //
        if (0 < start_1) {
            this.append_segment(AdornmentSegmentFormatter.conjure(z, start_s));
        }

        if (argument_index == -1) {
            this.append_segment(MethodNameSegmentFormatter.conjure(z));
        } else {
            this.append_segment(argument_inspection.conjure_argument_segment(z, argument_index));
            add_used_index(argument_index);
        }


        //
        //  Subsequent segments
        //
        while (found) {
            int                         next_end_5 = braces_matcher.end(5);

            if (next_end_5 == -1) {
                z.RUNTIME("format string is malformed: {}", format);
            }

            start_1             = braces_matcher.start(1);
            method_name_segment = (braces_matcher.start(2) != -1);

            if (method_name_segment) {
                argument_inspection = null;
            } else {
                String                      group_3 = braces_matcher.group(3);

                if (group_3 == null) {
                    if (automatic_index == -6) {
                        this.raise_both_automatic_and_manual_field_number();
                    }

                    automatic_index += 1;
                    argument_index  = automatic_index;
                } else {
                    if (automatic_index >= 0) {
                        this.raise_both_automatic_and_manual_field_number();
                    }

                    argument_index = Integer.parseInt(group_3);
                }

                argument_inspection = z.format_map.find(braces_matcher.group(4));
            }

            if (end_5 < start_1) {
                start_s = format.substring(end_5, start_1);

                this.append_segment(AdornmentSegmentFormatter.conjure(z, start_s));
            }

            if (argument_index == -1) {
                this.append_segment(MethodNameSegmentFormatter.conjure(z));
            } else {
                this.append_segment(argument_inspection.conjure_argument_segment(z, argument_index));
                add_used_index(argument_index);
            }

            end_5 = next_end_5;

            braces_matcher.region(end_5, format_total);

            if ( ! braces_matcher.lookingAt()) {
                break;
            }
        }

        if (end_5 < format_total) {
            String                      end_s = format.substring(end_5);

            this.append_segment(AdornmentSegmentFormatter.conjure(z, end_s));
        }

        this.examine_missing();

        if (false) {
            final Gem_StringBuilder     builder = z.conjure__StringBuilder();

            builder.append("format: ");
            builder.quote(format);

            z.output(builder.finish__AND__recycle());

            for (int                    i = 0; i < segment_total; i ++) {
                final SegmentFormattable    segment = segment_many[i];
                final Gem_StringBuilder     b2 = z.conjure__StringBuilder();

                b2.append(i, " :");
                b2.portray(segment);

                z.output(b2.finish__AND__recycle());
            }
        }

        int                             expected = this.used_index_total;

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
        int                         shrunk_total = segment_total;

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


    //
    //  Null any references (for garbage collection purposes)
    //
    //  NOTE:
    //      Not really useful, since all the same data is saved elsewhere, and will never be garbage collectd ...
    //      ...  However, doing this just on principle anyway ...
    //
    private void                        scrub()
    {
        int                             segment_total = this.segment_total;

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


    //
    //  Public static
    //
    public static MessageFormattable    parse_format(Zone z, String format)
    {
        ParseFormat                     parse_format = z.pop__parse_format__OR__null();

        if (parse_format == null) {
            parse_format = ParseFormat.create(z, format);
        } else {
            parse_format.recycle(format);
        }

        MessageFormattable              r =  parse_format.parse_format__work();

        parse_format.scrub();
        z.store_parse_format(parse_format);

        return r;
    }
}
