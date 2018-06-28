//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.lang.Object;
import java.lang.System;
import link.crystal.Gem.Core.Gem;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Exception.ExceptionFunctions;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Inspection.Inspection;


public abstract class   Gem_Object <INSPECTION extends Inspection>
    extends             Object
    implements          Inspectable<INSPECTION>//,
{
    //
    //  Interface Inspectable
    //
    public abstract INSPECTION          inspect();


    @Override
    public /*overrideable*/ void        portray(final Gem_StringBuilder builder)
    {
        final INSPECTION                inspection = this.inspect();

        builder.append("<", inspection.simple_class_name, ">");
    }


    //
    //  Public (ASSERT)
    //
    public static final boolean         fact(boolean condition, final String format)
    {
        if (condition) {
            return true;
        }

        ExceptionFunctions.ASSERTION_FAILED(2, format);

        return false;
    }


    public static final boolean         fact(boolean condition, final String format, final Object v)
    {
        if (condition) {
            return true;
        }

        ExceptionFunctions.ASSERTION_FAILED(2, format, v);

        return false;
    }


    public static final boolean         fact_between(final int start, final int v, final int end)
    {
        if (start <= v && v <= end) {
            return true;
        }

        ExceptionFunctions.ASSERT(2, "{} is not between {} and {}", v, start, end);

        return false;
    }


    public static final boolean         fact_null(final Object p, final String name)
    {
        if (p == null) {
            return true;
        }

        ExceptionFunctions.ASSERT(2, "`{}` is not null", name);

        return false;
    }


    public static final boolean         fact_pointer(final Object p, final String name)
    {
        if (p != null) {
            return true;
        }

        ExceptionFunctions.ASSERT(2, "`{}` is null", name);

        return false;
    }


    //
    //  Public (ERRORS)
    //
    public static final void            INVALID_ROUTINE()
    {
        ExceptionFunctions.RUNTIME(2, "invalid routine");
    }


    public static final void            RUNTIME(final String error_message, final Object ... arguments)
    {
        ExceptionFunctions.RUNTIME(2, error_message, arguments);
    }


    //
    //  Public (arrange)
    //
    public static final String          arrange(final String format)
    {
        return Gem.arrange(2, format);
    }


    public static final String          arrange(final String format, final Object v)
    {
        return Gem.arrange(2, format, v);
    }


    public static final String          arrange(final String format, final Object v, final Object w)
    {
        return Gem.arrange(2, format, v, w);
    }


    public static final String          arrange(final String format, final Object v, final Object w, final Object x)
    {
        return Gem.arrange(2, format, v, w, x);
    }


    public static final String          arrange(
            final String                        format,
            final Object                        v,
            final Object                        w,
            final Object                        x,
            final Object                        y//
        )
    {
        return Gem.arrange(2, format, v, w, x, y);
    }


    public static final String          arrange(
            final String                        format,
            final Object                        v,
            final Object                        w,
            final Object                        x,
            final Object                        y4,
            final Object                        y5//,
        )
    {
        return Gem.arrange(2, format, v, w, x, y4, y5);
    }


    public static final String          arrange(
            final String                        format,
            final Object                        v,
            final Object                        w,
            final Object                        x,
            final Object                        y4,
            final Object                        y5,
            final Object                        y6//,
        )
    {
        return Gem.arrange(2, format, v, w, x, y4, y5, y6);
    }


    public static final String          arrange(
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
        return Gem.arrange(2, format, v, w, x, y4, y5, y6, y7, other_arguments);
    }


    //
    //  Public (line)
    //
    public static /*overrideable*/ void     line()
    {
        Gem.line();
    }


    public static final void            line(final String format)
    {
        Gem.line(2, format);
    }


    public static final void            line(final String format, final Object v)
    {
        Gem.line(2, format, v);
    }


    public static final void            line(final String format, final Object v, final Object w)
    {
        Gem.line(2, format, v, w);
    }


    public static final void            line(final String format, final Object v, final Object w, final Object x)
    {
        Gem.line(2, format, v, w, x);
    }


    public static final void            line(
            final String                        format,
            final Object                        v,
            final Object                        w,
            final Object                        x,
            final Object                        y//,
        )
    {
        Gem.line(2, format, v, w, x, y);
    }


    public static final void            line(
            final String                        format,
            final Object                        v,
            final Object                        w,
            final Object                        x,
            final Object                        y4,
            final Object                        y5//,
        )
    {
        Gem.line(2, format, v, w, x, y4, y5);
    }


    public static final void            line(
            final String                        format,
            final Object                        v,
            final Object                        w,
            final Object                        x,
            final Object                        y4,
            final Object                        y5,
            final Object                        y6//,
        )
    {
        Gem.line(2, format, v, w, x, y4, y5, y6);
    }


    public static final void            line(
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
        Gem.line(2, format, v, w, x, y4, y5, y6, y7, other_arguments);
    }


    //
    //  Public (other)
    //
    public static /*overrideable*/ int  limit_to_between(final int minimum, final int v, final int maximum)
    {
        return Gem.limit_to_between(minimum, v, maximum);
    }


    public static /*overrideable*/ void     output(final String s)
    {
        Gem.output(s);
    }
}
