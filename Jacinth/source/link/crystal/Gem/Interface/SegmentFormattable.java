//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Interface;


import java.lang.Object;
import java.lang.String;
import java.lang.StringBuilder;


public interface   SegmentFormattable
{
    void                                build(StringBuilder builder, String[] arguments);
    String                              portray();
}
