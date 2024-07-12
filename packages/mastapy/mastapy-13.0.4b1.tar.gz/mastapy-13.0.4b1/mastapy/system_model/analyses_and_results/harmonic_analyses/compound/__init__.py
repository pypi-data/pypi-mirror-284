"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5900 import AbstractAssemblyCompoundHarmonicAnalysis
    from ._5901 import AbstractShaftCompoundHarmonicAnalysis
    from ._5902 import AbstractShaftOrHousingCompoundHarmonicAnalysis
    from ._5903 import (
        AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis,
    )
    from ._5904 import AGMAGleasonConicalGearCompoundHarmonicAnalysis
    from ._5905 import AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis
    from ._5906 import AGMAGleasonConicalGearSetCompoundHarmonicAnalysis
    from ._5907 import AssemblyCompoundHarmonicAnalysis
    from ._5908 import BearingCompoundHarmonicAnalysis
    from ._5909 import BeltConnectionCompoundHarmonicAnalysis
    from ._5910 import BeltDriveCompoundHarmonicAnalysis
    from ._5911 import BevelDifferentialGearCompoundHarmonicAnalysis
    from ._5912 import BevelDifferentialGearMeshCompoundHarmonicAnalysis
    from ._5913 import BevelDifferentialGearSetCompoundHarmonicAnalysis
    from ._5914 import BevelDifferentialPlanetGearCompoundHarmonicAnalysis
    from ._5915 import BevelDifferentialSunGearCompoundHarmonicAnalysis
    from ._5916 import BevelGearCompoundHarmonicAnalysis
    from ._5917 import BevelGearMeshCompoundHarmonicAnalysis
    from ._5918 import BevelGearSetCompoundHarmonicAnalysis
    from ._5919 import BoltCompoundHarmonicAnalysis
    from ._5920 import BoltedJointCompoundHarmonicAnalysis
    from ._5921 import ClutchCompoundHarmonicAnalysis
    from ._5922 import ClutchConnectionCompoundHarmonicAnalysis
    from ._5923 import ClutchHalfCompoundHarmonicAnalysis
    from ._5924 import CoaxialConnectionCompoundHarmonicAnalysis
    from ._5925 import ComponentCompoundHarmonicAnalysis
    from ._5926 import ConceptCouplingCompoundHarmonicAnalysis
    from ._5927 import ConceptCouplingConnectionCompoundHarmonicAnalysis
    from ._5928 import ConceptCouplingHalfCompoundHarmonicAnalysis
    from ._5929 import ConceptGearCompoundHarmonicAnalysis
    from ._5930 import ConceptGearMeshCompoundHarmonicAnalysis
    from ._5931 import ConceptGearSetCompoundHarmonicAnalysis
    from ._5932 import ConicalGearCompoundHarmonicAnalysis
    from ._5933 import ConicalGearMeshCompoundHarmonicAnalysis
    from ._5934 import ConicalGearSetCompoundHarmonicAnalysis
    from ._5935 import ConnectionCompoundHarmonicAnalysis
    from ._5936 import ConnectorCompoundHarmonicAnalysis
    from ._5937 import CouplingCompoundHarmonicAnalysis
    from ._5938 import CouplingConnectionCompoundHarmonicAnalysis
    from ._5939 import CouplingHalfCompoundHarmonicAnalysis
    from ._5940 import CVTBeltConnectionCompoundHarmonicAnalysis
    from ._5941 import CVTCompoundHarmonicAnalysis
    from ._5942 import CVTPulleyCompoundHarmonicAnalysis
    from ._5943 import CycloidalAssemblyCompoundHarmonicAnalysis
    from ._5944 import CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis
    from ._5945 import CycloidalDiscCompoundHarmonicAnalysis
    from ._5946 import CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysis
    from ._5947 import CylindricalGearCompoundHarmonicAnalysis
    from ._5948 import CylindricalGearMeshCompoundHarmonicAnalysis
    from ._5949 import CylindricalGearSetCompoundHarmonicAnalysis
    from ._5950 import CylindricalPlanetGearCompoundHarmonicAnalysis
    from ._5951 import DatumCompoundHarmonicAnalysis
    from ._5952 import ExternalCADModelCompoundHarmonicAnalysis
    from ._5953 import FaceGearCompoundHarmonicAnalysis
    from ._5954 import FaceGearMeshCompoundHarmonicAnalysis
    from ._5955 import FaceGearSetCompoundHarmonicAnalysis
    from ._5956 import FEPartCompoundHarmonicAnalysis
    from ._5957 import FlexiblePinAssemblyCompoundHarmonicAnalysis
    from ._5958 import GearCompoundHarmonicAnalysis
    from ._5959 import GearMeshCompoundHarmonicAnalysis
    from ._5960 import GearSetCompoundHarmonicAnalysis
    from ._5961 import GuideDxfModelCompoundHarmonicAnalysis
    from ._5962 import HypoidGearCompoundHarmonicAnalysis
    from ._5963 import HypoidGearMeshCompoundHarmonicAnalysis
    from ._5964 import HypoidGearSetCompoundHarmonicAnalysis
    from ._5965 import InterMountableComponentConnectionCompoundHarmonicAnalysis
    from ._5966 import KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis
    from ._5967 import KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis
    from ._5968 import KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis
    from ._5969 import KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis
    from ._5970 import KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis
    from ._5971 import KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis
    from ._5972 import KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis
    from ._5973 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis,
    )
    from ._5974 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis,
    )
    from ._5975 import MassDiscCompoundHarmonicAnalysis
    from ._5976 import MeasurementComponentCompoundHarmonicAnalysis
    from ._5977 import MountableComponentCompoundHarmonicAnalysis
    from ._5978 import OilSealCompoundHarmonicAnalysis
    from ._5979 import PartCompoundHarmonicAnalysis
    from ._5980 import PartToPartShearCouplingCompoundHarmonicAnalysis
    from ._5981 import PartToPartShearCouplingConnectionCompoundHarmonicAnalysis
    from ._5982 import PartToPartShearCouplingHalfCompoundHarmonicAnalysis
    from ._5983 import PlanetaryConnectionCompoundHarmonicAnalysis
    from ._5984 import PlanetaryGearSetCompoundHarmonicAnalysis
    from ._5985 import PlanetCarrierCompoundHarmonicAnalysis
    from ._5986 import PointLoadCompoundHarmonicAnalysis
    from ._5987 import PowerLoadCompoundHarmonicAnalysis
    from ._5988 import PulleyCompoundHarmonicAnalysis
    from ._5989 import RingPinsCompoundHarmonicAnalysis
    from ._5990 import RingPinsToDiscConnectionCompoundHarmonicAnalysis
    from ._5991 import RollingRingAssemblyCompoundHarmonicAnalysis
    from ._5992 import RollingRingCompoundHarmonicAnalysis
    from ._5993 import RollingRingConnectionCompoundHarmonicAnalysis
    from ._5994 import RootAssemblyCompoundHarmonicAnalysis
    from ._5995 import ShaftCompoundHarmonicAnalysis
    from ._5996 import ShaftHubConnectionCompoundHarmonicAnalysis
    from ._5997 import ShaftToMountableComponentConnectionCompoundHarmonicAnalysis
    from ._5998 import SpecialisedAssemblyCompoundHarmonicAnalysis
    from ._5999 import SpiralBevelGearCompoundHarmonicAnalysis
    from ._6000 import SpiralBevelGearMeshCompoundHarmonicAnalysis
    from ._6001 import SpiralBevelGearSetCompoundHarmonicAnalysis
    from ._6002 import SpringDamperCompoundHarmonicAnalysis
    from ._6003 import SpringDamperConnectionCompoundHarmonicAnalysis
    from ._6004 import SpringDamperHalfCompoundHarmonicAnalysis
    from ._6005 import StraightBevelDiffGearCompoundHarmonicAnalysis
    from ._6006 import StraightBevelDiffGearMeshCompoundHarmonicAnalysis
    from ._6007 import StraightBevelDiffGearSetCompoundHarmonicAnalysis
    from ._6008 import StraightBevelGearCompoundHarmonicAnalysis
    from ._6009 import StraightBevelGearMeshCompoundHarmonicAnalysis
    from ._6010 import StraightBevelGearSetCompoundHarmonicAnalysis
    from ._6011 import StraightBevelPlanetGearCompoundHarmonicAnalysis
    from ._6012 import StraightBevelSunGearCompoundHarmonicAnalysis
    from ._6013 import SynchroniserCompoundHarmonicAnalysis
    from ._6014 import SynchroniserHalfCompoundHarmonicAnalysis
    from ._6015 import SynchroniserPartCompoundHarmonicAnalysis
    from ._6016 import SynchroniserSleeveCompoundHarmonicAnalysis
    from ._6017 import TorqueConverterCompoundHarmonicAnalysis
    from ._6018 import TorqueConverterConnectionCompoundHarmonicAnalysis
    from ._6019 import TorqueConverterPumpCompoundHarmonicAnalysis
    from ._6020 import TorqueConverterTurbineCompoundHarmonicAnalysis
    from ._6021 import UnbalancedMassCompoundHarmonicAnalysis
    from ._6022 import VirtualComponentCompoundHarmonicAnalysis
    from ._6023 import WormGearCompoundHarmonicAnalysis
    from ._6024 import WormGearMeshCompoundHarmonicAnalysis
    from ._6025 import WormGearSetCompoundHarmonicAnalysis
    from ._6026 import ZerolBevelGearCompoundHarmonicAnalysis
    from ._6027 import ZerolBevelGearMeshCompoundHarmonicAnalysis
    from ._6028 import ZerolBevelGearSetCompoundHarmonicAnalysis
