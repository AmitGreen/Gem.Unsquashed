//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Silver;


import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Interface.Inspectable;


public abstract class   SilverProxy<PROXY extends SilverProxy, CLIENT extends Object> 
    extends             Gem_Object<Inspection>
//  extends             Object
    implements          Inspectable<Inspection>//,                      //  Via Gem_Object
{
    //
    //  Members
    //
    protected final CLIENT              client;


    //
    //  Constructor
    //
    protected                           SilverProxy(CLIENT client)
    {
        this.client = client;
    }


    //
    //  Interface Inspectable
    //
    public abstract Inspection          inspect();
}
