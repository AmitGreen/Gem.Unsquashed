//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.SegmentFormattable;
import link.crystal.Gem.Support.PortrayFunctions;


public class    ArgumentSegmentFormatter
    extends     Gem_Object<Inspection>
//  extends     Object
    implements  SegmentFormattable,
                Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create("Gem.Format.ArgumentSegmentFormatter");


    //
    //  Members
    //
    private int                         argument_index;


    //
    //  Constructor & Factory
    //
    private                             ArgumentSegmentFormatter(int argument_index)
    {
        this.argument_index = argument_index;
    }


    static public ArgumentSegmentFormatter  create__ALLY__Storehouse_ArgumentSegmentFormatter(int argument_index)
    {
        return new ArgumentSegmentFormatter(argument_index);
    }


    //
    //  Interface Inspectable
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }


    //
    //  Interface SegmentFormattable
    //
    public String                       select_2(String a, String b)
    {
        int                             argument_index = this.argument_index;

        if (argument_index == 0) {
            return a;
        }

        if (argument_index == 1) {
            return b;
        }

        raise_runtime_exception("ArgumentSegmentFormatter.select_2: argument_index is {0} (expected 0 or 1)",
                                argument_index);

        return null;
    }


    public String                       select_3(String a, String b, String c)
    {
        int                             argument_index = this.argument_index;

        if (argument_index == 0) {
            return a;
        }

        if (argument_index == 1) {
            return b;
        }

        if (argument_index == 2) {
            return c;
        }

        raise_runtime_exception("ArgumentSegmentFormatter.select_3: argument_index is {0} (expected 0, 1, or 2)",
                                argument_index);

        return null;
    }


    public String                       select_4(String a, String b, String c, String d)
    {
        int                             argument_index = this.argument_index;

        if (argument_index == 0) {
            return a;
        }

        if (argument_index == 1) {
            return b;
        }

        if (argument_index == 2) {
            return c;
        }

        if (argument_index == 3) {
            return d;
        }

        raise_runtime_exception("{0}: argument_index is {1} (expected number between 0 and 3)",
                                "ArgumentSegmentFormatter.select_4",
                                argument_index);

        return null;
    }


    public String                       select_5(String a, String b, String c, String d, String e)
    {
        int                             argument_index = this.argument_index;

        if (argument_index == 0) {
            return a;
        }

        if (argument_index == 1) {
            return b;
        }

        if (argument_index == 2) {
            return c;
        }

        if (argument_index == 3) {
            return d;
        }

        if (argument_index == 4) {
            return e;
        }

        raise_runtime_exception("{0}: argument_index is {1} (expected number between 0 and 4)",
                                "ArgumentSegmentFormatter.select_4",
                                argument_index);

        return null;
    }


    public String                       select_many(String[] arguments)
    {
        return arguments[this.argument_index];
    }


    public String                       portray()
    {
        return "<ArgumentSegmentFormatter " + Integer.toString(this.argument_index) + ">";
    }
}
