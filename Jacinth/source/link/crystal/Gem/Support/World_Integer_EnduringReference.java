//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.Comparable;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Interface.Gem_Comparable;
import link.crystal.Gem.Interface.Gem_Reference_Interface;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.World.Comparable_Inspection;
import link.crystal.Gem.World.World_Integer;


public class    World_Integer_EnduringReference
    extends     Gem_Object             <Comparable_Inspection>
//  extends     Object
    implements  Gem_Reference_Interface<Comparable_Inspection, World_Integer, Comparable_Inspection>,
                Gem_Comparable         <Comparable_Inspection>,                 //  Via Gem_WeakReferenceable_Interface
                Comparable<Gem_Comparable<? extends Comparable_Inspection>>,    //  Via Gem_Comparable
                Inspectable            <Comparable_Inspection>//,               //  Via Gem_Comparable
{
    private static final Comparable_Inspection  inspection = (
            Comparable_Inspection.create("World_Integer_EnduringReference", 13)
        );


    //
    //  Members
    //
    public final World_Integer          client;


    //
    //  Constructor
    //
    private                             World_Integer_EnduringReference(World_Integer client)
    {
        this.client = client;
    }


    public static World_Integer_EnduringReference   create__ALLY__Gem(World_Integer client)
    {
        return new World_Integer_EnduringReference(client);
    }


    //
    //  Ancestor Object
    //
    //  NOTE:
    //      Do not need to override `.equals` -- as `World_Integer_EnduringReference` are unique (and thus can use
    //      `Object.equals` which uses identity as the equal test).
    //
    @Override
    public int                          hashCode()
    {
        return this.client.value;
    }


    //
    //  Interface Gem_Comparable (and java.lang.Comparable)
    //
    public int                          compareTo(Gem_Comparable<? extends Comparable_Inspection> that)
    {
        final int                       that__class_order = that.inspect().class_order;

        if (that__class_order == 9) {                                   //  9 = World_Integer_WeakReference
            final World_Integer_WeakReference   that_2 = (World_Integer_WeakReference) that;

            return this.client.value - that_2.value;
        }

        final int                       class_compare = 13 - that__class_order;

        if (class_compare != 0) {
            return class_compare;
        }

        final World_Integer_EnduringReference   that_2 = (World_Integer_EnduringReference) that;

        return this.client.value - that_2.client.value;
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
        builder.append("<World_Integer_EnduringReference ");
        builder.portray(client);
        builder.append(">");
    }


    //
    //  Interface Gem_Reference_Interface
    //
    @Override
    public World_Integer                client()
    {
        return this.client;
    }


    @Override
    public boolean                      enqueue()
    {
        INVALID_ROUTINE();

        return false;
    }
}
