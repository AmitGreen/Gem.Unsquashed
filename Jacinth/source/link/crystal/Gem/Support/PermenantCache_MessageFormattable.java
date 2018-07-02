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
import link.crystal.Gem.Interface.MessageFormattable;


public class    PermenantCache_MessageFormattable
    extends     HashMap<String, MessageFormattable>
    implements  Inspectable<Inspection>//,
{
    private static Inspection           inspection = Inspection.create_with_portrait(
            "Gem.Core.PermenantCache_MessageFormattable"//,
        );


    //
    //  Private static
    //
    private static final int                            initial_capacity = 1009;
    private static PermenantCache_MessageFormattable    singleton        = null;



    //
    //  Constructor & Factory
    //
    private                             PermenantCache_MessageFormattable(int initial_capacity)
    {
        super(initial_capacity);
    }


    private static PermenantCache_MessageFormattable    create()
    {
        return new PermenantCache_MessageFormattable(PermenantCache_MessageFormattable.initial_capacity);
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
        return "<Gem.Core.PermenantCache_MessageFormattable>";
    }


    //
    //  Private
    //
    private static PermenantCache_MessageFormattable    singleton()
    {
        PermenantCache_MessageFormattable   singleton = PermenantCache_MessageFormattable.singleton;

        if (singleton != null) {
            return singleton;
        }

        singleton =
            PermenantCache_MessageFormattable.singleton = PermenantCache_MessageFormattable.create();

        return singleton;
    }


    //
    //  Public
    //
    public static void                  dump()
    {
        PermenantCache_MessageFormattable   singleton = PermenantCache_MessageFormattable.singleton;

        if (singleton == null) {
            singleton = PermenantCache_MessageFormattable.singleton();
        }

        List<String>                    values = new ArrayList<String>(singleton.keySet());

        Collections.sort(values);

        int                             total = values.size();

        Gem_Object.line("Dump of PermenantCache_MessageFormattable");
        Gem_Object.line("  " + String.format("%30s", "size") + ": " + Integer.toString(total));

        for (int                        i = 0; i < total; i ++) {
            String                      k = values.get(i);
            MessageFormattable          v = singleton.get(k);

            Gem_Object.line("  " + String.format("%30s", PortrayFunctions.portray_string(k)) + ": " + v.portray());
        }

        Gem_Object.line("End of dump of PermenantCache_MessageFormattable");
    }


    public static void                  insert(String k, MessageFormattable v)
    {
        PermenantCache_MessageFormattable   singleton = PermenantCache_MessageFormattable.singleton;

        if (singleton == null) {
            singleton = PermenantCache_MessageFormattable.singleton();
        }

        MessageFormattable              previous = singleton.putIfAbsent(k, v);

        if (previous != null) {
            throw new RuntimeException(
                    (
                          "PermenantCache_MessageFormattable.insert: previos value for "
                        + PortrayFunctions.portray_string(k)
                        + " already exists: "
                        + previous.portray()
                    )
                );
        }
    }


    public static MessageFormattable    lookup(String k)
    {
        PermenantCache_MessageFormattable   singleton = PermenantCache_MessageFormattable.singleton;

        if (singleton == null) {
            singleton = PermenantCache_MessageFormattable.singleton();
        }

        return singleton.get(k);
    }
}
