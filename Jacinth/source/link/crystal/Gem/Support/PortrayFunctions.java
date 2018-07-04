//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.Integer;
import java.lang.Object;
import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;


public abstract class   PortrayFunctions
    extends             Gem_Object//<Inspection>
//  extends             Object
{
    //
    //  Public Static
    //
    public static String                portray(Zone z, Object v)
    {
        if (v == null) {
            return "<null>";
        }

        if (v instanceof Inspectable) {
            return ((Inspectable) v).portray(z);
        }

        Class<?>                        v_class = v.getClass();

        if (v_class == Integer$class) {
            return v.toString();
        }

        if (v_class == String$class) {
            return (String) v;
        }

        if (v_class == Thread$class) {
            return "<" + v.toString() + ">";
        }

        if (v_class == Gem_StringBuilder$array$class)
        {
            Gem_StringBuilder[]     v2 = (Gem_StringBuilder[]) v;

            return z.arrange("<Gem_StringBuilder size<{0}>>", v2.length);
        }

        return "<" + v_class.getSimpleName() + ": " + v.toString() + ">";
    }


    public static String                quote_string(Zone z, String s)
    {
        if (s == null) {
            z.RUNTIME("quote_string: `s` is null");
        }

        Gem_StringBuilder               builder = null;
        int                             start = 0;
        int                             total = s.length();

        for (int                        i = 0; i < total; i ++) {
            int                         code_point = s.codePointAt(i);

            if (code_point == 34) {
                if (start < i) {
                    if (builder == null) {
                        builder = z.conjure__StringBuilder();

                        builder.append("\\\"");
                    }

                    builder.append(s.substring(start, i), "\\\"");
                    start = i + 1;
                    continue;
                }
            }

            if (code_point == 92) {
                if (start < i) {
                    if (builder == null) {
                        builder = z.conjure__StringBuilder();

                        builder.append("\\\"");
                    }

                    builder.append(s.substring(start, i), "\\\\");
                    start = i + 1;
                    continue;
                }
            }
        }

        if (builder == null) {
            return "\"" + s + "\"";
        }

        if (start < total) {
            builder.append(s.substring(start));
        }

        builder.append("\"");

        return builder.finish__AND__recycle();
    }


    public static String                quote_string_or_null(Zone z, String s)
    {
        if (s == null) {
            return "<null>";
        }

        return quote_string(z, s);
    }
}
