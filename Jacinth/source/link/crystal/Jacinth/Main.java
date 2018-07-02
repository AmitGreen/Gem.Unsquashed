//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Jacinth;


import link.crystal.Gem.Support.Storehouse_ArgumentSegmentFormatter;
import link.crystal.Gem.Support.Storehouse_MessageFormattable;
import link.crystal.Gem.Support.Storehouse_String;
import link.crystal.Gem.Support.Storehouse_StringSegmentFormatter;
import link.crystal.Mirror.Shape;


public class    Main 
{
    public static void                  main(String[] args)
    {
        Shape                           circle = Shape.create("circle");

        circle.skew();

        Storehouse_ArgumentSegmentFormatter.dump();
        Storehouse_MessageFormattable      .dump();
        Storehouse_String                  .dump();
        Storehouse_StringSegmentFormatter  .dump();
    }
}
