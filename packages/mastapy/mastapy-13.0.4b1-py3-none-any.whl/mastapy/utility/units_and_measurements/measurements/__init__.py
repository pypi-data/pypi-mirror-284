"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1630 import Acceleration
    from ._1631 import Angle
    from ._1632 import AnglePerUnitTemperature
    from ._1633 import AngleSmall
    from ._1634 import AngleVerySmall
    from ._1635 import AngularAcceleration
    from ._1636 import AngularCompliance
    from ._1637 import AngularJerk
    from ._1638 import AngularStiffness
    from ._1639 import AngularVelocity
    from ._1640 import Area
    from ._1641 import AreaSmall
    from ._1642 import CarbonEmissionFactor
    from ._1643 import CurrentDensity
    from ._1644 import CurrentPerLength
    from ._1645 import Cycles
    from ._1646 import Damage
    from ._1647 import DamageRate
    from ._1648 import DataSize
    from ._1649 import Decibel
    from ._1650 import Density
    from ._1651 import ElectricalResistance
    from ._1652 import ElectricalResistivity
    from ._1653 import ElectricCurrent
    from ._1654 import Energy
    from ._1655 import EnergyPerUnitArea
    from ._1656 import EnergyPerUnitAreaSmall
    from ._1657 import EnergySmall
    from ._1658 import Enum
    from ._1659 import FlowRate
    from ._1660 import Force
    from ._1661 import ForcePerUnitLength
    from ._1662 import ForcePerUnitPressure
    from ._1663 import ForcePerUnitTemperature
    from ._1664 import FractionMeasurementBase
    from ._1665 import FractionPerTemperature
    from ._1666 import Frequency
    from ._1667 import FuelConsumptionEngine
    from ._1668 import FuelEfficiencyVehicle
    from ._1669 import Gradient
    from ._1670 import HeatConductivity
    from ._1671 import HeatTransfer
    from ._1672 import HeatTransferCoefficientForPlasticGearTooth
    from ._1673 import HeatTransferResistance
    from ._1674 import Impulse
    from ._1675 import Index
    from ._1676 import Inductance
    from ._1677 import Integer
    from ._1678 import InverseShortLength
    from ._1679 import InverseShortTime
    from ._1680 import Jerk
    from ._1681 import KinematicViscosity
    from ._1682 import LengthLong
    from ._1683 import LengthMedium
    from ._1684 import LengthPerUnitTemperature
    from ._1685 import LengthShort
    from ._1686 import LengthToTheFourth
    from ._1687 import LengthVeryLong
    from ._1688 import LengthVeryShort
    from ._1689 import LengthVeryShortPerLengthShort
    from ._1690 import LinearAngularDamping
    from ._1691 import LinearAngularStiffnessCrossTerm
    from ._1692 import LinearDamping
    from ._1693 import LinearFlexibility
    from ._1694 import LinearStiffness
    from ._1695 import MagneticFieldStrength
    from ._1696 import MagneticFlux
    from ._1697 import MagneticFluxDensity
    from ._1698 import MagneticVectorPotential
    from ._1699 import MagnetomotiveForce
    from ._1700 import Mass
    from ._1701 import MassPerUnitLength
    from ._1702 import MassPerUnitTime
    from ._1703 import MomentOfInertia
    from ._1704 import MomentOfInertiaPerUnitLength
    from ._1705 import MomentPerUnitPressure
    from ._1706 import Number
    from ._1707 import Percentage
    from ._1708 import Power
    from ._1709 import PowerPerSmallArea
    from ._1710 import PowerPerUnitTime
    from ._1711 import PowerSmall
    from ._1712 import PowerSmallPerArea
    from ._1713 import PowerSmallPerMass
    from ._1714 import PowerSmallPerUnitAreaPerUnitTime
    from ._1715 import PowerSmallPerUnitTime
    from ._1716 import PowerSmallPerVolume
    from ._1717 import Pressure
    from ._1718 import PressurePerUnitTime
    from ._1719 import PressureVelocityProduct
    from ._1720 import PressureViscosityCoefficient
    from ._1721 import Price
    from ._1722 import PricePerUnitMass
    from ._1723 import QuadraticAngularDamping
    from ._1724 import QuadraticDrag
    from ._1725 import RescaledMeasurement
    from ._1726 import Rotatum
    from ._1727 import SafetyFactor
    from ._1728 import SpecificAcousticImpedance
    from ._1729 import SpecificHeat
    from ._1730 import SquareRootOfUnitForcePerUnitArea
    from ._1731 import StiffnessPerUnitFaceWidth
    from ._1732 import Stress
    from ._1733 import Temperature
    from ._1734 import TemperatureDifference
    from ._1735 import TemperaturePerUnitTime
    from ._1736 import Text
    from ._1737 import ThermalContactCoefficient
    from ._1738 import ThermalExpansionCoefficient
    from ._1739 import ThermoElasticFactor
    from ._1740 import Time
    from ._1741 import TimeShort
    from ._1742 import TimeVeryShort
    from ._1743 import Torque
    from ._1744 import TorqueConverterInverseK
    from ._1745 import TorqueConverterK
    from ._1746 import TorquePerCurrent
    from ._1747 import TorquePerSquareRootOfPower
    from ._1748 import TorquePerUnitTemperature
    from ._1749 import Velocity
    from ._1750 import VelocitySmall
    from ._1751 import Viscosity
    from ._1752 import Voltage
    from ._1753 import VoltagePerAngularVelocity
    from ._1754 import Volume
    from ._1755 import WearCoefficient
    from ._1756 import Yank
