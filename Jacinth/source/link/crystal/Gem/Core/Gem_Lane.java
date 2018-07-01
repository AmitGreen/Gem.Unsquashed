//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.lang.RuntimeException;
import java.lang.Thread;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Interface.Inspectable;


public class    Gem_Lane
    extends     Gem_Object<Inspection>
//  extends     Object
    implements  Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create_with_portrait("Gem.Gem_Lane");


    //
    //  Static members
    //
    public static Thread                silver_thread = null;


    //
    //  Members
    //


    //
    //  Constructor & Factory
    //
    private                             Gem_Lane()
    {
    }


    public static Gem_Lane              create()
    {
        return new Gem_Lane();
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
    public static void                  initialize()
    {
        if (Gem_Lane.silver_thread != null) {
            throw new RuntimeException("Gem_Lane.initialize: called more than once");
        }

        Gem_Lane.silver_thread = Thread.currentThread();
    }
}
