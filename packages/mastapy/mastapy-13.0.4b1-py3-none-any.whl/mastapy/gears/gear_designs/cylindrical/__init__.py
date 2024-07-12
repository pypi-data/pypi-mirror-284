"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1002 import AddendumModificationDistributionRule
    from ._1003 import BacklashSpecification
    from ._1004 import BasicRackProfiles
    from ._1005 import CaseHardeningProperties
    from ._1006 import CreateNewSuitableCutterOption
    from ._1007 import CrossedAxisCylindricalGearPair
    from ._1008 import CrossedAxisCylindricalGearPairLineContact
    from ._1009 import CrossedAxisCylindricalGearPairPointContact
    from ._1010 import Customer102DataSheetChangeLog
    from ._1011 import Customer102DataSheetChangeLogItem
    from ._1012 import Customer102DataSheetNote
    from ._1013 import Customer102DataSheetNotes
    from ._1014 import Customer102DataSheetTolerances
    from ._1015 import Customer102ToleranceDefinition
    from ._1016 import CylindricalGearAbstractRack
    from ._1017 import CylindricalGearAbstractRackFlank
    from ._1018 import CylindricalGearBasicRack
    from ._1019 import CylindricalGearBasicRackFlank
    from ._1020 import CylindricalGearCuttingOptions
    from ._1021 import CylindricalGearDefaults
    from ._1022 import CylindricalGearDesign
    from ._1023 import CylindricalGearDesignConstraint
    from ._1024 import CylindricalGearDesignConstraints
    from ._1025 import CylindricalGearDesignConstraintsDatabase
    from ._1026 import CylindricalGearDesignConstraintSettings
    from ._1027 import CylindricalGearFlankDesign
    from ._1028 import CylindricalGearMeshDesign
    from ._1029 import CylindricalGearMeshFlankDesign
    from ._1030 import CylindricalGearMicroGeometrySettings
    from ._1031 import CylindricalGearMicroGeometrySettingsDatabase
    from ._1032 import CylindricalGearMicroGeometrySettingsItem
    from ._1033 import CylindricalGearPinionTypeCutter
    from ._1034 import CylindricalGearPinionTypeCutterFlank
    from ._1035 import CylindricalGearProfileMeasurement
    from ._1036 import CylindricalGearProfileMeasurementType
    from ._1037 import CylindricalGearProfileModifications
    from ._1038 import CylindricalGearSetDesign
    from ._1039 import CylindricalGearSetFlankDesign
    from ._1040 import CylindricalGearSetMacroGeometryOptimiser
    from ._1041 import CylindricalGearSetManufacturingConfigurationSelection
    from ._1042 import CylindricalGearSetMicroGeometrySettings
    from ._1043 import CylindricalGearSetOptimisationWrapper
    from ._1044 import CylindricalGearTableMGItemDetail
    from ._1045 import CylindricalGearTableWithMGCharts
    from ._1046 import CylindricalGearToothThicknessSpecification
    from ._1047 import CylindricalMeshAngularBacklash
    from ._1048 import CylindricalMeshedGear
    from ._1049 import CylindricalMeshedGearFlank
    from ._1050 import CylindricalMeshLinearBacklashSpecification
    from ._1051 import CylindricalPlanetaryGearSetDesign
    from ._1052 import CylindricalPlanetGearDesign
    from ._1053 import DIN3967AllowanceSeries
    from ._1054 import DIN3967ToleranceSeries
    from ._1055 import DoubleAxisScaleAndRange
    from ._1056 import FinishToothThicknessDesignSpecification
    from ._1057 import GearFitSystems
    from ._1058 import GearManufacturingConfigSetupViewModel
    from ._1059 import GearSetManufacturingConfigurationSetup
    from ._1060 import GeometrySpecificationType
    from ._1061 import HardenedMaterialProperties
    from ._1062 import HardnessProfileCalculationMethod
    from ._1063 import HeatTreatmentType
    from ._1064 import ISO6336Geometry
    from ._1065 import ISO6336GeometryBase
    from ._1066 import ISO6336GeometryForShapedGears
    from ._1067 import ISO6336GeometryManufactured
    from ._1068 import LinearBacklashSpecification
    from ._1069 import LTCALoadCaseModifiableSettings
    from ._1070 import LTCASettings
    from ._1071 import MicroGeometryConvention
    from ._1072 import MicroGeometryProfileConvention
    from ._1073 import Micropitting
    from ._1074 import MullerResidualStressDefinition
    from ._1075 import NamedPlanetAssemblyIndex
    from ._1076 import NamedPlanetSideBandAmplitudeFactor
    from ._1077 import ReadonlyToothThicknessSpecification
    from ._1078 import RelativeMeasurementViewModel
    from ._1079 import RelativeValuesSpecification
    from ._1080 import ResidualStressCalculationMethod
    from ._1081 import RootStressSurfaceChartOption
    from ._1082 import Scuffing
    from ._1083 import ScuffingCoefficientOfFrictionMethods
    from ._1084 import ScuffingTemperatureMethodsAGMA
    from ._1085 import ScuffingTemperatureMethodsISO
    from ._1086 import ShaperEdgeTypes
    from ._1087 import SpurGearLoadSharingCodes
    from ._1088 import StandardRack
    from ._1089 import StandardRackFlank
    from ._1090 import SurfaceRoughness
    from ._1091 import ThicknessType
    from ._1092 import TiffAnalysisSettings
    from ._1093 import TipAlterationCoefficientMethod
    from ._1094 import TolerancedMetalMeasurements
    from ._1095 import TolerancedValueSpecification
    from ._1096 import ToothFlankFractureAnalysisSettings
    from ._1097 import ToothThicknessSpecification
    from ._1098 import ToothThicknessSpecificationBase
    from ._1099 import TypeOfMechanismHousing
    from ._1100 import Usage
