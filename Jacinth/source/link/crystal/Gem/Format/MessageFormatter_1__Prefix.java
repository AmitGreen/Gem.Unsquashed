//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.String;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Format.MessageFormatter_Base;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Inspection.Inspection;


public final class  MessageFormatter_1__Prefix
    extends         MessageFormatter_Base<Inspection>
//  extends         Gem_Object           <Inspection>
//  extends         Object
    implements      MessageFormattable   <Inspection>,
                    Inspectable          <Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("MessageFormatter_1__Prefix");


    //
    //  Members
    //
    private final String                prefix;


    //
    //  Constructor & Factory
    //
    private                             MessageFormatter_1__Prefix(final String prefix)
    {
        this.prefix = prefix;
    }


    public static final MessageFormatter_1__Prefix  create(final Zone z, final String prefix)
    {
        final String                    interned__prefix = z.intern_permenant_string(prefix);

        return new MessageFormatter_1__Prefix(interned__prefix);
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
        builder.append("<MessageFormatter_1__Prefix ");
        builder.quote(this.prefix);
        builder.append(">");
    }


    //
    //  Interface MessageFormattable
    //
    @Override
    public final void                   augment(final Gem_StringBuilder builder, int depth, final Object v)
    {
        builder.append(this.prefix);
        builder.portray(v);
    }
}
