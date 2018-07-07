//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Format;


import java.lang.String;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Inspection;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Format.ArgumentSegmentFormatter;
import link.crystal.Gem.Format.ArgumentSegmentFormatter_Inspection;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Interface.MessageFormattable;
import link.crystal.Gem.Interface.SegmentFormattable;
import link.crystal.Gem.Support.Storehouse_StringSegmentFormatter;


public class    StringSegmentFormatter
    extends     ArgumentSegmentFormatter<StringSegmentFormatter_Inspection>
//  extends     MessageFormatter_Base   <StringSegmentFormatter_Inspection>
//  extends     Gem_Object              <StringSegmentFormatter_Inspection>
//  extends     Object
    implements  MessageFormattable,
                SegmentFormattable      <StringSegmentFormatter_Inspection>,
                Inspectable             <StringSegmentFormatter_Inspection>//,  //  Via Gem_Object
{
    public static final StringSegmentFormatter_Inspection   inspection = (
            StringSegmentFormatter_Inspection.create("StringSegmentFormatter")
        );


    //
    //  Constructor & Factory
    //
    private                             StringSegmentFormatter(int argument_index)
    {
        super(argument_index);
    }


    static public StringSegmentFormatter    conjure__ALLY__StringSegmentFormatter_Inspection(
            Zone                                z,
            int                                 argument_index//,
        )
    {
        final Storehouse_StringSegmentFormatter     cache = Storehouse_StringSegmentFormatter.singleton;

        final StringSegmentFormatter        previous = cache.lookup(argument_index);

        if (previous != null) {
            return previous;
        }

        final StringSegmentFormatter        r = new StringSegmentFormatter(argument_index);

        cache.insert(z, argument_index, r);

        return r;
    }


    //
    //  Interface Inspectable
    //
    public StringSegmentFormatter_Inspection    inspect()
    {
        return /*static*/ this.inspection;
    }


    //
    //  Interface MessageFormattable
    //
    @Override
    public void                         arrange(Gem_StringBuilder builder, int depth, Object v)
    {
        builder.append(v.toString());
    }


    //
    //  Interface SegmentFormattable
    //
    public void                         choose(Gem_StringBuilder builder, int depth)
    {
        INVALID_ROUTINE();
    }

    public void                         choose(Gem_StringBuilder builder, int depth, Object v)
    {
        final int                       argument_index = this.argument_index;

        if (argument_index == 0) {
            builder.append(v.toString());
            return;
        }

        RUNTIME("argument_index is {} (expected 0)", argument_index);
    }


    public void                         choose(Gem_StringBuilder builder, int depth, Object v, Object w)
    {
        final int                       argument_index = this.argument_index;

        if (argument_index == 0) {
            builder.append(v.toString());
            return;
        }

        if (argument_index == 1) {
            builder.append(w.toString());
            return;
        }

        RUNTIME("argument_index is {} (expected 0 or 1)", argument_index);
    }


    public void                         choose(Gem_StringBuilder builder, int depth, Object v, Object w, Object x)
    {
        final int                       argument_index = this.argument_index;

        if (argument_index == 0) {
            builder.append(v.toString());
            return;
        }

        if (argument_index == 1) {
            builder.append(w.toString());
            return;
        }

        if (argument_index == 2) {
            builder.append(x.toString());
            return;
        }

        RUNTIME("argument_index is {} (expected 0, 1, or 2)", argument_index);
    }


    public void                         choose(Gem_StringBuilder builder, int depth, Object v, Object w, Object x, Object y)
    {
        final int                       argument_index = this.argument_index;

        if (argument_index == 0) {
            builder.append(v.toString());
            return;
        }

        if (argument_index == 1) {
            builder.append(w.toString());
            return;
        }

        if (argument_index == 2) {
            builder.append(x.toString());
            return;
        }

        if (argument_index == 3) {
            builder.append(y.toString());
            return;
        }

        RUNTIME("argument_index is {} (expected number between 0 and 3)", argument_index);
    }


    public void                         choose(
            Gem_StringBuilder                   builder,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5//,
        )
    {
        final int                       argument_index = this.argument_index;

        if (argument_index == 0) {
            builder.append(v.toString());
            return;
        }

        if (argument_index == 1) {
            builder.append(w.toString());
            return;
        }

        if (argument_index == 2) {
            builder.append(x.toString());
            return;
        }

        if (argument_index == 3) {
            builder.append(y4.toString());
            return;
        }

        if (argument_index == 4) {
            builder.append(y5.toString());
            return;
        }

        RUNTIME("argument_index is {} (expected number between 0 and 4)", argument_index);
    }


    public void                         choose(
            Gem_StringBuilder                   builder,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5,
            Object                              y6//,
        )
    {
        final int                       argument_index = this.argument_index;

        if (argument_index == 0) {
            builder.append(v.toString());
            return;
        }

        if (argument_index == 1) {
            builder.append(w.toString());
            return;
        }

        if (argument_index == 2) {
            builder.append(x.toString());
            return;
        }

        if (argument_index == 3) {
            builder.append(y4.toString());
            return;
        }

        if (argument_index == 4) {
            builder.append(y5.toString());
            return;
        }

        if (argument_index == 5) {
            builder.append(y6.toString());
            return;
        }

        RUNTIME("argument_index is {} (expected number between 0 and 5)", argument_index);
    }


    public void                         choose(
            Gem_StringBuilder                   builder,
            int                                 depth,
            Object                              v,
            Object                              w,
            Object                              x,
            Object                              y4,
            Object                              y5,
            Object                              y6,
            Object                              y7,
            Object ...                          other_arguments//,
        )
    {
        final int                       argument_index = this.argument_index;

        if (argument_index == 0) {
            builder.append(v.toString());
            return;
        }

        if (argument_index == 1) {
            builder.append(w.toString());
            return;
        }

        if (argument_index == 2) {
            builder.append(x.toString());
            return;
        }

        if (argument_index == 3) {
            builder.append(y4.toString());
            return;
        }

        if (argument_index == 4) {
            builder.append(y5.toString());
            return;
        }

        if (argument_index == 5) {
            builder.append(y6.toString());
            return;
        }

        if (argument_index == 6) {
            builder.append(y7.toString());
            return;
        }

        builder.append(other_arguments[argument_index - 7].toString());
    }
}


class           StringSegmentFormatter_Inspection
    extends     ArgumentSegmentFormatter_Inspection<StringSegmentFormatter>
//  extends     Inspection
//  extends     Gem_Object<Inspection>
//  extends     Object
    implements  Inspectable<Inspection>//,                              //  Via Gem_Object
{
    private static final Inspection     inspection = Inspection.create("StringSegmentFormatter_Inspection");


    //
    //  Constructor & Factory
    //
    protected                           StringSegmentFormatter_Inspection(String simple_class_name)
    {
        super(simple_class_name);
    }


    public static StringSegmentFormatter_Inspection     create(String simple_class_name)
    {
        final Zone                      z = Zone.current_zone();

        final String                    interned__simple_class_name = z.intern_permenant_string(simple_class_name);

        return new StringSegmentFormatter_Inspection(interned__simple_class_name);
    }


    //
    //  Abstract ArgumentSegmentFormatter_Inspection
    //
    public StringSegmentFormatter   conjure_argument_segment(Zone z, int argument_index)
    {
        return StringSegmentFormatter.conjure__ALLY__StringSegmentFormatter_Inspection(z, argument_index);
    }


    //
    //  Interface Inspectable
    //
    public Inspection                   inspect()
    {
        return /*static*/ this.inspection;
    }
}
