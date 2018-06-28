//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.util.ArrayList;
import link.crystal.Gem.Core.Gem;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Exception.ExceptionFunctions;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Inspection.Inspection;


public abstract class   Gem_List    <INSPECTION extends Inspection, ELEMENT>
    extends             ArrayList                                  <ELEMENT>
//  extends             AbstractList                               <ELEMENT>
//  extends             AbstractCollection                         <ELEMENT>
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
    protected                           Gem_List(final Zone z, final int initial_capacity)
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


    public static final void            line(final String format, final Object v, final Object ... other_arguments)
    {
        Gem.line_1_plus(2, format, v, other_arguments);
    }


    //
    //  Public (other)
    //
    public static final void            output(final String s)
    {
        Gem.output(s);
    }
}
