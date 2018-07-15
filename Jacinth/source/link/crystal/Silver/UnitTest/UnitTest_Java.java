//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Silver.UnitTest;


import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Inspection.Inspection;
import link.crystal.Gem.Interface.Inspectable;


public final class  UnitTest_Java
    extends         Gem_Object <Inspection>
//  extends         Object
    implements      Inspectable<Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("UnitTest_Java");


    //
    //  Members
    //
    public final Zone                   z;


    //
    //  Constructor & Factory
    //
    private                             UnitTest_Java(final Zone z)
    {
        this.z = z;
    }


    public static final UnitTest_Java   create(final Zone z)
    {
        return new UnitTest_Java(z);
    }


    //
    //  Interface Inspectable
    //
    @Override
    public final Inspection             inspect()
    {
        return /*static*/ this.inspection;
    }


    //
    //  Public (Unit tests - Overload)
    //
    private final int                   overload()
    {
        line("overload() => 1");

        return 1;
    }


    private final int                   overload(final String v)
    {
        line("overload({p}) => 2", v);

        return 2;
    }


    private final int                   overload(final String v, final Object ... arguments)
    {
        line("overload({p}, {p}) => 3", v, arguments);

        return 3;
    }


    private final int                   overload(final int v)
    {
        line("overload({p}) => 4", v);

        return 4;
    }


    //
    //  NOTE:
    //      `v6` below will call the *NEXT* overload.
    //
    //      However, if this routine is changed from `missing_overload` to `overload` then v6a will call this routine.
    //
    private final int                   missing_overload(final int v, final Object w)
    {
        line("overload({p}, {p}) => 5", v, w);

        return 5;
    }


    private final int                   overload(final int v, final Object w, final Object ... arguments)
    {
        line("overload({p}, {p}, {p}) => 6", v, w, arguments);

        return 6;
    }


    //
    //  NOTE:
    //      Here we show that `final Object ...` can either have all the same argument before it
    //      (In which case it is *NOT* called if there are no extra arguments) [The v3a .vs. v3b test];
    //
    //          -- OR --
    //
    //      If there are not the same argumetns before it (In which case it *CAN* be called if there
    //      are no extra arguments) [The v6a test]
    //
    public final boolean                test_overload()
    {
        //
        //  v2 .vs. v3     -- Not ambigious, will call v2 with two argument or v3 with 3 or more arguments
        //  v4 .vs. v6a    -- Not ambigious, will call v4 with one argument or v6 with 2 or more arguments ...
        //    
        final int                       v1  = overload();
        final int                       v2  = overload("two");
        final int                       v3a = overload("three", "four");
        final int                       v3b = overload("three", "four", "five");
        final int                       v4  = overload(4);
        final int                       v6a = overload(6, "five");
        final int                       v6b = overload(6, "six", "seven");

        assert fact(v1  == 1, "v1  == 1");
        assert fact(v2  == 2, "v2  == 2");
        assert fact(v3a == 3, "v3a == 3");
        assert fact(v3b == 3, "v3b == 3");
        assert fact(v4  == 4, "v4  == 4");
        assert fact(v6a == 6, "v6a == 6");
        assert fact(v6b == 6, "v6b == 6");

        return true;
    }
}
