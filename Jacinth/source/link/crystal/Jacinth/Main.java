//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Jacinth;


import link.crystal.Gem.Core.PermenantMessageFormattable;
import link.crystal.Gem.Core.PermenantString;
import link.crystal.Gem.Format.PermenantArgumentFormatter;
import link.crystal.Mirror.Shape;


public class    Main 
{
    public static void                  main(String[] args)
    {
        Shape                           circle = Shape.create("circle");

        circle.skew();

        PermenantArgumentFormatter .dump();
        PermenantMessageFormattable.dump();
        PermenantString            .dump();
    }
}
