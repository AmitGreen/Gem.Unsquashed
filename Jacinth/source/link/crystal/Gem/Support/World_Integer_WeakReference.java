//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.Comparable;
import java.lang.ref.WeakReference;
import link.crystal.Gem.Core.Gem;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Inspection.Comparable_Inspection;
import link.crystal.Gem.Inspection.Gem_Reference_Inspection;
import link.crystal.Gem.Interface.Gem_Comparable;
import link.crystal.Gem.Interface.Gem_ComparableReference_Interface;
import link.crystal.Gem.Interface.Gem_Reference_Interface;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Support.Gem_ReferenceQueue;
import link.crystal.Gem.Support.Gem_WeakReference;
import link.crystal.Gem.World.World_Integer;


public class    World_Integer_WeakReference
    extends     Gem_WeakReference      <Gem_Reference_Inspection, World_Integer, Comparable_Inspection>
//  extends     WeakReference                                 <World_Integer>
//  extends     Reference                                     <World_Integer>
//  extends     Object
    implements  Gem_ComparableReference_Interface<Gem_Reference_Inspection, World_Integer, Comparable_Inspection>,
                Gem_Reference_Interface          <Gem_Reference_Inspection>,    //  Via Gem_ComparableReference_Interface
                Gem_Comparable                   <Gem_Reference_Inspection>,    //  Via Gem_ComparableReference_Interface
                Comparable<Gem_Comparable<? extends Comparable_Inspection>>,    //  Via Gem_Comparable
                Inspectable                      <Gem_Reference_Inspection>//,
{
    private static final Gem_Reference_Inspection   inspection = Gem_Reference_Inspection.create(
            "World_Integer_WeakReference",
            Comparable_Inspection.CLASS_ORDER__WORLD_INTEGER_REFERENCE,
            "weak"//,)
        );


    //
    //  Members
    //
    private       String                world_name;
    public  final int                   value;


    //
    //  Constructor
    //
    private                             World_Integer_WeakReference(
            World_Integer                       client,
            Gem_ReferenceQueue                  reference_queue,
            int                                 value//,
        )
    {
        super(client, reference_queue);

        this.world_name = null;
        this.value      = value;
    }


    public static World_Integer_WeakReference   create__ALLY__Gem(
            World_Integer                       client,
            Gem_ReferenceQueue                  reference_queue//,
        )
    {
        final int                       value = client.value;

        return new World_Integer_WeakReference(client, reference_queue, value);
    }


    //
    //  Ancestor Object
    //
    @Override
    public int                          hashCode()
    {
        return this.value;
    }


    //
    //  NOTE:
    //      Only need to compare to another `World_Integer_WeakReference`, by using the identity test `==`` as
    //      `World_Integer_WeakReference` instances are unique.
    //
    //  HOWEVER:
    //      Do need to compare to a `World_Integer_WeakReference` (since might be replaced by it in the cache).
    //
    @Override
    public boolean                      equals(Object that)
    {
        if (this == that) {
            return true;
        }

        if ( ! (that instanceof World_Integer_EnduringReference)) {
            return false;
        }

        World_Integer_EnduringReference     that_2 = (World_Integer_EnduringReference) that;

        return this.value == that_2.client.value;
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

            return this.value - that_2.client.value;
        }

        assert fact(that__reference_inspection.is_weak_reference, "fact(that__reference_inspection.is_weak_reference)");

        final World_Integer_WeakReference   that_2 = (World_Integer_WeakReference) that;

        return this.value - that_2.value;
    }


    //
    //  Interface Gem_Comparable
    //
    //<empty>


    //
    //  Interface Gem_QueueableReference_Interface
    //
    public void                         reap()
    {
        final Gem_ComparableReference_Interface<
                  ? extends Comparable_Inspection,
                  World_Integer,
                  Comparable_Inspection
              >                         previous = Gem.integer_cache.remove(this);

        if (previous != this) {
            RUNTIME("failed to remove {}", this);
        }
    }


    //
    //  Interface Gem_Reference_Interface
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
        World_Integer                   client = this.get();

        if (client == null) {
            builder.append("<World_Integer_WeakReference exhausted; ", this.value, ">");
            return;
        }

        builder.append("<World_Integer_WeakReference ");
        builder.portray(client);
        builder.append(">");
    }
}
