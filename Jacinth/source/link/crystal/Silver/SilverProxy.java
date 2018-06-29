//   Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Silver;


import java.lang.Object;


public class    SilverProxy<PROXY extends SilverProxy, CLIENT extends Object> 
{
    //
    //  Members
    //
    protected final CLIENT              client;


    //
    //  Constructor & Factory
    //
    protected                           SilverProxy(CLIENT client)
    {
        this.client = client;
    }
}
