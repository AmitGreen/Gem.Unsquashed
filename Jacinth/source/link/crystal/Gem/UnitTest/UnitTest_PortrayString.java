
//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.UnitTest;


import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Inspection.Inspection;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Support.AnalyzeString;
import link.crystal.Mirror.Shape;


final class         PortrayStringData_2
    extends         Gem_Object <Inspection>
//  extends         Object
    implements      Inspectable<Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("PortrayStringData_2");


    //
    //  Members
    //
    public final String                 s;
    public final String                 raw_expected;


    //
    //  Constructor & Factory
    //
    private                             PortrayStringData_2(final String s, final String raw_expected)
    {
        this.s            = s;
        this.raw_expected = raw_expected;
    }


    public static final PortrayStringData_2     create(final String s, final String raw_expected)
    {
        return new PortrayStringData_2(s, raw_expected);
    }


    //
    //  Interface Inspectable
    //
    @Override
    public final Inspection             inspect()
    {
        return /*static*/ this.inspection;
    }


    @Override
    public final void                   portray(final Gem_StringBuilder builder)
    {
        builder.append("<PortrayStringData_2 ");
        builder.java_quote(this.s);
        builder.append("; ", this.raw_expected, ">");
    }
}


public final class  UnitTest_PortrayString
    extends         Gem_Object <Inspection>
//  extends         Object
    implements      Inspectable<Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("UnitTest_PortrayString");


    //
    //  Members
    //
    public final Zone                   z;


    //
    //  Static Members (Unit Test Data)
    //
    static public final PortrayStringData_2[]   portray_string_many = new PortrayStringData_2[] {
            //<A_A>
                //
                //  A_A: ra
                //
                PortrayStringData_2.create(
                       "wink \\\"\\\"'",
                    "r\"wink \\\"\\\"'\""//,
                )//,
        };


    //
    //  Constructor & Factory
    //
    private                             UnitTest_PortrayString(final Zone z)
    {
        this.z = z;
    }


    public static final UnitTest_PortrayString  create(final Zone z)
    {
        return new UnitTest_PortrayString(z);
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
    //  Public (Unit tests)
    //
    public final boolean                test_portray_string()
    {
        line("===   Unit Test:  Portray String   ===");

        final PortrayStringData_2[]     portray_string_many = UnitTest_PortrayString.portray_string_many;

        final int                       portray_string_total = portray_string_many.length;

        for (/*:*/ int                  i = 0; i < portray_string_total; i ++) {
            final PortrayStringData_2   portray_string_data = portray_string_many[i];
            
            final String                s            = portray_string_data.s;
            final String                raw_expected = portray_string_data.raw_expected;

            final String                actual = AnalyzeString.analyze_raw_string(s);

            if ( ! actual.equals(raw_expected)) {
                line("portray_raw_string({p})", s);
                line("  actual:   {}", actual);
                line("  expected: {}", raw_expected);

            //  RUNTIME("portray_raw_string({p}) failed", s);
            }
        }

        line("INCOMPLETE:   Unit Test:  Portray String");
        
        return true;
    }
}
