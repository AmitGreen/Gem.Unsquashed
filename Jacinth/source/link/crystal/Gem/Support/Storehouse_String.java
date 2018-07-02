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


public class    Storehouse_String
    extends     HashMap<String, String>
    implements  Inspectable<Inspection>//,
{
    private static Inspection           inspection = Inspection.create("Gem.Support.Storehouse_String");


    //
    //  Private static
    //
    private static final int            initial_capacity = 1009;
    private static Storehouse_String    singleton        = null;



    //
    //  Constructor & Factory
    //
    private                             Storehouse_String(int initial_capacity)
    {
        super(initial_capacity);
    }


    private static Storehouse_String    create()
    {
        return new Storehouse_String(Storehouse_String.initial_capacity);
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
        return "<Gem.Support.Storehouse_String>";
    }


    //
    //  Private
    //
    private static Storehouse_String    singleton()
    {
        Storehouse_String               singleton = Storehouse_String.singleton;

        if (singleton != null) {
            return singleton;
        }

        singleton =
            Storehouse_String.singleton = Storehouse_String.create();

        return singleton;
    }


    //
    //  Public
    //
    public static void                  dump()
    {
        Storehouse_String               singleton = Storehouse_String.singleton;

        if (singleton == null) {
            singleton = Storehouse_String.singleton();
        }

        List<String>                    values = new ArrayList<String>(singleton.keySet());

        Collections.sort(values);

        int                             total = values.size();

        Gem_Object.line("Dump of Storehouse_String");
        Gem_Object.line("      size: " + Integer.toString(total));

        for (int                        i = 0; i < total; i ++) {
            Gem_Object.line("  value[" + Integer.toString(i) + "]: " + PortrayFunctions.portray_string(values.get(i)));
        }

        Gem_Object.line("End of dump of Storehouse_String");
    }


    public static String                intern_permenant_string(String s)
    {
        if (s == null) {
            throw new RuntimeException("Storehouse_String.intern_permenant_string: `s` is null");
        }

        Storehouse_String               singleton = Storehouse_String.singleton;

        if (singleton == null) {
            singleton = Storehouse_String.singleton();
        }

        String                          previous = singleton.putIfAbsent(s, s);

        if (previous != null) {
            return previous;
        }

        return s;
    }
}
