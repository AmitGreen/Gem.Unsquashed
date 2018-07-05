//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.lang.StringBuilder;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Support.Storehouse_MessageFormattable;


public class    Gem_StringBuilder
    extends     Gem_Object<Inspection>
//  extends     Object
    implements  Inspectable<Inspection>//,
{
    private static Inspection           inspection = Inspection.create_with_portrait("Gem_StringBuilder");


    //
    //  Members
    //
    public final Zone                   z;
    private final StringBuilder         builder;
    private boolean                     finished;


    //
    //  Constructor, Factory, & Recycle
    //
    private                             Gem_StringBuilder(Zone z, StringBuilder builder)
    {
        this.z        = z;
        this.builder  = builder;
        this.finished = false;
    }


    public static Gem_StringBuilder     create__ALLY__Gem_Zone(Zone z)
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


    //
    //  Public (arrange)
    //
    public void                         arrange(String format)
    {
        final Zone                      z = this.z;

        MessageFormattable              formattable = Storehouse_MessageFormattable.lookup(z, format);

        if (formattable == null) {
            formattable = ParseFormat.parse_format(z, format);

            Storehouse_MessageFormattable.insert(z, format, formattable);
        }

        formattable.arrange(this, 2);
    }


    public void                         arrange(String format, Object v)
    {
        final Zone                      z = this.z;

        MessageFormattable              formattable = Storehouse_MessageFormattable.lookup(z, format);

        if (formattable == null) {
            formattable = ParseFormat.parse_format(z, format);

            Storehouse_MessageFormattable.insert(z, format, formattable);
        }

        formattable.arrange(this, 2, v);
    }


    public void                         arrange(String format, Object v, Object w)
    {
        final Zone                      z = this.z;

        MessageFormattable              formattable = Storehouse_MessageFormattable.lookup(z, format);

        if (formattable == null) {
            formattable = ParseFormat.parse_format(z, format);

            Storehouse_MessageFormattable.insert(z, format, formattable);
        }

        formattable.arrange(this, 2, v, w);
    }


    public void                         arrange(String format, Object v, Object w, Object x)
    {
        final Zone                      z = this.z;

        MessageFormattable              formattable = Storehouse_MessageFormattable.lookup(z, format);

        if (formattable == null) {
            formattable = ParseFormat.parse_format(z, format);

            Storehouse_MessageFormattable.insert(z, format, formattable);
        }

        formattable.arrange(this, 2, v, w, x);
    }


    public void                         arrange(
            String                              format,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y//
        )
    {
        final Zone                      z = this.z;

        MessageFormattable              formattable = Storehouse_MessageFormattable.lookup(z, format);

        if (formattable == null) {
            formattable = ParseFormat.parse_format(z, format);

            Storehouse_MessageFormattable.insert(z, format, formattable);
        }

        formattable.arrange(this, 2, v, w, x, y);
    }


    public void                         arrange(
            String                              format,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5//,
        )
    {
        final Zone                      z = this.z;

        MessageFormattable              formattable = Storehouse_MessageFormattable.lookup(z, format);

        if (formattable == null) {
            formattable = ParseFormat.parse_format(z, format);

            Storehouse_MessageFormattable.insert(z, format, formattable);
        }

        formattable.arrange(this, 2, v, w, x, y4, y5);
    }


    public void                         arrange(
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

        MessageFormattable              formattable = Storehouse_MessageFormattable.lookup(z, format);

        if (formattable == null) {
            formattable = ParseFormat.parse_format(z, format);

            Storehouse_MessageFormattable.insert(z, format, formattable);
        }

        formattable.arrange(this, 2, v, w, x, y4, y5, y6);
    }


    public void                         arrange(
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

        MessageFormattable              formattable = Storehouse_MessageFormattable.lookup(z, format);

        if (formattable == null) {
            formattable = ParseFormat.parse_format(z, format);

            Storehouse_MessageFormattable.insert(z, format, formattable);
        }

        formattable.arrange(this, 2, v, w, x, y4, y5, y6, y7, other_arguments);
    }


    //
    //  Public (others)
    //
    public String                       finish__AND__recycle()
    {
        if (this.finished) {
            this.z.RUNTIME("`.finished` already set");
        }

        this.finished = true;

        this.z.recycle__StringBuilder(this);

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

        Class<?>                        v_class = v.getClass();

        if (v_class == Integer$class) {
            this.builder.append((Integer) v);
            return;
        }

        if (v_class == String$class) {
            this.builder.append((String) v);
            return;
        }

        if (v_class == Thread$class) {
            this.builder.append("<").append(v.toString()).append(">");
            return;
        }

        if (v_class == Gem_StringBuilder$array$class)
        {
            Gem_StringBuilder[]     v2 = (Gem_StringBuilder[]) v;

            this.builder.append(z.arrange("<Gem_StringBuilder size<{0}>>", v2.length));
            return;
        }

        this.builder.append("<").append(v_class.getSimpleName()).append(": ").append(v.toString()).append(">");
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

        Class<?>                        v_class = v.getClass();

        if (v_class == Integer$class) {
            this.builder.append((Integer) v);
            return;
        }

        if (v_class == String$class) {
            this.quote((String) v);
            return;
        }

        if (v_class == Thread$class) {
            this.builder.append("<").append(v.toString()).append(">");
            return;
        }

        if (v_class == Gem_StringBuilder$array$class)
        {
            Gem_StringBuilder[]     v2 = (Gem_StringBuilder[]) v;

            this.builder.append(z.arrange("<Gem_StringBuilder size<{0}>>", v2.length));
            return;
        }

        this.builder.append("<").append(v_class.getSimpleName()).append(": ").append(v.toString()).append(">");
    }


    public void                         quote(String s)
    {
        if (s == null) {
            final Zone                  z = this.z;

            z.RUNTIME("`s` is null");
        }

        builder.append("\"");

        int                             start = 0;
        int                             total = s.length();

        for (int                        i = 0; i < total; i ++) {
            int                         code_point = s.codePointAt(i);

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
