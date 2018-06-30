//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.RuntimeException;
import java.lang.String;
import link.crystal.Gem.Core.GemObject;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.PortrayFunctions;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.SegmentFormattable;


public class    SegmentFormatter
    extends     GemObject<Inspection>
//  extends     Object
    implements  SegmentFormattable,
                Inspectable<Inspection>//,                              //  Via GemObject
{
    private static Inspection           inspection = Inspection.create("Gem.Format.SegmentFormatter");


    //
    //  Members
    //
    private int                         argument_index;


    //
    //  Constructor & Factory
    //
    private                             SegmentFormatter(int argument_index)
    {
        this.argument_index = argument_index;
    }


    static public SegmentFormatter      create(int argument_index)
    {
        return new SegmentFormatter(argument_index);
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
    public void                         build(StringBuilder builder, String[] arguments)
    {
        throw new RuntimeException("SegmentFormatter.build: incomplete");
    }


    public String                       portray()
    {
        return "<SegmentFormattable " + Integer.toString(this.argument_index) + ">";
    }
}
