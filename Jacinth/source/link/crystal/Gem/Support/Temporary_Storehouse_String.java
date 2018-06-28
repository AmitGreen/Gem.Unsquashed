//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.String;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import link.crystal.Gem.Core.Gem;
import link.crystal.Gem.Core.Gem_StringSet;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Exception.ExceptionFunctions;
import link.crystal.Gem.Interface.Storehouse_String__Interface;


public final class  Temporary_Storehouse_String
    extends         HashMap        <String, String>
//  extends         AbstractHashMap<String, String>
//  extends         Object
    implements      Storehouse_String__Interface
{
    //
    //  Private static
    //
    private static final int                initial_capacity = 1009;


    //
    //  Private
    //
    private final Zone                      z;



    //
    //  Constructor & Factory
    //
    private                             Temporary_Storehouse_String(final Zone z, final int initial_capacity)
    {
        super(initial_capacity);

        this.z = z;
    }


    public static final Temporary_Storehouse_String     create__ALLY__Zone(final Zone z)
    {
        return new Temporary_Storehouse_String(z, Temporary_Storehouse_String.initial_capacity);
    }


    //
    //  Private (ASSERT)
    //
    public static final boolean         fact(boolean condition, final String format)
    {
        if (condition) {
            return true;
        }

        ExceptionFunctions.ASSERTION_FAILED(2, format);

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
    //  Public (line)
    //
    public static final void            line(final String format, final Object v)
    {
        Gem.line(2, format, v);
    }


    //
    //  Interface Storehouse_String__Interface
    //
    public final void                   dump(final String name)
    {
        List<String>                    keys = new ArrayList<String>(this.keySet());

        Collections.sort(keys);

        final int                       total = keys.size();

        line("Dump of Temporary_Storehouse_String {}", name);
        line("      size: {}", total);

        for (/*:*/ int                  i = 0; i < total; i ++) {
            final String                k = keys.get(i);

            line("  {p}", k);
        }

        line("End of dump of Temporary_Storehouse_String {}", name);
    }


    public final String                 intern_permenant_string(final Zone z, final String s)
    {
        assert fact        (this.z == z, "this.z == z");
        assert fact_pointer(s, "s");

        final String                    previous = this.putIfAbsent(s, s);

        if (previous != null) {
            return previous;
        }

        return s;
    }
}
