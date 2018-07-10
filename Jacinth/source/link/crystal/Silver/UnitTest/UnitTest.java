//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Silver.UnitTest;


import link.crystal.Gem.Core.Gem;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Support.Gem_ReferenceQueue;
import link.crystal.Gem.Support.Gem_TimeUnit;
import link.crystal.Gem.Support.Map_String_Inspection;
import link.crystal.Gem.Support.Storehouse_AdornmentSegmentFormatter;
import link.crystal.Gem.Support.Storehouse_MessageFormattable;
import link.crystal.Gem.Support.Storehouse_PortraySegmentFormatter;
import link.crystal.Gem.Support.Storehouse_String;
import link.crystal.Gem.Support.UniqueName;
import link.crystal.Gem.World.Inspection;
import link.crystal.Gem.World.World_Integer;
import link.crystal.Gem.World.World_String;
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
    private boolean                     test_arrange()
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


    private boolean                     test_development()
    {
        return test_unique_name();
    }


    private boolean                     test_integer()
    {
        World_Integer                   seven = Gem.conjure__World_Integer(7);
        final World_Integer             eight = Gem.conjure__World_Integer(8);

        line("{+}: {} .vs {}: {}", seven, eight, seven.compareTo(eight));

        World_Integer                   seven_2 = Gem.conjure__World_Integer(7);

        assert fact(seven == seven_2, "seven == seven_2");

        Gem.integer_cache.dump("integer cache - before");

        seven =
            seven_2 = null;

        //Gem.reference_queue.garbage_collect__AND__possible_sleep();
        Gem.reference_queue.garbage_collect();

        Gem.integer_cache.dump("integer cache - after");

        World_Integer                   seven_3 = Gem.conjure__World_Integer(7);

        return true;
    }


    private boolean                     test_string()
    {
        World_String                    seven = Gem.conjure__World_String("seven");
        final World_String              eight = Gem.conjure__World_String("eight");

        line("{+}: {} .vs {}: {}", seven, eight, seven.compareTo(eight));

        World_String                   seven_2 = Gem.conjure__World_String("seven");

        assert fact(seven == seven_2, "seven == seven_2");

        Gem.string_cache.dump("string cache - before");

        seven =
            seven_2 = null;

        Gem.reference_queue.garbage_collect__AND__possible_sleep();
        //Gem.reference_queue.garbage_collect();

        Gem.string_cache.dump("string cache - after");

        World_String                    seven_3 = Gem.conjure__World_String("seven");

        return true;
    }


    private boolean                     test_time_unit()
    {
        Gem_TimeUnit.test();

        return true;
    }



    private boolean                     test_unique_name()
    {
        final Zone                      z = Zone.current_zone();

        final UniqueName                apple = UniqueName.create__ALLY__Gem(z, "apple");

        line("apple: {}", apple);

        for (;;) {
            int                         v = apple.value__ALLY__UnitTest();

            String                      s = apple.next();

            if (v < 10 || (v % 1000000 == 0) || v >= 0x7FFFFFF0) {
                line("{p}", s);
            }

            if (v == 7777777) {
                apple.skip_value__ALLY__UnitTest(0x7FFFFF00);
            }

            if (v == 0x7FFFFFFF) {
                break;
            }
        }

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
        if (name.equals("old"))         {       return this.test_arrange();         }

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

        if (false) {
            //Gem.dump();
            //Gem.map_string_inspection                         .dump("Inspections");
            //Storehouse_MessageFormattable                   .dump(z);
            //Storehouse_PortraySegmentFormatter  .singleton  .dump(z);
            //Storehouse_String                               .dump(z);
            //Storehouse_AdornmentSegmentFormatter.singleton  .dump("Storehouse_AdornmentSegmentFormatter.singleton");
            z.dump();
        }
    }
}
