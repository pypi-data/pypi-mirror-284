"""MeasurementBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import overridable, list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy.utility.units_and_measurements import _1628
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_BASE = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements", "MeasurementBase"
)

if TYPE_CHECKING:
    from mastapy.utility import _1616
    from mastapy.utility.units_and_measurements.measurements import (
        _1630,
        _1631,
        _1632,
        _1633,
        _1634,
        _1635,
        _1636,
        _1637,
        _1638,
        _1639,
        _1640,
        _1641,
        _1642,
        _1643,
        _1644,
        _1645,
        _1646,
        _1647,
        _1648,
        _1649,
        _1650,
        _1651,
        _1652,
        _1653,
        _1654,
        _1655,
        _1656,
        _1657,
        _1658,
        _1659,
        _1660,
        _1661,
        _1662,
        _1663,
        _1664,
        _1665,
        _1666,
        _1667,
        _1668,
        _1669,
        _1670,
        _1671,
        _1672,
        _1673,
        _1674,
        _1675,
        _1676,
        _1677,
        _1678,
        _1679,
        _1680,
        _1681,
        _1682,
        _1683,
        _1684,
        _1685,
        _1686,
        _1687,
        _1688,
        _1689,
        _1690,
        _1691,
        _1692,
        _1693,
        _1694,
        _1695,
        _1696,
        _1697,
        _1698,
        _1699,
        _1700,
        _1701,
        _1702,
        _1703,
        _1704,
        _1705,
        _1706,
        _1707,
        _1708,
        _1709,
        _1710,
        _1711,
        _1712,
        _1713,
        _1714,
        _1715,
        _1716,
        _1717,
        _1718,
        _1719,
        _1720,
        _1721,
        _1722,
        _1723,
        _1724,
        _1725,
        _1726,
        _1727,
        _1728,
        _1729,
        _1730,
        _1731,
        _1732,
        _1733,
        _1734,
        _1735,
        _1736,
        _1737,
        _1738,
        _1739,
        _1740,
        _1741,
        _1742,
        _1743,
        _1744,
        _1745,
        _1746,
        _1747,
        _1748,
        _1749,
        _1750,
        _1751,
        _1752,
        _1753,
        _1754,
        _1755,
        _1756,
    )


__docformat__ = "restructuredtext en"
__all__ = ("MeasurementBase",)


Self = TypeVar("Self", bound="MeasurementBase")


class MeasurementBase(_0.APIBase):
    """MeasurementBase

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MeasurementBase")

    class _Cast_MeasurementBase:
        """Special nested class for casting MeasurementBase to subclasses."""

        def __init__(
            self: "MeasurementBase._Cast_MeasurementBase", parent: "MeasurementBase"
        ):
            self._parent = parent

        @property
        def acceleration(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1630.Acceleration":
            from mastapy.utility.units_and_measurements.measurements import _1630

            return self._parent._cast(_1630.Acceleration)

        @property
        def angle(self: "MeasurementBase._Cast_MeasurementBase") -> "_1631.Angle":
            from mastapy.utility.units_and_measurements.measurements import _1631

            return self._parent._cast(_1631.Angle)

        @property
        def angle_per_unit_temperature(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1632.AnglePerUnitTemperature":
            from mastapy.utility.units_and_measurements.measurements import _1632

            return self._parent._cast(_1632.AnglePerUnitTemperature)

        @property
        def angle_small(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1633.AngleSmall":
            from mastapy.utility.units_and_measurements.measurements import _1633

            return self._parent._cast(_1633.AngleSmall)

        @property
        def angle_very_small(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1634.AngleVerySmall":
            from mastapy.utility.units_and_measurements.measurements import _1634

            return self._parent._cast(_1634.AngleVerySmall)

        @property
        def angular_acceleration(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1635.AngularAcceleration":
            from mastapy.utility.units_and_measurements.measurements import _1635

            return self._parent._cast(_1635.AngularAcceleration)

        @property
        def angular_compliance(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1636.AngularCompliance":
            from mastapy.utility.units_and_measurements.measurements import _1636

            return self._parent._cast(_1636.AngularCompliance)

        @property
        def angular_jerk(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1637.AngularJerk":
            from mastapy.utility.units_and_measurements.measurements import _1637

            return self._parent._cast(_1637.AngularJerk)

        @property
        def angular_stiffness(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1638.AngularStiffness":
            from mastapy.utility.units_and_measurements.measurements import _1638

            return self._parent._cast(_1638.AngularStiffness)

        @property
        def angular_velocity(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1639.AngularVelocity":
            from mastapy.utility.units_and_measurements.measurements import _1639

            return self._parent._cast(_1639.AngularVelocity)

        @property
        def area(self: "MeasurementBase._Cast_MeasurementBase") -> "_1640.Area":
            from mastapy.utility.units_and_measurements.measurements import _1640

            return self._parent._cast(_1640.Area)

        @property
        def area_small(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1641.AreaSmall":
            from mastapy.utility.units_and_measurements.measurements import _1641

            return self._parent._cast(_1641.AreaSmall)

        @property
        def carbon_emission_factor(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1642.CarbonEmissionFactor":
            from mastapy.utility.units_and_measurements.measurements import _1642

            return self._parent._cast(_1642.CarbonEmissionFactor)

        @property
        def current_density(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1643.CurrentDensity":
            from mastapy.utility.units_and_measurements.measurements import _1643

            return self._parent._cast(_1643.CurrentDensity)

        @property
        def current_per_length(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1644.CurrentPerLength":
            from mastapy.utility.units_and_measurements.measurements import _1644

            return self._parent._cast(_1644.CurrentPerLength)

        @property
        def cycles(self: "MeasurementBase._Cast_MeasurementBase") -> "_1645.Cycles":
            from mastapy.utility.units_and_measurements.measurements import _1645

            return self._parent._cast(_1645.Cycles)

        @property
        def damage(self: "MeasurementBase._Cast_MeasurementBase") -> "_1646.Damage":
            from mastapy.utility.units_and_measurements.measurements import _1646

            return self._parent._cast(_1646.Damage)

        @property
        def damage_rate(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1647.DamageRate":
            from mastapy.utility.units_and_measurements.measurements import _1647

            return self._parent._cast(_1647.DamageRate)

        @property
        def data_size(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1648.DataSize":
            from mastapy.utility.units_and_measurements.measurements import _1648

            return self._parent._cast(_1648.DataSize)

        @property
        def decibel(self: "MeasurementBase._Cast_MeasurementBase") -> "_1649.Decibel":
            from mastapy.utility.units_and_measurements.measurements import _1649

            return self._parent._cast(_1649.Decibel)

        @property
        def density(self: "MeasurementBase._Cast_MeasurementBase") -> "_1650.Density":
            from mastapy.utility.units_and_measurements.measurements import _1650

            return self._parent._cast(_1650.Density)

        @property
        def electrical_resistance(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1651.ElectricalResistance":
            from mastapy.utility.units_and_measurements.measurements import _1651

            return self._parent._cast(_1651.ElectricalResistance)

        @property
        def electrical_resistivity(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1652.ElectricalResistivity":
            from mastapy.utility.units_and_measurements.measurements import _1652

            return self._parent._cast(_1652.ElectricalResistivity)

        @property
        def electric_current(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1653.ElectricCurrent":
            from mastapy.utility.units_and_measurements.measurements import _1653

            return self._parent._cast(_1653.ElectricCurrent)

        @property
        def energy(self: "MeasurementBase._Cast_MeasurementBase") -> "_1654.Energy":
            from mastapy.utility.units_and_measurements.measurements import _1654

            return self._parent._cast(_1654.Energy)

        @property
        def energy_per_unit_area(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1655.EnergyPerUnitArea":
            from mastapy.utility.units_and_measurements.measurements import _1655

            return self._parent._cast(_1655.EnergyPerUnitArea)

        @property
        def energy_per_unit_area_small(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1656.EnergyPerUnitAreaSmall":
            from mastapy.utility.units_and_measurements.measurements import _1656

            return self._parent._cast(_1656.EnergyPerUnitAreaSmall)

        @property
        def energy_small(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1657.EnergySmall":
            from mastapy.utility.units_and_measurements.measurements import _1657

            return self._parent._cast(_1657.EnergySmall)

        @property
        def enum(self: "MeasurementBase._Cast_MeasurementBase") -> "_1658.Enum":
            from mastapy.utility.units_and_measurements.measurements import _1658

            return self._parent._cast(_1658.Enum)

        @property
        def flow_rate(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1659.FlowRate":
            from mastapy.utility.units_and_measurements.measurements import _1659

            return self._parent._cast(_1659.FlowRate)

        @property
        def force(self: "MeasurementBase._Cast_MeasurementBase") -> "_1660.Force":
            from mastapy.utility.units_and_measurements.measurements import _1660

            return self._parent._cast(_1660.Force)

        @property
        def force_per_unit_length(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1661.ForcePerUnitLength":
            from mastapy.utility.units_and_measurements.measurements import _1661

            return self._parent._cast(_1661.ForcePerUnitLength)

        @property
        def force_per_unit_pressure(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1662.ForcePerUnitPressure":
            from mastapy.utility.units_and_measurements.measurements import _1662

            return self._parent._cast(_1662.ForcePerUnitPressure)

        @property
        def force_per_unit_temperature(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1663.ForcePerUnitTemperature":
            from mastapy.utility.units_and_measurements.measurements import _1663

            return self._parent._cast(_1663.ForcePerUnitTemperature)

        @property
        def fraction_measurement_base(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1664.FractionMeasurementBase":
            from mastapy.utility.units_and_measurements.measurements import _1664

            return self._parent._cast(_1664.FractionMeasurementBase)

        @property
        def fraction_per_temperature(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1665.FractionPerTemperature":
            from mastapy.utility.units_and_measurements.measurements import _1665

            return self._parent._cast(_1665.FractionPerTemperature)

        @property
        def frequency(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1666.Frequency":
            from mastapy.utility.units_and_measurements.measurements import _1666

            return self._parent._cast(_1666.Frequency)

        @property
        def fuel_consumption_engine(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1667.FuelConsumptionEngine":
            from mastapy.utility.units_and_measurements.measurements import _1667

            return self._parent._cast(_1667.FuelConsumptionEngine)

        @property
        def fuel_efficiency_vehicle(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1668.FuelEfficiencyVehicle":
            from mastapy.utility.units_and_measurements.measurements import _1668

            return self._parent._cast(_1668.FuelEfficiencyVehicle)

        @property
        def gradient(self: "MeasurementBase._Cast_MeasurementBase") -> "_1669.Gradient":
            from mastapy.utility.units_and_measurements.measurements import _1669

            return self._parent._cast(_1669.Gradient)

        @property
        def heat_conductivity(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1670.HeatConductivity":
            from mastapy.utility.units_and_measurements.measurements import _1670

            return self._parent._cast(_1670.HeatConductivity)

        @property
        def heat_transfer(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1671.HeatTransfer":
            from mastapy.utility.units_and_measurements.measurements import _1671

            return self._parent._cast(_1671.HeatTransfer)

        @property
        def heat_transfer_coefficient_for_plastic_gear_tooth(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1672.HeatTransferCoefficientForPlasticGearTooth":
            from mastapy.utility.units_and_measurements.measurements import _1672

            return self._parent._cast(_1672.HeatTransferCoefficientForPlasticGearTooth)

        @property
        def heat_transfer_resistance(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1673.HeatTransferResistance":
            from mastapy.utility.units_and_measurements.measurements import _1673

            return self._parent._cast(_1673.HeatTransferResistance)

        @property
        def impulse(self: "MeasurementBase._Cast_MeasurementBase") -> "_1674.Impulse":
            from mastapy.utility.units_and_measurements.measurements import _1674

            return self._parent._cast(_1674.Impulse)

        @property
        def index(self: "MeasurementBase._Cast_MeasurementBase") -> "_1675.Index":
            from mastapy.utility.units_and_measurements.measurements import _1675

            return self._parent._cast(_1675.Index)

        @property
        def inductance(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1676.Inductance":
            from mastapy.utility.units_and_measurements.measurements import _1676

            return self._parent._cast(_1676.Inductance)

        @property
        def integer(self: "MeasurementBase._Cast_MeasurementBase") -> "_1677.Integer":
            from mastapy.utility.units_and_measurements.measurements import _1677

            return self._parent._cast(_1677.Integer)

        @property
        def inverse_short_length(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1678.InverseShortLength":
            from mastapy.utility.units_and_measurements.measurements import _1678

            return self._parent._cast(_1678.InverseShortLength)

        @property
        def inverse_short_time(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1679.InverseShortTime":
            from mastapy.utility.units_and_measurements.measurements import _1679

            return self._parent._cast(_1679.InverseShortTime)

        @property
        def jerk(self: "MeasurementBase._Cast_MeasurementBase") -> "_1680.Jerk":
            from mastapy.utility.units_and_measurements.measurements import _1680

            return self._parent._cast(_1680.Jerk)

        @property
        def kinematic_viscosity(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1681.KinematicViscosity":
            from mastapy.utility.units_and_measurements.measurements import _1681

            return self._parent._cast(_1681.KinematicViscosity)

        @property
        def length_long(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1682.LengthLong":
            from mastapy.utility.units_and_measurements.measurements import _1682

            return self._parent._cast(_1682.LengthLong)

        @property
        def length_medium(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1683.LengthMedium":
            from mastapy.utility.units_and_measurements.measurements import _1683

            return self._parent._cast(_1683.LengthMedium)

        @property
        def length_per_unit_temperature(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1684.LengthPerUnitTemperature":
            from mastapy.utility.units_and_measurements.measurements import _1684

            return self._parent._cast(_1684.LengthPerUnitTemperature)

        @property
        def length_short(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1685.LengthShort":
            from mastapy.utility.units_and_measurements.measurements import _1685

            return self._parent._cast(_1685.LengthShort)

        @property
        def length_to_the_fourth(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1686.LengthToTheFourth":
            from mastapy.utility.units_and_measurements.measurements import _1686

            return self._parent._cast(_1686.LengthToTheFourth)

        @property
        def length_very_long(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1687.LengthVeryLong":
            from mastapy.utility.units_and_measurements.measurements import _1687

            return self._parent._cast(_1687.LengthVeryLong)

        @property
        def length_very_short(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1688.LengthVeryShort":
            from mastapy.utility.units_and_measurements.measurements import _1688

            return self._parent._cast(_1688.LengthVeryShort)

        @property
        def length_very_short_per_length_short(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1689.LengthVeryShortPerLengthShort":
            from mastapy.utility.units_and_measurements.measurements import _1689

            return self._parent._cast(_1689.LengthVeryShortPerLengthShort)

        @property
        def linear_angular_damping(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1690.LinearAngularDamping":
            from mastapy.utility.units_and_measurements.measurements import _1690

            return self._parent._cast(_1690.LinearAngularDamping)

        @property
        def linear_angular_stiffness_cross_term(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1691.LinearAngularStiffnessCrossTerm":
            from mastapy.utility.units_and_measurements.measurements import _1691

            return self._parent._cast(_1691.LinearAngularStiffnessCrossTerm)

        @property
        def linear_damping(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1692.LinearDamping":
            from mastapy.utility.units_and_measurements.measurements import _1692

            return self._parent._cast(_1692.LinearDamping)

        @property
        def linear_flexibility(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1693.LinearFlexibility":
            from mastapy.utility.units_and_measurements.measurements import _1693

            return self._parent._cast(_1693.LinearFlexibility)

        @property
        def linear_stiffness(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1694.LinearStiffness":
            from mastapy.utility.units_and_measurements.measurements import _1694

            return self._parent._cast(_1694.LinearStiffness)

        @property
        def magnetic_field_strength(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1695.MagneticFieldStrength":
            from mastapy.utility.units_and_measurements.measurements import _1695

            return self._parent._cast(_1695.MagneticFieldStrength)

        @property
        def magnetic_flux(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1696.MagneticFlux":
            from mastapy.utility.units_and_measurements.measurements import _1696

            return self._parent._cast(_1696.MagneticFlux)

        @property
        def magnetic_flux_density(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1697.MagneticFluxDensity":
            from mastapy.utility.units_and_measurements.measurements import _1697

            return self._parent._cast(_1697.MagneticFluxDensity)

        @property
        def magnetic_vector_potential(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1698.MagneticVectorPotential":
            from mastapy.utility.units_and_measurements.measurements import _1698

            return self._parent._cast(_1698.MagneticVectorPotential)

        @property
        def magnetomotive_force(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1699.MagnetomotiveForce":
            from mastapy.utility.units_and_measurements.measurements import _1699

            return self._parent._cast(_1699.MagnetomotiveForce)

        @property
        def mass(self: "MeasurementBase._Cast_MeasurementBase") -> "_1700.Mass":
            from mastapy.utility.units_and_measurements.measurements import _1700

            return self._parent._cast(_1700.Mass)

        @property
        def mass_per_unit_length(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1701.MassPerUnitLength":
            from mastapy.utility.units_and_measurements.measurements import _1701

            return self._parent._cast(_1701.MassPerUnitLength)

        @property
        def mass_per_unit_time(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1702.MassPerUnitTime":
            from mastapy.utility.units_and_measurements.measurements import _1702

            return self._parent._cast(_1702.MassPerUnitTime)

        @property
        def moment_of_inertia(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1703.MomentOfInertia":
            from mastapy.utility.units_and_measurements.measurements import _1703

            return self._parent._cast(_1703.MomentOfInertia)

        @property
        def moment_of_inertia_per_unit_length(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1704.MomentOfInertiaPerUnitLength":
            from mastapy.utility.units_and_measurements.measurements import _1704

            return self._parent._cast(_1704.MomentOfInertiaPerUnitLength)

        @property
        def moment_per_unit_pressure(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1705.MomentPerUnitPressure":
            from mastapy.utility.units_and_measurements.measurements import _1705

            return self._parent._cast(_1705.MomentPerUnitPressure)

        @property
        def number(self: "MeasurementBase._Cast_MeasurementBase") -> "_1706.Number":
            from mastapy.utility.units_and_measurements.measurements import _1706

            return self._parent._cast(_1706.Number)

        @property
        def percentage(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1707.Percentage":
            from mastapy.utility.units_and_measurements.measurements import _1707

            return self._parent._cast(_1707.Percentage)

        @property
        def power(self: "MeasurementBase._Cast_MeasurementBase") -> "_1708.Power":
            from mastapy.utility.units_and_measurements.measurements import _1708

            return self._parent._cast(_1708.Power)

        @property
        def power_per_small_area(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1709.PowerPerSmallArea":
            from mastapy.utility.units_and_measurements.measurements import _1709

            return self._parent._cast(_1709.PowerPerSmallArea)

        @property
        def power_per_unit_time(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1710.PowerPerUnitTime":
            from mastapy.utility.units_and_measurements.measurements import _1710

            return self._parent._cast(_1710.PowerPerUnitTime)

        @property
        def power_small(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1711.PowerSmall":
            from mastapy.utility.units_and_measurements.measurements import _1711

            return self._parent._cast(_1711.PowerSmall)

        @property
        def power_small_per_area(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1712.PowerSmallPerArea":
            from mastapy.utility.units_and_measurements.measurements import _1712

            return self._parent._cast(_1712.PowerSmallPerArea)

        @property
        def power_small_per_mass(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1713.PowerSmallPerMass":
            from mastapy.utility.units_and_measurements.measurements import _1713

            return self._parent._cast(_1713.PowerSmallPerMass)

        @property
        def power_small_per_unit_area_per_unit_time(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1714.PowerSmallPerUnitAreaPerUnitTime":
            from mastapy.utility.units_and_measurements.measurements import _1714

            return self._parent._cast(_1714.PowerSmallPerUnitAreaPerUnitTime)

        @property
        def power_small_per_unit_time(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1715.PowerSmallPerUnitTime":
            from mastapy.utility.units_and_measurements.measurements import _1715

            return self._parent._cast(_1715.PowerSmallPerUnitTime)

        @property
        def power_small_per_volume(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1716.PowerSmallPerVolume":
            from mastapy.utility.units_and_measurements.measurements import _1716

            return self._parent._cast(_1716.PowerSmallPerVolume)

        @property
        def pressure(self: "MeasurementBase._Cast_MeasurementBase") -> "_1717.Pressure":
            from mastapy.utility.units_and_measurements.measurements import _1717

            return self._parent._cast(_1717.Pressure)

        @property
        def pressure_per_unit_time(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1718.PressurePerUnitTime":
            from mastapy.utility.units_and_measurements.measurements import _1718

            return self._parent._cast(_1718.PressurePerUnitTime)

        @property
        def pressure_velocity_product(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1719.PressureVelocityProduct":
            from mastapy.utility.units_and_measurements.measurements import _1719

            return self._parent._cast(_1719.PressureVelocityProduct)

        @property
        def pressure_viscosity_coefficient(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1720.PressureViscosityCoefficient":
            from mastapy.utility.units_and_measurements.measurements import _1720

            return self._parent._cast(_1720.PressureViscosityCoefficient)

        @property
        def price(self: "MeasurementBase._Cast_MeasurementBase") -> "_1721.Price":
            from mastapy.utility.units_and_measurements.measurements import _1721

            return self._parent._cast(_1721.Price)

        @property
        def price_per_unit_mass(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1722.PricePerUnitMass":
            from mastapy.utility.units_and_measurements.measurements import _1722

            return self._parent._cast(_1722.PricePerUnitMass)

        @property
        def quadratic_angular_damping(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1723.QuadraticAngularDamping":
            from mastapy.utility.units_and_measurements.measurements import _1723

            return self._parent._cast(_1723.QuadraticAngularDamping)

        @property
        def quadratic_drag(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1724.QuadraticDrag":
            from mastapy.utility.units_and_measurements.measurements import _1724

            return self._parent._cast(_1724.QuadraticDrag)

        @property
        def rescaled_measurement(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1725.RescaledMeasurement":
            from mastapy.utility.units_and_measurements.measurements import _1725

            return self._parent._cast(_1725.RescaledMeasurement)

        @property
        def rotatum(self: "MeasurementBase._Cast_MeasurementBase") -> "_1726.Rotatum":
            from mastapy.utility.units_and_measurements.measurements import _1726

            return self._parent._cast(_1726.Rotatum)

        @property
        def safety_factor(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1727.SafetyFactor":
            from mastapy.utility.units_and_measurements.measurements import _1727

            return self._parent._cast(_1727.SafetyFactor)

        @property
        def specific_acoustic_impedance(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1728.SpecificAcousticImpedance":
            from mastapy.utility.units_and_measurements.measurements import _1728

            return self._parent._cast(_1728.SpecificAcousticImpedance)

        @property
        def specific_heat(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1729.SpecificHeat":
            from mastapy.utility.units_and_measurements.measurements import _1729

            return self._parent._cast(_1729.SpecificHeat)

        @property
        def square_root_of_unit_force_per_unit_area(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1730.SquareRootOfUnitForcePerUnitArea":
            from mastapy.utility.units_and_measurements.measurements import _1730

            return self._parent._cast(_1730.SquareRootOfUnitForcePerUnitArea)

        @property
        def stiffness_per_unit_face_width(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1731.StiffnessPerUnitFaceWidth":
            from mastapy.utility.units_and_measurements.measurements import _1731

            return self._parent._cast(_1731.StiffnessPerUnitFaceWidth)

        @property
        def stress(self: "MeasurementBase._Cast_MeasurementBase") -> "_1732.Stress":
            from mastapy.utility.units_and_measurements.measurements import _1732

            return self._parent._cast(_1732.Stress)

        @property
        def temperature(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1733.Temperature":
            from mastapy.utility.units_and_measurements.measurements import _1733

            return self._parent._cast(_1733.Temperature)

        @property
        def temperature_difference(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1734.TemperatureDifference":
            from mastapy.utility.units_and_measurements.measurements import _1734

            return self._parent._cast(_1734.TemperatureDifference)

        @property
        def temperature_per_unit_time(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1735.TemperaturePerUnitTime":
            from mastapy.utility.units_and_measurements.measurements import _1735

            return self._parent._cast(_1735.TemperaturePerUnitTime)

        @property
        def text(self: "MeasurementBase._Cast_MeasurementBase") -> "_1736.Text":
            from mastapy.utility.units_and_measurements.measurements import _1736

            return self._parent._cast(_1736.Text)

        @property
        def thermal_contact_coefficient(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1737.ThermalContactCoefficient":
            from mastapy.utility.units_and_measurements.measurements import _1737

            return self._parent._cast(_1737.ThermalContactCoefficient)

        @property
        def thermal_expansion_coefficient(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1738.ThermalExpansionCoefficient":
            from mastapy.utility.units_and_measurements.measurements import _1738

            return self._parent._cast(_1738.ThermalExpansionCoefficient)

        @property
        def thermo_elastic_factor(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1739.ThermoElasticFactor":
            from mastapy.utility.units_and_measurements.measurements import _1739

            return self._parent._cast(_1739.ThermoElasticFactor)

        @property
        def time(self: "MeasurementBase._Cast_MeasurementBase") -> "_1740.Time":
            from mastapy.utility.units_and_measurements.measurements import _1740

            return self._parent._cast(_1740.Time)

        @property
        def time_short(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1741.TimeShort":
            from mastapy.utility.units_and_measurements.measurements import _1741

            return self._parent._cast(_1741.TimeShort)

        @property
        def time_very_short(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1742.TimeVeryShort":
            from mastapy.utility.units_and_measurements.measurements import _1742

            return self._parent._cast(_1742.TimeVeryShort)

        @property
        def torque(self: "MeasurementBase._Cast_MeasurementBase") -> "_1743.Torque":
            from mastapy.utility.units_and_measurements.measurements import _1743

            return self._parent._cast(_1743.Torque)

        @property
        def torque_converter_inverse_k(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1744.TorqueConverterInverseK":
            from mastapy.utility.units_and_measurements.measurements import _1744

            return self._parent._cast(_1744.TorqueConverterInverseK)

        @property
        def torque_converter_k(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1745.TorqueConverterK":
            from mastapy.utility.units_and_measurements.measurements import _1745

            return self._parent._cast(_1745.TorqueConverterK)

        @property
        def torque_per_current(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1746.TorquePerCurrent":
            from mastapy.utility.units_and_measurements.measurements import _1746

            return self._parent._cast(_1746.TorquePerCurrent)

        @property
        def torque_per_square_root_of_power(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1747.TorquePerSquareRootOfPower":
            from mastapy.utility.units_and_measurements.measurements import _1747

            return self._parent._cast(_1747.TorquePerSquareRootOfPower)

        @property
        def torque_per_unit_temperature(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1748.TorquePerUnitTemperature":
            from mastapy.utility.units_and_measurements.measurements import _1748

            return self._parent._cast(_1748.TorquePerUnitTemperature)

        @property
        def velocity(self: "MeasurementBase._Cast_MeasurementBase") -> "_1749.Velocity":
            from mastapy.utility.units_and_measurements.measurements import _1749

            return self._parent._cast(_1749.Velocity)

        @property
        def velocity_small(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1750.VelocitySmall":
            from mastapy.utility.units_and_measurements.measurements import _1750

            return self._parent._cast(_1750.VelocitySmall)

        @property
        def viscosity(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1751.Viscosity":
            from mastapy.utility.units_and_measurements.measurements import _1751

            return self._parent._cast(_1751.Viscosity)

        @property
        def voltage(self: "MeasurementBase._Cast_MeasurementBase") -> "_1752.Voltage":
            from mastapy.utility.units_and_measurements.measurements import _1752

            return self._parent._cast(_1752.Voltage)

        @property
        def voltage_per_angular_velocity(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1753.VoltagePerAngularVelocity":
            from mastapy.utility.units_and_measurements.measurements import _1753

            return self._parent._cast(_1753.VoltagePerAngularVelocity)

        @property
        def volume(self: "MeasurementBase._Cast_MeasurementBase") -> "_1754.Volume":
            from mastapy.utility.units_and_measurements.measurements import _1754

            return self._parent._cast(_1754.Volume)

        @property
        def wear_coefficient(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "_1755.WearCoefficient":
            from mastapy.utility.units_and_measurements.measurements import _1755

            return self._parent._cast(_1755.WearCoefficient)

        @property
        def yank(self: "MeasurementBase._Cast_MeasurementBase") -> "_1756.Yank":
            from mastapy.utility.units_and_measurements.measurements import _1756

            return self._parent._cast(_1756.Yank)

        @property
        def measurement_base(
            self: "MeasurementBase._Cast_MeasurementBase",
        ) -> "MeasurementBase":
            return self._parent

        def __getattr__(self: "MeasurementBase._Cast_MeasurementBase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MeasurementBase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def absolute_tolerance(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.AbsoluteTolerance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @absolute_tolerance.setter
    @enforce_parameter_types
    def absolute_tolerance(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.AbsoluteTolerance = value

    @property
    def default_unit(self: Self) -> "list_with_selected_item.ListWithSelectedItem_Unit":
        """ListWithSelectedItem[mastapy.utility.units_and_measurements.Unit]"""
        temp = self.wrapped.DefaultUnit

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_Unit",
        )(temp)

    @default_unit.setter
    @enforce_parameter_types
    def default_unit(self: Self, value: "_1628.Unit"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_Unit.wrapper_type()
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.DefaultUnit = value

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def percentage_tolerance(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.PercentageTolerance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @percentage_tolerance.setter
    @enforce_parameter_types
    def percentage_tolerance(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.PercentageTolerance = value

    @property
    def rounding_digits(self: Self) -> "int":
        """int"""
        temp = self.wrapped.RoundingDigits

        if temp is None:
            return 0

        return temp

    @rounding_digits.setter
    @enforce_parameter_types
    def rounding_digits(self: Self, value: "int"):
        self.wrapped.RoundingDigits = int(value) if value is not None else 0

    @property
    def rounding_method(self: Self) -> "_1616.RoundingMethods":
        """mastapy.utility.RoundingMethods"""
        temp = self.wrapped.RoundingMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Utility.RoundingMethods")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy.utility._1616", "RoundingMethods")(
            value
        )

    @rounding_method.setter
    @enforce_parameter_types
    def rounding_method(self: Self, value: "_1616.RoundingMethods"):
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.Utility.RoundingMethods")
        self.wrapped.RoundingMethod = value

    @property
    def current_unit(self: Self) -> "_1628.Unit":
        """mastapy.utility.units_and_measurements.Unit

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CurrentUnit

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def available_units(self: Self) -> "List[_1628.Unit]":
        """List[mastapy.utility.units_and_measurements.Unit]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AvailableUnits

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(self: Self) -> "MeasurementBase._Cast_MeasurementBase":
        return self._Cast_MeasurementBase(self)
