//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Core;


import java.lang.RuntimeException;
import java.lang.Thread;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Interface.Inspectable;


public class    Gem_Lane
    extends     Gem_Object<Inspection>
//  extends     Object
    implements  Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create_with_portrait("Gem.Gem_Lane");


    //
    //  Static members
    //
    private static Pattern              braces_pattern = Pattern.compile("\\{(0|[1-9][0-9]*)?(\\})?");
    private static Thread               first_thread   = null;
    private static Gem_Lane             first_lane     = null;


    //
    //  Members
    //
    private static Thread               lane_thread;
    private static Matcher              braces_matcher;


    //
    //  Constructor & Factory
    //
    private                             Gem_Lane(Thread lane_thread)
    {
        this.lane_thread    = lane_thread;
        this.braces_matcher = null;
    }


    public static Gem_Lane              create(Thread lane_thread)
    {
        return new Gem_Lane(lane_thread);
    }


    //
    //  Interface Inspectable
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }


    //
    //  Public (braces_matcher)
    //
    //
    //  NOTE:
    //      Due to possible nested called in a single thread, we might need multiple copies of the 'Matcher'.
    //
    //      Hence 'fetch_braces_matcher' will *always* return a "clean" braces_matcher; Either:
    //
    //          1.  A newly created one (first time & when nesting); OR
    //          2.  A previously use one (that is no longer used & been reset)
    //
    //  NOTE:
    //      The `store_braces_matcher` routine *ONLY* saves the last version of `braces_matcher`; any previous
    //      version is discarded, as we only bother to "cache" a single value per thread.
    //
    public Matcher                      pop_or_create__braces_matcher(String s)
    {
        Matcher                         braces_matcher = this.braces_matcher;

        if (braces_matcher != null) {
            braces_matcher.reset(s);

            this.braces_matcher = null;

            return braces_matcher;
        }

        return Gem_Lane.braces_pattern.matcher(s);
    }


    public void                         store_braces_matcher(Matcher braces_matcher)
    {
        this.braces_matcher = braces_matcher;       //  Overwrite any previously saved copy of braces_matcher
    }


    //
    //  Public
    //
    public static Gem_Lane              current_lane()
    {
        Gem_Lane                        first_lane = Gem_Lane.first_lane;

        if (first_lane == null) {
            throw new RuntimeException("Gem_Lane.current_lane: Gem_Lane.initialize not yet called");
        }


        if (Gem_Lane.first_thread != Thread.currentThread()) {
            throw new RuntimeException("Gem_Lane.current_lane: only single threaded currently supported");
        }

        return first_lane;
    }


    public static void                  initialize()
    {
        if (Gem_Lane.first_lane != null) {
            throw new RuntimeException("Gem_Lane.initialize: called more than once");
        }

        Thread                          first_thread = Thread.currentThread();

        Gem_Lane.first_thread = first_thread;
        Gem_Lane.first_lane   = Gem_Lane.create(first_thread);
    }
}
