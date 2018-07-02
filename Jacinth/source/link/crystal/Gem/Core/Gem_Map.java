//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.util.HashMap;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Support.OutputFunctions;
import link.crystal.Gem.Support.PortrayFunctions;


public abstract class   Gem_Map<INSPECTION extends Inspection, K, V>
    extends             HashMap        <K, V>
//  extends             AbstractHashMap<K, V>
//  extends             Object
    implements          Inspectable<INSPECTION>//,
{
    //
    //  Constructor
    //
    protected                           Gem_Map(int initial_capacity)
    {
        super(initial_capacity);
    }


    //
    //  Interface Inspectable
    //
    public abstract INSPECTION          inspect();
    public abstract String              portray();


    //
    //  Abstract
    //
    public abstract void                dump(String name);


    //
    //  Public
    //
    public static void                  line()
    {
        OutputFunctions.line();
    }


    public static void                  line(String s)
    {
        OutputFunctions.line(s);
    }


    public static void                  line(String format, Object first_argument, Object ... other_arguments)
    {
        OutputFunctions.line(format, first_argument, other_arguments);
    }


    public static String                portray(Object v)
    {
        return PortrayFunctions.portray(v);
    }


    public static String                portray_string(String s)
    {
        return PortrayFunctions.portray_string(s);
    }
}
