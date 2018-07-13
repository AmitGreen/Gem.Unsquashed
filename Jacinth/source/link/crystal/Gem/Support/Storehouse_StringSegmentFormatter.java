//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.String;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Format.StringSegmentFormatter;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Support.Storehouse_SmallList;
import link.crystal.Gem.Inspection.Inspection;


public class    Storehouse_StringSegmentFormatter
    extends     Storehouse_SmallList<Storehouse_StringSegmentFormatter, StringSegmentFormatter>
//  extends     Gem_Object <Inspection>
//  extends     Object
    implements  Inspectable<Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("Storehouse_StringSegmentFormatter");


    //
    //  Static members
    //
    public static final int             initial_capacity = 100;


    //
    //  Constructor & Factory
    //
    private                             Storehouse_StringSegmentFormatter(
            Zone                                z,
            StringSegmentFormatter[]            segment_many//,
        )
    {
        super(z, segment_many);
    }


    public static Storehouse_StringSegmentFormatter     create__ALLY__Zone(Zone z)
    {
        final StringSegmentFormatter[]     segment_many = (
                new StringSegmentFormatter[Storehouse_StringSegmentFormatter.initial_capacity]
            );

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
