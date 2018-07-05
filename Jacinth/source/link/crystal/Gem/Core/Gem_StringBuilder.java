//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.lang.StringBuilder;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;


public class    Gem_StringBuilder
    extends     Gem_Object<Inspection>
//  extends     Object
    implements  Inspectable<Inspection>//,
{
    private static Inspection           inspection = Inspection.create_with_portrait("Gem.Core.Gem_StringBuilder");


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


    public String                       portray(Zone z)
    {
        return "<Gem.Core.Gem_StringBuilder>";
    }


    //
    //  Public
    //
    public void                         append(int v)
    {
        this.builder.append(v);
    }


    public void                         append(String s)
    {
        this.builder.append(s);
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


    public void                         append(String a, String b, String c, int d, String e)
    {
        this.builder.append(a).append(b).append(c).append(d).append(e);
    }


    public void                         append(String a, String b, String c, String d, String e)
    {
        this.builder.append(a).append(b).append(c).append(d).append(e);
    }


    public void                         append(String a, String b, String c, String d, int e)
    {
        this.builder.append(a).append(b).append(c).append(d).append(e);
    }


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
        final StringBuilder             builder = this.builder;

        if (v == null) {
            builder.append("<null>");
            return;
        }

        if (v instanceof Inspectable) {
            final Zone                   z = this.z;

            builder.append(((Inspectable) v).portray(z));
            return;
        }

        Class<?>                        v_class = v.getClass();

        if (v_class == Integer$class) {
            builder.append((Integer) v);
            return;
        }

        if (v_class == String$class) {
            builder.append((String) v);
            return;
        }

        if (v_class == Thread$class) {
            builder.append("<").append(v.toString()).append(">");
            return;
        }

        if (v_class == Gem_StringBuilder$array$class)
        {
            Gem_StringBuilder[]     v2 = (Gem_StringBuilder[]) v;

            builder.append(z.arrange("<Gem_StringBuilder size<{0}>>", v2.length));
            return;
        }

        builder.append("<").append(v_class.getSimpleName()).append(": ").append(v.toString()).append(">");
        return;
    }

}
