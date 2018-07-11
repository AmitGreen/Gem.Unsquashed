//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Silver;


import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Interface.Gem_Comparable;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.World.Comparable_Inspection;
import link.crystal.Gem.World.World_String;


public class    Silver_String
    extends     Gem_Object    <Comparable_Inspection>
//  extends     Object
    implements  Gem_Comparable<Comparable_Inspection>,
                Inspectable   <Comparable_Inspection>//,                //  Via Gem_Object
{
    private static final Comparable_Inspection  inspection = Comparable_Inspection.create("Silver_String", 12);


    //
    //  Members
    //
    private       String                world_name;
    public  final World_String          world_s;
    public  final String                s_0;


    //
    //  Constructor & Factory
    //
    protected                           Silver_String(World_String world_s)
    {
        this.world_name = null;
        this.world_s    = world_s;
        this.s_0        = null;
    }


    public static Silver_String         create__ALLY__Gem(World_String world_s)
    {
        return new Silver_String(world_s);
    }


    //
    //  Interface Gem_Comparable
    //
    public int                          compareTo(Gem_Comparable<? extends Comparable_Inspection> that)
    {
        final int                       class_compare = 11 - that.inspect().class_order;

        if (class_compare != 0) {
            return class_compare;
        }

        final Silver_String            that_2 = (Silver_String) that;

        return this.world_s.compareTo(that_2.world_s);
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
        builder.quote(this.world_s.s);
        builder.append(">");
    }
}
