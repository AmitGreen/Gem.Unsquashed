//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Jacinth;


import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Support.Map_String_Inspection;
import link.crystal.Gem.Support.Storehouse_AdornmentSegmentFormatter;
import link.crystal.Gem.Support.Storehouse_MessageFormattable;
import link.crystal.Gem.Support.Storehouse_PortraySegmentFormatter;
import link.crystal.Gem.Support.Storehouse_String;
import link.crystal.Mirror.Shape;


public class    Main
{
    public static void                  main(String[] args)
    {
        Zone                            z = Zone.current_zone();

        Shape                           circle = Shape.create(z, "circle");

        circle.skew(z);

        //assert Gem_Object.fact_pointer(null, "test");
        //assert Gem_Object.fact_between(7, 6, 77);

        //z.line("{+}");
        z.line("hi: {{ and {{ yes {p} then }}", "hmm");
        //z.line("{+}: test {}", 7);
        //z.line("that: {+}");
        //z.line("that: {}", "hi");
        //z.line("that: {0}", "bye");
        //z.line("prefix {0} suffix", "middle");

        if (true) {
            //Map_String_Inspection.singleton().dump(z, "Inspections");

            Storehouse_MessageFormattable       .dump(z);
            //Storehouse_PortraySegmentFormatter  .singleton.dump(z);
            //Storehouse_String                   .dump(z);
            Storehouse_AdornmentSegmentFormatter.singleton.dump(z, "Storehouse_AdornmentSegmentFormatter.singleton");
            //z.dump(z);
        }

    }
}
