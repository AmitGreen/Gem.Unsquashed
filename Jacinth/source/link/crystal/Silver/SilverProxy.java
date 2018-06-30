//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Silver;


import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.GemObject;
import link.crystal.Gem.Interface.Inspectable;


public abstract class   SilverProxy<PROXY extends SilverProxy, CLIENT extends Object> 
    extends             GemObject<Inspection>
//  extends             Object
    implements          Inspectable<Inspection>//,                      //  Via GemObject
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
