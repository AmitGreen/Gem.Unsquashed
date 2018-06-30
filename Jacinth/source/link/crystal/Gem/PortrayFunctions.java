//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem;


import java.lang.Object;
import java.lang.RuntimeException;
import java.lang.String;
import java.lang.StringBuilder;
import link.crystal.Gem.GemObject;


public abstract class   PortrayFunctions
    extends             GemObject
{
    //
    //  Public Static
    //
    public static String                portray(Object v)
    {
        Class<?>                        v_class = v.getClass();

        if (v_class == String$class) {
            return (String) v;
        }

        throw new RuntimeException("unknown class: " + v_class.getSimpleName());

        //return "<" + v_class.getSimpleName() + ">";
    }


    public static String                portray_string(String s)
    {
        if (s == null) {
            throw new RuntimeException("PortrayFunctions.portray_string: `s` is null");
        }

        StringBuilder                   b     = null;
        int                             start = 0;
        int                             total = s.length();

        for (int                        i = 0; i < total; i ++) {
            int                         code_point = s.codePointAt(i);

            if (code_point == 34) {
                if (start < i) {
                    if (b == null) {
                        b = new StringBuilder(1 + 2 * total + 1);

                        b.append("\\\"");
                    }

                    b.append(s.substring(start, i));
                    b.append("\\\"");
                    start = i + 1;
                    continue;
                }
            }

            if (code_point == 92) {
                if (start < i) {
                    if (b == null) {
                        b = new StringBuilder(1 + 2 * total + 1);

                        b.append("\\\"");
                    }

                    b.append(s.substring(start, i));
                    b.append("\\\\");
                    start = i + 1;
                    continue;
                }
            }
        }

        if (b == null) {
            return "\"" + s + "\"";
        }

        b.append(s.substring(start));
        b.append("\"");

        return b.toString();
    }


    public static String                portray_string_or_null(String s)
    {
        if (s == null) {
            return "<null>";
        }

        return portray_string(s);
    }
}
