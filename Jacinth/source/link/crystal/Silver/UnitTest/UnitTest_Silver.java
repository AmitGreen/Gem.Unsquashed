//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Silver.UnitTest;


import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Inspection.Inspection;
import link.crystal.Gem.Interface.Inspectable;


public final class  UnitTest_Silver
    extends         Gem_Object <Inspection>
//  extends         Object
    implements      Inspectable<Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("UnitTest_Silver");


    //
    //  Members
    //
    public  final Zone                  z;


    //
    //  Constructor & Factory
    //
    protected                           UnitTest_Silver(final Zone z)
    {
        this.z = z;
    }


    private static final UnitTest_Silver    create(final Zone z)
    {
        return new UnitTest_Silver(z);
    }


    //
    //  Interface Inspectable
    //
    @Override
    public final Inspection             inspect()
    {
        return /*static*/ this.inspection;
    }
}
