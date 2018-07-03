//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.lang.RuntimeException;
import java.lang.Thread;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.ParseFormat;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Support.OutputFunctions;


public class    Zone
    extends     Gem_Object<Inspection>
//  extends     Object
    implements  Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create_with_portrait("Gem.Core.Zone");


    //
    //  Static members
    //
    private static Thread               first_thread = null;
    private static Zone                 first_zone   = null;


    //
    //  Members
    //
    private static Thread               lane_thread;
    private ParseFormat                 parse_format;


    //
    //  Constructor & Factory
    //
    private                             Zone(Thread lane_thread)
    {
        this.lane_thread  = lane_thread;
        this.parse_format = null;
    }


    public static Zone                  create(Thread lane_thread)
    {
        return new Zone(lane_thread);
    }


    //
    //  Interface Inspectable
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }


    //
    //  Public (parse_format)
    //
    //  NOTE:
    //      Due to possible nested called in a single thread, we might need multiple copies of the 'parse_format'.
    //
    //      The `store_parse_format` routine *ONLY* saves the last version of `pares_format`; any previous
    //      version is discarded, as we only bother to "cache" a single value per thread.
    //
    public ParseFormat                  pop__parse_format__OR__null()
    {
        ParseFormat                     parse_format = this.parse_format;

        this.parse_format = null;

        return parse_format;
    }


    public void                         store_parse_format(ParseFormat parse_format)
    {
        this.parse_format = parse_format;                       //  Overwrite any previously saved copy of parse_format
    }


    //
    //  Public
    //
    public static Zone                  current_zone()
    {
        Thread                          thread = Thread.currentThread();

        if (Zone.first_thread == thread) {
            return Zone.first_zone;
        }

        if (Zone.first_thread != null) {
            //
            //  NOTE:
            //
            //      throw `RuntimeException` directly here, to avoid recursive calls
            //
            //      (since calling `RAISE_runtime_exception` might internally call this routine, leading to recursive calls)
            //
            throw new RuntimeException("Zone.current_zone: only single threaded currently supported");
        }

        Zone                    first_zone = Zone.create(thread);

        Zone.first_thread = thread;
        Zone.first_zone   = first_zone;

        return first_zone;
    }


    public void                         line()
    {
        OutputFunctions.line(this);
    }


    public void                         line(String s)
    {
        OutputFunctions.line(this, s);
    }


    public void                         line(String format, Object first_argument, Object ... other_arguments)
    {
        OutputFunctions.line(this, format, first_argument, other_arguments);
    }
}
