//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Silver.UnitTest;


import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Support.Map_String_Inspection;
import link.crystal.Gem.Support.Storehouse_AdornmentSegmentFormatter;
import link.crystal.Gem.Support.Storehouse_MessageFormattable;
import link.crystal.Gem.Support.Storehouse_PortraySegmentFormatter;
import link.crystal.Gem.Support.Storehouse_String;
import link.crystal.Gem.World.Inspection;
import link.crystal.Gem.World.World_Integer;
import link.crystal.Mirror.Shape;


public class    UnitTest
    extends     Gem_Object <Inspection>
//  extends     Object
    implements  Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static final Inspection     inspection = Inspection.create("UnitTest");


    //
    //  Members
    //
    public final Zone                   z;


    //
    //  Constructor & Factory
    //
    protected                           UnitTest(Zone z)
    {
        this.z = z;
    }


    private static UnitTest             create(Zone z)
    {
        return new UnitTest(z);
    }


    //
    //  Private (tests)
    //
    private boolean                     test_development()
    {
        final World_Integer             seven = World_Integer.create(7);
        final World_Integer             eight = World_Integer.create(8);

        line("{} .vs {}: {}", seven, eight, seven.compareTo(eight));

        return true;
    }


    private boolean                     test_old()
    {
        final Zone                      z = Zone.current_zone();

        final Shape                     circle = Shape.create(z, "circle");

        circle.skew();

        //assert Gem_Object.fact_pointer(null, "test");
        //assert Gem_Object.fact_between(7, 6, 77);

        line("{+}: created: {}", 7);
        line("hi: {{ and {{ yes {p} then }}", arrange("arrange {}", 7));

        //line("{+}");
        //line("{+}: test {}", 7);
        //line("that: {+}");
        //line("that: {}", "hi");
        //line("that: {0}", "bye");
        //line("prefix {0} suffix", "middle");

        return true;
    }


    //
    //  Private
    //
    private boolean                     run_test(String ... arguments)
    {
        final int                       arguments_total = arguments.length;

        if (arguments_total > 1) {
            RUNTIME("{} arguments given (expected 0 or 1)", arguments_total);
        }

        final String                    name = (arguments_total == 0 ? "development" : arguments[0]);

        if (name.equals("development")) {       return this.test_development();     }
        if (name.equals("old"))         {       return this.test_old();             }

        RUNTIME("unknown unit test: {p}", name);

        return false;
    }


    //
    //  Interface Inspectable
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }


    //
    //  Public
    //
    public static void                  unit_test(String ... arguments)
    {
        final Zone                      z = Zone.current_zone();

        final UnitTest                  unit_test = UnitTest.create(z);

        unit_test.run_test(arguments);

        if (true) {
            //Map_String_Inspection               .singleton().dump("Inspections");
            //Storehouse_MessageFormattable                   .dump(z);
            //Storehouse_PortraySegmentFormatter  .singleton  .dump(z);
            //Storehouse_String                               .dump(z);
            //Storehouse_AdornmentSegmentFormatter.singleton  .dump("Storehouse_AdornmentSegmentFormatter.singleton");
            //z.dump();
        }
    }
}
