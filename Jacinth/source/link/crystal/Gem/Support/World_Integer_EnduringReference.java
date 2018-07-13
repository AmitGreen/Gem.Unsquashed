//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.Comparable;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Inspection.Comparable_Inspection;
import link.crystal.Gem.Inspection.Gem_Reference_Inspection;
import link.crystal.Gem.Interface.Gem_Comparable;
import link.crystal.Gem.Interface.Gem_ComparableReference_Interface;
import link.crystal.Gem.Interface.Gem_Reference_Interface;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.World.World_Integer;


public class    World_Integer_EnduringReference
    extends     Gem_Object             <Gem_Reference_Inspection>
//  extends     Object
    implements  Gem_ComparableReference_Interface<Gem_Reference_Inspection, World_Integer, Comparable_Inspection>,
                Gem_Reference_Interface          <Gem_Reference_Inspection>,    //  Via Gem_ComparableReference_Interface
                Gem_Comparable                   <Gem_Reference_Inspection>,    //  Via Gem_ComparableReference_Interface
                Comparable<Gem_Comparable<? extends Comparable_Inspection>>,    //  Via Gem_Comparable
                Inspectable                      <Gem_Reference_Inspection>//,
{
    private static final Gem_Reference_Inspection   inspection = Gem_Reference_Inspection.create(
            "World_Integer_EnduringReference",
            Comparable_Inspection.CLASS_ORDER__WORLD_INTEGER_REFERENCE,
            "enduring"//,
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
    @Override
    public int                          hashCode()
    {
        return this.client.value;
    }


    //
    //  NOTE:
    //      Only need to compare to another `World_Integer_EnduringReference`, by using the identity test `==`` as
    //      `World_Integer_EnduringReference` instances are unique.
    //
    //  HOWEVER:
    //      Do need to compare to a `World_Integer_WeakReference` (since might be replacing it in the cache).
    //
    public boolean                      equals(Object that)
    {
        if (this == that) {
            return true;
        }

        if ( ! (that instanceof World_Integer_WeakReference)) {
            return false;
        }

        World_Integer_WeakReference     that_2 = (World_Integer_WeakReference) that;

        return this.client.value == that_2.value;
    }


    //
    //  Interface java.lang.Comparable
    //
    @Override
    public int                          compareTo(Gem_Comparable<? extends Comparable_Inspection> that)
    {
        final Comparable_Inspection     that_inspection = that.inspect();

        final int                       class_compare = (
                Comparable_Inspection.CLASS_ORDER__WORLD_INTEGER_REFERENCE - that_inspection.class_order
            );

        if (class_compare != 0) {
            return class_compare;
        }

        //
        //  SINCE:
        //      `that` has a class order of `Comparable_Inspection.CLASS_ORDER__WORLD_INTEGER_REFERENCE`
        //
        //  THEREFORE:
        //      `that_inspection` is of type `Gem_Reference_Inspection`
        //
        final Gem_Reference_Inspection  that__reference_inspection = (Gem_Reference_Inspection) that_inspection;

        if (that__reference_inspection.is_enduring_reference) {
            final World_Integer_EnduringReference   that_2 = (World_Integer_EnduringReference) that;

            return this.client.value - that_2.client.value;
        }

        assert fact(that__reference_inspection.is_weak_reference, "fact(that__reference_inspection.is_weak_reference)");

        final World_Integer_WeakReference   that_2 = (World_Integer_WeakReference) that;

        return this.client.value - that_2.value;
    }


    //
    //  Interface Gem_Comparable
    //
    //<empty>


    //
    //  Interface Inspectable
    //
    public Gem_Reference_Inspection     inspect()
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
    //  Interface Gem_ComparableReference_Interface
    //
    @Override
    public World_Integer                client_OR_enqueue()
    {
        return this.client;
    }


    //
    //  Interface Gem_Reference_Interface
    //
    //<empty>
}
