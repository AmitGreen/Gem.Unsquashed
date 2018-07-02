//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.RuntimeException;
import java.lang.String;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import link.crystal.Gem.Core.Gem_StringMap;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Support.PortrayFunctions;


public class    Storehouse_MessageFormattable
    extends     Gem_StringMap<Inspection,         MessageFormattable>
//  extends     HashMap                  <String, MessageFormattable>
//  extends     AbstractHashMap          <String, MessageFormattable>
//  extends     Object
    implements  Inspectable<Inspection>//,                              //  Via Gem_Map<?, ?, ?>
{
    private static Inspection           inspection = Inspection.create_with_portrait(
            "Gem.Core.Storehouse_MessageFormattable"//,
        );


    //
    //  Private static
    //
    private static final int                        initial_capacity = 1009;
    private static Storehouse_MessageFormattable    singleton        = null;



    //
    //  Constructor & Factory
    //
    private                             Storehouse_MessageFormattable(int initial_capacity)
    {
        super(initial_capacity);
    }


    private static Storehouse_MessageFormattable    create()
    {
        return new Storehouse_MessageFormattable(Storehouse_MessageFormattable.initial_capacity);
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
        return "<Gem.Core.Storehouse_MessageFormattable>";
    }


    //
    //  Private
    //
    private static Storehouse_MessageFormattable    singleton()
    {
        Storehouse_MessageFormattable   singleton = Storehouse_MessageFormattable.singleton;

        if (singleton != null) {
            return singleton;
        }

        singleton =
            Storehouse_MessageFormattable.singleton = Storehouse_MessageFormattable.create();

        return singleton;
    }


    //
    //  Public
    //
    public static void                  dump()
    {
        Storehouse_MessageFormattable   singleton = Storehouse_MessageFormattable.singleton;

        if (singleton == null) {
            singleton = Storehouse_MessageFormattable.singleton();
        }

        List<String>                    keys = new ArrayList<String>(singleton.keySet());

        Collections.sort(keys);

        int                             total = keys.size();

        Gem_Object.line("Dump of Storehouse_MessageFormattable");
        Gem_Object.line("  " + String.format("%30s", "size") + ": " + Integer.toString(total));

        for (int                        i = 0; i < total; i ++) {
            String                      k = keys.get(i);
            MessageFormattable          v = singleton.get(k);

            Gem_Object.line("  " + String.format("%30s", PortrayFunctions.portray_string(k)) + ": " + v.portray());
        }

        Gem_Object.line("End of dump of Storehouse_MessageFormattable");
    }


    public static void                  insert(String k, MessageFormattable v)
    {
        Storehouse_MessageFormattable   singleton = Storehouse_MessageFormattable.singleton;

        if (singleton == null) {
            singleton = Storehouse_MessageFormattable.singleton();
        }

        MessageFormattable              previous = singleton.putIfAbsent(k, v);

        if (previous != null) {
            throw new RuntimeException(
                    (
                          "Storehouse_MessageFormattable.insert: previos value for "
                        + PortrayFunctions.portray_string(k)
                        + " already exists: "
                        + previous.portray()
                    )
                );
        }
    }


    public static MessageFormattable    lookup(String k)
    {
        Storehouse_MessageFormattable   singleton = Storehouse_MessageFormattable.singleton;

        if (singleton == null) {
            singleton = Storehouse_MessageFormattable.singleton();
        }

        return singleton.get(k);
    }
}