else:
    import_structure = {
        "_5900": ["AbstractAssemblyCompoundHarmonicAnalysis"],
        "_5901": ["AbstractShaftCompoundHarmonicAnalysis"],
        "_5902": ["AbstractShaftOrHousingCompoundHarmonicAnalysis"],
        "_5903": [
            "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis"
        ],
        "_5904": ["AGMAGleasonConicalGearCompoundHarmonicAnalysis"],
        "_5905": ["AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis"],
        "_5906": ["AGMAGleasonConicalGearSetCompoundHarmonicAnalysis"],
        "_5907": ["AssemblyCompoundHarmonicAnalysis"],
        "_5908": ["BearingCompoundHarmonicAnalysis"],
        "_5909": ["BeltConnectionCompoundHarmonicAnalysis"],
        "_5910": ["BeltDriveCompoundHarmonicAnalysis"],
        "_5911": ["BevelDifferentialGearCompoundHarmonicAnalysis"],
        "_5912": ["BevelDifferentialGearMeshCompoundHarmonicAnalysis"],
        "_5913": ["BevelDifferentialGearSetCompoundHarmonicAnalysis"],
        "_5914": ["BevelDifferentialPlanetGearCompoundHarmonicAnalysis"],
        "_5915": ["BevelDifferentialSunGearCompoundHarmonicAnalysis"],
        "_5916": ["BevelGearCompoundHarmonicAnalysis"],
        "_5917": ["BevelGearMeshCompoundHarmonicAnalysis"],
        "_5918": ["BevelGearSetCompoundHarmonicAnalysis"],
        "_5919": ["BoltCompoundHarmonicAnalysis"],
        "_5920": ["BoltedJointCompoundHarmonicAnalysis"],
        "_5921": ["ClutchCompoundHarmonicAnalysis"],
        "_5922": ["ClutchConnectionCompoundHarmonicAnalysis"],
        "_5923": ["ClutchHalfCompoundHarmonicAnalysis"],
        "_5924": ["CoaxialConnectionCompoundHarmonicAnalysis"],
        "_5925": ["ComponentCompoundHarmonicAnalysis"],
        "_5926": ["ConceptCouplingCompoundHarmonicAnalysis"],
        "_5927": ["ConceptCouplingConnectionCompoundHarmonicAnalysis"],
        "_5928": ["ConceptCouplingHalfCompoundHarmonicAnalysis"],
        "_5929": ["ConceptGearCompoundHarmonicAnalysis"],
        "_5930": ["ConceptGearMeshCompoundHarmonicAnalysis"],
        "_5931": ["ConceptGearSetCompoundHarmonicAnalysis"],
        "_5932": ["ConicalGearCompoundHarmonicAnalysis"],
        "_5933": ["ConicalGearMeshCompoundHarmonicAnalysis"],
        "_5934": ["ConicalGearSetCompoundHarmonicAnalysis"],
        "_5935": ["ConnectionCompoundHarmonicAnalysis"],
        "_5936": ["ConnectorCompoundHarmonicAnalysis"],
        "_5937": ["CouplingCompoundHarmonicAnalysis"],
        "_5938": ["CouplingConnectionCompoundHarmonicAnalysis"],
        "_5939": ["CouplingHalfCompoundHarmonicAnalysis"],
        "_5940": ["CVTBeltConnectionCompoundHarmonicAnalysis"],
        "_5941": ["CVTCompoundHarmonicAnalysis"],
        "_5942": ["CVTPulleyCompoundHarmonicAnalysis"],
        "_5943": ["CycloidalAssemblyCompoundHarmonicAnalysis"],
        "_5944": ["CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis"],
        "_5945": ["CycloidalDiscCompoundHarmonicAnalysis"],
        "_5946": ["CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysis"],
        "_5947": ["CylindricalGearCompoundHarmonicAnalysis"],
        "_5948": ["CylindricalGearMeshCompoundHarmonicAnalysis"],
        "_5949": ["CylindricalGearSetCompoundHarmonicAnalysis"],
        "_5950": ["CylindricalPlanetGearCompoundHarmonicAnalysis"],
        "_5951": ["DatumCompoundHarmonicAnalysis"],
        "_5952": ["ExternalCADModelCompoundHarmonicAnalysis"],
        "_5953": ["FaceGearCompoundHarmonicAnalysis"],
        "_5954": ["FaceGearMeshCompoundHarmonicAnalysis"],
        "_5955": ["FaceGearSetCompoundHarmonicAnalysis"],
        "_5956": ["FEPartCompoundHarmonicAnalysis"],
        "_5957": ["FlexiblePinAssemblyCompoundHarmonicAnalysis"],
        "_5958": ["GearCompoundHarmonicAnalysis"],
        "_5959": ["GearMeshCompoundHarmonicAnalysis"],
        "_5960": ["GearSetCompoundHarmonicAnalysis"],
        "_5961": ["GuideDxfModelCompoundHarmonicAnalysis"],
        "_5962": ["HypoidGearCompoundHarmonicAnalysis"],
        "_5963": ["HypoidGearMeshCompoundHarmonicAnalysis"],
        "_5964": ["HypoidGearSetCompoundHarmonicAnalysis"],
        "_5965": ["InterMountableComponentConnectionCompoundHarmonicAnalysis"],
        "_5966": ["KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis"],
        "_5967": ["KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis"],
        "_5968": ["KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis"],
        "_5969": ["KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis"],
        "_5970": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis"],
        "_5971": ["KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis"],
        "_5972": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis"],
        "_5973": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis"
        ],
        "_5974": ["KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis"],
        "_5975": ["MassDiscCompoundHarmonicAnalysis"],
        "_5976": ["MeasurementComponentCompoundHarmonicAnalysis"],
        "_5977": ["MountableComponentCompoundHarmonicAnalysis"],
        "_5978": ["OilSealCompoundHarmonicAnalysis"],
        "_5979": ["PartCompoundHarmonicAnalysis"],
        "_5980": ["PartToPartShearCouplingCompoundHarmonicAnalysis"],
        "_5981": ["PartToPartShearCouplingConnectionCompoundHarmonicAnalysis"],
        "_5982": ["PartToPartShearCouplingHalfCompoundHarmonicAnalysis"],
        "_5983": ["PlanetaryConnectionCompoundHarmonicAnalysis"],
        "_5984": ["PlanetaryGearSetCompoundHarmonicAnalysis"],
        "_5985": ["PlanetCarrierCompoundHarmonicAnalysis"],
        "_5986": ["PointLoadCompoundHarmonicAnalysis"],
        "_5987": ["PowerLoadCompoundHarmonicAnalysis"],
        "_5988": ["PulleyCompoundHarmonicAnalysis"],
        "_5989": ["RingPinsCompoundHarmonicAnalysis"],
        "_5990": ["RingPinsToDiscConnectionCompoundHarmonicAnalysis"],
        "_5991": ["RollingRingAssemblyCompoundHarmonicAnalysis"],
        "_5992": ["RollingRingCompoundHarmonicAnalysis"],
        "_5993": ["RollingRingConnectionCompoundHarmonicAnalysis"],
        "_5994": ["RootAssemblyCompoundHarmonicAnalysis"],
        "_5995": ["ShaftCompoundHarmonicAnalysis"],
        "_5996": ["ShaftHubConnectionCompoundHarmonicAnalysis"],
        "_5997": ["ShaftToMountableComponentConnectionCompoundHarmonicAnalysis"],
        "_5998": ["SpecialisedAssemblyCompoundHarmonicAnalysis"],
        "_5999": ["SpiralBevelGearCompoundHarmonicAnalysis"],
        "_6000": ["SpiralBevelGearMeshCompoundHarmonicAnalysis"],
        "_6001": ["SpiralBevelGearSetCompoundHarmonicAnalysis"],
        "_6002": ["SpringDamperCompoundHarmonicAnalysis"],
        "_6003": ["SpringDamperConnectionCompoundHarmonicAnalysis"],
        "_6004": ["SpringDamperHalfCompoundHarmonicAnalysis"],
        "_6005": ["StraightBevelDiffGearCompoundHarmonicAnalysis"],
        "_6006": ["StraightBevelDiffGearMeshCompoundHarmonicAnalysis"],
        "_6007": ["StraightBevelDiffGearSetCompoundHarmonicAnalysis"],
        "_6008": ["StraightBevelGearCompoundHarmonicAnalysis"],
        "_6009": ["StraightBevelGearMeshCompoundHarmonicAnalysis"],
        "_6010": ["StraightBevelGearSetCompoundHarmonicAnalysis"],
        "_6011": ["StraightBevelPlanetGearCompoundHarmonicAnalysis"],
        "_6012": ["StraightBevelSunGearCompoundHarmonicAnalysis"],
        "_6013": ["SynchroniserCompoundHarmonicAnalysis"],
        "_6014": ["SynchroniserHalfCompoundHarmonicAnalysis"],
        "_6015": ["SynchroniserPartCompoundHarmonicAnalysis"],
        "_6016": ["SynchroniserSleeveCompoundHarmonicAnalysis"],
        "_6017": ["TorqueConverterCompoundHarmonicAnalysis"],
        "_6018": ["TorqueConverterConnectionCompoundHarmonicAnalysis"],
        "_6019": ["TorqueConverterPumpCompoundHarmonicAnalysis"],
        "_6020": ["TorqueConverterTurbineCompoundHarmonicAnalysis"],
        "_6021": ["UnbalancedMassCompoundHarmonicAnalysis"],
        "_6022": ["VirtualComponentCompoundHarmonicAnalysis"],
        "_6023": ["WormGearCompoundHarmonicAnalysis"],
        "_6024": ["WormGearMeshCompoundHarmonicAnalysis"],
        "_6025": ["WormGearSetCompoundHarmonicAnalysis"],
        "_6026": ["ZerolBevelGearCompoundHarmonicAnalysis"],
        "_6027": ["ZerolBevelGearMeshCompoundHarmonicAnalysis"],
        "_6028": ["ZerolBevelGearSetCompoundHarmonicAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundHarmonicAnalysis",
    "AbstractShaftCompoundHarmonicAnalysis",
    "AbstractShaftOrHousingCompoundHarmonicAnalysis",
    "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
    "AGMAGleasonConicalGearCompoundHarmonicAnalysis",
    "AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis",
    "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
    "AssemblyCompoundHarmonicAnalysis",
    "BearingCompoundHarmonicAnalysis",
    "BeltConnectionCompoundHarmonicAnalysis",
    "BeltDriveCompoundHarmonicAnalysis",
    "BevelDifferentialGearCompoundHarmonicAnalysis",
    "BevelDifferentialGearMeshCompoundHarmonicAnalysis",
    "BevelDifferentialGearSetCompoundHarmonicAnalysis",
    "BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
    "BevelDifferentialSunGearCompoundHarmonicAnalysis",
    "BevelGearCompoundHarmonicAnalysis",
    "BevelGearMeshCompoundHarmonicAnalysis",
    "BevelGearSetCompoundHarmonicAnalysis",
    "BoltCompoundHarmonicAnalysis",
    "BoltedJointCompoundHarmonicAnalysis",
    "ClutchCompoundHarmonicAnalysis",
    "ClutchConnectionCompoundHarmonicAnalysis",
    "ClutchHalfCompoundHarmonicAnalysis",
    "CoaxialConnectionCompoundHarmonicAnalysis",
    "ComponentCompoundHarmonicAnalysis",
    "ConceptCouplingCompoundHarmonicAnalysis",
    "ConceptCouplingConnectionCompoundHarmonicAnalysis",
    "ConceptCouplingHalfCompoundHarmonicAnalysis",
    "ConceptGearCompoundHarmonicAnalysis",
    "ConceptGearMeshCompoundHarmonicAnalysis",
    "ConceptGearSetCompoundHarmonicAnalysis",
    "ConicalGearCompoundHarmonicAnalysis",
    "ConicalGearMeshCompoundHarmonicAnalysis",
    "ConicalGearSetCompoundHarmonicAnalysis",
    "ConnectionCompoundHarmonicAnalysis",
    "ConnectorCompoundHarmonicAnalysis",
    "CouplingCompoundHarmonicAnalysis",
    "CouplingConnectionCompoundHarmonicAnalysis",
    "CouplingHalfCompoundHarmonicAnalysis",
    "CVTBeltConnectionCompoundHarmonicAnalysis",
    "CVTCompoundHarmonicAnalysis",
    "CVTPulleyCompoundHarmonicAnalysis",
    "CycloidalAssemblyCompoundHarmonicAnalysis",
    "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
    "CycloidalDiscCompoundHarmonicAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysis",
    "CylindricalGearCompoundHarmonicAnalysis",
    "CylindricalGearMeshCompoundHarmonicAnalysis",
    "CylindricalGearSetCompoundHarmonicAnalysis",
    "CylindricalPlanetGearCompoundHarmonicAnalysis",
    "DatumCompoundHarmonicAnalysis",
    "ExternalCADModelCompoundHarmonicAnalysis",
    "FaceGearCompoundHarmonicAnalysis",
    "FaceGearMeshCompoundHarmonicAnalysis",
    "FaceGearSetCompoundHarmonicAnalysis",
    "FEPartCompoundHarmonicAnalysis",
    "FlexiblePinAssemblyCompoundHarmonicAnalysis",
    "GearCompoundHarmonicAnalysis",
    "GearMeshCompoundHarmonicAnalysis",
    "GearSetCompoundHarmonicAnalysis",
    "GuideDxfModelCompoundHarmonicAnalysis",
    "HypoidGearCompoundHarmonicAnalysis",
    "HypoidGearMeshCompoundHarmonicAnalysis",
    "HypoidGearSetCompoundHarmonicAnalysis",
    "InterMountableComponentConnectionCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis",
    "MassDiscCompoundHarmonicAnalysis",
    "MeasurementComponentCompoundHarmonicAnalysis",
    "MountableComponentCompoundHarmonicAnalysis",
    "OilSealCompoundHarmonicAnalysis",
    "PartCompoundHarmonicAnalysis",
    "PartToPartShearCouplingCompoundHarmonicAnalysis",
    "PartToPartShearCouplingConnectionCompoundHarmonicAnalysis",
    "PartToPartShearCouplingHalfCompoundHarmonicAnalysis",
    "PlanetaryConnectionCompoundHarmonicAnalysis",
    "PlanetaryGearSetCompoundHarmonicAnalysis",
    "PlanetCarrierCompoundHarmonicAnalysis",
    "PointLoadCompoundHarmonicAnalysis",
    "PowerLoadCompoundHarmonicAnalysis",
    "PulleyCompoundHarmonicAnalysis",
    "RingPinsCompoundHarmonicAnalysis",
    "RingPinsToDiscConnectionCompoundHarmonicAnalysis",
    "RollingRingAssemblyCompoundHarmonicAnalysis",
    "RollingRingCompoundHarmonicAnalysis",
    "RollingRingConnectionCompoundHarmonicAnalysis",
    "RootAssemblyCompoundHarmonicAnalysis",
    "ShaftCompoundHarmonicAnalysis",
    "ShaftHubConnectionCompoundHarmonicAnalysis",
    "ShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
    "SpecialisedAssemblyCompoundHarmonicAnalysis",
    "SpiralBevelGearCompoundHarmonicAnalysis",
    "SpiralBevelGearMeshCompoundHarmonicAnalysis",
    "SpiralBevelGearSetCompoundHarmonicAnalysis",
    "SpringDamperCompoundHarmonicAnalysis",
    "SpringDamperConnectionCompoundHarmonicAnalysis",
    "SpringDamperHalfCompoundHarmonicAnalysis",
    "StraightBevelDiffGearCompoundHarmonicAnalysis",
    "StraightBevelDiffGearMeshCompoundHarmonicAnalysis",
    "StraightBevelDiffGearSetCompoundHarmonicAnalysis",
    "StraightBevelGearCompoundHarmonicAnalysis",
    "StraightBevelGearMeshCompoundHarmonicAnalysis",
    "StraightBevelGearSetCompoundHarmonicAnalysis",
    "StraightBevelPlanetGearCompoundHarmonicAnalysis",
    "StraightBevelSunGearCompoundHarmonicAnalysis",
    "SynchroniserCompoundHarmonicAnalysis",
    "SynchroniserHalfCompoundHarmonicAnalysis",
    "SynchroniserPartCompoundHarmonicAnalysis",
    "SynchroniserSleeveCompoundHarmonicAnalysis",
    "TorqueConverterCompoundHarmonicAnalysis",
    "TorqueConverterConnectionCompoundHarmonicAnalysis",
    "TorqueConverterPumpCompoundHarmonicAnalysis",
    "TorqueConverterTurbineCompoundHarmonicAnalysis",
    "UnbalancedMassCompoundHarmonicAnalysis",
    "VirtualComponentCompoundHarmonicAnalysis",
    "WormGearCompoundHarmonicAnalysis",
    "WormGearMeshCompoundHarmonicAnalysis",
    "WormGearSetCompoundHarmonicAnalysis",
    "ZerolBevelGearCompoundHarmonicAnalysis",
    "ZerolBevelGearMeshCompoundHarmonicAnalysis",
    "ZerolBevelGearSetCompoundHarmonicAnalysis",
)
