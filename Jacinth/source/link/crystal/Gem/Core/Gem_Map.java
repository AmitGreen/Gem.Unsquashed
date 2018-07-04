//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.util.HashMap;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Support.ExceptionFunctions;
import link.crystal.Gem.Support.PortrayFunctions;


public abstract class   Gem_Map<INSPECTION extends Inspection, K, V>
    extends             HashMap        <K, V>
//  extends             AbstractHashMap<K, V>
//  extends             Object
    implements          Inspectable<INSPECTION>//,
{
    //
    //  Members
    //
    protected final Zone                z;


    //
    //  Constructor
    //
    protected                           Gem_Map(Zone z, int initial_capacity)
    {
        super(initial_capacity);

        this.z = z;
    }


    //
    //  Interface Inspectable
    //
    public abstract INSPECTION          inspect();
    public abstract String              portray(Zone z);


    //
    //  Abstract
    //
    public abstract void                dump(Zone z, String name);


    //
    //  Public
    //
    public V                            lookup(K k)
    {
        return this.get(k);
    }


    public void                         insert(K k, V v)
    {
        final V                         previous = this.putIfAbsent(k, v);

        if (previous != null) {
            final Zone                  z = this.z;

            z.RUNTIME("previous value for {0} already exists: {1}", k, v);
        }
    }
}
