//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Jacinth;


import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Support.Storehouse_ArgumentSegmentFormatter;
import link.crystal.Gem.Support.Storehouse_MessageFormattable;
import link.crystal.Gem.Support.Storehouse_String;
import link.crystal.Gem.Support.Storehouse_StringSegmentFormatter;
import link.crystal.Mirror.Shape;


public class    Main
{
    public static void                  main(String[] args)
    {
        Zone                            z = Zone.current_zone();

        Shape                           circle = Shape.create(z, "circle");

        circle.skew(z);

        z.line("{+}");
        z.line("{}", "{}");
        z.line("{+}: test {}", 7);
        z.line("that: {+}");
        z.line("that: {}", "hi");
        z.line("that: {0}", "bye");
        z.line("prefixl {0} suffix", "middle");

        if (true) {
            Storehouse_ArgumentSegmentFormatter.singleton.dump(z);
            Storehouse_MessageFormattable      .dump(z);
            Storehouse_String                  .dump(z);
            Storehouse_StringSegmentFormatter  .singleton.dump(z, "Storehouse_StringSegmentFormatter.singleton");

            z.dump(z);
        }

    }
}
