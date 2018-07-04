//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Zone;
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
    public static ArgumentSegmentFormatter  conjure(Zone z, int argument_index)
    {
        ArgumentSegmentFormatter[]      segment_many = Storehouse_ArgumentSegmentFormatter.segment_many;

        int                             segment_total = segment_many.length;

        if ( ! (0 <= argument_index && argument_index < segment_total)) {
            z.RUNTIME("`argument_index`<{1}> must be between 0 and {2}", argument_index, segment_total + 1);
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


    public static void                  dump(Zone z)
    {
        ArgumentSegmentFormatter[]      segment_many = Storehouse_ArgumentSegmentFormatter.segment_many;

        int                             segment_total = segment_many.length;

        z.line("Dump of Storehouse_ArgumentSegmentFormatter");
        z.line("  size:  " + Integer.toString(segment_total));

        for (int                        i = 0; i < segment_total; i ++) {
            ArgumentSegmentFormatter    argument_formatter = segment_many[i];

            if (argument_formatter == null) {
                continue;
            }

            z.line("  " + Integer.toString(i) + ": " + argument_formatter.portray(z));
        }

        z.line("End of dump of Storehouse_ArgumentSegmentFormatter");
    }
}
