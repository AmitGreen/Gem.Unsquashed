//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Support;


import java.lang.String;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Format.ArgumentSegmentFormatter;


public class    Storehouse_ArgumentSegmentFormatter
    extends     Gem_Object<Inspection>
//  extends     Object
    implements  Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static Inspection           inspection = Inspection.create("Gem.Format.Storehouse_ArgumentSegmentFormatter");


    //
    //  Static members
    //
    public  static final Storehouse_ArgumentSegmentFormatter    singleton = (
            Storehouse_ArgumentSegmentFormatter.create(100)
        );


    //
    //  Members
    //
    private final Zone                          z;
    private final ArgumentSegmentFormatter[]    segment_many;


    //
    //  Constructor & Factory
    //
    private                             Storehouse_ArgumentSegmentFormatter(
            Zone                                z,
            ArgumentSegmentFormatter[]          segment_many//,
        )
    {
        this.z            = z;
        this.segment_many = segment_many;
    }


    private static Storehouse_ArgumentSegmentFormatter  create(int capacity)
    {
        final Zone                      z = Zone.current_zone();

        final ArgumentSegmentFormatter[]    segment_many = new ArgumentSegmentFormatter[capacity];

        return new Storehouse_ArgumentSegmentFormatter(z, segment_many);
    }


    //
    //  Interface Inspectable
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }


    //
    //  Public
    //
    public void                         insert(int argument_index, ArgumentSegmentFormatter segment)
    {
        final ArgumentSegmentFormatter[]    segment_many = this.segment_many;

        final int                       segment_allocated = segment_many.length;

        if ( ! (0 <= argument_index && argument_index < segment_allocated)) {
            final Zone                  z = this.z;

            z.RUNTIME("`argument_index`<{}> must be between 0 and {}", argument_index, segment_allocated - 1);
        }

        if (segment_many[argument_index] != null) {
            final Zone                  z = this.z;

            z.RUNTIME("`segment_many[{}]` != null", argument_index);
        }

        segment_many[argument_index] = segment;
    }


    public ArgumentSegmentFormatter     lookup(int argument_index)
    {
        final ArgumentSegmentFormatter[]    segment_many = this.segment_many;

        final int                       segment_allocated = segment_many.length;

        if ( ! (0 <= argument_index && argument_index < segment_allocated)) {
            final Zone                  z = this.z;

            z.RUNTIME("`argument_index`<{}> must be between 0 and {}", argument_index, segment_allocated - 1);
        }

        return this.segment_many[argument_index];
    }


    public void                         dump(Zone z)
    {
        ArgumentSegmentFormatter[]      segment_many = this.segment_many;

        final int                       segment_allocated = segment_many.length;

        z.line("Dump of Storehouse_ArgumentSegmentFormatter");
        z.line("  size:  " + Integer.toString(segment_allocated));

        for (int                        i = 0; i < segment_allocated; i ++) {
            ArgumentSegmentFormatter    argument_formatter = segment_many[i];

            if (argument_formatter == null) {
                continue;
            }

            z.line("  " + Integer.toString(i) + ": " + argument_formatter.portray(z));
        }

        z.line("End of dump of Storehouse_ArgumentSegmentFormatter");
    }
}
