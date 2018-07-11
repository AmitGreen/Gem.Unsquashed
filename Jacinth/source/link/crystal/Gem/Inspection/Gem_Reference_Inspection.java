//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Inspection;


import java.lang.Comparable;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Format.ArgumentSegmentFormatter;
import link.crystal.Gem.Interface.Gem_Comparable;
import link.crystal.Gem.Interface.Inspectable;
import link.crystal.Gem.Inspection.Comparable_Inspection;
import link.crystal.Gem.Inspection.World_Inspection;


public final class  Gem_Reference_Inspection
    extends         Comparable_Inspection
//  extends         Inspection
//  extends         Gem_Object    <World_Inspection>
//  extends         Object
    implements      Gem_Comparable<World_Inspection>,
                    Comparable<Gem_Comparable<? extends Comparable_Inspection>>,    //  Via Gem_Comparable
                    Inspectable   <World_Inspection>//,                             //  Via Gem_Object
{
    private static final World_Inspection   inspection = World_Inspection.create("Gem_Reference_Inspection", 14);


    //
    //  Members
    //
    public final boolean                is_enduring_reference;
    public final boolean                is_weak_reference;


    //
    //  Constructor & Factory
    //
    private                             Gem_Reference_Inspection(
            final String                        simple_class_name,
            final int                           class_order,
        /*  final boolean                       is_world_inspection = false,  */
            final boolean                       is_enduring_reference,
            final boolean                       is_weak_reference//,
        )
    {
        super(simple_class_name, class_order, false);

        this.is_enduring_reference = is_enduring_reference;
        this.is_weak_reference     = is_weak_reference;
    }


    public static final Gem_Reference_Inspection    create(
            final String                        simple_class_name,
            final int                           class_order,
        /*  final boolean                       is_world_inspection = false,  */
            final boolean                       is_enduring_reference,
            final boolean                       is_weak_reference//,
        )
    {
        assert fact ((is_enduring_reference ? 1 : 0) + (is_weak_reference ? 1 : 0) == 1,
                     "one & exactly one of is_{enduring,weak}_reference must be set");

        final Zone                      z = Zone.current_zone();

        final String                    interned__simple_class_name = z.intern_permenant_string(simple_class_name);

        return new Gem_Reference_Inspection(
                   interned__simple_class_name,
                   class_order,
               /*  is_world_inspection = false,  */
                   is_enduring_reference,
                   is_weak_reference//,
               );
    }


    //
    //  Interface Gem_Comparable (and java.lang.Comparable)
    //
    //<inherited public int         compareTo(Gem_Comparable<? extends Comparable_Inspection> that);>


    //
    //  Interface Inspectable
    //
    public final World_Inspection       inspect()
    {
        return /*static*/ this.inspection;
    }


    public final void                   portray(Gem_StringBuilder builder)
    {
        this.portray_prefix(builder);

        if (this.is_enduring_reference) {
            builder.append("; is_enduring_reference");
        }

        if (this.is_weak_reference) {
            builder.append("; is_weak_reference");
        }

        builder.append(">");
    }
}
