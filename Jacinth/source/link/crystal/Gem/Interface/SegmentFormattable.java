//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Interface;


import java.lang.String;
import link.crystal.Gem.Core.Zone;


public interface   SegmentFormattable
{
    String                              portray    (Zone z);
    String                              select_1   (Zone z, String a);
    String                              select_2   (Zone z, String a, String b);
    String                              select_3   (Zone z, String a, String b, String c);
    String                              select_4   (Zone z, String a, String b, String c, String d);
    String                              select_5   (Zone z, String a, String b, String c, String d, String e);
    String                              select_many(Zone z, String[] arguments);
}
