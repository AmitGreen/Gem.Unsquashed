//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.World;


import java.lang.Comparable;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Interface.Gem_Comparable;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.Gem_Referenceable_Interface;
import link.crystal.Gem.Inspection.Comparable_Inspection;


public class    World_Integer
    extends     Gem_Object                 <Comparable_Inspection>
//  extends     Object
    implements  Gem_Referenceable_Interface<Comparable_Inspection>,
                Gem_Comparable             <Comparable_Inspection>,
                Comparable<Gem_Comparable<? extends Comparable_Inspection>>,    //  Via Gem_Comparable
                Inspectable                <Comparable_Inspection>//,           //  Via Gem_Comparable
{
    private static final Comparable_Inspection  inspection = Comparable_Inspection.create(
            "World_Integer",
            Comparable_Inspection.CLASS_ORDER__World_Integer//,
        );


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


    public static World_Integer         create__ALLY__Gem(int value)
    {
        return new World_Integer(value);
    }


    //
    //  Interface java.lang.Comparable
    //
    @Override
    public int                          compareTo(Gem_Comparable<? extends Comparable_Inspection> that)
    {
        final int                       class_compare = (
                Comparable_Inspection.CLASS_ORDER__World_Integer - that.inspect().class_order
            );

        if (class_compare != 0) {
            return class_compare;
        }

        final World_Integer             that_2 = (World_Integer) that;

        return this.value - that_2.value;
    }


    //
    //  Interface Gem_Comparable
    //
    //<empty>


    //
    //  Interface Inspectable
    //
    public Comparable_Inspection        inspect()
    {
        return /*static*/ this.inspection;
    }


    public void                         portray(Gem_StringBuilder builder)
    {
        builder.append("<", this.value, ">");
    }
}
