//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.RuntimeException;
import java.lang.String;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.PortrayFunctions;
import link.crystal.Gem.Interface.Inspectable;


public class    PermenantCache_String
    extends     HashMap<String, String>
    implements  Inspectable<Inspection>//,
{
    private static Inspection           inspection = Inspection.create("Gem.Support.PermenantCache_String");


    //
    //  Private static
    //
    private static final int                initial_capacity = 1009;
    private static PermenantCache_String    singleton        = null;



    //
    //  Constructor & Factory
    //
    private                             PermenantCache_String(int initial_capacity)
    {
        super(initial_capacity);
    }


    private static PermenantCache_String    create()
    {
        return new PermenantCache_String(PermenantCache_String.initial_capacity);
    }


    //
    //  Interface Inspectable
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }


    public String                       portray()
    {
        return "<Gem.Support.PermenantCache_String>";
    }


    //
    //  Private
    //
    private static PermenantCache_String    singleton()
    {
        PermenantCache_String           singleton = PermenantCache_String.singleton;

        if (singleton != null) {
            return singleton;
        }

        singleton =
            PermenantCache_String.singleton = PermenantCache_String.create();

        return singleton;
    }


    //
    //  Public
    //
    public static void                  dump()
    {
        PermenantCache_String           singleton = PermenantCache_String.singleton;

        if (singleton == null) {
            singleton = PermenantCache_String.singleton();
        }

        List<String>                    values = new ArrayList<String>(singleton.keySet());

        Collections.sort(values);

        int                             total = values.size();

        Gem_Object.line("Dump of PermenantCache_String");
        Gem_Object.line("      size: " + Integer.toString(total));

        for (int                        i = 0; i < total; i ++) {
            Gem_Object.line("  value[" + Integer.toString(i) + "]: " + PortrayFunctions.portray_string(values.get(i)));
        }

        Gem_Object.line("End of dump of PermenantCache_String");
    }


    public static String                intern_permenant_string(String s)
    {
        if (s == null) {
            throw new RuntimeException("PermenantCache_String.intern_permenant_string: `s` is null");
        }

        PermenantCache_String           singleton = PermenantCache_String.singleton;

        if (singleton == null) {
            singleton = PermenantCache_String.singleton();
        }

        String                          previous = singleton.putIfAbsent(s, s);

        if (previous != null) {
            return previous;
        }

        return s;
    }
}
