//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Gem_Comparable;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Support.World_Integer_WeakReference;
import link.crystal.Gem.World.Inspection;
import link.crystal.Gem.World.World_Integer;


public class    World_Integer_Key
    extends     Gem_Object <Inspection>
//  extends     Object
    implements  Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static final Inspection     inspection = Inspection.create("World_Integer_Key");


    //
    //  Members
    //
    private final Zone                  z;
    public int                          value;


    //
    //  Constructor, Factory, & Recycle
    //
    protected                           World_Integer_Key(Zone z)
    {
        this.z     = z;
        this.value = 0;
    }


    public static World_Integer_Key     create__ALLY__Zone(Zone z)
    {
        return new World_Integer_Key(z);
    }


    public void                         recycle(int value)
    {
        this.value = value;
    }


    //
    //  Abstract object
    //
    @Override
    public int                          hashCode()
    {
        return this.value;
    }


    @Override
    public boolean                      equals(Object that)
    {
        if ( ! (that instanceof World_Integer_WeakReference)) {
            return false;
        }

        World_Integer_WeakReference     weak_reference = (World_Integer_WeakReference) that;

        return this.value == weak_reference.value;
    }


    //
    //  Interface Inspectable
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }


    public void                         portray(Gem_StringBuilder builder)
    {
        builder.append("<World_Integer_Key ", this.value, ">");
    }
}