else:
    import_structure = {
        "_1630": ["Acceleration"],
        "_1631": ["Angle"],
        "_1632": ["AnglePerUnitTemperature"],
        "_1633": ["AngleSmall"],
        "_1634": ["AngleVerySmall"],
        "_1635": ["AngularAcceleration"],
        "_1636": ["AngularCompliance"],
        "_1637": ["AngularJerk"],
        "_1638": ["AngularStiffness"],
        "_1639": ["AngularVelocity"],
        "_1640": ["Area"],
        "_1641": ["AreaSmall"],
        "_1642": ["CarbonEmissionFactor"],
        "_1643": ["CurrentDensity"],
        "_1644": ["CurrentPerLength"],
        "_1645": ["Cycles"],
        "_1646": ["Damage"],
        "_1647": ["DamageRate"],
        "_1648": ["DataSize"],
        "_1649": ["Decibel"],
        "_1650": ["Density"],
        "_1651": ["ElectricalResistance"],
        "_1652": ["ElectricalResistivity"],
        "_1653": ["ElectricCurrent"],
        "_1654": ["Energy"],
        "_1655": ["EnergyPerUnitArea"],
        "_1656": ["EnergyPerUnitAreaSmall"],
        "_1657": ["EnergySmall"],
        "_1658": ["Enum"],
        "_1659": ["FlowRate"],
        "_1660": ["Force"],
        "_1661": ["ForcePerUnitLength"],
        "_1662": ["ForcePerUnitPressure"],
        "_1663": ["ForcePerUnitTemperature"],
        "_1664": ["FractionMeasurementBase"],
        "_1665": ["FractionPerTemperature"],
        "_1666": ["Frequency"],
        "_1667": ["FuelConsumptionEngine"],
        "_1668": ["FuelEfficiencyVehicle"],
        "_1669": ["Gradient"],
        "_1670": ["HeatConductivity"],
        "_1671": ["HeatTransfer"],
        "_1672": ["HeatTransferCoefficientForPlasticGearTooth"],
        "_1673": ["HeatTransferResistance"],
        "_1674": ["Impulse"],
        "_1675": ["Index"],
        "_1676": ["Inductance"],
        "_1677": ["Integer"],
        "_1678": ["InverseShortLength"],
        "_1679": ["InverseShortTime"],
        "_1680": ["Jerk"],
        "_1681": ["KinematicViscosity"],
        "_1682": ["LengthLong"],
        "_1683": ["LengthMedium"],
        "_1684": ["LengthPerUnitTemperature"],
        "_1685": ["LengthShort"],
        "_1686": ["LengthToTheFourth"],
        "_1687": ["LengthVeryLong"],
        "_1688": ["LengthVeryShort"],
        "_1689": ["LengthVeryShortPerLengthShort"],
        "_1690": ["LinearAngularDamping"],
        "_1691": ["LinearAngularStiffnessCrossTerm"],
        "_1692": ["LinearDamping"],
        "_1693": ["LinearFlexibility"],
        "_1694": ["LinearStiffness"],
        "_1695": ["MagneticFieldStrength"],
        "_1696": ["MagneticFlux"],
        "_1697": ["MagneticFluxDensity"],
        "_1698": ["MagneticVectorPotential"],
        "_1699": ["MagnetomotiveForce"],
        "_1700": ["Mass"],
        "_1701": ["MassPerUnitLength"],
        "_1702": ["MassPerUnitTime"],
        "_1703": ["MomentOfInertia"],
        "_1704": ["MomentOfInertiaPerUnitLength"],
        "_1705": ["MomentPerUnitPressure"],
        "_1706": ["Number"],
        "_1707": ["Percentage"],
        "_1708": ["Power"],
        "_1709": ["PowerPerSmallArea"],
        "_1710": ["PowerPerUnitTime"],
        "_1711": ["PowerSmall"],
        "_1712": ["PowerSmallPerArea"],
        "_1713": ["PowerSmallPerMass"],
        "_1714": ["PowerSmallPerUnitAreaPerUnitTime"],
        "_1715": ["PowerSmallPerUnitTime"],
        "_1716": ["PowerSmallPerVolume"],
        "_1717": ["Pressure"],
        "_1718": ["PressurePerUnitTime"],
        "_1719": ["PressureVelocityProduct"],
        "_1720": ["PressureViscosityCoefficient"],
        "_1721": ["Price"],
        "_1722": ["PricePerUnitMass"],
        "_1723": ["QuadraticAngularDamping"],
        "_1724": ["QuadraticDrag"],
        "_1725": ["RescaledMeasurement"],
        "_1726": ["Rotatum"],
        "_1727": ["SafetyFactor"],
        "_1728": ["SpecificAcousticImpedance"],
        "_1729": ["SpecificHeat"],
        "_1730": ["SquareRootOfUnitForcePerUnitArea"],
        "_1731": ["StiffnessPerUnitFaceWidth"],
        "_1732": ["Stress"],
        "_1733": ["Temperature"],
        "_1734": ["TemperatureDifference"],
        "_1735": ["TemperaturePerUnitTime"],
        "_1736": ["Text"],
        "_1737": ["ThermalContactCoefficient"],
        "_1738": ["ThermalExpansionCoefficient"],
        "_1739": ["ThermoElasticFactor"],
        "_1740": ["Time"],
        "_1741": ["TimeShort"],
        "_1742": ["TimeVeryShort"],
        "_1743": ["Torque"],
        "_1744": ["TorqueConverterInverseK"],
        "_1745": ["TorqueConverterK"],
        "_1746": ["TorquePerCurrent"],
        "_1747": ["TorquePerSquareRootOfPower"],
        "_1748": ["TorquePerUnitTemperature"],
        "_1749": ["Velocity"],
        "_1750": ["VelocitySmall"],
        "_1751": ["Viscosity"],
        "_1752": ["Voltage"],
        "_1753": ["VoltagePerAngularVelocity"],
        "_1754": ["Volume"],
        "_1755": ["WearCoefficient"],
        "_1756": ["Yank"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Acceleration",
    "Angle",
    "AnglePerUnitTemperature",
    "AngleSmall",
    "AngleVerySmall",
    "AngularAcceleration",
    "AngularCompliance",
    "AngularJerk",
    "AngularStiffness",
    "AngularVelocity",
    "Area",
    "AreaSmall",
    "CarbonEmissionFactor",
    "CurrentDensity",
    "CurrentPerLength",
    "Cycles",
    "Damage",
    "DamageRate",
    "DataSize",
    "Decibel",
    "Density",
    "ElectricalResistance",
    "ElectricalResistivity",
    "ElectricCurrent",
    "Energy",
    "EnergyPerUnitArea",
    "EnergyPerUnitAreaSmall",
    "EnergySmall",
    "Enum",
    "FlowRate",
    "Force",
    "ForcePerUnitLength",
    "ForcePerUnitPressure",
    "ForcePerUnitTemperature",
    "FractionMeasurementBase",
    "FractionPerTemperature",
    "Frequency",
    "FuelConsumptionEngine",
    "FuelEfficiencyVehicle",
    "Gradient",
    "HeatConductivity",
    "HeatTransfer",
    "HeatTransferCoefficientForPlasticGearTooth",
    "HeatTransferResistance",
    "Impulse",
    "Index",
    "Inductance",
    "Integer",
    "InverseShortLength",
    "InverseShortTime",
    "Jerk",
    "KinematicViscosity",
    "LengthLong",
    "LengthMedium",
    "LengthPerUnitTemperature",
    "LengthShort",
    "LengthToTheFourth",
    "LengthVeryLong",
    "LengthVeryShort",
    "LengthVeryShortPerLengthShort",
    "LinearAngularDamping",
    "LinearAngularStiffnessCrossTerm",
    "LinearDamping",
    "LinearFlexibility",
    "LinearStiffness",
    "MagneticFieldStrength",
    "MagneticFlux",
    "MagneticFluxDensity",
    "MagneticVectorPotential",
    "MagnetomotiveForce",
    "Mass",
    "MassPerUnitLength",
    "MassPerUnitTime",
    "MomentOfInertia",
    "MomentOfInertiaPerUnitLength",
    "MomentPerUnitPressure",
    "Number",
    "Percentage",
    "Power",
    "PowerPerSmallArea",
    "PowerPerUnitTime",
    "PowerSmall",
    "PowerSmallPerArea",
    "PowerSmallPerMass",
    "PowerSmallPerUnitAreaPerUnitTime",
    "PowerSmallPerUnitTime",
    "PowerSmallPerVolume",
    "Pressure",
    "PressurePerUnitTime",
    "PressureVelocityProduct",
    "PressureViscosityCoefficient",
    "Price",
    "PricePerUnitMass",
    "QuadraticAngularDamping",
    "QuadraticDrag",
    "RescaledMeasurement",
    "Rotatum",
    "SafetyFactor",
    "SpecificAcousticImpedance",
    "SpecificHeat",
    "SquareRootOfUnitForcePerUnitArea",
    "StiffnessPerUnitFaceWidth",
    "Stress",
    "Temperature",
    "TemperatureDifference",
    "TemperaturePerUnitTime",
    "Text",
    "ThermalContactCoefficient",
    "ThermalExpansionCoefficient",
    "ThermoElasticFactor",
    "Time",
    "TimeShort",
    "TimeVeryShort",
    "Torque",
    "TorqueConverterInverseK",
    "TorqueConverterK",
    "TorquePerCurrent",
    "TorquePerSquareRootOfPower",
    "TorquePerUnitTemperature",
    "Velocity",
    "VelocitySmall",
    "Viscosity",
    "Voltage",
    "VoltagePerAngularVelocity",
    "Volume",
    "WearCoefficient",
    "Yank",
)
