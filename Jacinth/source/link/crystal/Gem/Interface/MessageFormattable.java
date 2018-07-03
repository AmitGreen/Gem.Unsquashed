//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Interface;


import java.lang.Object;
import java.lang.String;
import link.crystal.Gem.Core.Zone;


public interface   MessageFormattable
{
    String                              arrange(Zone z, Object first_argument, Object ... other_arguments);
    void                                line   (Zone z, Object first_argument, Object ... other_arguments);
    String                              portray(Zone z);
}
