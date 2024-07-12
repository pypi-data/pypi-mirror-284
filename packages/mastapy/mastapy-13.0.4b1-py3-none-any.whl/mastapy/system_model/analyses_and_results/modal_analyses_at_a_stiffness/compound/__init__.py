"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5009 import AbstractAssemblyCompoundModalAnalysisAtAStiffness
    from ._5010 import AbstractShaftCompoundModalAnalysisAtAStiffness
    from ._5011 import AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness
    from ._5012 import (
        AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5013 import AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness
    from ._5014 import AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness
    from ._5015 import AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness
    from ._5016 import AssemblyCompoundModalAnalysisAtAStiffness
    from ._5017 import BearingCompoundModalAnalysisAtAStiffness
    from ._5018 import BeltConnectionCompoundModalAnalysisAtAStiffness
    from ._5019 import BeltDriveCompoundModalAnalysisAtAStiffness
    from ._5020 import BevelDifferentialGearCompoundModalAnalysisAtAStiffness
    from ._5021 import BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness
    from ._5022 import BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness
    from ._5023 import BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness
    from ._5024 import BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness
    from ._5025 import BevelGearCompoundModalAnalysisAtAStiffness
    from ._5026 import BevelGearMeshCompoundModalAnalysisAtAStiffness
    from ._5027 import BevelGearSetCompoundModalAnalysisAtAStiffness
    from ._5028 import BoltCompoundModalAnalysisAtAStiffness
    from ._5029 import BoltedJointCompoundModalAnalysisAtAStiffness
    from ._5030 import ClutchCompoundModalAnalysisAtAStiffness
    from ._5031 import ClutchConnectionCompoundModalAnalysisAtAStiffness
    from ._5032 import ClutchHalfCompoundModalAnalysisAtAStiffness
    from ._5033 import CoaxialConnectionCompoundModalAnalysisAtAStiffness
    from ._5034 import ComponentCompoundModalAnalysisAtAStiffness
    from ._5035 import ConceptCouplingCompoundModalAnalysisAtAStiffness
    from ._5036 import ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness
    from ._5037 import ConceptCouplingHalfCompoundModalAnalysisAtAStiffness
    from ._5038 import ConceptGearCompoundModalAnalysisAtAStiffness
    from ._5039 import ConceptGearMeshCompoundModalAnalysisAtAStiffness
    from ._5040 import ConceptGearSetCompoundModalAnalysisAtAStiffness
    from ._5041 import ConicalGearCompoundModalAnalysisAtAStiffness
    from ._5042 import ConicalGearMeshCompoundModalAnalysisAtAStiffness
    from ._5043 import ConicalGearSetCompoundModalAnalysisAtAStiffness
    from ._5044 import ConnectionCompoundModalAnalysisAtAStiffness
    from ._5045 import ConnectorCompoundModalAnalysisAtAStiffness
    from ._5046 import CouplingCompoundModalAnalysisAtAStiffness
    from ._5047 import CouplingConnectionCompoundModalAnalysisAtAStiffness
    from ._5048 import CouplingHalfCompoundModalAnalysisAtAStiffness
    from ._5049 import CVTBeltConnectionCompoundModalAnalysisAtAStiffness
    from ._5050 import CVTCompoundModalAnalysisAtAStiffness
    from ._5051 import CVTPulleyCompoundModalAnalysisAtAStiffness
    from ._5052 import CycloidalAssemblyCompoundModalAnalysisAtAStiffness
    from ._5053 import (
        CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5054 import CycloidalDiscCompoundModalAnalysisAtAStiffness
    from ._5055 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5056 import CylindricalGearCompoundModalAnalysisAtAStiffness
    from ._5057 import CylindricalGearMeshCompoundModalAnalysisAtAStiffness
    from ._5058 import CylindricalGearSetCompoundModalAnalysisAtAStiffness
    from ._5059 import CylindricalPlanetGearCompoundModalAnalysisAtAStiffness
    from ._5060 import DatumCompoundModalAnalysisAtAStiffness
    from ._5061 import ExternalCADModelCompoundModalAnalysisAtAStiffness
    from ._5062 import FaceGearCompoundModalAnalysisAtAStiffness
    from ._5063 import FaceGearMeshCompoundModalAnalysisAtAStiffness
    from ._5064 import FaceGearSetCompoundModalAnalysisAtAStiffness
    from ._5065 import FEPartCompoundModalAnalysisAtAStiffness
    from ._5066 import FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness
    from ._5067 import GearCompoundModalAnalysisAtAStiffness
    from ._5068 import GearMeshCompoundModalAnalysisAtAStiffness
    from ._5069 import GearSetCompoundModalAnalysisAtAStiffness
    from ._5070 import GuideDxfModelCompoundModalAnalysisAtAStiffness
    from ._5071 import HypoidGearCompoundModalAnalysisAtAStiffness
    from ._5072 import HypoidGearMeshCompoundModalAnalysisAtAStiffness
    from ._5073 import HypoidGearSetCompoundModalAnalysisAtAStiffness
    from ._5074 import (
        InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5075 import (
        KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness,
    )
    from ._5076 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness,
    )
    from ._5077 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness,
    )
    from ._5078 import (
        KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness,
    )
    from ._5079 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness,
    )
    from ._5080 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness,
    )
    from ._5081 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness,
    )
    from ._5082 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtAStiffness,
    )
    from ._5083 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness,
    )
    from ._5084 import MassDiscCompoundModalAnalysisAtAStiffness
    from ._5085 import MeasurementComponentCompoundModalAnalysisAtAStiffness
    from ._5086 import MountableComponentCompoundModalAnalysisAtAStiffness
    from ._5087 import OilSealCompoundModalAnalysisAtAStiffness
    from ._5088 import PartCompoundModalAnalysisAtAStiffness
    from ._5089 import PartToPartShearCouplingCompoundModalAnalysisAtAStiffness
    from ._5090 import (
        PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5091 import PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness
    from ._5092 import PlanetaryConnectionCompoundModalAnalysisAtAStiffness
    from ._5093 import PlanetaryGearSetCompoundModalAnalysisAtAStiffness
    from ._5094 import PlanetCarrierCompoundModalAnalysisAtAStiffness
    from ._5095 import PointLoadCompoundModalAnalysisAtAStiffness
    from ._5096 import PowerLoadCompoundModalAnalysisAtAStiffness
    from ._5097 import PulleyCompoundModalAnalysisAtAStiffness
    from ._5098 import RingPinsCompoundModalAnalysisAtAStiffness
    from ._5099 import RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness
    from ._5100 import RollingRingAssemblyCompoundModalAnalysisAtAStiffness
    from ._5101 import RollingRingCompoundModalAnalysisAtAStiffness
    from ._5102 import RollingRingConnectionCompoundModalAnalysisAtAStiffness
    from ._5103 import RootAssemblyCompoundModalAnalysisAtAStiffness
    from ._5104 import ShaftCompoundModalAnalysisAtAStiffness
    from ._5105 import ShaftHubConnectionCompoundModalAnalysisAtAStiffness
    from ._5106 import (
        ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5107 import SpecialisedAssemblyCompoundModalAnalysisAtAStiffness
    from ._5108 import SpiralBevelGearCompoundModalAnalysisAtAStiffness
    from ._5109 import SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness
    from ._5110 import SpiralBevelGearSetCompoundModalAnalysisAtAStiffness
    from ._5111 import SpringDamperCompoundModalAnalysisAtAStiffness
    from ._5112 import SpringDamperConnectionCompoundModalAnalysisAtAStiffness
    from ._5113 import SpringDamperHalfCompoundModalAnalysisAtAStiffness
    from ._5114 import StraightBevelDiffGearCompoundModalAnalysisAtAStiffness
    from ._5115 import StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness
    from ._5116 import StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness
    from ._5117 import StraightBevelGearCompoundModalAnalysisAtAStiffness
    from ._5118 import StraightBevelGearMeshCompoundModalAnalysisAtAStiffness
    from ._5119 import StraightBevelGearSetCompoundModalAnalysisAtAStiffness
    from ._5120 import StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness
    from ._5121 import StraightBevelSunGearCompoundModalAnalysisAtAStiffness
    from ._5122 import SynchroniserCompoundModalAnalysisAtAStiffness
    from ._5123 import SynchroniserHalfCompoundModalAnalysisAtAStiffness
    from ._5124 import SynchroniserPartCompoundModalAnalysisAtAStiffness
    from ._5125 import SynchroniserSleeveCompoundModalAnalysisAtAStiffness
    from ._5126 import TorqueConverterCompoundModalAnalysisAtAStiffness
    from ._5127 import TorqueConverterConnectionCompoundModalAnalysisAtAStiffness
    from ._5128 import TorqueConverterPumpCompoundModalAnalysisAtAStiffness
    from ._5129 import TorqueConverterTurbineCompoundModalAnalysisAtAStiffness
    from ._5130 import UnbalancedMassCompoundModalAnalysisAtAStiffness
    from ._5131 import VirtualComponentCompoundModalAnalysisAtAStiffness
    from ._5132 import WormGearCompoundModalAnalysisAtAStiffness
    from ._5133 import WormGearMeshCompoundModalAnalysisAtAStiffness
    from ._5134 import WormGearSetCompoundModalAnalysisAtAStiffness
    from ._5135 import ZerolBevelGearCompoundModalAnalysisAtAStiffness
    from ._5136 import ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness
    from ._5137 import ZerolBevelGearSetCompoundModalAnalysisAtAStiffness
else:
    import_structure = {
        "_5009": ["AbstractAssemblyCompoundModalAnalysisAtAStiffness"],
        "_5010": ["AbstractShaftCompoundModalAnalysisAtAStiffness"],
        "_5011": ["AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness"],
        "_5012": [
            "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness"
        ],
        "_5013": ["AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness"],
        "_5014": ["AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5015": ["AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness"],
        "_5016": ["AssemblyCompoundModalAnalysisAtAStiffness"],
        "_5017": ["BearingCompoundModalAnalysisAtAStiffness"],
        "_5018": ["BeltConnectionCompoundModalAnalysisAtAStiffness"],
        "_5019": ["BeltDriveCompoundModalAnalysisAtAStiffness"],
        "_5020": ["BevelDifferentialGearCompoundModalAnalysisAtAStiffness"],
        "_5021": ["BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5022": ["BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness"],
        "_5023": ["BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness"],
        "_5024": ["BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness"],
        "_5025": ["BevelGearCompoundModalAnalysisAtAStiffness"],
        "_5026": ["BevelGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5027": ["BevelGearSetCompoundModalAnalysisAtAStiffness"],
        "_5028": ["BoltCompoundModalAnalysisAtAStiffness"],
        "_5029": ["BoltedJointCompoundModalAnalysisAtAStiffness"],
        "_5030": ["ClutchCompoundModalAnalysisAtAStiffness"],
        "_5031": ["ClutchConnectionCompoundModalAnalysisAtAStiffness"],
        "_5032": ["ClutchHalfCompoundModalAnalysisAtAStiffness"],
        "_5033": ["CoaxialConnectionCompoundModalAnalysisAtAStiffness"],
        "_5034": ["ComponentCompoundModalAnalysisAtAStiffness"],
        "_5035": ["ConceptCouplingCompoundModalAnalysisAtAStiffness"],
        "_5036": ["ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness"],
        "_5037": ["ConceptCouplingHalfCompoundModalAnalysisAtAStiffness"],
        "_5038": ["ConceptGearCompoundModalAnalysisAtAStiffness"],
        "_5039": ["ConceptGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5040": ["ConceptGearSetCompoundModalAnalysisAtAStiffness"],
        "_5041": ["ConicalGearCompoundModalAnalysisAtAStiffness"],
        "_5042": ["ConicalGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5043": ["ConicalGearSetCompoundModalAnalysisAtAStiffness"],
        "_5044": ["ConnectionCompoundModalAnalysisAtAStiffness"],
        "_5045": ["ConnectorCompoundModalAnalysisAtAStiffness"],
        "_5046": ["CouplingCompoundModalAnalysisAtAStiffness"],
        "_5047": ["CouplingConnectionCompoundModalAnalysisAtAStiffness"],
        "_5048": ["CouplingHalfCompoundModalAnalysisAtAStiffness"],
        "_5049": ["CVTBeltConnectionCompoundModalAnalysisAtAStiffness"],
        "_5050": ["CVTCompoundModalAnalysisAtAStiffness"],
        "_5051": ["CVTPulleyCompoundModalAnalysisAtAStiffness"],
        "_5052": ["CycloidalAssemblyCompoundModalAnalysisAtAStiffness"],
        "_5053": [
            "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness"
        ],
        "_5054": ["CycloidalDiscCompoundModalAnalysisAtAStiffness"],
        "_5055": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness"
        ],
        "_5056": ["CylindricalGearCompoundModalAnalysisAtAStiffness"],
        "_5057": ["CylindricalGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5058": ["CylindricalGearSetCompoundModalAnalysisAtAStiffness"],
        "_5059": ["CylindricalPlanetGearCompoundModalAnalysisAtAStiffness"],
        "_5060": ["DatumCompoundModalAnalysisAtAStiffness"],
        "_5061": ["ExternalCADModelCompoundModalAnalysisAtAStiffness"],
        "_5062": ["FaceGearCompoundModalAnalysisAtAStiffness"],
        "_5063": ["FaceGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5064": ["FaceGearSetCompoundModalAnalysisAtAStiffness"],
        "_5065": ["FEPartCompoundModalAnalysisAtAStiffness"],
        "_5066": ["FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness"],
        "_5067": ["GearCompoundModalAnalysisAtAStiffness"],
        "_5068": ["GearMeshCompoundModalAnalysisAtAStiffness"],
        "_5069": ["GearSetCompoundModalAnalysisAtAStiffness"],
        "_5070": ["GuideDxfModelCompoundModalAnalysisAtAStiffness"],
        "_5071": ["HypoidGearCompoundModalAnalysisAtAStiffness"],
        "_5072": ["HypoidGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5073": ["HypoidGearSetCompoundModalAnalysisAtAStiffness"],
        "_5074": ["InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness"],
        "_5075": [
            "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness"
        ],
        "_5076": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness"
        ],
        "_5077": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness"
        ],
        "_5078": [
            "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness"
        ],
        "_5079": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness"
        ],
        "_5080": [
            "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness"
        ],
        "_5081": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness"
        ],
        "_5082": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtAStiffness"
        ],
        "_5083": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness"
        ],
        "_5084": ["MassDiscCompoundModalAnalysisAtAStiffness"],
        "_5085": ["MeasurementComponentCompoundModalAnalysisAtAStiffness"],
        "_5086": ["MountableComponentCompoundModalAnalysisAtAStiffness"],
        "_5087": ["OilSealCompoundModalAnalysisAtAStiffness"],
        "_5088": ["PartCompoundModalAnalysisAtAStiffness"],
        "_5089": ["PartToPartShearCouplingCompoundModalAnalysisAtAStiffness"],
        "_5090": ["PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness"],
        "_5091": ["PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness"],
        "_5092": ["PlanetaryConnectionCompoundModalAnalysisAtAStiffness"],
        "_5093": ["PlanetaryGearSetCompoundModalAnalysisAtAStiffness"],
        "_5094": ["PlanetCarrierCompoundModalAnalysisAtAStiffness"],
        "_5095": ["PointLoadCompoundModalAnalysisAtAStiffness"],
        "_5096": ["PowerLoadCompoundModalAnalysisAtAStiffness"],
        "_5097": ["PulleyCompoundModalAnalysisAtAStiffness"],
        "_5098": ["RingPinsCompoundModalAnalysisAtAStiffness"],
        "_5099": ["RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness"],
        "_5100": ["RollingRingAssemblyCompoundModalAnalysisAtAStiffness"],
        "_5101": ["RollingRingCompoundModalAnalysisAtAStiffness"],
        "_5102": ["RollingRingConnectionCompoundModalAnalysisAtAStiffness"],
        "_5103": ["RootAssemblyCompoundModalAnalysisAtAStiffness"],
        "_5104": ["ShaftCompoundModalAnalysisAtAStiffness"],
        "_5105": ["ShaftHubConnectionCompoundModalAnalysisAtAStiffness"],
        "_5106": [
            "ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness"
        ],
        "_5107": ["SpecialisedAssemblyCompoundModalAnalysisAtAStiffness"],
        "_5108": ["SpiralBevelGearCompoundModalAnalysisAtAStiffness"],
        "_5109": ["SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5110": ["SpiralBevelGearSetCompoundModalAnalysisAtAStiffness"],
        "_5111": ["SpringDamperCompoundModalAnalysisAtAStiffness"],
        "_5112": ["SpringDamperConnectionCompoundModalAnalysisAtAStiffness"],
        "_5113": ["SpringDamperHalfCompoundModalAnalysisAtAStiffness"],
        "_5114": ["StraightBevelDiffGearCompoundModalAnalysisAtAStiffness"],
        "_5115": ["StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5116": ["StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness"],
        "_5117": ["StraightBevelGearCompoundModalAnalysisAtAStiffness"],
        "_5118": ["StraightBevelGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5119": ["StraightBevelGearSetCompoundModalAnalysisAtAStiffness"],
        "_5120": ["StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness"],
        "_5121": ["StraightBevelSunGearCompoundModalAnalysisAtAStiffness"],
        "_5122": ["SynchroniserCompoundModalAnalysisAtAStiffness"],
        "_5123": ["SynchroniserHalfCompoundModalAnalysisAtAStiffness"],
        "_5124": ["SynchroniserPartCompoundModalAnalysisAtAStiffness"],
        "_5125": ["SynchroniserSleeveCompoundModalAnalysisAtAStiffness"],
        "_5126": ["TorqueConverterCompoundModalAnalysisAtAStiffness"],
        "_5127": ["TorqueConverterConnectionCompoundModalAnalysisAtAStiffness"],
        "_5128": ["TorqueConverterPumpCompoundModalAnalysisAtAStiffness"],
        "_5129": ["TorqueConverterTurbineCompoundModalAnalysisAtAStiffness"],
        "_5130": ["UnbalancedMassCompoundModalAnalysisAtAStiffness"],
        "_5131": ["VirtualComponentCompoundModalAnalysisAtAStiffness"],
        "_5132": ["WormGearCompoundModalAnalysisAtAStiffness"],
        "_5133": ["WormGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5134": ["WormGearSetCompoundModalAnalysisAtAStiffness"],
        "_5135": ["ZerolBevelGearCompoundModalAnalysisAtAStiffness"],
        "_5136": ["ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5137": ["ZerolBevelGearSetCompoundModalAnalysisAtAStiffness"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundModalAnalysisAtAStiffness",
    "AbstractShaftCompoundModalAnalysisAtAStiffness",
    "AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness",
    "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
    "AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness",
    "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness",
    "AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness",
    "AssemblyCompoundModalAnalysisAtAStiffness",
    "BearingCompoundModalAnalysisAtAStiffness",
    "BeltConnectionCompoundModalAnalysisAtAStiffness",
    "BeltDriveCompoundModalAnalysisAtAStiffness",
    "BevelDifferentialGearCompoundModalAnalysisAtAStiffness",
    "BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness",
    "BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness",
    "BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness",
    "BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness",
    "BevelGearCompoundModalAnalysisAtAStiffness",
    "BevelGearMeshCompoundModalAnalysisAtAStiffness",
    "BevelGearSetCompoundModalAnalysisAtAStiffness",
    "BoltCompoundModalAnalysisAtAStiffness",
    "BoltedJointCompoundModalAnalysisAtAStiffness",
    "ClutchCompoundModalAnalysisAtAStiffness",
    "ClutchConnectionCompoundModalAnalysisAtAStiffness",
    "ClutchHalfCompoundModalAnalysisAtAStiffness",
    "CoaxialConnectionCompoundModalAnalysisAtAStiffness",
    "ComponentCompoundModalAnalysisAtAStiffness",
    "ConceptCouplingCompoundModalAnalysisAtAStiffness",
    "ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness",
    "ConceptCouplingHalfCompoundModalAnalysisAtAStiffness",
    "ConceptGearCompoundModalAnalysisAtAStiffness",
    "ConceptGearMeshCompoundModalAnalysisAtAStiffness",
    "ConceptGearSetCompoundModalAnalysisAtAStiffness",
    "ConicalGearCompoundModalAnalysisAtAStiffness",
    "ConicalGearMeshCompoundModalAnalysisAtAStiffness",
    "ConicalGearSetCompoundModalAnalysisAtAStiffness",
    "ConnectionCompoundModalAnalysisAtAStiffness",
    "ConnectorCompoundModalAnalysisAtAStiffness",
    "CouplingCompoundModalAnalysisAtAStiffness",
    "CouplingConnectionCompoundModalAnalysisAtAStiffness",
    "CouplingHalfCompoundModalAnalysisAtAStiffness",
    "CVTBeltConnectionCompoundModalAnalysisAtAStiffness",
    "CVTCompoundModalAnalysisAtAStiffness",
    "CVTPulleyCompoundModalAnalysisAtAStiffness",
    "CycloidalAssemblyCompoundModalAnalysisAtAStiffness",
    "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness",
    "CycloidalDiscCompoundModalAnalysisAtAStiffness",
    "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness",
    "CylindricalGearCompoundModalAnalysisAtAStiffness",
    "CylindricalGearMeshCompoundModalAnalysisAtAStiffness",
    "CylindricalGearSetCompoundModalAnalysisAtAStiffness",
    "CylindricalPlanetGearCompoundModalAnalysisAtAStiffness",
    "DatumCompoundModalAnalysisAtAStiffness",
    "ExternalCADModelCompoundModalAnalysisAtAStiffness",
    "FaceGearCompoundModalAnalysisAtAStiffness",
    "FaceGearMeshCompoundModalAnalysisAtAStiffness",
    "FaceGearSetCompoundModalAnalysisAtAStiffness",
    "FEPartCompoundModalAnalysisAtAStiffness",
    "FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness",
    "GearCompoundModalAnalysisAtAStiffness",
    "GearMeshCompoundModalAnalysisAtAStiffness",
    "GearSetCompoundModalAnalysisAtAStiffness",
    "GuideDxfModelCompoundModalAnalysisAtAStiffness",
    "HypoidGearCompoundModalAnalysisAtAStiffness",
    "HypoidGearMeshCompoundModalAnalysisAtAStiffness",
    "HypoidGearSetCompoundModalAnalysisAtAStiffness",
    "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness",
    "MassDiscCompoundModalAnalysisAtAStiffness",
    "MeasurementComponentCompoundModalAnalysisAtAStiffness",
    "MountableComponentCompoundModalAnalysisAtAStiffness",
    "OilSealCompoundModalAnalysisAtAStiffness",
    "PartCompoundModalAnalysisAtAStiffness",
    "PartToPartShearCouplingCompoundModalAnalysisAtAStiffness",
    "PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness",
    "PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness",
    "PlanetaryConnectionCompoundModalAnalysisAtAStiffness",
    "PlanetaryGearSetCompoundModalAnalysisAtAStiffness",
    "PlanetCarrierCompoundModalAnalysisAtAStiffness",
    "PointLoadCompoundModalAnalysisAtAStiffness",
    "PowerLoadCompoundModalAnalysisAtAStiffness",
    "PulleyCompoundModalAnalysisAtAStiffness",
    "RingPinsCompoundModalAnalysisAtAStiffness",
    "RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness",
    "RollingRingAssemblyCompoundModalAnalysisAtAStiffness",
    "RollingRingCompoundModalAnalysisAtAStiffness",
    "RollingRingConnectionCompoundModalAnalysisAtAStiffness",
    "RootAssemblyCompoundModalAnalysisAtAStiffness",
    "ShaftCompoundModalAnalysisAtAStiffness",
    "ShaftHubConnectionCompoundModalAnalysisAtAStiffness",
    "ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
    "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
    "SpiralBevelGearCompoundModalAnalysisAtAStiffness",
    "SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness",
    "SpiralBevelGearSetCompoundModalAnalysisAtAStiffness",
    "SpringDamperCompoundModalAnalysisAtAStiffness",
    "SpringDamperConnectionCompoundModalAnalysisAtAStiffness",
    "SpringDamperHalfCompoundModalAnalysisAtAStiffness",
    "StraightBevelDiffGearCompoundModalAnalysisAtAStiffness",
    "StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness",
    "StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness",
    "StraightBevelGearCompoundModalAnalysisAtAStiffness",
    "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",
    "StraightBevelGearSetCompoundModalAnalysisAtAStiffness",
    "StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness",
    "StraightBevelSunGearCompoundModalAnalysisAtAStiffness",
    "SynchroniserCompoundModalAnalysisAtAStiffness",
    "SynchroniserHalfCompoundModalAnalysisAtAStiffness",
    "SynchroniserPartCompoundModalAnalysisAtAStiffness",
    "SynchroniserSleeveCompoundModalAnalysisAtAStiffness",
    "TorqueConverterCompoundModalAnalysisAtAStiffness",
    "TorqueConverterConnectionCompoundModalAnalysisAtAStiffness",
    "TorqueConverterPumpCompoundModalAnalysisAtAStiffness",
    "TorqueConverterTurbineCompoundModalAnalysisAtAStiffness",
    "UnbalancedMassCompoundModalAnalysisAtAStiffness",
    "VirtualComponentCompoundModalAnalysisAtAStiffness",
    "WormGearCompoundModalAnalysisAtAStiffness",
    "WormGearMeshCompoundModalAnalysisAtAStiffness",
    "WormGearSetCompoundModalAnalysisAtAStiffness",
    "ZerolBevelGearCompoundModalAnalysisAtAStiffness",
    "ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness",
    "ZerolBevelGearSetCompoundModalAnalysisAtAStiffness",
)
