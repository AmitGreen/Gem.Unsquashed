//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Silver;


import link.crystal.Gem.Inspection;
import link.crystal.Gem.GemObject;


public abstract class   SilverProxy<PROXY extends SilverProxy, CLIENT extends Object> 
    extends             GemObject
//  extends             Object
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
    //  Abstract GemObject
    //
    public abstract Inspection          inspect();
}
