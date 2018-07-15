//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Inspection.Inspection;
import link.crystal.Gem.Interface.Inspectable;


public abstract class   PortrayString
    extends             Gem_Object <Inspection>
    implements          Inspectable<Inspection>//,
{
    //
    //  Static members
    //
    public static final PortrayString_Normal   normal_apostrophe = (
            PortrayString_Normal.create__ALLY__PortrayString('\'', "'")
        );


    //
    //  Abstract <me>
    //
    public abstract String              portray_string(final String s);
    public abstract void                portray_string(final Gem_StringBuilder builder, final String s);
};


final class             PortrayString_Normal
    extends             PortrayString
//  extends             Gem_Object <Inspection>
    implements          Inspectable<Inspection>//,
{
    private static final Inspection     inspection = Inspection.create("PortrayString_Normal");


    //
    //  Members
    //
    private final char                  quote_c;
    private final String                quote_s;


    //
    //  Constructor & Factory
    //
    protected                           PortrayString_Normal(final char quote_c, final String quote_s)
    {
        this.quote_c = quote_c;
        this.quote_s = quote_s;
    }


    //
    //  Constructor & Factory
    //
    public static final PortrayString_Normal    create__ALLY__PortrayString(final char quote_c, final String quote_s)
    {
        return new PortrayString_Normal(quote_c, quote_s);
    }


    //
    //  Interface Inspectable
    //
    @Override
    public final Inspection             inspect()
    {
        return /*static*/ this.inspection;
    }


    //inherited public void             portray(final Gem_StringBuilder builder);


    //
    //  Abstract PortrayString
    //
    public final String                 portray_string(final String s)
    {
        final String                    quote_s = this.quote_s;

        return quote_s + s + quote_s;
    }


    public final void                   portray_string(final Gem_StringBuilder builder, final String s)
    {
        final char                      quote_c = this.quote_c;

        builder.append(quote_c, s, quote_c);
    }
}
