//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.World;


import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Interface.Gem_Comparable;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.Reference_Interface;
import link.crystal.Gem.Interface.WeakReferenceable_Interface;
import link.crystal.Gem.World.Comparable_Inspection;


public class    World_String
    extends     Gem_Object                 <Comparable_Inspection>
//  extends     Object
    implements  WeakReferenceable_Interface<Comparable_Inspection>,
                Reference_Interface        <Comparable_Inspection>,     //  Via WeakReferenceable_Interface
                Gem_Comparable             <Comparable_Inspection>,     //  Via Reference_Interface
                Inspectable                <Comparable_Inspection>//,   //  Via Gem_Comparable
{
    private static final Comparable_Inspection  inspection = Comparable_Inspection.create("World_String", 10);


    //
    //  Members
    //
    private       String                world_name;
    public  final String                s;


    //
    //  Constructor & Factory
    //
    protected                           World_String(String s)
    {
        this.world_name = null;
        this.s          = s;
    }


    public static World_String          create__ALLY__Gem(String s)
    {
        return new World_String(s);
    }


    //
    //  Interface Gem_Comparable
    //
    public int                          compareTo(Gem_Comparable<? extends Comparable_Inspection> that)
    {
        final int                       class_compare = 10 - that.inspect().class_order;

        if (class_compare != 0) {
            return class_compare;
        }

        final World_String             that_2 = (World_String) that;

        return this.s.compareTo(that_2.s);
    }


    //
    //  Interface Inspectable
    //
    public Comparable_Inspection        inspect()
    {
        return /*static*/ this.inspection;
    }


    public void                         portray(Gem_StringBuilder builder)
    {
        builder.append("<");
        builder.quote(this.s);
        builder.append(">");
    }
}