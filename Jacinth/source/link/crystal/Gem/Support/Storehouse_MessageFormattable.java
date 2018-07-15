//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.String;
import link.crystal.Gem.Core.Gem_StringMap;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Format.ParseFormat;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Inspection.Inspection;


public final class  Storehouse_MessageFormattable
    extends         Gem_StringMap<Inspection,         MessageFormattable<?>>
//  extends         HashMap                  <String, MessageFormattable<?>>
//  extends         AbstractHashMap          <String, MessageFormattable<?>>
//  extends         Object
    implements      Inspectable  <Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("Storehouse_MessageFormattable");


    //
    //  Private static
    //
    private static final int                        initial_capacity = 1009;


    //
    //  Constructor & Factory
    //
    private                             Storehouse_MessageFormattable(final Zone z, final int initial_capacity)
    {
        super(z, initial_capacity);
    }


    public static final Storehouse_MessageFormattable   create__ALLY__Zone(final Zone z)
    {
        return new Storehouse_MessageFormattable(z, Storehouse_MessageFormattable.initial_capacity);
    }


    //
    //  Interface Inspectable
    //
    @Override
    public final Inspection             inspect()
    {
        return /*static*/ this.inspection;
    }
}
