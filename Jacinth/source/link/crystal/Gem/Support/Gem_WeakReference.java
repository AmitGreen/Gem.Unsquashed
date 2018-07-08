//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.io.PrintStream;
import java.lang.ref.WeakReference;
import java.lang.System;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.WeakReferenceable;
import link.crystal.Gem.World.Inspection;


public abstract class   Gem_WeakReference<INSPECTION extends Inspection, CLIENT extends WeakReferenceable>
    extends             WeakReference  <CLIENT>
//  extends             Reference      <CLIENT>
//  extends             Object
    implements          Inspectable<INSPECTION>//,
{
    //
    //  Public static
    //
    public static final PrintStream     standard_output = System.out;


    //
    //  Constructor
    //
    protected                           Gem_WeakReference(CLIENT client)
    {
        super(client);
    }


    //
    //  Interface Inspectable
    //
    public abstract INSPECTION          inspect();
    public abstract void                portray(Gem_StringBuilder builder);


    //
    //  Public (other)
    //
    public static void                  output(String s)
    {
        standard_output.println(s);
    }
}
