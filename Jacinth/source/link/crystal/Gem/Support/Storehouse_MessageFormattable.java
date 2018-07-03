//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.String;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import link.crystal.Gem.Core.Gem_StringMap;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;


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
    public static void                  dump(Zone z)
    {
        Storehouse_MessageFormattable   singleton = Storehouse_MessageFormattable.singleton;

        if (singleton == null) {
            singleton = Storehouse_MessageFormattable.singleton();
        }

        List<String>                    keys = new ArrayList<String>(singleton.keySet());

        Collections.sort(keys);

        int                             total = keys.size();

        z.line("Dump of Storehouse_MessageFormattable");
        z.line("  " + String.format("%30s", "size") + ": " + Integer.toString(total));

        for (int                        i = 0; i < total; i ++) {
            String                      k = keys.get(i);
            MessageFormattable          v = singleton.get(k);

            z.line("  " + String.format("%30s", portray_string(k)) + ": " + v.portray());
        }

        z.line("End of dump of Storehouse_MessageFormattable");
    }


    public static void                  insert(Zone z, String k, MessageFormattable v)
    {
        Storehouse_MessageFormattable   singleton = Storehouse_MessageFormattable.singleton;

        if (singleton == null) {
            singleton = Storehouse_MessageFormattable.singleton();
        }

        MessageFormattable              previous = singleton.putIfAbsent(k, v);

        if (previous != null) {
            z.RAISE_runtime_exception("Storehouse_MessageFormattable.insert: previous value for {0} already exists: {1}",
                                      portray_string(k),
                                      previous.portray());
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
