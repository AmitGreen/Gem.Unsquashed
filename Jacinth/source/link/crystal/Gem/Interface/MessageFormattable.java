//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Interface;


import java.lang.Object;
import java.lang.String;


public interface   MessageFormattable
{
    String                              arrange(Object first_argument, Object ... other_arguments);
    void                                line   (Object first_argument, Object ... other_arguments);
}
