//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.String;
import link.crystal.Gem.Core.Gem_StringMap;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Format.ArgumentSegmentFormatter_Inspection;
import link.crystal.Gem.Format.NormalSegmentFormatter;
import link.crystal.Gem.Format.PortraySegmentFormatter;
import link.crystal.Gem.Format.StringSegmentFormatter;
import link.crystal.Gem.Interface.Inspectable;


public class    Map__String__ArgumentSegmentFormatter_Inspection
    extends     Gem_StringMap  <Inspection,         ArgumentSegmentFormatter_Inspection>
//  extends     Gem_Map        <Inspection, String, ArgumentSegmentFormatter_Inspection>
//  extends     HashMap                    <String, ArgumentSegmentFormatter_Inspection>
//  extends     AbstractHashMap            <String, ArgumentSegmentFormatter_Inspection>
//  extends     Object
    implements  Inspectable<Inspection>//,                              //  Via Gem_StringMap<?>
{
    private static Inspection           inspection = (
            Inspection.create("Map__String__ArgumentSegmentFormatter_Inspection")
        );


    //
    //  Static members
    //
    private static final int            initial_capacity = 11;



    //
    //  Constructor & Factory
    //
    private                             Map__String__ArgumentSegmentFormatter_Inspection(Zone z, int initial_capacity)
    {
        super(z, initial_capacity);
    }


    public static Map__String__ArgumentSegmentFormatter_Inspection  CREATE_AND_POPULATE(Zone z)
    {
        Map__String__ArgumentSegmentFormatter_Inspection    r = (
                new Map__String__ArgumentSegmentFormatter_Inspection(
                    z,
                    Map__String__ArgumentSegmentFormatter_Inspection.initial_capacity//,
                )
            );

        r.put("",  NormalSegmentFormatter .inspection);
        r.put("p", PortraySegmentFormatter.inspection);
        r.put("s", StringSegmentFormatter .inspection);

        return r;
    }


    //
    //  Interface Inspectable
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }
}
