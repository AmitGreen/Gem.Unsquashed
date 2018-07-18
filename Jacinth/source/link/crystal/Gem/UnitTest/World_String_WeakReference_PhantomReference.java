//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.UnitTest;


import java.lang.ref.PhantomReference;
import link.crystal.Gem.Core.Gem;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Inspection.Comparable_Inspection;
import link.crystal.Gem.Inspection.Gem_Reference_Inspection;
import link.crystal.Gem.Interface.Gem_QueueableReference_Interface;
import link.crystal.Gem.Interface.Gem_Reference_Interface;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Support.Gem_ReferenceQueue;
import link.crystal.Gem.Support.Gem_WeakReference;
import link.crystal.Gem.Support.World_String_WeakReference;
import link.crystal.Gem.World.World_String;


public final class  World_String_WeakReference_PhantomReference
    extends         PhantomReference<World_String_WeakReference>
//  extends         Reference       <World_String_WeakReference>
//  extends         Object
    implements      Gem_QueueableReference_Interface<Gem_Reference_Inspection>,
                    Gem_Reference_Interface         <Gem_Reference_Inspection>,    //  Via Gem_QueueableReference_Interface
                    Inspectable                     <Gem_Reference_Inspection>//,
{
    private static final Gem_Reference_Inspection   inspection = Gem_Reference_Inspection.create(
            "World_String_WeakReference_PhantomReference",
            Comparable_Inspection.CLASS_ORDER__NONE,
            "phantom"//,
        );


    //
    //  Members
    //
    public final String                 s;


    //
    //  Constructor
    //
    private                             World_String_WeakReference_PhantomReference(
            final World_String_WeakReference    client,
            final Gem_ReferenceQueue            reference_queue,
            final String                        s//,
        )
    {
        super(client, reference_queue);

        this.s          = s;
    }


    public static final World_String_WeakReference_PhantomReference     create__ALLY__Gem(
            final World_String_WeakReference    client,
            final Gem_ReferenceQueue            reference_queue//,
        )
    {
        final String                    s = client.s;

        return new World_String_WeakReference_PhantomReference(client, reference_queue, s);
    }


    //
    //  Interface Gem_QueueableReference_Interface
    //
    @Override
    public final void                   reap()
    {
        line("=== REAP ===: {}", this);
    }


    //
    //  Interface Gem_Reference_Interface
    //
    //<empty>


    //
    //  Interface Inspectable
    //
    @Override
    public Gem_Reference_Inspection     inspect()
    {
        return /*static*/ this.inspection;
    }


    @Override
    public final void                   portray(final Gem_StringBuilder builder)
    {
        builder.append("<World_String_WeakReference_PhantomReference ");
        builder.java_quote(this.s);
        builder.append(">");
    }


    //
    //  Public (line)
    //
    public static final void            line()
    {
        Gem.line();
    }


    public static final void            line(final String format)
    {
        Gem.line(2, format);
    }


    public static final void            line(final String format, final Object v)
    {
        Gem.line(2, format, v);
    }


    public static final void            line(final String format, final Object v, final Object ... other_arguments)
    {
        Gem.line_1_plus(2, format, v, other_arguments);
    }
}
