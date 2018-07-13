//  Copyright (c) 2018 Amit Green.  All rights reserved.


package link.crystal.Gem.Inspection;


import java.lang.Comparable;
import link.crystal.Gem.Core.Gem_StringBuilder;
import link.crystal.Gem.Core.Zone;
import link.crystal.Gem.Format.ArgumentSegmentFormatter;
import link.crystal.Gem.Inspection.Comparable_Inspection;
import link.crystal.Gem.Inspection.World_Inspection;
import link.crystal.Gem.Interface.Gem_Comparable;
import link.crystal.Gem.Interface.Inspectable;


public final class  Gem_Reference_Inspection
    extends         Comparable_Inspection
//  extends         Inspection
//  extends         Gem_Object    <World_Inspection>
//  extends         Object
    implements      Gem_Comparable<World_Inspection>,
                    Comparable<Gem_Comparable<? extends Comparable_Inspection>>,    //  Via Gem_Comparable
                    Inspectable   <World_Inspection>//,
{
    private static final World_Inspection   inspection = World_Inspection.create("Gem_Reference_Inspection");


    //
    //  Members
    //
    public final boolean                is_enduring_reference;
    public final boolean                is_phantom_reference;
    public final boolean                is_weak_reference;


    //
    //  Constructor & Factory
    //
    private                             Gem_Reference_Inspection(
            final String                        simple_class_name,
            final int                           class_order,
        /*  final boolean                       is_world_inspection = false,  */
            final boolean                       is_enduring_reference,
            final boolean                       is_phantom_reference,
            final boolean                       is_weak_reference//,
        )
    {
        super(simple_class_name, class_order, false);

        this.is_enduring_reference = is_enduring_reference;
        this.is_phantom_reference  = is_phantom_reference;
        this.is_weak_reference     = is_weak_reference;
    }


    public static final Gem_Reference_Inspection    create(
            final String                        simple_class_name,
            final int                           class_order,
        /*  final boolean                       is_world_inspection = false,  */
            final String                        reference_type//,
        )
    {
        final boolean                   is_enduring_reference = reference_type.equals("enduring");
        final boolean                   is_phantom_reference  = reference_type.equals("phantom");
        final boolean                   is_weak_reference     = reference_type.equals("weak");

        assert fact (
                (
                        (
                              (is_enduring_reference ? 1 : 0)
                            + (is_phantom_reference  ? 1 : 0)
                            + (is_weak_reference     ? 1 : 0)
                        )
                    == 1
                ),
                "one & exactly one of is_{enduring,phantom,weak}_reference must be set"//,
            );

        final Zone                      z = Zone.current_zone();

        final String                    interned__simple_class_name = z.intern_permenant_string(simple_class_name);

        return new Gem_Reference_Inspection(
                   interned__simple_class_name,
                   class_order,
               /*  is_world_inspection = false,  */
                   is_enduring_reference,
                   is_phantom_reference,
                   is_weak_reference//,
               );
    }


    //
    //  Interface java.lang.Comparable
    //
    //<inherited public int         compareTo(Gem_Comparable<? extends Comparable_Inspection> that);>


    //
    //  Interface Gem_Comparable
    //
    //<empty>


    //
    //  Interface Inspectable
    //
    public final World_Inspection       inspect()
    {
        return /*static*/ this.inspection;
    }


    public final void                   portray(final Gem_StringBuilder builder)
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
