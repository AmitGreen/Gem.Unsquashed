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
import link.crystal.Gem.Format.StringSegmentFormatter;
import link.crystal.Gem.Interface.Inspectable;


public class    Storehouse_StringSegmentFormatter
    extends     HashMap<String, StringSegmentFormatter>
    implements  Inspectable<Inspection>//,
{
    private static Inspection           inspection = Inspection.create("Gem.Support.Storehouse_StringSegmentFormatter");


    //
    //  Private static
    //
    private static final int                            initial_capacity = 101;
    private static Storehouse_StringSegmentFormatter    singleton        = null;



    //
    //  Constructor & Factory
    //
    private                             Storehouse_StringSegmentFormatter(int initial_capacity)
    {
        super(initial_capacity);
    }


    private static Storehouse_StringSegmentFormatter    create()
    {
        return new Storehouse_StringSegmentFormatter(Storehouse_StringSegmentFormatter.initial_capacity);
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
        return "<Gem.Support.Storehouse_StringSegmentFormatter>";
    }


    //
    //  Private
    //
    private static Storehouse_StringSegmentFormatter    singleton()
    {
        Storehouse_StringSegmentFormatter   singleton = Storehouse_StringSegmentFormatter.singleton;

        if (singleton != null) {
            return singleton;
        }

        singleton =
            Storehouse_StringSegmentFormatter.singleton = Storehouse_StringSegmentFormatter.create();

        return singleton;
    }


    //
    //  Public
    //
    public static void                  dump()
    {
        Storehouse_StringSegmentFormatter   singleton = Storehouse_StringSegmentFormatter.singleton;

        if (singleton == null) {
            singleton = Storehouse_StringSegmentFormatter.singleton();
        }

        List<String>                    keys = new ArrayList<String>(singleton.keySet());

        Collections.sort(keys);

        int                             total = keys.size();

        Gem_Object.line("Dump of Storehouse_StringSegmentFormatter");
        Gem_Object.line("      size: " + Integer.toString(total));

        for (int                        i = 0; i < total; i ++) {
            String                      k = keys.get(i);
            StringSegmentFormatter      v = singleton.get(k);

            Gem_Object.line("  " + String.format("%30s", PortrayFunctions.portray_string(k)) + ": " + v.portray());
        }

        Gem_Object.line("End of dump of Storehouse_StringSegmentFormatter");
    }
}
