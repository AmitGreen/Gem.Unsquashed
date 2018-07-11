//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.Comparable;
import java.lang.ref.WeakReference;
import link.crystal.Gem.Core.Gem;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Interface.Gem_Comparable;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.Reference_Interface;
import link.crystal.Gem.Support.Gem_ReferenceQueue;
import link.crystal.Gem.Support.Gem_WeakReference;
import link.crystal.Gem.World.Comparable_Inspection;
import link.crystal.Gem.World.Inspection;
import link.crystal.Gem.World.World_Integer;


public class    World_Integer_WeakReference
    extends     Gem_WeakReference<Comparable_Inspection, World_Integer, Comparable_Inspection>
//  extends     WeakReference                           <World_Integer>
//  extends     Reference                               <World_Integer>
//  extends     Object
    implements  Reference_Interface      <Comparable_Inspection>,
                Gem_Comparable           <Comparable_Inspection>,
                Comparable<Gem_Comparable<? extends Comparable_Inspection>>,      //  Via Gem_Comparable
                Inspectable              <Comparable_Inspection>//,     //  Via Gem_Comparable
{
    private static final Comparable_Inspection  inspection = (
            Comparable_Inspection.create("World_Integer_WeakReference", 9)
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
    //  NOTE:
    //      Do not need to override `.equals` -- as World_Integer_WeakReference are unique (and thus can use
    //      `Object.equals` which uses identity as the equal test).
    //
    @Override
    public int                          hashCode()
    {
        return this.value;
    }


    //
    //  Interface Gem_Comparable (and java.lang.Comparable)
    //
    public int                          compareTo(Gem_Comparable<? extends Comparable_Inspection> that)
    {
        final int                       class_compare = 9 - that.inspect().class_order;

        if (class_compare != 0) {
            return class_compare;
        }

        final World_Integer_WeakReference   that_2 = (World_Integer_WeakReference) that;

        return this.value - that_2.value;
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
        World_Integer                   client = this.get();

        if (client == null) {
            builder.append("<World_Integer_WeakReference exhausted; ", this.value, ">");
            return;
        }

        builder.append("<World_Integer_WeakReference ");
        builder.portray(client);
        builder.append(">");
    }


    //
    //  Interface Reference_Interface
    //
    //<empty>


    //
    //  Interface WeakReference
    //
    public void                         reap()
    {
        final World_Integer_WeakReference   previous = Gem.integer_cache.remove(this);

        if (previous != this) {
            RUNTIME("failed to remove {}", this);
        }
    }
}
