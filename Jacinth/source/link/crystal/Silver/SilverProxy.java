//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Silver;


import link.crystal.Silver.SilverObject;


public abstract class   SilverProxy<PROXY extends SilverProxy, CLIENT extends Object> 
    extends             SilverObject
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
    //  Abstract SilverObject
    //
    public abstract Inspection          inspect();
}
