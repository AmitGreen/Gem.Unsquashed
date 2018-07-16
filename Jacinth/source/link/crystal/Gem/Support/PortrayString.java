//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Inspection.Inspection;
import link.crystal.Gem.Interface.Inspectable;


public abstract class   PortrayString
    extends             Gem_Object <Inspection>
    implements          Inspectable<Inspection>//,
{
    //
    //  Static members
    //
    public static final PortrayString   backslash_with_apostrophe = (
            PortrayString_Backslash.create__ALLY__PortrayString("'", "'", 39)   //  39 = ordinal("'")
        );

    public static final PortrayString   backslash_with_quotation_mark = (
            PortrayString_Backslash.create__ALLY__PortrayString("'", "'", 34)   //  34 = ordinal('"')
        );

    public static final PortrayString   normal_with_apostrophe = (
            PortrayString_Normal.create__ALLY__PortrayString("'", "'")
        );

    public static final PortrayString   normal_with_quotation_mark = (
            PortrayString_Normal.create__ALLY__PortrayString("\"", "\"")
        );

    public static final PortrayString   normal_with_triple_apostrophe = (
            PortrayString_Normal.create__ALLY__PortrayString("'''", "'''")
        );

    public static final PortrayString   normal_with_triple_quotation_mark = (
            PortrayString_Normal.create__ALLY__PortrayString("\"\"\"", "\"\"\"")
        );

    public static final PortrayString   raw_with_apostrophe = (
            PortrayString_Normal.create__ALLY__PortrayString("r'", "'")
        );

    public static final PortrayString   raw_with_quotation_mark = (
            PortrayString_Normal.create__ALLY__PortrayString("r\"", "\"")
        );

    public static final PortrayString   raw_with_triple_apostrophe = (
            PortrayString_Normal.create__ALLY__PortrayString("r'''", "'''")
        );

    public static final PortrayString   raw_with_triple_quotation_mark = (
            PortrayString_Normal.create__ALLY__PortrayString("r\"\"\"", "\"\"\"")
        );


    //
    //  Abstract <me>
    //
    public abstract void                portray_string(final Gem_StringBuilder builder, final String s);


    //
    //  Public
    //
    public /*overrideable*/ String      portray_string(final String s)
    {
        final Zone                      z = Zone.current_zone();

        final Gem_StringBuilder         builder = z.summon_StringBuilder();

        this.portray_string(builder, s);

        return builder.finish_AND_recycle();
    }
}


final class             PortrayString_Backslash
    extends             PortrayString
//  extends             Gem_Object <Inspection>
    implements          Inspectable<Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("PortrayString_Backslash");


    //
    //  Members
    //
    private final String                prefix;
    private final String                suffix;
    private final int                   quote_code_point;


    //
    //  Constructor & Factory
    //
    private                             PortrayString_Backslash(
            final String                        prefix,
            final String                        suffix,
            final int                           quote_code_point//,
        )
    {
        this.prefix           = prefix;
        this.suffix           = suffix;
        this.quote_code_point = quote_code_point;
    }


    public static final PortrayString_Backslash     create__ALLY__PortrayString(
            final String                        prefix,
            final String                        suffix,
            final int                           quote_code_point//,
        )
    {
        return new PortrayString_Backslash(prefix, suffix, quote_code_point);
    }


    //
    //  Interface Inspectable
    //
    @Override
    public final Inspection             inspect()
    {
        return /*static*/ this.inspection;
    }


    public final void                   portray(final Gem_StringBuilder builder)
    {
        builder.append("<PortrayString_Backslash ");
        builder.quote(this.prefix);
        builder.append(" ");
        builder.quote(this.suffix);
        builder.append(">");
    }


    //
    //  Abstract PortrayString
    //
    public final void                   portray_string(final Gem_StringBuilder builder, final String s)
    {
        final int                       quote_code_point = this.quote_code_point;

        final AsciiTable[]              table = AsciiTable.table;

        builder.append(this.prefix);

        /*:*/ int                       start = 0;
        final int                       total = s.length();

        for (/*:*/ int                  i = 0; i < total; /*  i is incremented in the loop by 1 or 2  */) {
            final int                   code_point = s.codePointAt(i);

            if (code_point < 128) {
                AsciiTable              ascii = table[code_point];

                if (ascii.is_boring_printable || code_point == quote_code_point) {
                    i ++;
                    continue;
                }

                if (start < i) {
                    builder.append_sub_string(s, start, i);
                }

                assert fact_pointer(ascii.portray_0, "ascii.portray_0");

                builder.append(ascii.portray_0);

                i ++;

                start = i;

                continue;
            }

            i += Character.charCount(code_point);
        }

        if (start < total) {
            builder.append_sub_string(s, start);
        }

        builder.append(this.suffix);
    }
}


final class             PortrayString_Normal
    extends             PortrayString
