//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Interface;


import java.lang.String;
import link.crystal.Gem.Core.Zone;


//
//  NOTE:
//      Interface `Interface__Storehouse_String` does *NOT* extend `Inspectable` since it is used for
//      `Temporary_Storehouse_String` (which must *NOT* be `Inspectable` -- to avoid class initialiation loops).
//
public interface    Interface__Storehouse_String
{
    //
    //  Interface <me>
    //
    public void                         dump                   (String name);
    public String                       intern_permenant_string(Zone z, String s);
}
