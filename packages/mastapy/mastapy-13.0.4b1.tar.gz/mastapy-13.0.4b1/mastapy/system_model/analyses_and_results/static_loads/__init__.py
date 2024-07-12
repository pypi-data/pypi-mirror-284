"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6825 import LoadCase
    from ._6826 import StaticLoadCase
    from ._6827 import TimeSeriesLoadCase
    from ._6828 import AbstractAssemblyLoadCase
    from ._6829 import AbstractShaftLoadCase
    from ._6830 import AbstractShaftOrHousingLoadCase
    from ._6831 import AbstractShaftToMountableComponentConnectionLoadCase
    from ._6832 import AdditionalAccelerationOptions
    from ._6833 import AdvancedTimeSteppingAnalysisForModulationStaticLoadCase
    from ._6834 import AdvancedTimeSteppingAnalysisForModulationType
    from ._6835 import AGMAGleasonConicalGearLoadCase
    from ._6836 import AGMAGleasonConicalGearMeshLoadCase
    from ._6837 import AGMAGleasonConicalGearSetLoadCase
    from ._6838 import AllRingPinsManufacturingError
    from ._6839 import AnalysisType
    from ._6840 import AssemblyLoadCase
    from ._6841 import BearingLoadCase
    from ._6842 import BeltConnectionLoadCase
    from ._6843 import BeltDriveLoadCase
    from ._6844 import BevelDifferentialGearLoadCase
    from ._6845 import BevelDifferentialGearMeshLoadCase
    from ._6846 import BevelDifferentialGearSetLoadCase
    from ._6847 import BevelDifferentialPlanetGearLoadCase
    from ._6848 import BevelDifferentialSunGearLoadCase
    from ._6849 import BevelGearLoadCase
    from ._6850 import BevelGearMeshLoadCase
    from ._6851 import BevelGearSetLoadCase
    from ._6852 import BoltedJointLoadCase
    from ._6853 import BoltLoadCase
    from ._6854 import ClutchConnectionLoadCase
    from ._6855 import ClutchHalfLoadCase
    from ._6856 import ClutchLoadCase
    from ._6857 import CMSElementFaceGroupWithSelectionOption
    from ._6858 import CoaxialConnectionLoadCase
    from ._6859 import ComponentLoadCase
    from ._6860 import ConceptCouplingConnectionLoadCase
    from ._6861 import ConceptCouplingHalfLoadCase
    from ._6862 import ConceptCouplingLoadCase
    from ._6863 import ConceptGearLoadCase
    from ._6864 import ConceptGearMeshLoadCase
    from ._6865 import ConceptGearSetLoadCase
    from ._6866 import ConicalGearLoadCase
    from ._6867 import ConicalGearManufactureError
    from ._6868 import ConicalGearMeshLoadCase
    from ._6869 import ConicalGearSetHarmonicLoadData
    from ._6870 import ConicalGearSetLoadCase
    from ._6871 import ConnectionLoadCase
    from ._6872 import ConnectorLoadCase
    from ._6873 import CouplingConnectionLoadCase
    from ._6874 import CouplingHalfLoadCase
    from ._6875 import CouplingLoadCase
    from ._6876 import CVTBeltConnectionLoadCase
    from ._6877 import CVTLoadCase
    from ._6878 import CVTPulleyLoadCase
    from ._6879 import CycloidalAssemblyLoadCase
    from ._6880 import CycloidalDiscCentralBearingConnectionLoadCase
    from ._6881 import CycloidalDiscLoadCase
    from ._6882 import CycloidalDiscPlanetaryBearingConnectionLoadCase
    from ._6883 import CylindricalGearLoadCase
    from ._6884 import CylindricalGearManufactureError
    from ._6885 import CylindricalGearMeshLoadCase
    from ._6886 import CylindricalGearSetHarmonicLoadData
    from ._6887 import CylindricalGearSetLoadCase
    from ._6888 import CylindricalPlanetGearLoadCase
    from ._6889 import DataFromMotorPackagePerMeanTorque
    from ._6890 import DataFromMotorPackagePerSpeed
    from ._6891 import DatumLoadCase
    from ._6892 import ElectricMachineDataImportType
    from ._6893 import ElectricMachineHarmonicLoadData
    from ._6894 import ElectricMachineHarmonicLoadDataFromExcel
    from ._6895 import ElectricMachineHarmonicLoadDataFromFlux
    from ._6896 import ElectricMachineHarmonicLoadDataFromJMAG
    from ._6897 import ElectricMachineHarmonicLoadDataFromMASTA
    from ._6898 import ElectricMachineHarmonicLoadDataFromMotorCAD
    from ._6899 import ElectricMachineHarmonicLoadDataFromMotorPackages
    from ._6900 import ElectricMachineHarmonicLoadExcelImportOptions
    from ._6901 import ElectricMachineHarmonicLoadFluxImportOptions
    from ._6902 import ElectricMachineHarmonicLoadImportOptionsBase
    from ._6903 import ElectricMachineHarmonicLoadJMAGImportOptions
    from ._6904 import ElectricMachineHarmonicLoadMotorCADImportOptions
    from ._6905 import ExternalCADModelLoadCase
    from ._6906 import FaceGearLoadCase
    from ._6907 import FaceGearMeshLoadCase
    from ._6908 import FaceGearSetLoadCase
    from ._6909 import FEPartLoadCase
    from ._6910 import FlexiblePinAssemblyLoadCase
    from ._6911 import ForceAndTorqueScalingFactor
    from ._6912 import GearLoadCase
    from ._6913 import GearManufactureError
    from ._6914 import GearMeshLoadCase
    from ._6915 import GearMeshTEOrderType
    from ._6916 import GearSetHarmonicLoadData
    from ._6917 import GearSetLoadCase
    from ._6918 import GuideDxfModelLoadCase
    from ._6919 import HarmonicExcitationType
    from ._6920 import HarmonicLoadDataCSVImport
    from ._6921 import HarmonicLoadDataExcelImport
    from ._6922 import HarmonicLoadDataFluxImport
    from ._6923 import HarmonicLoadDataImportBase
    from ._6924 import HarmonicLoadDataImportFromMotorPackages
    from ._6925 import HarmonicLoadDataJMAGImport
    from ._6926 import HarmonicLoadDataMotorCADImport
    from ._6927 import HypoidGearLoadCase
    from ._6928 import HypoidGearMeshLoadCase
    from ._6929 import HypoidGearSetLoadCase
    from ._6930 import ImportType
    from ._6931 import InformationAtRingPinToDiscContactPointFromGeometry
    from ._6932 import InnerDiameterReference
    from ._6933 import InterMountableComponentConnectionLoadCase
    from ._6934 import KlingelnbergCycloPalloidConicalGearLoadCase
    from ._6935 import KlingelnbergCycloPalloidConicalGearMeshLoadCase
    from ._6936 import KlingelnbergCycloPalloidConicalGearSetLoadCase
    from ._6937 import KlingelnbergCycloPalloidHypoidGearLoadCase
    from ._6938 import KlingelnbergCycloPalloidHypoidGearMeshLoadCase
    from ._6939 import KlingelnbergCycloPalloidHypoidGearSetLoadCase
    from ._6940 import KlingelnbergCycloPalloidSpiralBevelGearLoadCase
    from ._6941 import KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase
    from ._6942 import KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase
    from ._6943 import MassDiscLoadCase
    from ._6944 import MeasurementComponentLoadCase
    from ._6945 import MeshStiffnessSource
    from ._6946 import MountableComponentLoadCase
    from ._6947 import NamedSpeed
    from ._6948 import OilSealLoadCase
    from ._6949 import ParametricStudyType
    from ._6950 import PartLoadCase
    from ._6951 import PartToPartShearCouplingConnectionLoadCase
    from ._6952 import PartToPartShearCouplingHalfLoadCase
    from ._6953 import PartToPartShearCouplingLoadCase
    from ._6954 import PlanetaryConnectionLoadCase
    from ._6955 import PlanetaryGearSetLoadCase
    from ._6956 import PlanetarySocketManufactureError
    from ._6957 import PlanetCarrierLoadCase
    from ._6958 import PlanetManufactureError
    from ._6959 import PointLoadHarmonicLoadData
    from ._6960 import PointLoadLoadCase
    from ._6961 import PowerLoadLoadCase
    from ._6962 import PulleyLoadCase
    from ._6963 import ResetMicroGeometryOptions
    from ._6964 import RingPinManufacturingError
    from ._6965 import RingPinsLoadCase
    from ._6966 import RingPinsToDiscConnectionLoadCase
    from ._6967 import RollingRingAssemblyLoadCase
    from ._6968 import RollingRingConnectionLoadCase
    from ._6969 import RollingRingLoadCase
    from ._6970 import RootAssemblyLoadCase
    from ._6971 import ShaftHubConnectionLoadCase
    from ._6972 import ShaftLoadCase
    from ._6973 import ShaftToMountableComponentConnectionLoadCase
    from ._6974 import SpecialisedAssemblyLoadCase
    from ._6975 import SpiralBevelGearLoadCase
    from ._6976 import SpiralBevelGearMeshLoadCase
    from ._6977 import SpiralBevelGearSetLoadCase
    from ._6978 import SpringDamperConnectionLoadCase
    from ._6979 import SpringDamperHalfLoadCase
    from ._6980 import SpringDamperLoadCase
    from ._6981 import StraightBevelDiffGearLoadCase
    from ._6982 import StraightBevelDiffGearMeshLoadCase
    from ._6983 import StraightBevelDiffGearSetLoadCase
    from ._6984 import StraightBevelGearLoadCase
    from ._6985 import StraightBevelGearMeshLoadCase
    from ._6986 import StraightBevelGearSetLoadCase
    from ._6987 import StraightBevelPlanetGearLoadCase
    from ._6988 import StraightBevelSunGearLoadCase
    from ._6989 import SynchroniserHalfLoadCase
    from ._6990 import SynchroniserLoadCase
    from ._6991 import SynchroniserPartLoadCase
    from ._6992 import SynchroniserSleeveLoadCase
    from ._6993 import TEExcitationType
    from ._6994 import TorqueConverterConnectionLoadCase
    from ._6995 import TorqueConverterLoadCase
    from ._6996 import TorqueConverterPumpLoadCase
    from ._6997 import TorqueConverterTurbineLoadCase
    from ._6998 import TorqueRippleInputType
    from ._6999 import TorqueSpecificationForSystemDeflection
    from ._7000 import TransmissionEfficiencySettings
    from ._7001 import UnbalancedMassHarmonicLoadData
    from ._7002 import UnbalancedMassLoadCase
    from ._7003 import VirtualComponentLoadCase
    from ._7004 import WormGearLoadCase
    from ._7005 import WormGearMeshLoadCase
    from ._7006 import WormGearSetLoadCase
    from ._7007 import ZerolBevelGearLoadCase
    from ._7008 import ZerolBevelGearMeshLoadCase
    from ._7009 import ZerolBevelGearSetLoadCase
