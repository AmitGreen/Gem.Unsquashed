//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.String;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Format.PortraySegmentFormatter;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Support.Storehouse_SmallList;
import link.crystal.Gem.World.Inspection;


public class    Storehouse_PortraySegmentFormatter
    extends     Storehouse_SmallList<Storehouse_PortraySegmentFormatter, PortraySegmentFormatter>
//  extends     Gem_Object <Inspection>
//  extends     Object
    implements  Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static final Inspection     inspection = Inspection.create("Storehouse_PortraySegmentFormatter");


    //
    //  Static members
    //
    public static final int             initial_capacity = 100;


    //
    //  Constructor & Factory
    //
    private                             Storehouse_PortraySegmentFormatter(
            Zone                                z,
            PortraySegmentFormatter[]           segment_many//,
        )
    {
        super(z, segment_many);
    }


    public static Storehouse_PortraySegmentFormatter    create__ALLY__Zone(Zone z)
    {
        final PortraySegmentFormatter[]     segment_many = (
                new PortraySegmentFormatter[Storehouse_PortraySegmentFormatter.initial_capacity]
            );

        return new Storehouse_PortraySegmentFormatter(z, segment_many);
    }


    //
    //  Interface Inspectable
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }
}
