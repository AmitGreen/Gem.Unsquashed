//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.String;
import link.crystal.Gem.Core.Gem_StringMap;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Format.StringSegmentFormatter;
import link.crystal.Gem.Interface.Inspectable;


public class    Storehouse_AdornmentSegmentFormatter
    extends     Gem_StringMap  <Inspection,         StringSegmentFormatter>
//  extends     Gem_Map        <Inspection, String, StringSegmentFormatter>
//  extends     HashMap                    <String, StringSegmentFormatter>
//  extends     AbstractHashMap            <String, StringSegmentFormatter>
//  extends     Object
    implements  Inspectable<Inspection>//,                              //  Via Gem_StringMap<StringSegmentFormatter>
{
    private static Inspection           inspection = (
            Inspection.create("Gem.Support.Storehouse_AdornmentSegmentFormatter")
        );


    //
    //  Static members
    //
    public static Storehouse_AdornmentSegmentFormatter  singleton = Storehouse_AdornmentSegmentFormatter.create(101);



    //
    //  Constructor & Factory
    //
    private                             Storehouse_AdornmentSegmentFormatter(Zone z, int initial_capacity)
    {
        super(z, initial_capacity);
    }


    private static Storehouse_AdornmentSegmentFormatter     create(int initial_capacity)
    {
        final Zone                      z = Zone.current_zone();

        return new Storehouse_AdornmentSegmentFormatter(z, initial_capacity);
    }


    //
    //  Interface Inspectable
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }
}
