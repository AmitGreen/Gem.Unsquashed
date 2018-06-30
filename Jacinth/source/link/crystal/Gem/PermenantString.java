//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem;


import java.lang.String;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import link.crystal.Gem.Inspection;
import link.crystal.Gem.Interface.Inspectable;


public class    PermenantString
    extends     HashMap<String, String>
    implements  Inspectable<Inspection>//,
{
    private static Inspection           inspection = Inspection.create("Gem.PermenantString");


    //
    //  Private static
    //
    private static final int            initial_capacity = 1009;
    private static PermenantString      singleton        = null;



    //
    //  Constructor & Factory
    //
    private                             PermenantString(int initial_capacity)
    {
        super(initial_capacity);
    }


    private static PermenantString      create()
    {
        return new PermenantString(PermenantString.initial_capacity);
    }


    //
    //  Interface Inspectable
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }


    //
    //  Private
    //
    private static PermenantString      singleton()
    {
        PermenantString                 singleton = PermenantString.singleton;

        if (singleton != null) {
            return singleton;
        }

        singleton =
            PermenantString.singleton = PermenantString.create();

        return singleton;
    }


    //
    //  Public
    //
    public static void                  dump()
    {
        PermenantString                 singleton = PermenantString.singleton;

        if (singleton == null) {
            singleton = PermenantString.singleton();
        }

        List<String>                    values = new ArrayList<String>(singleton.keySet());

        Collections.sort(values);

        int                             total = values.size();

        GemObject.line("Dump of PermenantString");
        GemObject.line("      size: " + Integer.toString(total));

        for (int                        i = 0; i < total; i ++) {
            GemObject.line("  value[" + Integer.toString(i) + "]: " + values.get(i));
        }

        GemObject.line("End of dump of PermenantString");
    }


    public static String                intern_permenant_string(String s)
    {
        PermenantString                 singleton = PermenantString.singleton;

        if (singleton == null) {
            singleton = PermenantString.singleton();
        }

        String                          previous = singleton.putIfAbsent(s, s);

        if (previous != null) {
            return previous;
        }

        return s;
    }
}
