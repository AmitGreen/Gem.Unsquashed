//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.lang.Character;
import java.lang.StringBuilder;
import link.crystal.Gem.Core.Gem;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Exception.ExceptionFunctions;
import link.crystal.Gem.Format.ParseFormat;
import link.crystal.Gem.Inspection.Inspection;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Support.AsciiTable;


public final class  Gem_StringBuilder
    extends         Gem_Object <Inspection>
//  extends         Object
    implements      Inspectable<Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("Gem_StringBuilder");


    //
    //  Members
    //
    public  final Zone                  z;
    private final StringBuilder         builder;
    private /*:*/ boolean               finished;


    //
    //  Constructor, Factory, & Recycle
    //
    private                             Gem_StringBuilder(final Zone z, final StringBuilder builder)
    {
        this.z        = z;
        this.builder  = builder;
        this.finished = false;
    }


    public static final Gem_StringBuilder   create__ALLY__Zone(final Zone z)
    {
        final StringBuilder             builder = new StringBuilder();

        return new Gem_StringBuilder(z, builder);
    }


    public final Gem_StringBuilder      recycle()
    {
        final StringBuilder             builder = this.builder;

        builder.delete(0, builder.length());

        this.finished = false;

        return this;
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
        final StringBuilder             client = builder.builder;

        if (this == builder) {
            //
            //  NOTE:
            //      Special case, we are using this Gem_StringBuilder to show itself ...
            //
            builder.augment("<GemStringBuilder builder<{} of {}>; MYSELF>", client.length(), client.capacity());
            return;
        }

        builder.augment("<GemStringBuilder builder<{} of {}; {p}>>", client.length(), client.capacity(), client.toString());
    }


    //
    //  Public (append)
    //
    public final void                   append(final int v)
    {
        this.builder.append(v);
    }


    public final void                   append(final String s)
    {
        this.builder.append(s);
    }


    public final void                   append(final int a, final String b)
    {
        this.builder.append(a).append(b);
    }


    public final void                   append(final String a, final String b)
    {
        this.builder.append(a).append(b);
    }


    public final void                   append(final char a, final String b, final char c)
    {
        this.builder.append(a).append(b).append(c);
    }


    public final void                   append(final String a, final int b, final String c)
    {
        this.builder.append(a).append(b).append(c);
    }


    public final void                   append(final String a, final String b, final String c)
    {
        this.builder.append(a).append(b).append(c);
    }


    public final void                   append(final String a, final String b, final String c, final String d)
    {
        this.builder.append(a).append(b).append(c).append(d);
    }


    public final void                   append(final String a, final int b, final String c, final int d, final String e)
    {
        this.builder.append(a).append(b).append(c).append(d).append(e);
    }


    public final void                   append(
            final String                        a,
            final String                        b,
            final String                        c,
            final int                           d,
            final String                        e//,
        )
    {
        this.builder.append(a).append(b).append(c).append(d).append(e);
    }


    public final void                   append(
            final String                        a,
            final String                        b,
            final String                        c,
            final String                        d,
            final int                           e//,
        )
    {
        this.builder.append(a).append(b).append(c).append(d).append(e);
    }


    public final void                   append(
            final String                        a,
            final String                        b,
            final String                        c,
            final String                        d,
            final String                        e//,
        )
    {
        this.builder.append(a).append(b).append(c).append(d).append(e);
    }


    public final void                   append(
            final String                        a,
            final String                        b,
            final String                        c,
            final String                        d,
            final String                        e,
            final int                           f//,
        )
    {
        this.builder.append(a).append(b).append(c).append(d).append(e).append(f);
    }


    public final void                   append(
            final String                        a,
            final String                        b,
            final String                        c,
            final String                        d,
            final String                        e,
            final String                        f,
            final String                        g//,
        )
    {
        this.builder.append(a).append(b).append(c).append(d).append(e).append(f).append(g);
    }


    public final void                   append(
            final String                        a,
            final String                        b,
            final String                        c,
            final String                        d,
            final String                        e,
            final String                        f,
            final String                        g,
            final String                        h//,
        )
    {
        this.builder.append(a).append(b).append(c).append(d).append(e).append(f).append(g).append(h);
    }


    public final void                   append(
            final String                        a,
            final String                        b,
            final String                        c,
            final String                        d,
            final String                        e,
            final String                        f,
            final String                        g,
            final String                        h8,
            final String                        h9//,
        )
    {
        this.builder.append(a).append(b).append(c).append(d).append(e).append(f).append(g).append(h8).append(h9);
    }


    //
    //  Public (append sub-string)
    //
    public final void                   append_slice(final String s, final int offset)
    {
        final int                       total = s.length();

        assert fact_pointer(s, "s");
        assert fact_between(0, offset, total);

        if (offset < total) {
            this.builder.append(s, offset, total);
        }
    }


    public final void                   append_slice(final String s, final int offset, final int end_plus_1)
    {
        assert fact_pointer(s, "s");
        assert fact_between(0, offset, end_plus_1);
        assert fact_between(0, end_plus_1, s.length());

        if (offset < end_plus_1) {
            this.builder.append(s, offset, end_plus_1);
        }
    }


    //
    //  Public (augment)
    //
    public final void                   augment(final String format)
    {
        final Zone                      z = this.z;

        final MessageFormattable<?>     formattable = ParseFormat.parse_format(z, format);

        formattable.augment(this, 2);
    }


    public final void                   augment(final String format, final Object v)
    {
        final Zone                      z = this.z;

        final MessageFormattable<?>     formattable = ParseFormat.parse_format(z, format);

        formattable.augment(this, 2, v);
    }


    public final void                   augment(final String format, final Object v, final Object w)
    {
        final Zone                      z = this.z;

        final MessageFormattable<?>     formattable = ParseFormat.parse_format(z, format);

        formattable.augment(this, 2, v, w);
    }


    public final void                   augment(final String format, final Object v, final Object w, final Object x)
    {
        final Zone                      z = this.z;

        final MessageFormattable<?>     formattable = ParseFormat.parse_format(z, format);

        formattable.augment(this, 2, v, w, x);
    }


    public final void                   augment(
            final String                        format,
            final Object                        v,
            final Object                        w,
            final Object                        x,
            final Object                        y//
        )
    {
        final Zone                      z = this.z;

        final MessageFormattable<?>     formattable = ParseFormat.parse_format(z, format);

        formattable.augment(this, 2, v, w, x, y);
    }


    public final void                   augment(
            final String                        format,
            final Object                        v,
            final Object                        w,
            final Object                        x,
            final Object                        y4,
            final Object                        y5//,
        )
    {
        final Zone                      z = this.z;

        final MessageFormattable<?>     formattable = ParseFormat.parse_format(z, format);

        formattable.augment(this, 2, v, w, x, y4, y5);
    }


    public final void                   augment(
            final String                        format,
            final Object                        v,
            final Object                        w,
            final Object                        x,
            final Object                        y4,
            final Object                        y5,
            final Object                        y6//,
        )
    {
        final Zone                      z = this.z;

        final MessageFormattable<?>     formattable = ParseFormat.parse_format(z, format);

        formattable.augment(this, 2, v, w, x, y4, y5, y6);
    }


    public final void                   augment(
            final String                        format,
            final Object                        v,
            final Object                        w,
            final Object                        x,
            final Object                        y4,
            final Object                        y5,
            final Object                        y6,
            final Object                        y7,
            final Object ...                    other_arguments//,
        )
    {
        final Zone                      z = this.z;

        final MessageFormattable<?>     formattable = ParseFormat.parse_format(z, format);

        formattable.augment(this, 2, v, w, x, y4, y5, y6, y7, other_arguments);
    }


    //
    //  Public (others)
    //
    public final String                 finish_AND_keep()
    {
        assert fact( ! this.finished, "! this.finished");

        this.finished = true;

        return this.builder.toString();
    }


    public final String                 finish_AND_recycle()
    {
        assert fact( ! this.finished, "! this.finished");

        this.finished = true;

        this.z.recycle__StringBuilder__ALLY__Gem_StringBuilder(this);

        return this.builder.toString();
    }


    public final void                   format(final Object v)
    {
        if (v == null) {
            this.builder.append("<null>");
            return;
        }

        if (v instanceof Inspectable) {
            ((Inspectable) v).portray(this);
            return;
        }

        final Class<?>                  v_class = v.getClass();

        if (v_class == Gem.Integer$class) {
            this.builder.append((Integer) v);
            return;
        }

        if (v_class == Gem.String$class) {
            this.builder.append((String) v);
            return;
        }

        if (v_class == Gem.Thread$class) {
            this.builder.append("<").append(v.toString()).append(">");
            return;
        }

        if (v_class == Gem.Gem_StringBuilder$array$class)
        {
            final Gem_StringBuilder[]   v2 = (Gem_StringBuilder[]) v;

            this.augment("<Gem_StringBuilder size{p}>", v2.length);
            return;
        }

        /*:*/ String                class_name = v_class.getSimpleName();

        if (class_name.equals("")) {
            class_name = v_class.getName();
        }

        this.builder.append("<").append(class_name).append(": ").append(v.toString()).append(">");
    }


    public final void                   java_quote(final String s)
    {
        assert fact_pointer(s, "s");

        final StringBuilder             builder = this.builder;

        final AsciiTable[]              table = AsciiTable.table_with_boring_apostrophe;

        builder.append("\"");

        /*:*/ int                       begin = 0;
        final int                       total = s.length();

        for (/*:*/ int                  i = 0; i < total; /*  i is incremented in the loop by 1 or 2  */) {
            final int                   code_point = s.codePointAt(i);

            if (code_point >= 128) {
                i += Character.charCount(code_point);
                continue;
            }

            i ++;

            AsciiTable              ascii = table[code_point];

            if (ascii.is_boring_printable) {
                continue;
            }

            if (begin < i) {
                builder.append(s, begin, i);                            //  append sub-string
                begin = i;
            }

            builder.append(ascii.portray_0);
        }

        if (begin < total) {
            builder.append(s, begin, total);                            //  append sub-string
        }

        builder.append("\"");
    }


    public final void                   portray(final Object v)
    {
        if (v == null) {
            this.builder.append("<null>");
            return;
        }

        if (v instanceof Inspectable) {
            ((Inspectable) v).portray(this);
            return;
        }

        final Class<?>                  v_class = v.getClass();

        if (v_class == Gem.Integer$class) {
            this.builder.append("<int ").append((Integer) v).append(">");
            return;
        }

        if (v_class == Gem.String$class) {
            this.java_quote((String) v);
            return;
        }

        if (v_class == Gem.Thread$class) {
            this.builder.append("<").append(v.toString()).append(">");
            return;
        }

        if (v_class == Gem.Gem_StringBuilder$array$class)
        {
            final Gem_StringBuilder[]   v2 = (Gem_StringBuilder[]) v;

            this.augment("<Gem_StringBuilder size{p}>", v2.length);
            return;
        }

        /*:*/ String                class_name = v_class.getSimpleName();

        if (class_name.equals("")) {
            class_name = v_class.getName();
        }

        this.builder.append("<").append(class_name).append(": ").append(v.toString()).append(">");
    }
}
