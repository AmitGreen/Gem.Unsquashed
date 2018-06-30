//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.lang.RuntimeException;
import java.lang.String;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.PortrayFunctions;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;


public class    PermenantMessageFormattable
    extends     HashMap<String, MessageFormattable>
    implements  Inspectable<Inspection>//,
{
    private static Inspection           inspection = Inspection.create("Gem.Core.PermenantMessageFormattable");


    //
    //  Private static
    //
    private static final int                    initial_capacity = 1009;
    private static PermenantMessageFormattable  singleton        = null;



    //
    //  Constructor & Factory
    //
    private                             PermenantMessageFormattable(int initial_capacity)
    {
        super(initial_capacity);
    }


    private static PermenantMessageFormattable  create()
    {
        return new PermenantMessageFormattable(PermenantMessageFormattable.initial_capacity);
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
    private static PermenantMessageFormattable  singleton()
    {
        PermenantMessageFormattable     singleton = PermenantMessageFormattable.singleton;

        if (singleton != null) {
            return singleton;
        }

        singleton =
            PermenantMessageFormattable.singleton = PermenantMessageFormattable.create();

        return singleton;
    }


    //
    //  Public
    //
    public static void                  dump()
    {
        PermenantMessageFormattable     singleton = PermenantMessageFormattable.singleton;

        if (singleton == null) {
            singleton = PermenantMessageFormattable.singleton();
        }

        List<String>                    values = new ArrayList<String>(singleton.keySet());

        Collections.sort(values);

        int                             total = values.size();

        GemObject.line("Dump of PermenantMessageFormattable");
        GemObject.line("  " + String.format("%30s", "size") + ": " + Integer.toString(total));

        for (int                        i = 0; i < total; i ++) {
            String                      k = values.get(i);
            MessageFormattable          v = singleton.get(k);

            GemObject.line("  " + String.format("%30s", PortrayFunctions.portray_string(k)) + ": " + v.portray());
        }

        GemObject.line("End of dump of PermenantMessageFormattable");
    }


    public static void                  insert(String k, MessageFormattable v)
    {
        PermenantMessageFormattable     singleton = PermenantMessageFormattable.singleton;

        if (singleton == null) {
            singleton = PermenantMessageFormattable.singleton();
        }

        MessageFormattable              previous = singleton.putIfAbsent(k, v);

        if (previous != null) {
            throw new RuntimeException(
                    (
                          "PermenantMessageFormattable.insert: previos value for "
                        + PortrayFunctions.portray_string(k)
                        + " already exists: "
                        + previous.portray()
                    )
                );
        }
    }


    public static MessageFormattable    lookup(String k)
    {
        PermenantMessageFormattable     singleton = PermenantMessageFormattable.singleton;

        if (singleton == null) {
            singleton = PermenantMessageFormattable.singleton();
        }

        return singleton.get(k);
    }
}
