//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.UnitTest;


import link.crystal.Gem.Core.Gem;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Inspection.Inspection;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Support.AnalyzeString;
import link.crystal.Gem.Support.AsciiTable;
import link.crystal.Gem.Support.Gem_ReferenceQueue;
import link.crystal.Gem.Support.Gem_TimeUnit;
import link.crystal.Gem.Support.Map_String_Inspection;
import link.crystal.Gem.Support.Storehouse_AdornmentSegmentFormatter;
import link.crystal.Gem.Support.Storehouse_MessageFormattable;
import link.crystal.Gem.Support.Storehouse_PortraySegmentFormatter;
import link.crystal.Gem.Support.Storehouse_String;
import link.crystal.Gem.Support.UniqueName;
import link.crystal.Gem.Support.World_String_WeakReference;
import link.crystal.Gem.UnitTest.World_String_WeakReference_PhantomReference;
import link.crystal.Gem.World.World_Integer;
import link.crystal.Gem.World.World_String;


public final class  UnitTest_Gem
    extends         Gem_Object <Inspection>
//  extends         Object
    implements      Inspectable<Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("UnitTest_Gem");


    //
    //  Members
    //
    public  final Zone                                          z;
    private /*:*/ World_String_WeakReference_PhantomReference   phantom;


    //
    //  Constructor & Factory
    //
    private                             UnitTest_Gem(final Zone z)
    {
        this.z       = z;
        this.phantom = null;
    }


    public final static UnitTest_Gem    create(final Zone z)
    {
        return new UnitTest_Gem(z);
    }


    //
    //  Public (Unit tests)
    //
    public final boolean                test_analyze_string()
    {
        AnalyzeString.show_analyze_string("Can't");

        return true;
    }


    public final boolean                test_arrange()
    {
        final Zone                      z = Zone.current_zone();

        //assert Gem_Object.fact_pointer(null, "test");
        //assert Gem_Object.fact_between(7, 6, 77);

        line("{+}: created: {}", 7);
        line("hi: {{ and {{ yes {p} then }}", arrange("\"arrange {}", 7));

        //line("{+}");
        //line("{+}: test {}", 7);
        //line("that: {+}");
        //line("that: {}", "hi");
        //line("that: {0}", "bye");
        //line("prefix {0} suffix", "middle");

        return true;
    }


    public final boolean                test_integer()
    {
        final Zone                      z = this.z;

        /*:*/ World_Integer             seven = z.conjure_integer(7);
        /*:*/ World_Integer             eight = z.conjure_integer(8);
        /*:*/ World_Integer             nine  = z.conjure_integer(9);

        line("{+}: {} .vs {}: {}", seven, eight, seven.compareTo(eight));

        /*:*/ World_Integer             seven_2 = z.conjure_integer(7);

        assert fact(seven == seven_2, "seven == seven_2");

        Gem.integer_cache.dump("integer cache - before");

        seven =
            seven_2 = null;

        eight = null;
        nine = null;

        Gem.reference_queue.garbage_collect__AND__possible_sleep();
        //Gem.reference_queue.garbage_collect();

        Gem.integer_cache.dump("integer cache - after");

        World_Integer                   seven_3 = z.conjure_integer(7);

        return true;
    }


    public final boolean                test_string()
    {
        Gem.store_unit_test__ALLY__UnitTest(this);

        /*:*/ World_String              seven = z.conjure_string("seven");
        /*:*/ World_String              eight = z.conjure_string("eight");
        /*:*/ World_String              nine  = z.conjure_string("nine");

        line("{+}: {} .vs {}: {}", seven, eight, seven.compareTo(eight));

        /*:*/ World_String             seven_2 = z.conjure_string("seven");
        /*:*/ World_String             eight_2 = z.conjure_enduring_string("eight");

        assert fact(seven == seven_2, "seven == seven_2");
        assert fact(eight == eight_2, "eight == eight_2");

        Gem.string_cache.dump("string cache - before");

        seven =
            seven_2 = null;

        eight = null;
        nine  = null;

        Gem.reference_queue.garbage_collect__AND__possible_sleep();
        //Gem.reference_queue.garbage_collect();

        Gem.string_cache.dump("string cache - after");

        World_String                    seven_3 = z.conjure_string("seven");

        return true;
    }


    public final boolean                test_time_unit()
    {
        Gem_TimeUnit.test();

        return true;
    }


    public final boolean                test_unique_name()
    {
        final Zone                      z = Zone.current_zone();

        final UniqueName                apple = UniqueName.create__ALLY__Gem(z, "apple");

        line("apple: {}", apple);

        for (;;) {
            final int                   v = apple.value__ALLY__UnitTest();

            final String                s = apple.next();

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
    public final void                   discarding__World_String_WeakReference(
            final World_String_WeakReference    weak_reference//,
        )
    {
        assert fact_null(this.phantom, "this.phantom");

        this.phantom = World_String_WeakReference_PhantomReference.create__ALLY__Gem(
                weak_reference,
                Gem.reference_queue//,
            );

        line("discarding__World_String_WeakReference({}): phantom{}", weak_reference, phantom);
    }
}
