//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.RuntimeException;
import java.lang.String;
import link.crystal.Gem.Core.GemObject;
import link.crystal.Gem.Format.ArgumentFormatter;


public abstract class   PermenantArgumentFormatter
    extends             GemObject//<Inspection>
//  extends     Object
{
    //
    //  Private static
    //
    private static final ArgumentFormatter[]    many = new ArgumentFormatter[100];


    //
    //  Public
    //
    public static ArgumentFormatter     conjure(int argument_index)
    {
        ArgumentFormatter[]             many  = PermenantArgumentFormatter.many;
        int                             total = many.length;

        if ( ! (0 <= argument_index && argument_index < total)) {
            throw new RuntimeException(
                    (
                          "PermenantArgumentFormatter.conjure: `argument_index` must be between 0 and "
                        + Integer.toString(total + 1)
                        + " (actual value: "
                        + Integer.toString(argument_index)
                        + ")"
                    )
                );
        }

        ArgumentFormatter               previous = many[argument_index];

        if (previous != null) {
            return previous;
        }

        ArgumentFormatter               r = ArgumentFormatter.create__ALLY__PermenantArgumentFormatter(argument_index);

        many[argument_index] = r;

        return r;
    }


    public static void                  dump()
    {
        ArgumentFormatter[]             many  = PermenantArgumentFormatter.many;
        int                             total = many.length;

        GemObject.line("Dump of PermenantArgumentFormatter");
        GemObject.line("  size:  " + Integer.toString(total));

        for (int                        i = 0; i < total; i ++) {
            ArgumentFormatter           argument_formatter = many[i];

            if (argument_formatter == null) {
                continue;
            }

            GemObject.line("  " + Integer.toString(i) + ": " + argument_formatter.portray());
        }

        GemObject.line("End of dump of PermenantArgumentFormatter");
    }
}
