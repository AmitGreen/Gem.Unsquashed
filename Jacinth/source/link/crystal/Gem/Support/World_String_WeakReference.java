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
import link.crystal.Gem.World.World_String;


public class    World_String_WeakReference
    extends     Gem_WeakReference                 <Gem_Reference_Inspection, World_String, Comparable_Inspection>
//  extends     WeakReference                                               <World_String>
//  extends     Reference                                                   <World_String>
//  extends     Object
    implements  Gem_ComparableReference_Interface<Gem_Reference_Inspection, World_String, Comparable_Inspection>,
                Gem_Reference_Interface          <Gem_Reference_Inspection>,    //  Via Gem_ComparableReference_Interface
                Gem_Comparable                   <Gem_Reference_Inspection>,    //  Via Gem_ComparableReference_Interface
                Comparable<Gem_Comparable<? extends Comparable_Inspection>>,    //  Via Gem_Comparable
                Inspectable                      <Gem_Reference_Inspection>//,  //  Via Gem_Comparable
{
    private static final Gem_Reference_Inspection   inspection = Gem_Reference_Inspection.create(
            "World_String_WeakReference",
            Comparable_Inspection.CLASS_ORDER__WORLD_STRING_REFERENCE,
            "weak"//,
        );


    //
    //  Members
    //
    private       String                world_name;
    public  final int                   pulp;
    public  final String                s;


    //
    //  Constructor
    //
    private                             World_String_WeakReference(
            World_String                        client,
            Gem_ReferenceQueue                  reference_queue,
            int                                 pulp,
            String                              s//,
        )
    {
        super(client, reference_queue);

        this.world_name = null;
        this.pulp       = pulp;
        this.s          = s;
    }


    public static World_String_WeakReference    create__ALLY__Gem(
            World_String                        client,
            Gem_ReferenceQueue                  reference_queue//,
        )
    {
        final String                    s = client.s;

        final int                       pulp = s.hashCode();

        return new World_String_WeakReference(client, reference_queue, pulp, s);
    }


    //
    //  Ancestor Object
    //
    //  NOTE:
    //      Do not need to override `.equals` -- as World_String_WeakReference are unique (and thus can use
    //      `Object.equals` which uses identity as the equal test).
    //
    @Override
    public int                          hashCode()
    {
        return this.pulp;
    }


    //
    //  NOTE:
    //      Only need to compare to another `World_String_WeakReference`, by using the identity test `==`` as
    //      `World_String_WeakReference` instances are unique.
    //
    //  HOWEVER:
    //      Do need to compare to a `World_String_WeakReference` (since might be replaced by it in the cache).
    //
    @Override
    public boolean                      equals(Object that)
    {
        if (this == that) {
            return true;
        }

        if ( ! (that instanceof World_String_EnduringReference)) {
            return false;
        }

        World_String_EnduringReference  that_2 = (World_String_EnduringReference) that;

        return this.s.equals(that_2.client.s);
    }


    //
    //  Interface java.lang.Comparable
    //
    @Override
    public int                          compareTo(Gem_Comparable<? extends Comparable_Inspection> that)
    {
        final Comparable_Inspection     that_inspection = that.inspect();

        final int                       class_compare = (
                Comparable_Inspection.CLASS_ORDER__WORLD_STRING_REFERENCE - that_inspection.class_order
            );

        if (class_compare != 0) {
            return class_compare;
        }

        //
        //  SINCE:
        //      `that` has a class order of `Comparable_Inspection.CLASS_ORDER__WORLD_STRING_REFERENCE`
        //
        //  THEREFORE:
        //      `that_inspection` is of type `Gem_Reference_Inspection`
        //
        final Gem_Reference_Inspection  that__reference_inspection = (Gem_Reference_Inspection) that_inspection;

        if (that__reference_inspection.is_enduring_reference) {
            final World_String_EnduringReference    that_2 = (World_String_EnduringReference) that;

            return this.s.compareTo(that_2.client.s);
        }

        assert fact(that__reference_inspection.is_weak_reference, "fact(that__reference_inspection.is_weak_reference)");

        final World_String_WeakReference    that_2 = (World_String_WeakReference) that;

        return this.s.compareTo(that_2.s);
    }


    //
    //  Interface Gem_Comparable
    //
    //<empty>


    //
    //  Interface Gem_ComparableReference_Interface
    //
    public void                         reap()
    {
        final Gem_ComparableReference_Interface<
                  ? extends Comparable_Inspection,
                  World_String,
                  Comparable_Inspection
              >                         previous = Gem.string_cache.remove(this);

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
        World_String                    client = this.get();

        if (client == null) {
            builder.append("<World_String_WeakReference exhausted; ", this.s, ">");
            return;
        }

        builder.append("<World_String_WeakReference ");
        builder.portray(client);
        builder.append(">");
    }
}
