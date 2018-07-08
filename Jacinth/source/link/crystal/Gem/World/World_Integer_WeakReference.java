//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.World;


import java.lang.ref.WeakReference;
import link.crystal.Gem.Core.Gem;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.WeakReferenceable;
import link.crystal.Gem.Support.Gem_ReferenceQueue;
import link.crystal.Gem.Support.Gem_WeakReference;
import link.crystal.Gem.World.Inspection;
import link.crystal.Gem.World.World_Integer;


public class    World_Integer_WeakReference
    extends     Gem_WeakReference<Inspection, World_Integer>
//  extends     WeakReference                <World_Integer>
//  extends     Reference                    <World_Integer>
//  extends     Object
    implements  Inspectable<Inspection>//,                              //  Via Gem_WeakReference<?, ?>
{
    private static final Inspection     inspection = Inspection.create("World_Integer_WeakReference");


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


    public static World_Integer_WeakReference   create(World_Integer client)
    {
        final Gem_ReferenceQueue        reference_queue = Gem.conjure__Gem_ReferenceQueue();
        final int                       value           = client.value;

        return new World_Integer_WeakReference(client, reference_queue, value);
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
    //  Interface WeakReference
    //
    public void                         reap()
    {
        line("REAP: {}", this);
    }
}
