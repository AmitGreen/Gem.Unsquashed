//   Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Silver;


import java.lang.Object;


public class    Proxy<PROXY extends Proxy, CLIENT extends Object> 
{
    //
    //  Members
    //
    protected final CLIENT              client;


    //
    //  Constructor & Factory
    //
    protected                           Proxy(CLIENT client)
    {
        this.client = client;
    }
}
