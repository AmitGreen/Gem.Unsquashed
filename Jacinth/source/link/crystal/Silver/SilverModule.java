//   Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Silver;


import java.lang.Object;


public class    SilverModule
    extends     Object
{
    //
    //  Public Static members
    //
    public static boolean               startup = true;


    //
    //  Public
    //
    public static void                  initialize()
    {
        SilverModule.startup = false;
        
        System.out.println("SilverModule.initialize");
    }
}
