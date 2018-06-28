//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Silver;


import java.lang.Object;


public final class  SilverModule
    extends         Object
{
    //
    //  Public Static members
    //
    public static /*:*/ boolean         startup = true;


    //
    //  Public
    //
    public static final void            initialize()
    {
        SilverModule.startup = false;

        System.out.println("SilverModule.initialize");
    }
}
