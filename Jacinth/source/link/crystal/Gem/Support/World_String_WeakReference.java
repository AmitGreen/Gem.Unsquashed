//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.ref.WeakReference;
import link.crystal.Gem.Core.Gem;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Interface.Gem_Comparable;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.WeakReferenceable;
import link.crystal.Gem.Support.Gem_ReferenceQueue;
import link.crystal.Gem.Support.Gem_WeakReference;
import link.crystal.Gem.World.Comparable_Inspection;
import link.crystal.Gem.World.Inspection;
import link.crystal.Gem.World.World_String;


public class    World_String_WeakReference
    extends     Gem_WeakReference<Comparable_Inspection, World_String>
//  extends     WeakReference                <World_String>
//  extends     Reference                    <World_String>
//  extends     Object
    implements  Inspectable      <Comparable_Inspection>//,             //  Via Gem_WeakReference<?, ?>
{
    private static final Comparable_Inspection  inspection = (
            Comparable_Inspection.create("World_String_WeakReference", 11)
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
            String                              s,
            int                                 pulp//,
        )
    {
        super(client, reference_queue);

        this.world_name = null;
        this.s          = s;
        this.pulp       = pulp;
    }


    public static World_String_WeakReference    create__ALLY__Gem(
            World_String                        client,
            Gem_ReferenceQueue                  reference_queue//,
        )
    {
        final String                    s    = client.s;
        final int                       pulp = s.hashCode();

        return new World_String_WeakReference(client, reference_queue, s, pulp);
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
    //  Interface Gem_Comparable
    //
    public int                          compareTo(Gem_Comparable that)
    {
        final int                       class_compare = 11 - that.inspect().class_order;

        if (class_compare != 0) {
            return class_compare;
        }

        final World_String_WeakReference    that_2 = (World_String_WeakReference) that;

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
        World_String                    client = this.get();

        if (client == null) {
            builder.append("<World_String_WeakReference exhausted; ", this.s, ">");
            return;
        }

        builder.append("<World_String_WeakReference ");
        builder.portray(client);
        builder.append(">");
    }


    //
    //  Interface WeakReference
    //
    public void                         reap()
    {
        final World_String_WeakReference    previous = Gem.string_cache.remove(this);

        if (previous != this) {
            RUNTIME("failed to remove {}", this);
        }
    }
}
