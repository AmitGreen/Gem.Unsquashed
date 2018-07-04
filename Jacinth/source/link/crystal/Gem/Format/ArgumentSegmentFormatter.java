//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.String;
import link.crystal.Gem.Core.Gem_Object;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.SegmentFormattable;


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
    public void                         select_1(Gem_StringBuilder builder, Object a)
    {
        final int                       argument_index = this.argument_index;

        final Zone                      z = builder.z;

        if (argument_index == 0) {
            builder.append(z.portray(a));
            return;
        }

        z.RAISE_runtime_exception("argument_index is {} (expected 0)", argument_index);
    }


    public void                         select_2(Gem_StringBuilder builder, Object a, Object b)
    {
        final int                       argument_index = this.argument_index;

        final Zone                      z = builder.z;

        if (argument_index == 0) {
            builder.append(z.portray(a));
            return;
        }

        if (argument_index == 1) {
            builder.append(z.portray(b));
            return;
        }

        z.RAISE_runtime_exception("ArgumentSegmentFormatter.s)elect_2: argument_index is {} (expected 0 or 1)",
                                  argument_index);
    }


    public String                       select_2(Zone z, String a, String b)
    {
        final int                       argument_index = this.argument_index;

        if (argument_index == 0) {
            return a;
        }

        if (argument_index == 1) {
            return b;
        }

        z.RAISE_runtime_exception("ArgumentSegmentFormatter.select_2: argument_index is {} (expected 0 or 1)",
                                  argument_index);

        return null;
    }


    public void                         select_3(Gem_StringBuilder builder, Object a, Object b, Object c)
    {
        final int                       argument_index = this.argument_index;

        final Zone                      z = builder.z;

        if (argument_index == 0) {
            builder.append(z.portray(a));
            return;
        }

        if (argument_index == 1) {
            builder.append(z.portray(b));
            return;
        }

        if (argument_index == 2) {
            builder.append(z.portray(c));
            return;
        }

        z.RAISE_runtime_exception("argument_index is {} (expected 0, 1, or 2)", argument_index);
    }


    public void                         select_4(Gem_StringBuilder builder, Object a, Object b, Object c, Object d)
    {
        final int                       argument_index = this.argument_index;

        final Zone                      z = builder.z;

        if (argument_index == 0) {
            builder.append(z.portray(a));
            return;
        }

        if (argument_index == 1) {
            builder.append(z.portray(b));
            return;
        }

        if (argument_index == 2) {
            builder.append(z.portray(c));
            return;
        }

        if (argument_index == 3) {
            builder.append(z.portray(d));
            return;
        }

        z.RAISE_runtime_exception("argument_index is {} (expected number between 0 and 3)", argument_index);
    }


    public String                       select_5(Zone z, String a, String b, String c, String d, String e)
    {
        final int                       argument_index = this.argument_index;

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

        z.RAISE_runtime_exception("argument_index is {} (expected number between 0 and 4)", argument_index);

        return null;
    }


    public String                       select_many(Zone z, String[] arguments)
    {
        return arguments[this.argument_index];
    }


    public String                       portray(Zone z)
    {
        return "<ArgumentSegmentFormatter " + Integer.toString(this.argument_index) + ">";
    }
}
