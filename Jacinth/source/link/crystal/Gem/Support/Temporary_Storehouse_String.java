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


public class    Temporary_Storehouse_String
    extends     HashMap        <String, String>
//  extends     AbstractHashMap<String, String>
//  extends     Object
    implements  Storehouse_String__Interface
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
    private                             Temporary_Storehouse_String(Zone z, int initial_capacity)
    {
        super(initial_capacity);

        this.z = z;
    }


    public static Temporary_Storehouse_String   create__ALLY__Zone(Zone z)
    {
        return new Temporary_Storehouse_String(z, Temporary_Storehouse_String.initial_capacity);
    }


    //
    //  Private (ASSERT)
    //
    public static boolean               fact(boolean condition, String format)
    {
        if (condition) {
            return true;
        }

        ExceptionFunctions.ASSERTION_FAILED(2, format);

        return false;
    }


    public static boolean               fact_pointer(Object p, String name)
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
    public static void                  line(String format, Object v)
    {
        Gem.line(2, format, v);
    }


    //
    //  Interface Storehouse_String__Interface
    //
    public void                         dump(String name)
    {
        List<String>                    keys = new ArrayList<String>(this.keySet());

        Collections.sort(keys);

        final int                       total = keys.size();

        line("Dump of Temporary_Storehouse_String {}", name);
        line("      size: {}", total);

        for (int                        i = 0; i < total; i ++) {
            final String                k = keys.get(i);

            line("  {p}", k);
        }

        line("End of dump of Temporary_Storehouse_String {}", name);
    }


    public String                       intern_permenant_string(Zone z, String s)
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
