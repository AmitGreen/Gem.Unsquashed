//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.Comparable;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Interface.Gem_Comparable;
import link.crystal.Gem.Interface.Gem_Reference_Interface;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Inspection.Comparable_Inspection;
import link.crystal.Gem.World.World_String;


public class    World_String_EnduringReference
    extends     Gem_Object             <Comparable_Inspection>
//  extends     Object
    implements  Gem_Reference_Interface<Comparable_Inspection, World_String, Comparable_Inspection>,
                Gem_Comparable         <Comparable_Inspection>,                 //  Via Gem_WeakReferenceable_Interface
                Comparable<Gem_Comparable<? extends Comparable_Inspection>>,    //  Via Gem_Comparable
                Inspectable            <Comparable_Inspection>//,               //  Via Gem_Comparable
{
    private static final Comparable_Inspection  inspection = (
            Comparable_Inspection.create("World_String_EnduringReference", 15)
        );


    //
    //  Members
    //
    public final int                    pulp;
    public final World_String           client;


    //
    //  Constructor
    //
    private                             World_String_EnduringReference(int pulp, World_String client)
    {
        this.pulp   = pulp;
        this.client = client;
    }


    public static World_String_EnduringReference    create__ALLY__Gem(World_String client)
    {
        final int                       pulp = 1478849573 ^ client.hashCode();

        return new World_String_EnduringReference(pulp, client);
    }


    //
    //  Ancestor Object
    //
    //  NOTE:
    //      Do not need to override `.equals` -- as `World_String_EnduringReference` are unique (and thus can use
    //      `Object.equals` which uses identity as the equal test).
    //
    @Override
    public int                          hashCode()
    {
        return this.pulp;
    }


    //
    //  Interface Gem_Comparable (and java.lang.Comparable)
    //
    public int                          compareTo(Gem_Comparable<? extends Comparable_Inspection> that)
    {
        final int                       that__class_order = that.inspect().class_order;

        if (that__class_order == 11) {                                  //  11 = World_String_WeakReference
            final World_String_WeakReference    that_2 = (World_String_WeakReference) that;

            return this.client.s.compareTo(that_2.s);
        }

        final int                       class_compare = 13 - that__class_order;

        if (class_compare != 0) {
            return class_compare;
        }

        final World_String_EnduringReference   that_2 = (World_String_EnduringReference) that;

        return this.client.s.compareTo(that_2.client.s);
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
        builder.append("<World_String_EnduringReference ");
        builder.portray(client);
        builder.append(">");
    }


    //
    //  Interface Gem_Reference_Interface
    //
    @Override
    public World_String                 client_OR_enqueue()
    {
        return this.client;
    }
}
