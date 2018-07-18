//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Silver.UnitTest;


import link.crystal.Gem.Core.Gem;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Inspection.Inspection;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Support.AnalyzeString;
import link.crystal.Gem.Support.AsciiTable;
import link.crystal.Gem.Support.BuildStringState;
import link.crystal.Gem.Support.Map_String_Inspection;
import link.crystal.Gem.Support.Storehouse_AdornmentSegmentFormatter;
import link.crystal.Gem.Support.Storehouse_MessageFormattable;
import link.crystal.Gem.Support.Storehouse_PortraySegmentFormatter;
import link.crystal.Gem.Support.Storehouse_String;
import link.crystal.Gem.UnitTest.UnitTest_Gem;
import link.crystal.Gem.UnitTest.UnitTest_PortrayString;
import link.crystal.Silver.UnitTest.UnitTest_Java;
import link.crystal.Silver.UnitTest.UnitTest_Silver;


public final class  UnitTest
    extends         Gem_Object <Inspection>
//  extends         Object
    implements      Inspectable<Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("UnitTest");


    //
    //  Members
    //
    public final Zone                   z;


    //
    //  Constructor & Factory
    //
    private                             UnitTest(final Zone z)
    {
        this.z = z;
    }


    private static UnitTest             create(final Zone z)
    {
        return new UnitTest(z);
    }


    //
    //  Private (tests)
    //
    private final boolean               test_development()
    {
        final Zone                      z = this.z;

        return UnitTest_Gem.create(z).test_string();
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
    //  Public
    //
    public static final void            unit_test(final String ... arguments)
    {
        final Zone                      z = Zone.current_zone();

        if (arguments.length == 0) {
            UnitTest_PortrayString.create(z).test_portray_string();
            //UnitTest_Gem.create(z).test_analyze_string();
            //UnitTest_Gem.create(z).test_arrange();
            //UnitTest_Gem.create(z).test_string();
            //UnitTest_Silver.create(z).test_shape();

            //UnitTest.create(z).test_development();
        } else {
            final int                   arguments_total = arguments.length;

            if (arguments_total > 1) {
                RUNTIME("{} arguments given (expected 0 or 1)", arguments_total);
            }

            final String                name = (arguments_total == 0 ? "development" : arguments[0]);

            if (name.equals("development")) {
                UnitTest.create(z).test_development();
            } else if (name.equals("shape")) {
                UnitTest_Silver.create(z).test_shape();
            } else {
                RUNTIME("unknown unit test: {p}", name);
            }
        }

        if (true) {
            //AsciiTable.dump();
            AnalyzeString.dump();
            //BuildStringState.dump();;
            //Gem.dump();
            //Gem.map_string_inspection                       .dump("Inspections");
            //Storehouse_AdornmentSegmentFormatter.singleton  .dump("Storehouse_AdornmentSegmentFormatter.singleton");
            //Storehouse_MessageFormattable                   .dump(z);
            //Storehouse_PortraySegmentFormatter  .singleton  .dump(z);
            //Storehouse_String                               .dump(z);
            //z.dump();
        }
    }
}
