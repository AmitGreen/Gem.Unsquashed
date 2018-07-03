//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Interface;


import java.lang.String;
import java.lang.StringBuilder;


public interface   SegmentFormattable
{
    String                              portray    ();
    String                              select_2   (String a, String b);
    String                              select_3   (String a, String b, String c);
    String                              select_4   (String a, String b, String c, String d);
    String                              select_5   (String a, String b, String c, String d, String e);
    String                              select_many(String[] arguments);
}
