//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.util.HashMap;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Exception.ExceptionFunctions;
import link.crystal.Gem.Interface.Inspectable;


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
    public abstract void                portray(Gem_StringBuilder builder);


    //
    //  Abstract
    //
    public abstract void                dump(Zone z, String name);


    //
    //  Public (ASSERT)
    //
    public static boolean               fact(boolean condition, String format)
    {
        if (condition) {
            return true;
        }

        ExceptionFunctions.ASSERTION_FAILED(2, "assertion failed: {}", format);

        return false;
    }


    public static boolean               fact_null(Object p, String name)
    {
        if (p == null) {
            return true;
        }

        ExceptionFunctions.ASSERT(2, "`{}` is not null", name);

        return false;
    }


    public static boolean               fact_pointer(Object p, String name)
    {
        if (p != null) {
            return true;
        }

        final Zone                      z = Zone.current_zone();

        ExceptionFunctions.ASSERT(2, "`{}` is null", name);

        return false;
    }


    //
    //  Public (ERRORS)
    //
    public void                         RUNTIME(String error_message, Object ... arguments)
    {
        ExceptionFunctions.RUNTIME(2, error_message, arguments);
    }


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
            RUNTIME("previous value for {} already exists: {}", k, v);
        }
    }
}