//  extends             Gem_Object <Inspection>
    implements          Inspectable<Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("PortrayString_Normal");


    //
    //  Members
    //
    private final String                prefix;
    private final String                suffix;


    //
    //  Constructor & Factory
    //
    protected                           PortrayString_Normal(final String prefix, final String suffix)
    {
        this.prefix = prefix;
        this.suffix = suffix;
    }


    public static final PortrayString_Normal    create__ALLY__PortrayString(final String prefix, final String suffix)
    {
        return new PortrayString_Normal(prefix, suffix);
    }


    //
    //  Interface Inspectable
    //
    @Override
    public final Inspection             inspect()
    {
        return /*static*/ this.inspection;
    }


    @Override
    public final void                   portray(final Gem_StringBuilder builder)
    {
        builder.append("<PortrayString_Normal ");
        builder.quote(this.prefix);
        builder.append(" ");
        builder.quote(this.suffix);
        builder.append(">");
    }


    //
    //  Abstract PortrayString
    //
    public final void                   portray_string(final Gem_StringBuilder builder, final String s)
    {
        builder.append(this.prefix, s, this.suffix);
    }


    //
    //  Public
    //
    @Override
    public final String                 portray_string(final String s)
    {
        return this.prefix + s + this.suffix;
    }


}


final class             PortrayString_TripleWithBackslash
    extends             PortrayString
//  extends             Gem_Object <Inspection>
    implements          Inspectable<Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("PortrayString_TripleWithBackslash");


    //
    //  Members
    //
    private final boolean               apostrophe;
    private final String                prefix;
    private final EphemeralStringState  first_state;
    private final EphemeralStringState  second_state;


    //
    //  Constructor & Factory
    //
    private                             PortrayString_TripleWithBackslash(
            final boolean                       apostrophe,
            final String                        prefix,
            final EphemeralStringState          first_state,
            final EphemeralStringState          second_state//,
        )
    {
        this.apostrophe   = apostrophe;
        this.prefix       = prefix;
        this.first_state  = first_state;
        this.second_state = second_state;
    }


    public static final PortrayString_TripleWithBackslash   create__ALLY__PortrayString(
            final boolean                       apostrophe,
            final String                        prefix,
            final EphemeralStringState          first_state,
            final EphemeralStringState          second_state//,
        )
    {
        return new PortrayString_TripleWithBackslash(apostrophe, prefix, first_state, second_state);
    }


    //
    //  Interface Inspectable
    //
    @Override
    public final Inspection             inspect()
    {
        return /*static*/ this.inspection;
    }


    public final void                   portray(final Gem_StringBuilder builder)
    {
        builder.append("<PortrayString_TripleWithBackslash ", (this.apostrophe ? "apostrope" : "quotation_mark"));
        builder.quote(this.prefix);
        builder.append(" ", this.first_state.debug_name, " ", this.second_state.debug_name, ">");
    }


    //
    //  Abstract PortrayString
    //
    public final void                   portray_string(final Gem_StringBuilder builder, final String s)
    {
        builder.append(this.prefix);

        final boolean                   apostrophe   = this.apostrophe;
        final EphemeralStringState      first_state  = this.first_state;
        final EphemeralStringState      second_state = this.second_state;

        /*:*/ int                       start = 0;
        final int                       total = s.length();
        /*:*/ EphemeralStringState      state = first_state;

        for (/*:*/ int                  i = 0; i < total; /*  i is incremented in the loop by 1 or 2  */) {
            final int                   code_point = s.codePointAt(i);

            if (code_point < 128) {
                AsciiTable              ascii = /*table[code_point]*/null;

                if (ascii.is_boring_printable /*|| code_point == quote_code_point*/) {
                    i ++;
                    continue;
                }

                if (start < i) {
                    builder.append_sub_string(s, start, i);
                }

                i ++;

                start = i;

                if (apostrophe) {
                    if (code_point == 39) {                             //  39 = ordinal("'")
                        String previous = /*portray_inside_triple.get(state)*/null;

                        if (previous != null) {
                            builder.append(previous);
                        }

                        state = state.A;
                        continue;
                    }
                } else {
                    if (code_point == 34) {                             //  34 = ordinal('"')
                        String previous = /*portray_inside_triple.get(state)*/null;

                        if (previous != null) {
                            builder.append(previous);
                        }

                        state = state.Q;
                        continue;
                    }
                }

                assert fact_pointer(ascii.portray_0, "ascii.portray_0");

                builder.append(ascii.portray_0);

                start = i;

                continue;
            }

            i += Character.charCount(code_point);

            if (state != second_state) {
                if (state != null) {
                    builder.append(/*portray_inside_tripe.get(state)*/"?");
                }

                state = second_state;
            }
        }

        if (start < total) {
            builder.append_sub_string(s, start);
        }

        builder.append(/*this.suffix*/null);
    }
}
