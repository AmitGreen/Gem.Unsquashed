//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.lang.StringBuilder;
import link.crystal.Gem.Core.Gem;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Exception.ExceptionFunctions;
import link.crystal.Gem.Format.ParseFormat;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Inspection.Inspection;


public class    Gem_StringBuilder
    extends     Gem_Object <Inspection>
//  extends     Object
    implements  Inspectable<Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("Gem_StringBuilder");


    //
    //  Members
    //
    public  final Zone                  z;
    private final StringBuilder         builder;
    private       boolean               finished;


    //
    //  Constructor, Factory, & Recycle
    //
    private                             Gem_StringBuilder(Zone z, StringBuilder builder)
    {
        this.z        = z;
        this.builder  = builder;
        this.finished = false;
    }


    public static Gem_StringBuilder     create__ALLY__Zone(Zone z)
    {
        final StringBuilder             builder = new StringBuilder();

        return new Gem_StringBuilder(z, builder);
    }


    public Gem_StringBuilder            recycle()
    {
        final StringBuilder             builder = this.builder;

        builder.delete(0, builder.length());

        this.finished = false;

        return this;
    }


    //
    //  Interface Inspectable
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }


    @Override
    public void                         portray(Gem_StringBuilder builder)
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
    public void                         append(int v)
    {
        this.builder.append(v);
    }


    public void                         append(String s)
    {
        this.builder.append(s);
    }


    public void                         append(int a, String b)
    {
        this.builder.append(a).append(b);
    }


    public void                         append(String a, String b)
    {
        this.builder.append(a).append(b);
    }


    public void                         append(String a, int b, String c)
    {
        this.builder.append(a).append(b).append(c);
    }


    public void                         append(String a, String b, String c)
    {
        this.builder.append(a).append(b).append(c);
    }


    public void                         append(String a, String b, String c, String d)
    {
        this.builder.append(a).append(b).append(c).append(d);
    }


    public void                         append(String a, int b, String c, int d, String e)
    {
        this.builder.append(a).append(b).append(c).append(d).append(e);
    }


    public void                         append(String a, String b, String c, int d, String e)
    {
        this.builder.append(a).append(b).append(c).append(d).append(e);
    }


    public void                         append(String a, String b, String c, String d, int e)
    {
        this.builder.append(a).append(b).append(c).append(d).append(e);
    }


    public void                         append(String a, String b, String c, String d, String e)
    {
        this.builder.append(a).append(b).append(c).append(d).append(e);
    }


    public void                         append(String a, String b, String c, String d, String e, int f)
    {
        this.builder.append(a).append(b).append(c).append(d).append(e).append(f);
    }


    //
    //  Public (augment)
    //
    public void                         augment(String format)
    {
        final Zone                      z = this.z;

        final MessageFormattable<?>     formattable = ParseFormat.parse_format(z, format);

        formattable.augment(this, 2);
    }


    public void                         augment(String format, Object v)
    {
        final Zone                      z = this.z;

        final MessageFormattable<?>     formattable = ParseFormat.parse_format(z, format);

        formattable.augment(this, 2, v);
    }


    public void                         augment(String format, Object v, Object w)
    {
        final Zone                      z = this.z;

        final MessageFormattable<?>     formattable = ParseFormat.parse_format(z, format);

        formattable.augment(this, 2, v, w);
    }


    public void                         augment(String format, Object v, Object w, Object x)
    {
        final Zone                      z = this.z;

        final MessageFormattable<?>     formattable = ParseFormat.parse_format(z, format);

        formattable.augment(this, 2, v, w, x);
    }


    public void                         augment(
            String                              format,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y//
        )
    {
        final Zone                      z = this.z;

        final MessageFormattable<?>     formattable = ParseFormat.parse_format(z, format);

        formattable.augment(this, 2, v, w, x, y);
    }


    public void                         augment(
            String                              format,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5//,
        )
    {
        final Zone                      z = this.z;

        final MessageFormattable<?>     formattable = ParseFormat.parse_format(z, format);

        formattable.augment(this, 2, v, w, x, y4, y5);
    }


    public void                         augment(
            String                              format,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5,
            Object                              y6//,
        )
    {
        final Zone                      z = this.z;

        final MessageFormattable<?>     formattable = ParseFormat.parse_format(z, format);

        formattable.augment(this, 2, v, w, x, y4, y5, y6);
    }


    public void                         augment(
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
        final Zone                      z = this.z;

        final MessageFormattable<?>     formattable = ParseFormat.parse_format(z, format);

        formattable.augment(this, 2, v, w, x, y4, y5, y6, y7, other_arguments);
    }


    //
    //  Public (others)
    //
    public String                       finish_AND_keep()
    {
        assert fact( ! this.finished, "! this.finished");

        this.finished = true;

        return this.builder.toString();
    }


    public String                       finish_AND_recycle()
    {
        assert fact( ! this.finished, "! this.finished");

        this.finished = true;

        this.z.recycle__StringBuilder__ALLY__Gem_StringBuilder(this);

        return this.builder.toString();
    }


    public void                         format(Object v)
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

        String                      class_name = v_class.getSimpleName();

        if (class_name.equals("")) {
            class_name = v_class.getName();
        }

        this.builder.append("<").append(class_name).append(": ").append(v.toString()).append(">");
    }


    public void                         portray(Object v)
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
            this.quote((String) v);
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

        String                      class_name = v_class.getSimpleName();

        if (class_name.equals("")) {
            class_name = v_class.getName();
        }

        this.builder.append("<").append(class_name).append(": ").append(v.toString()).append(">");
    }


    public void                         quote(String s)
    {
        assert fact_pointer(s, "s");

        builder.append("\"");

        int                             start = 0;
        final int                       total = s.length();

        for (int                        i = 0; i < total; i ++) {
            final int                   code_point = s.codePointAt(i);

            if (code_point == 34) {
                if (start < i) {
                    builder.append(s.substring(start, i)).append("\\\"");
                    start = i + 1;
                    continue;
                }
            }

            if (code_point == 92) {
                if (start < i) {
                    builder.append(s.substring(start, i)).append("\\\\");
                    start = i + 1;
                    continue;
                }
            }
        }

        if (start < total) {
            builder.append(s.substring(start));
        }

        builder.append("\"");
    }
}
