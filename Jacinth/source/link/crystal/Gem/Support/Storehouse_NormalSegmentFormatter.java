//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.String;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Format.NormalSegmentFormatter;
import link.crystal.Gem.Support.Storehouse_SmallList;


public class    Storehouse_NormalSegmentFormatter
    extends     Storehouse_SmallList<Storehouse_NormalSegmentFormatter, NormalSegmentFormatter>
//  extends     Gem_Object<Inspection>
//  extends     Object
    implements  Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create("Storehouse_NormalSegmentFormatter");


    //
    //  Static members
    //
    public static final Storehouse_NormalSegmentFormatter   singleton = (
            Storehouse_NormalSegmentFormatter.create(100)
        );


    //
    //  Constructor & Factory
    //
    private                             Storehouse_NormalSegmentFormatter(
            Zone                                z,
            NormalSegmentFormatter[]            segment_many//,
        )
    {
        super(z, segment_many);
    }


    private static Storehouse_NormalSegmentFormatter    create(int capacity)
    {
        final Zone                      z = Zone.current_zone();

        final NormalSegmentFormatter[]  segment_many = new NormalSegmentFormatter[capacity];

        return new Storehouse_NormalSegmentFormatter(z, segment_many);
    }


    //
    //  Interface Inspectable
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }
}
