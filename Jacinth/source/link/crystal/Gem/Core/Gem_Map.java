//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.util.HashMap;
import link.crystal.Gem.Core.Gem;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Exception.ExceptionFunctions;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Inspection.Inspection;


public abstract class   Gem_Map     <INSPECTION extends Inspection, K, V>
    extends             HashMap                                    <K, V>
//  extends             AbstractHashMap                            <K, V>
//  extends             Object
    implements          Inspectable<INSPECTION>//,
{
    //
    //  Members
    //
    protected final Zone                z;


    //
    //  Constructor
    //
    protected                           Gem_Map(final Zone z, final int initial_capacity)
    {
        super(initial_capacity);

        this.z = z;
    }


    //
    //  Interface Inspectable
    //
    public abstract INSPECTION          inspect();
    public abstract void                portray(final Gem_StringBuilder builder);


    //
    //  Abstract
    //
    public abstract void                dump(final String name);


    //
    //  Public (ASSERT)
    //
    public static final boolean         fact(boolean condition, final String format)
    {
        if (condition) {
            return true;
        }

        ExceptionFunctions.ASSERTION_FAILED(2, "assertion failed: {}", format);

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

        final Zone                      z = Zone.current_zone();

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


    public final void                   RUNTIME(final String error_message, final Object ... arguments)
    {
        ExceptionFunctions.RUNTIME(2, error_message, arguments);
    }


    //
    //  Public (line)
    //
    public static final void            line()
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
    public final V                      lookup(final Zone z, final K k)
    {
        assert fact        (this.z == z, "this.z == z");
        assert fact_pointer(k, "k");

        return this.get(k);
    }


    public final void                   insert(final Zone z, final K k, final V v)
    {
        assert fact        (this.z == z, "this.z == z");
        assert fact_pointer(k, "k");
        assert fact_pointer(v, "v");

        final V                         previous = this.putIfAbsent(k, v);

        if (previous != null) {
            RUNTIME("previous value for {} already exists: {}", k, v);
        }
    }


    public static final void            output(final String s)
    {
        Gem.output(s);
    }
}