else:
    import_structure = {
        "_1002": ["AddendumModificationDistributionRule"],
        "_1003": ["BacklashSpecification"],
        "_1004": ["BasicRackProfiles"],
        "_1005": ["CaseHardeningProperties"],
        "_1006": ["CreateNewSuitableCutterOption"],
        "_1007": ["CrossedAxisCylindricalGearPair"],
        "_1008": ["CrossedAxisCylindricalGearPairLineContact"],
        "_1009": ["CrossedAxisCylindricalGearPairPointContact"],
        "_1010": ["Customer102DataSheetChangeLog"],
        "_1011": ["Customer102DataSheetChangeLogItem"],
        "_1012": ["Customer102DataSheetNote"],
        "_1013": ["Customer102DataSheetNotes"],
        "_1014": ["Customer102DataSheetTolerances"],
        "_1015": ["Customer102ToleranceDefinition"],
        "_1016": ["CylindricalGearAbstractRack"],
        "_1017": ["CylindricalGearAbstractRackFlank"],
        "_1018": ["CylindricalGearBasicRack"],
        "_1019": ["CylindricalGearBasicRackFlank"],
        "_1020": ["CylindricalGearCuttingOptions"],
        "_1021": ["CylindricalGearDefaults"],
        "_1022": ["CylindricalGearDesign"],
        "_1023": ["CylindricalGearDesignConstraint"],
        "_1024": ["CylindricalGearDesignConstraints"],
        "_1025": ["CylindricalGearDesignConstraintsDatabase"],
        "_1026": ["CylindricalGearDesignConstraintSettings"],
        "_1027": ["CylindricalGearFlankDesign"],
        "_1028": ["CylindricalGearMeshDesign"],
        "_1029": ["CylindricalGearMeshFlankDesign"],
        "_1030": ["CylindricalGearMicroGeometrySettings"],
        "_1031": ["CylindricalGearMicroGeometrySettingsDatabase"],
        "_1032": ["CylindricalGearMicroGeometrySettingsItem"],
        "_1033": ["CylindricalGearPinionTypeCutter"],
        "_1034": ["CylindricalGearPinionTypeCutterFlank"],
        "_1035": ["CylindricalGearProfileMeasurement"],
        "_1036": ["CylindricalGearProfileMeasurementType"],
        "_1037": ["CylindricalGearProfileModifications"],
        "_1038": ["CylindricalGearSetDesign"],
        "_1039": ["CylindricalGearSetFlankDesign"],
        "_1040": ["CylindricalGearSetMacroGeometryOptimiser"],
        "_1041": ["CylindricalGearSetManufacturingConfigurationSelection"],
        "_1042": ["CylindricalGearSetMicroGeometrySettings"],
        "_1043": ["CylindricalGearSetOptimisationWrapper"],
        "_1044": ["CylindricalGearTableMGItemDetail"],
        "_1045": ["CylindricalGearTableWithMGCharts"],
        "_1046": ["CylindricalGearToothThicknessSpecification"],
        "_1047": ["CylindricalMeshAngularBacklash"],
        "_1048": ["CylindricalMeshedGear"],
        "_1049": ["CylindricalMeshedGearFlank"],
        "_1050": ["CylindricalMeshLinearBacklashSpecification"],
        "_1051": ["CylindricalPlanetaryGearSetDesign"],
        "_1052": ["CylindricalPlanetGearDesign"],
        "_1053": ["DIN3967AllowanceSeries"],
        "_1054": ["DIN3967ToleranceSeries"],
        "_1055": ["DoubleAxisScaleAndRange"],
        "_1056": ["FinishToothThicknessDesignSpecification"],
        "_1057": ["GearFitSystems"],
        "_1058": ["GearManufacturingConfigSetupViewModel"],
        "_1059": ["GearSetManufacturingConfigurationSetup"],
        "_1060": ["GeometrySpecificationType"],
        "_1061": ["HardenedMaterialProperties"],
        "_1062": ["HardnessProfileCalculationMethod"],
        "_1063": ["HeatTreatmentType"],
        "_1064": ["ISO6336Geometry"],
        "_1065": ["ISO6336GeometryBase"],
        "_1066": ["ISO6336GeometryForShapedGears"],
        "_1067": ["ISO6336GeometryManufactured"],
        "_1068": ["LinearBacklashSpecification"],
        "_1069": ["LTCALoadCaseModifiableSettings"],
        "_1070": ["LTCASettings"],
        "_1071": ["MicroGeometryConvention"],
        "_1072": ["MicroGeometryProfileConvention"],
        "_1073": ["Micropitting"],
        "_1074": ["MullerResidualStressDefinition"],
        "_1075": ["NamedPlanetAssemblyIndex"],
        "_1076": ["NamedPlanetSideBandAmplitudeFactor"],
        "_1077": ["ReadonlyToothThicknessSpecification"],
        "_1078": ["RelativeMeasurementViewModel"],
        "_1079": ["RelativeValuesSpecification"],
        "_1080": ["ResidualStressCalculationMethod"],
        "_1081": ["RootStressSurfaceChartOption"],
        "_1082": ["Scuffing"],
        "_1083": ["ScuffingCoefficientOfFrictionMethods"],
        "_1084": ["ScuffingTemperatureMethodsAGMA"],
        "_1085": ["ScuffingTemperatureMethodsISO"],
        "_1086": ["ShaperEdgeTypes"],
        "_1087": ["SpurGearLoadSharingCodes"],
        "_1088": ["StandardRack"],
        "_1089": ["StandardRackFlank"],
        "_1090": ["SurfaceRoughness"],
        "_1091": ["ThicknessType"],
        "_1092": ["TiffAnalysisSettings"],
        "_1093": ["TipAlterationCoefficientMethod"],
        "_1094": ["TolerancedMetalMeasurements"],
        "_1095": ["TolerancedValueSpecification"],
        "_1096": ["ToothFlankFractureAnalysisSettings"],
        "_1097": ["ToothThicknessSpecification"],
        "_1098": ["ToothThicknessSpecificationBase"],
        "_1099": ["TypeOfMechanismHousing"],
        "_1100": ["Usage"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AddendumModificationDistributionRule",
    "BacklashSpecification",
    "BasicRackProfiles",
    "CaseHardeningProperties",
    "CreateNewSuitableCutterOption",
    "CrossedAxisCylindricalGearPair",
    "CrossedAxisCylindricalGearPairLineContact",
    "CrossedAxisCylindricalGearPairPointContact",
    "Customer102DataSheetChangeLog",
    "Customer102DataSheetChangeLogItem",
    "Customer102DataSheetNote",
    "Customer102DataSheetNotes",
    "Customer102DataSheetTolerances",
    "Customer102ToleranceDefinition",
    "CylindricalGearAbstractRack",
    "CylindricalGearAbstractRackFlank",
    "CylindricalGearBasicRack",
    "CylindricalGearBasicRackFlank",
    "CylindricalGearCuttingOptions",
    "CylindricalGearDefaults",
    "CylindricalGearDesign",
    "CylindricalGearDesignConstraint",
    "CylindricalGearDesignConstraints",
    "CylindricalGearDesignConstraintsDatabase",
    "CylindricalGearDesignConstraintSettings",
    "CylindricalGearFlankDesign",
    "CylindricalGearMeshDesign",
    "CylindricalGearMeshFlankDesign",
    "CylindricalGearMicroGeometrySettings",
    "CylindricalGearMicroGeometrySettingsDatabase",
    "CylindricalGearMicroGeometrySettingsItem",
    "CylindricalGearPinionTypeCutter",
    "CylindricalGearPinionTypeCutterFlank",
    "CylindricalGearProfileMeasurement",
    "CylindricalGearProfileMeasurementType",
    "CylindricalGearProfileModifications",
    "CylindricalGearSetDesign",
    "CylindricalGearSetFlankDesign",
    "CylindricalGearSetMacroGeometryOptimiser",
    "CylindricalGearSetManufacturingConfigurationSelection",
    "CylindricalGearSetMicroGeometrySettings",
    "CylindricalGearSetOptimisationWrapper",
    "CylindricalGearTableMGItemDetail",
    "CylindricalGearTableWithMGCharts",
    "CylindricalGearToothThicknessSpecification",
    "CylindricalMeshAngularBacklash",
    "CylindricalMeshedGear",
    "CylindricalMeshedGearFlank",
    "CylindricalMeshLinearBacklashSpecification",
    "CylindricalPlanetaryGearSetDesign",
    "CylindricalPlanetGearDesign",
    "DIN3967AllowanceSeries",
    "DIN3967ToleranceSeries",
    "DoubleAxisScaleAndRange",
    "FinishToothThicknessDesignSpecification",
    "GearFitSystems",
    "GearManufacturingConfigSetupViewModel",
    "GearSetManufacturingConfigurationSetup",
    "GeometrySpecificationType",
    "HardenedMaterialProperties",
    "HardnessProfileCalculationMethod",
    "HeatTreatmentType",
    "ISO6336Geometry",
    "ISO6336GeometryBase",
    "ISO6336GeometryForShapedGears",
    "ISO6336GeometryManufactured",
    "LinearBacklashSpecification",
    "LTCALoadCaseModifiableSettings",
    "LTCASettings",
    "MicroGeometryConvention",
    "MicroGeometryProfileConvention",
    "Micropitting",
    "MullerResidualStressDefinition",
    "NamedPlanetAssemblyIndex",
    "NamedPlanetSideBandAmplitudeFactor",
    "ReadonlyToothThicknessSpecification",
    "RelativeMeasurementViewModel",
    "RelativeValuesSpecification",
    "ResidualStressCalculationMethod",
    "RootStressSurfaceChartOption",
    "Scuffing",
    "ScuffingCoefficientOfFrictionMethods",
    "ScuffingTemperatureMethodsAGMA",
    "ScuffingTemperatureMethodsISO",
    "ShaperEdgeTypes",
    "SpurGearLoadSharingCodes",
    "StandardRack",
    "StandardRackFlank",
    "SurfaceRoughness",
    "ThicknessType",
    "TiffAnalysisSettings",
    "TipAlterationCoefficientMethod",
    "TolerancedMetalMeasurements",
    "TolerancedValueSpecification",
    "ToothFlankFractureAnalysisSettings",
    "ToothThicknessSpecification",
    "ToothThicknessSpecificationBase",
    "TypeOfMechanismHousing",
    "Usage",
)
