//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.String;
import link.crystal.Gem.Core.Gem_StringMap;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Format.StringSegmentFormatter;
import link.crystal.Gem.Interface.Inspectable;


public class    Storehouse_StringSegmentFormatter
    extends     Gem_StringMap  <Inspection,         StringSegmentFormatter>
//  extends     Gem_Map        <Inspection, String, StringSegmentFormatter>
//  extends     HashMap                    <String, StringSegmentFormatter>
//  extends     AbstractHashMap            <String, StringSegmentFormatter>
//  extends     Object
    implements  Inspectable<Inspection>//,                              //  Via Gem_StringMap<StringSegmentFormatter>
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
    public static StringSegmentFormatter    conjure(String s)
    {
        Storehouse_StringSegmentFormatter   singleton = Storehouse_StringSegmentFormatter.singleton;

        if (singleton == null) {
            singleton = Storehouse_StringSegmentFormatter.singleton();
        }

        StringSegmentFormatter          r = singleton.get(s);

        if (r != null) {
            return null;
        }

        r = StringSegmentFormatter.create__ALLY__Storehouse_StringSegmentFormatter(s);

        singleton.put(r.s(), r);

        return r;
    }


    public static void                  dump()
    {
        Storehouse_StringSegmentFormatter   singleton = Storehouse_StringSegmentFormatter.singleton;

        if (singleton == null) {
            singleton = Storehouse_StringSegmentFormatter.singleton();
        }

        singleton.dump("Storehouse_StringSegmentFormatter.singleton");
    }
}
