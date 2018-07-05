//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.String;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Format.StringSegmentFormatter;
import link.crystal.Gem.Support.Storehouse_SmallList;


public class    Storehouse_StringSegmentFormatter
    extends     Storehouse_SmallList<Storehouse_StringSegmentFormatter, StringSegmentFormatter>
//  extends     Gem_Object<Inspection>
//  extends     Object
    implements  Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create("Storehouse_StringSegmentFormatter");


    //
    //  Static members
    //
    public static final Storehouse_StringSegmentFormatter   singleton = Storehouse_StringSegmentFormatter.create(100);


    //
    //  Constructor & Factory
    //
    private                             Storehouse_StringSegmentFormatter(
            Zone                                z,
            StringSegmentFormatter[]           segment_many//,
        )
    {
        super(z, segment_many);
    }


    private static Storehouse_StringSegmentFormatter    create(int capacity)
    {
        final Zone                      z = Zone.current_zone();

        final StringSegmentFormatter[]  segment_many = new StringSegmentFormatter[capacity];

        return new Storehouse_StringSegmentFormatter(z, segment_many);
    }


    //
    //  Interface Inspectable
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }
}
