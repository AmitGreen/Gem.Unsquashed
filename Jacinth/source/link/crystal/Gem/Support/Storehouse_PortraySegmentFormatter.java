//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.String;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Format.PortraySegmentFormatter;
import link.crystal.Gem.Support.Storehouse_SmallList;


public class    Storehouse_PortraySegmentFormatter
    extends     Storehouse_SmallList<Storehouse_PortraySegmentFormatter, PortraySegmentFormatter>
//  extends     Gem_Object<Inspection>
//  extends     Object
    implements  Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create("Storehouse_PortraySegmentFormatter");


    //
    //  Static members
    //
    public static final Storehouse_PortraySegmentFormatter  singleton = (
            Storehouse_PortraySegmentFormatter.create(100)
        );


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


    private static Storehouse_PortraySegmentFormatter   create(int capacity)
    {
        final Zone                      z = Zone.current_zone();

        final PortraySegmentFormatter[]     segment_many = new PortraySegmentFormatter[capacity];

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