else:
    import_structure = {
        "_6825": ["LoadCase"],
        "_6826": ["StaticLoadCase"],
        "_6827": ["TimeSeriesLoadCase"],
        "_6828": ["AbstractAssemblyLoadCase"],
        "_6829": ["AbstractShaftLoadCase"],
        "_6830": ["AbstractShaftOrHousingLoadCase"],
        "_6831": ["AbstractShaftToMountableComponentConnectionLoadCase"],
        "_6832": ["AdditionalAccelerationOptions"],
        "_6833": ["AdvancedTimeSteppingAnalysisForModulationStaticLoadCase"],
        "_6834": ["AdvancedTimeSteppingAnalysisForModulationType"],
        "_6835": ["AGMAGleasonConicalGearLoadCase"],
        "_6836": ["AGMAGleasonConicalGearMeshLoadCase"],
        "_6837": ["AGMAGleasonConicalGearSetLoadCase"],
        "_6838": ["AllRingPinsManufacturingError"],
        "_6839": ["AnalysisType"],
        "_6840": ["AssemblyLoadCase"],
        "_6841": ["BearingLoadCase"],
        "_6842": ["BeltConnectionLoadCase"],
        "_6843": ["BeltDriveLoadCase"],
        "_6844": ["BevelDifferentialGearLoadCase"],
        "_6845": ["BevelDifferentialGearMeshLoadCase"],
        "_6846": ["BevelDifferentialGearSetLoadCase"],
        "_6847": ["BevelDifferentialPlanetGearLoadCase"],
        "_6848": ["BevelDifferentialSunGearLoadCase"],
        "_6849": ["BevelGearLoadCase"],
        "_6850": ["BevelGearMeshLoadCase"],
        "_6851": ["BevelGearSetLoadCase"],
        "_6852": ["BoltedJointLoadCase"],
        "_6853": ["BoltLoadCase"],
        "_6854": ["ClutchConnectionLoadCase"],
        "_6855": ["ClutchHalfLoadCase"],
        "_6856": ["ClutchLoadCase"],
        "_6857": ["CMSElementFaceGroupWithSelectionOption"],
        "_6858": ["CoaxialConnectionLoadCase"],
        "_6859": ["ComponentLoadCase"],
        "_6860": ["ConceptCouplingConnectionLoadCase"],
        "_6861": ["ConceptCouplingHalfLoadCase"],
        "_6862": ["ConceptCouplingLoadCase"],
        "_6863": ["ConceptGearLoadCase"],
        "_6864": ["ConceptGearMeshLoadCase"],
        "_6865": ["ConceptGearSetLoadCase"],
        "_6866": ["ConicalGearLoadCase"],
        "_6867": ["ConicalGearManufactureError"],
        "_6868": ["ConicalGearMeshLoadCase"],
        "_6869": ["ConicalGearSetHarmonicLoadData"],
        "_6870": ["ConicalGearSetLoadCase"],
        "_6871": ["ConnectionLoadCase"],
        "_6872": ["ConnectorLoadCase"],
        "_6873": ["CouplingConnectionLoadCase"],
        "_6874": ["CouplingHalfLoadCase"],
        "_6875": ["CouplingLoadCase"],
        "_6876": ["CVTBeltConnectionLoadCase"],
        "_6877": ["CVTLoadCase"],
        "_6878": ["CVTPulleyLoadCase"],
        "_6879": ["CycloidalAssemblyLoadCase"],
        "_6880": ["CycloidalDiscCentralBearingConnectionLoadCase"],
        "_6881": ["CycloidalDiscLoadCase"],
        "_6882": ["CycloidalDiscPlanetaryBearingConnectionLoadCase"],
        "_6883": ["CylindricalGearLoadCase"],
        "_6884": ["CylindricalGearManufactureError"],
        "_6885": ["CylindricalGearMeshLoadCase"],
        "_6886": ["CylindricalGearSetHarmonicLoadData"],
        "_6887": ["CylindricalGearSetLoadCase"],
        "_6888": ["CylindricalPlanetGearLoadCase"],
        "_6889": ["DataFromMotorPackagePerMeanTorque"],
        "_6890": ["DataFromMotorPackagePerSpeed"],
        "_6891": ["DatumLoadCase"],
        "_6892": ["ElectricMachineDataImportType"],
        "_6893": ["ElectricMachineHarmonicLoadData"],
        "_6894": ["ElectricMachineHarmonicLoadDataFromExcel"],
        "_6895": ["ElectricMachineHarmonicLoadDataFromFlux"],
        "_6896": ["ElectricMachineHarmonicLoadDataFromJMAG"],
        "_6897": ["ElectricMachineHarmonicLoadDataFromMASTA"],
        "_6898": ["ElectricMachineHarmonicLoadDataFromMotorCAD"],
        "_6899": ["ElectricMachineHarmonicLoadDataFromMotorPackages"],
        "_6900": ["ElectricMachineHarmonicLoadExcelImportOptions"],
        "_6901": ["ElectricMachineHarmonicLoadFluxImportOptions"],
        "_6902": ["ElectricMachineHarmonicLoadImportOptionsBase"],
        "_6903": ["ElectricMachineHarmonicLoadJMAGImportOptions"],
        "_6904": ["ElectricMachineHarmonicLoadMotorCADImportOptions"],
        "_6905": ["ExternalCADModelLoadCase"],
        "_6906": ["FaceGearLoadCase"],
        "_6907": ["FaceGearMeshLoadCase"],
        "_6908": ["FaceGearSetLoadCase"],
        "_6909": ["FEPartLoadCase"],
        "_6910": ["FlexiblePinAssemblyLoadCase"],
        "_6911": ["ForceAndTorqueScalingFactor"],
        "_6912": ["GearLoadCase"],
        "_6913": ["GearManufactureError"],
        "_6914": ["GearMeshLoadCase"],
        "_6915": ["GearMeshTEOrderType"],
        "_6916": ["GearSetHarmonicLoadData"],
        "_6917": ["GearSetLoadCase"],
        "_6918": ["GuideDxfModelLoadCase"],
        "_6919": ["HarmonicExcitationType"],
        "_6920": ["HarmonicLoadDataCSVImport"],
        "_6921": ["HarmonicLoadDataExcelImport"],
        "_6922": ["HarmonicLoadDataFluxImport"],
        "_6923": ["HarmonicLoadDataImportBase"],
        "_6924": ["HarmonicLoadDataImportFromMotorPackages"],
        "_6925": ["HarmonicLoadDataJMAGImport"],
        "_6926": ["HarmonicLoadDataMotorCADImport"],
        "_6927": ["HypoidGearLoadCase"],
        "_6928": ["HypoidGearMeshLoadCase"],
        "_6929": ["HypoidGearSetLoadCase"],
        "_6930": ["ImportType"],
        "_6931": ["InformationAtRingPinToDiscContactPointFromGeometry"],
        "_6932": ["InnerDiameterReference"],
        "_6933": ["InterMountableComponentConnectionLoadCase"],
        "_6934": ["KlingelnbergCycloPalloidConicalGearLoadCase"],
        "_6935": ["KlingelnbergCycloPalloidConicalGearMeshLoadCase"],
        "_6936": ["KlingelnbergCycloPalloidConicalGearSetLoadCase"],
        "_6937": ["KlingelnbergCycloPalloidHypoidGearLoadCase"],
        "_6938": ["KlingelnbergCycloPalloidHypoidGearMeshLoadCase"],
        "_6939": ["KlingelnbergCycloPalloidHypoidGearSetLoadCase"],
        "_6940": ["KlingelnbergCycloPalloidSpiralBevelGearLoadCase"],
        "_6941": ["KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase"],
        "_6942": ["KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase"],
        "_6943": ["MassDiscLoadCase"],
        "_6944": ["MeasurementComponentLoadCase"],
        "_6945": ["MeshStiffnessSource"],
        "_6946": ["MountableComponentLoadCase"],
        "_6947": ["NamedSpeed"],
        "_6948": ["OilSealLoadCase"],
        "_6949": ["ParametricStudyType"],
        "_6950": ["PartLoadCase"],
        "_6951": ["PartToPartShearCouplingConnectionLoadCase"],
        "_6952": ["PartToPartShearCouplingHalfLoadCase"],
        "_6953": ["PartToPartShearCouplingLoadCase"],
        "_6954": ["PlanetaryConnectionLoadCase"],
        "_6955": ["PlanetaryGearSetLoadCase"],
        "_6956": ["PlanetarySocketManufactureError"],
        "_6957": ["PlanetCarrierLoadCase"],
        "_6958": ["PlanetManufactureError"],
        "_6959": ["PointLoadHarmonicLoadData"],
        "_6960": ["PointLoadLoadCase"],
        "_6961": ["PowerLoadLoadCase"],
        "_6962": ["PulleyLoadCase"],
        "_6963": ["ResetMicroGeometryOptions"],
        "_6964": ["RingPinManufacturingError"],
        "_6965": ["RingPinsLoadCase"],
        "_6966": ["RingPinsToDiscConnectionLoadCase"],
        "_6967": ["RollingRingAssemblyLoadCase"],
        "_6968": ["RollingRingConnectionLoadCase"],
        "_6969": ["RollingRingLoadCase"],
        "_6970": ["RootAssemblyLoadCase"],
        "_6971": ["ShaftHubConnectionLoadCase"],
        "_6972": ["ShaftLoadCase"],
        "_6973": ["ShaftToMountableComponentConnectionLoadCase"],
        "_6974": ["SpecialisedAssemblyLoadCase"],
        "_6975": ["SpiralBevelGearLoadCase"],
        "_6976": ["SpiralBevelGearMeshLoadCase"],
        "_6977": ["SpiralBevelGearSetLoadCase"],
        "_6978": ["SpringDamperConnectionLoadCase"],
        "_6979": ["SpringDamperHalfLoadCase"],
        "_6980": ["SpringDamperLoadCase"],
        "_6981": ["StraightBevelDiffGearLoadCase"],
        "_6982": ["StraightBevelDiffGearMeshLoadCase"],
        "_6983": ["StraightBevelDiffGearSetLoadCase"],
        "_6984": ["StraightBevelGearLoadCase"],
        "_6985": ["StraightBevelGearMeshLoadCase"],
        "_6986": ["StraightBevelGearSetLoadCase"],
        "_6987": ["StraightBevelPlanetGearLoadCase"],
        "_6988": ["StraightBevelSunGearLoadCase"],
        "_6989": ["SynchroniserHalfLoadCase"],
        "_6990": ["SynchroniserLoadCase"],
        "_6991": ["SynchroniserPartLoadCase"],
        "_6992": ["SynchroniserSleeveLoadCase"],
        "_6993": ["TEExcitationType"],
        "_6994": ["TorqueConverterConnectionLoadCase"],
        "_6995": ["TorqueConverterLoadCase"],
        "_6996": ["TorqueConverterPumpLoadCase"],
        "_6997": ["TorqueConverterTurbineLoadCase"],
        "_6998": ["TorqueRippleInputType"],
        "_6999": ["TorqueSpecificationForSystemDeflection"],
        "_7000": ["TransmissionEfficiencySettings"],
        "_7001": ["UnbalancedMassHarmonicLoadData"],
        "_7002": ["UnbalancedMassLoadCase"],
        "_7003": ["VirtualComponentLoadCase"],
        "_7004": ["WormGearLoadCase"],
        "_7005": ["WormGearMeshLoadCase"],
        "_7006": ["WormGearSetLoadCase"],
        "_7007": ["ZerolBevelGearLoadCase"],
        "_7008": ["ZerolBevelGearMeshLoadCase"],
        "_7009": ["ZerolBevelGearSetLoadCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "LoadCase",
    "StaticLoadCase",
    "TimeSeriesLoadCase",
    "AbstractAssemblyLoadCase",
    "AbstractShaftLoadCase",
    "AbstractShaftOrHousingLoadCase",
    "AbstractShaftToMountableComponentConnectionLoadCase",
    "AdditionalAccelerationOptions",
    "AdvancedTimeSteppingAnalysisForModulationStaticLoadCase",
    "AdvancedTimeSteppingAnalysisForModulationType",
    "AGMAGleasonConicalGearLoadCase",
    "AGMAGleasonConicalGearMeshLoadCase",
    "AGMAGleasonConicalGearSetLoadCase",
    "AllRingPinsManufacturingError",
    "AnalysisType",
    "AssemblyLoadCase",
    "BearingLoadCase",
    "BeltConnectionLoadCase",
    "BeltDriveLoadCase",
    "BevelDifferentialGearLoadCase",
    "BevelDifferentialGearMeshLoadCase",
    "BevelDifferentialGearSetLoadCase",
    "BevelDifferentialPlanetGearLoadCase",
    "BevelDifferentialSunGearLoadCase",
    "BevelGearLoadCase",
    "BevelGearMeshLoadCase",
    "BevelGearSetLoadCase",
    "BoltedJointLoadCase",
    "BoltLoadCase",
    "ClutchConnectionLoadCase",
    "ClutchHalfLoadCase",
    "ClutchLoadCase",
    "CMSElementFaceGroupWithSelectionOption",
    "CoaxialConnectionLoadCase",
    "ComponentLoadCase",
    "ConceptCouplingConnectionLoadCase",
    "ConceptCouplingHalfLoadCase",
    "ConceptCouplingLoadCase",
    "ConceptGearLoadCase",
    "ConceptGearMeshLoadCase",
    "ConceptGearSetLoadCase",
    "ConicalGearLoadCase",
    "ConicalGearManufactureError",
    "ConicalGearMeshLoadCase",
    "ConicalGearSetHarmonicLoadData",
    "ConicalGearSetLoadCase",
    "ConnectionLoadCase",
    "ConnectorLoadCase",
    "CouplingConnectionLoadCase",
    "CouplingHalfLoadCase",
    "CouplingLoadCase",
    "CVTBeltConnectionLoadCase",
    "CVTLoadCase",
    "CVTPulleyLoadCase",
    "CycloidalAssemblyLoadCase",
    "CycloidalDiscCentralBearingConnectionLoadCase",
    "CycloidalDiscLoadCase",
    "CycloidalDiscPlanetaryBearingConnectionLoadCase",
    "CylindricalGearLoadCase",
    "CylindricalGearManufactureError",
    "CylindricalGearMeshLoadCase",
    "CylindricalGearSetHarmonicLoadData",
    "CylindricalGearSetLoadCase",
    "CylindricalPlanetGearLoadCase",
    "DataFromMotorPackagePerMeanTorque",
    "DataFromMotorPackagePerSpeed",
    "DatumLoadCase",
    "ElectricMachineDataImportType",
    "ElectricMachineHarmonicLoadData",
    "ElectricMachineHarmonicLoadDataFromExcel",
    "ElectricMachineHarmonicLoadDataFromFlux",
    "ElectricMachineHarmonicLoadDataFromJMAG",
    "ElectricMachineHarmonicLoadDataFromMASTA",
    "ElectricMachineHarmonicLoadDataFromMotorCAD",
    "ElectricMachineHarmonicLoadDataFromMotorPackages",
    "ElectricMachineHarmonicLoadExcelImportOptions",
    "ElectricMachineHarmonicLoadFluxImportOptions",
    "ElectricMachineHarmonicLoadImportOptionsBase",
    "ElectricMachineHarmonicLoadJMAGImportOptions",
    "ElectricMachineHarmonicLoadMotorCADImportOptions",
    "ExternalCADModelLoadCase",
    "FaceGearLoadCase",
    "FaceGearMeshLoadCase",
    "FaceGearSetLoadCase",
    "FEPartLoadCase",
    "FlexiblePinAssemblyLoadCase",
    "ForceAndTorqueScalingFactor",
    "GearLoadCase",
    "GearManufactureError",
    "GearMeshLoadCase",
    "GearMeshTEOrderType",
    "GearSetHarmonicLoadData",
    "GearSetLoadCase",
    "GuideDxfModelLoadCase",
    "HarmonicExcitationType",
    "HarmonicLoadDataCSVImport",
    "HarmonicLoadDataExcelImport",
    "HarmonicLoadDataFluxImport",
    "HarmonicLoadDataImportBase",
    "HarmonicLoadDataImportFromMotorPackages",
    "HarmonicLoadDataJMAGImport",
    "HarmonicLoadDataMotorCADImport",
    "HypoidGearLoadCase",
    "HypoidGearMeshLoadCase",
    "HypoidGearSetLoadCase",
    "ImportType",
    "InformationAtRingPinToDiscContactPointFromGeometry",
    "InnerDiameterReference",
    "InterMountableComponentConnectionLoadCase",
    "KlingelnbergCycloPalloidConicalGearLoadCase",
    "KlingelnbergCycloPalloidConicalGearMeshLoadCase",
    "KlingelnbergCycloPalloidConicalGearSetLoadCase",
    "KlingelnbergCycloPalloidHypoidGearLoadCase",
    "KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
    "KlingelnbergCycloPalloidHypoidGearSetLoadCase",
    "KlingelnbergCycloPalloidSpiralBevelGearLoadCase",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase",
    "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
    "MassDiscLoadCase",
    "MeasurementComponentLoadCase",
    "MeshStiffnessSource",
    "MountableComponentLoadCase",
    "NamedSpeed",
    "OilSealLoadCase",
    "ParametricStudyType",
    "PartLoadCase",
    "PartToPartShearCouplingConnectionLoadCase",
    "PartToPartShearCouplingHalfLoadCase",
    "PartToPartShearCouplingLoadCase",
    "PlanetaryConnectionLoadCase",
    "PlanetaryGearSetLoadCase",
    "PlanetarySocketManufactureError",
    "PlanetCarrierLoadCase",
    "PlanetManufactureError",
    "PointLoadHarmonicLoadData",
    "PointLoadLoadCase",
    "PowerLoadLoadCase",
    "PulleyLoadCase",
    "ResetMicroGeometryOptions",
    "RingPinManufacturingError",
    "RingPinsLoadCase",
    "RingPinsToDiscConnectionLoadCase",
    "RollingRingAssemblyLoadCase",
    "RollingRingConnectionLoadCase",
    "RollingRingLoadCase",
    "RootAssemblyLoadCase",
    "ShaftHubConnectionLoadCase",
    "ShaftLoadCase",
    "ShaftToMountableComponentConnectionLoadCase",
    "SpecialisedAssemblyLoadCase",
    "SpiralBevelGearLoadCase",
    "SpiralBevelGearMeshLoadCase",
    "SpiralBevelGearSetLoadCase",
    "SpringDamperConnectionLoadCase",
    "SpringDamperHalfLoadCase",
    "SpringDamperLoadCase",
    "StraightBevelDiffGearLoadCase",
    "StraightBevelDiffGearMeshLoadCase",
    "StraightBevelDiffGearSetLoadCase",
    "StraightBevelGearLoadCase",
    "StraightBevelGearMeshLoadCase",
    "StraightBevelGearSetLoadCase",
    "StraightBevelPlanetGearLoadCase",
    "StraightBevelSunGearLoadCase",
    "SynchroniserHalfLoadCase",
    "SynchroniserLoadCase",
    "SynchroniserPartLoadCase",
    "SynchroniserSleeveLoadCase",
    "TEExcitationType",
    "TorqueConverterConnectionLoadCase",
    "TorqueConverterLoadCase",
    "TorqueConverterPumpLoadCase",
    "TorqueConverterTurbineLoadCase",
    "TorqueRippleInputType",
    "TorqueSpecificationForSystemDeflection",
    "TransmissionEfficiencySettings",
    "UnbalancedMassHarmonicLoadData",
    "UnbalancedMassLoadCase",
    "VirtualComponentLoadCase",
    "WormGearLoadCase",
    "WormGearMeshLoadCase",
    "WormGearSetLoadCase",
    "ZerolBevelGearLoadCase",
    "ZerolBevelGearMeshLoadCase",
    "ZerolBevelGearSetLoadCase",
)
