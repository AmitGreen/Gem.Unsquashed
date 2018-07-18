//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Support.World_String_WeakReference;
import link.crystal.Gem.Inspection.Inspection;
import link.crystal.Gem.World.World_String;


public final class  World_String_Key
    extends         Gem_Object <Inspection>
//  extends         Object
    implements      Inspectable<Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("World_String_Key");


    //
    //  Members
    //
    private final Zone                  z;
    private /*:*/ int                   pulp;
    public  /*:*/ String                s;


    //
    //  Constructor, Factory, & Recycle
    //
    protected                           World_String_Key(final Zone z)
    {
        this.z = z;
        this.s = null;
    }


    public static final World_String_Key    create__ALLY__Zone(final Zone z)
    {
        return new World_String_Key(z);
    }


    public final void                   recycle(final String s)
    {
        this.pulp = s.hashCode();
        this.s    = s;
    }


    //
    //  Abstract object
    //
    @Override
    public final int                    hashCode()
    {
        return this.pulp;
    }


    @Override
    public final boolean                equals(final Object that)
    {
        if ( ! (that instanceof World_String_WeakReference)) {
            return false;
        }

        World_String_WeakReference      weak_reference = (World_String_WeakReference) that;

        return this.s.equals(weak_reference.s);
    }


    //
    //  Interface Inspectable
    //
    @Override
    public final Inspection             inspect()
    {
        return /*static*/ this.inspection;
    }


    @Override
    public final void                   portray(final Gem_StringBuilder builder)
    {
        builder.append("<World_String_Key ");
        builder.java_quote(this.s);
        builder.append(">");
    }
}
