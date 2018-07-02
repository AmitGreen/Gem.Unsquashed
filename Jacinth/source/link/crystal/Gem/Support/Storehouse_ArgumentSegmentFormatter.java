//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.RuntimeException;
import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Format.ArgumentSegmentFormatter;


public abstract class   Storehouse_ArgumentSegmentFormatter
    extends             Gem_Object//<Inspection>
//  extends     Object
{
    //
    //  Private static
    //
    private static final ArgumentSegmentFormatter[]     segment_many = new ArgumentSegmentFormatter[100];


    //
    //  Public
    //
    public static ArgumentSegmentFormatter  conjure(int argument_index)
    {
        ArgumentSegmentFormatter[]      segment_many = Storehouse_ArgumentSegmentFormatter.segment_many;

        int                             segment_total = segment_many.length;

        if ( ! (0 <= argument_index && argument_index < segment_total)) {
            throw new RuntimeException(
                    (
                          "Storehouse_ArgumentSegmentFormatter.conjure: `argument_index` must be between 0 and "
                        + Integer.toString(segment_total + 1)
                        + " (actual value: "
                        + Integer.toString(argument_index)
                        + ")"
                    )
                );
        }

        ArgumentSegmentFormatter        previous = segment_many[argument_index];

        if (previous != null) {
            return previous;
        }

        ArgumentSegmentFormatter        r = ArgumentSegmentFormatter.create__ALLY__Storehouse_ArgumentSegmentFormatter(
                argument_index//,
            );

        segment_many[argument_index] = r;

        return r;
    }


    public static void                  dump()
    {
        ArgumentSegmentFormatter[]      segment_many = Storehouse_ArgumentSegmentFormatter.segment_many;

        int                             segment_total = segment_many.length;

        Gem_Object.line("Dump of Storehouse_ArgumentSegmentFormatter");
        Gem_Object.line("  size:  " + Integer.toString(segment_total));

        for (int                        i = 0; i < segment_total; i ++) {
            ArgumentSegmentFormatter    argument_formatter = segment_many[i];

            if (argument_formatter == null) {
                continue;
            }

            Gem_Object.line("  " + Integer.toString(i) + ": " + argument_formatter.portray());
        }

        Gem_Object.line("End of dump of Storehouse_ArgumentSegmentFormatter");
    }
}
