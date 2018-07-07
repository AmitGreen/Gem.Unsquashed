//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.World;


import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Interface.Inspectable;


public class    World_Integer
    extends     Gem_Object<Inspection>
//  extends     Object
    implements  Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static final Inspection     inspection = Inspection.create("World_Integer");


    //
    //  Members
    //
    private       String                world_name;
    public  final int                   value;


    //
    //  Constructor & Factory
    //
    protected                           World_Integer(int value)
    {
        this.world_name = null;
        this.value      = value;
    }


    public static World_Integer         create(int value)
    {
        return new World_Integer(value);
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
        builder.append("<", this.value, ">");
    }
}
