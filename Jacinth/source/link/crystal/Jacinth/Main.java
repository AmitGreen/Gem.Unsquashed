//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Jacinth;


import link.crystal.Gem.Support.PermenantCache_ArgumentFormatter;
import link.crystal.Gem.Support.PermenantCache_MessageFormattable;
import link.crystal.Gem.Support.PermenantCache_String;
import link.crystal.Mirror.Shape;


public class    Main 
{
    public static void                  main(String[] args)
    {
        Shape                           circle = Shape.create("circle");

        circle.skew();

        PermenantCache_ArgumentFormatter .dump();
        PermenantCache_MessageFormattable.dump();
        PermenantCache_String            .dump();
    }
}
