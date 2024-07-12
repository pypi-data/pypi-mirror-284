"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7027 import AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7028 import AbstractShaftAdvancedTimeSteppingAnalysisForModulation
    from ._7029 import AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation
    from ._7030 import (
        AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7031 import AdvancedTimeSteppingAnalysisForModulation
    from ._7032 import AtsamExcitationsOrOthers
    from ._7033 import AtsamNaturalFrequencyViewOption
    from ._7034 import AdvancedTimeSteppingAnalysisForModulationOptions
    from ._7035 import AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation
    from ._7036 import (
        AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7037 import (
        AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7038 import AssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7039 import ATSAMResultsVsLargeTimeStepSettings
    from ._7040 import BearingAdvancedTimeSteppingAnalysisForModulation
    from ._7041 import BeltConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7042 import BeltDriveAdvancedTimeSteppingAnalysisForModulation
    from ._7043 import BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation
    from ._7044 import (
        BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7045 import BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7046 import (
        BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7047 import BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation
    from ._7048 import BevelGearAdvancedTimeSteppingAnalysisForModulation
    from ._7049 import BevelGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7050 import BevelGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7051 import BoltAdvancedTimeSteppingAnalysisForModulation
    from ._7052 import BoltedJointAdvancedTimeSteppingAnalysisForModulation
    from ._7053 import ClutchAdvancedTimeSteppingAnalysisForModulation
    from ._7054 import ClutchConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7055 import ClutchHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7056 import CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7057 import ComponentAdvancedTimeSteppingAnalysisForModulation
    from ._7058 import ConceptCouplingAdvancedTimeSteppingAnalysisForModulation
    from ._7059 import (
        ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7060 import ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7061 import ConceptGearAdvancedTimeSteppingAnalysisForModulation
    from ._7062 import ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7063 import ConceptGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7064 import ConicalGearAdvancedTimeSteppingAnalysisForModulation
    from ._7065 import ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7066 import ConicalGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7067 import ConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7068 import ConnectorAdvancedTimeSteppingAnalysisForModulation
    from ._7069 import CouplingAdvancedTimeSteppingAnalysisForModulation
    from ._7070 import CouplingConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7071 import CouplingHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7072 import CVTAdvancedTimeSteppingAnalysisForModulation
    from ._7073 import CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7074 import CVTPulleyAdvancedTimeSteppingAnalysisForModulation
    from ._7075 import CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7076 import CycloidalDiscAdvancedTimeSteppingAnalysisForModulation
    from ._7077 import (
        CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7078 import (
        CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7079 import CylindricalGearAdvancedTimeSteppingAnalysisForModulation
    from ._7080 import CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7081 import CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7082 import CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation
    from ._7083 import DatumAdvancedTimeSteppingAnalysisForModulation
    from ._7084 import ExternalCADModelAdvancedTimeSteppingAnalysisForModulation
    from ._7085 import FaceGearAdvancedTimeSteppingAnalysisForModulation
    from ._7086 import FaceGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7087 import FaceGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7088 import FEPartAdvancedTimeSteppingAnalysisForModulation
    from ._7089 import FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7090 import GearAdvancedTimeSteppingAnalysisForModulation
    from ._7091 import GearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7092 import GearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7093 import GuideDxfModelAdvancedTimeSteppingAnalysisForModulation
    from ._7094 import (
        HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7095 import HypoidGearAdvancedTimeSteppingAnalysisForModulation
    from ._7096 import HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7097 import HypoidGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7098 import (
        InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7099 import (
        KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7100 import (
        KlingelnbergCycloPalloidConicalGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7101 import (
        KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7102 import (
        KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7103 import (
        KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7104 import (
        KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7105 import (
        KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7106 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7107 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7108 import MassDiscAdvancedTimeSteppingAnalysisForModulation
    from ._7109 import MeasurementComponentAdvancedTimeSteppingAnalysisForModulation
    from ._7110 import MountableComponentAdvancedTimeSteppingAnalysisForModulation
    from ._7111 import OilSealAdvancedTimeSteppingAnalysisForModulation
    from ._7112 import PartAdvancedTimeSteppingAnalysisForModulation
    from ._7113 import PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation
    from ._7114 import (
        PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7115 import (
        PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7116 import PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7117 import PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7118 import PlanetCarrierAdvancedTimeSteppingAnalysisForModulation
    from ._7119 import PointLoadAdvancedTimeSteppingAnalysisForModulation
    from ._7120 import PowerLoadAdvancedTimeSteppingAnalysisForModulation
    from ._7121 import PulleyAdvancedTimeSteppingAnalysisForModulation
    from ._7122 import RingPinsAdvancedTimeSteppingAnalysisForModulation
    from ._7123 import RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7124 import RollingRingAdvancedTimeSteppingAnalysisForModulation
    from ._7125 import RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7126 import RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7127 import RootAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7128 import ShaftAdvancedTimeSteppingAnalysisForModulation
    from ._7129 import ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7130 import (
        ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7131 import SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7132 import SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation
    from ._7133 import SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7134 import SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7135 import SpringDamperAdvancedTimeSteppingAnalysisForModulation
    from ._7136 import SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7137 import SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7138 import StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation
    from ._7139 import (
        StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7140 import StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7141 import StraightBevelGearAdvancedTimeSteppingAnalysisForModulation
    from ._7142 import StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7143 import StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7144 import StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation
    from ._7145 import StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation
    from ._7146 import SynchroniserAdvancedTimeSteppingAnalysisForModulation
    from ._7147 import SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7148 import SynchroniserPartAdvancedTimeSteppingAnalysisForModulation
    from ._7149 import SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation
    from ._7150 import TorqueConverterAdvancedTimeSteppingAnalysisForModulation
    from ._7151 import (
        TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7152 import TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation
    from ._7153 import TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation
    from ._7154 import UnbalancedMassAdvancedTimeSteppingAnalysisForModulation
    from ._7155 import VirtualComponentAdvancedTimeSteppingAnalysisForModulation
    from ._7156 import WormGearAdvancedTimeSteppingAnalysisForModulation
    from ._7157 import WormGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7158 import WormGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7159 import ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation
    from ._7160 import ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7161 import ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation
else:
    import_structure = {
        "_7027": ["AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7028": ["AbstractShaftAdvancedTimeSteppingAnalysisForModulation"],
        "_7029": ["AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation"],
        "_7030": [
            "AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7031": ["AdvancedTimeSteppingAnalysisForModulation"],
        "_7032": ["AtsamExcitationsOrOthers"],
        "_7033": ["AtsamNaturalFrequencyViewOption"],
        "_7034": ["AdvancedTimeSteppingAnalysisForModulationOptions"],
        "_7035": ["AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7036": [
            "AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7037": ["AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7038": ["AssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7039": ["ATSAMResultsVsLargeTimeStepSettings"],
        "_7040": ["BearingAdvancedTimeSteppingAnalysisForModulation"],
        "_7041": ["BeltConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7042": ["BeltDriveAdvancedTimeSteppingAnalysisForModulation"],
        "_7043": ["BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7044": ["BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7045": ["BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7046": [
            "BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7047": ["BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7048": ["BevelGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7049": ["BevelGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7050": ["BevelGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7051": ["BoltAdvancedTimeSteppingAnalysisForModulation"],
        "_7052": ["BoltedJointAdvancedTimeSteppingAnalysisForModulation"],
        "_7053": ["ClutchAdvancedTimeSteppingAnalysisForModulation"],
        "_7054": ["ClutchConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7055": ["ClutchHalfAdvancedTimeSteppingAnalysisForModulation"],
        "_7056": ["CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7057": ["ComponentAdvancedTimeSteppingAnalysisForModulation"],
        "_7058": ["ConceptCouplingAdvancedTimeSteppingAnalysisForModulation"],
        "_7059": ["ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7060": ["ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation"],
        "_7061": ["ConceptGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7062": ["ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7063": ["ConceptGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7064": ["ConicalGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7065": ["ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7066": ["ConicalGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7067": ["ConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7068": ["ConnectorAdvancedTimeSteppingAnalysisForModulation"],
        "_7069": ["CouplingAdvancedTimeSteppingAnalysisForModulation"],
        "_7070": ["CouplingConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7071": ["CouplingHalfAdvancedTimeSteppingAnalysisForModulation"],
        "_7072": ["CVTAdvancedTimeSteppingAnalysisForModulation"],
        "_7073": ["CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7074": ["CVTPulleyAdvancedTimeSteppingAnalysisForModulation"],
        "_7075": ["CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7076": ["CycloidalDiscAdvancedTimeSteppingAnalysisForModulation"],
        "_7077": [
            "CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7078": [
            "CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7079": ["CylindricalGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7080": ["CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7081": ["CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7082": ["CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7083": ["DatumAdvancedTimeSteppingAnalysisForModulation"],
        "_7084": ["ExternalCADModelAdvancedTimeSteppingAnalysisForModulation"],
        "_7085": ["FaceGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7086": ["FaceGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7087": ["FaceGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7088": ["FEPartAdvancedTimeSteppingAnalysisForModulation"],
        "_7089": ["FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7090": ["GearAdvancedTimeSteppingAnalysisForModulation"],
        "_7091": ["GearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7092": ["GearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7093": ["GuideDxfModelAdvancedTimeSteppingAnalysisForModulation"],
        "_7094": [
            "HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7095": ["HypoidGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7096": ["HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7097": ["HypoidGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7098": [
            "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7099": [
            "KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7100": [
            "KlingelnbergCycloPalloidConicalGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7101": [
            "KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7102": [
            "KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7103": [
            "KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7104": [
            "KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7105": [
            "KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7106": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7107": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7108": ["MassDiscAdvancedTimeSteppingAnalysisForModulation"],
        "_7109": ["MeasurementComponentAdvancedTimeSteppingAnalysisForModulation"],
        "_7110": ["MountableComponentAdvancedTimeSteppingAnalysisForModulation"],
        "_7111": ["OilSealAdvancedTimeSteppingAnalysisForModulation"],
        "_7112": ["PartAdvancedTimeSteppingAnalysisForModulation"],
        "_7113": ["PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation"],
        "_7114": [
            "PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7115": [
            "PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7116": ["PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7117": ["PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7118": ["PlanetCarrierAdvancedTimeSteppingAnalysisForModulation"],
        "_7119": ["PointLoadAdvancedTimeSteppingAnalysisForModulation"],
        "_7120": ["PowerLoadAdvancedTimeSteppingAnalysisForModulation"],
        "_7121": ["PulleyAdvancedTimeSteppingAnalysisForModulation"],
        "_7122": ["RingPinsAdvancedTimeSteppingAnalysisForModulation"],
        "_7123": ["RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7124": ["RollingRingAdvancedTimeSteppingAnalysisForModulation"],
        "_7125": ["RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7126": ["RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7127": ["RootAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7128": ["ShaftAdvancedTimeSteppingAnalysisForModulation"],
        "_7129": ["ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7130": [
            "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7131": ["SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7132": ["SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7133": ["SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7134": ["SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7135": ["SpringDamperAdvancedTimeSteppingAnalysisForModulation"],
        "_7136": ["SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7137": ["SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation"],
        "_7138": ["StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7139": ["StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7140": ["StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7141": ["StraightBevelGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7142": ["StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7143": ["StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7144": ["StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7145": ["StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7146": ["SynchroniserAdvancedTimeSteppingAnalysisForModulation"],
        "_7147": ["SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation"],
        "_7148": ["SynchroniserPartAdvancedTimeSteppingAnalysisForModulation"],
        "_7149": ["SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation"],
        "_7150": ["TorqueConverterAdvancedTimeSteppingAnalysisForModulation"],
        "_7151": ["TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7152": ["TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation"],
        "_7153": ["TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation"],
        "_7154": ["UnbalancedMassAdvancedTimeSteppingAnalysisForModulation"],
        "_7155": ["VirtualComponentAdvancedTimeSteppingAnalysisForModulation"],
        "_7156": ["WormGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7157": ["WormGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7158": ["WormGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7159": ["ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7160": ["ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7161": ["ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
    "AbstractShaftAdvancedTimeSteppingAnalysisForModulation",
    "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
    "AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
    "AdvancedTimeSteppingAnalysisForModulation",
    "AtsamExcitationsOrOthers",
    "AtsamNaturalFrequencyViewOption",
    "AdvancedTimeSteppingAnalysisForModulationOptions",
    "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
    "AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
    "AssemblyAdvancedTimeSteppingAnalysisForModulation",
    "ATSAMResultsVsLargeTimeStepSettings",
    "BearingAdvancedTimeSteppingAnalysisForModulation",
    "BeltConnectionAdvancedTimeSteppingAnalysisForModulation",
    "BeltDriveAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
    "BevelGearAdvancedTimeSteppingAnalysisForModulation",
    "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "BevelGearSetAdvancedTimeSteppingAnalysisForModulation",
    "BoltAdvancedTimeSteppingAnalysisForModulation",
    "BoltedJointAdvancedTimeSteppingAnalysisForModulation",
    "ClutchAdvancedTimeSteppingAnalysisForModulation",
    "ClutchConnectionAdvancedTimeSteppingAnalysisForModulation",
    "ClutchHalfAdvancedTimeSteppingAnalysisForModulation",
    "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",
    "ComponentAdvancedTimeSteppingAnalysisForModulation",
    "ConceptCouplingAdvancedTimeSteppingAnalysisForModulation",
    "ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
    "ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation",
    "ConceptGearAdvancedTimeSteppingAnalysisForModulation",
    "ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "ConceptGearSetAdvancedTimeSteppingAnalysisForModulation",
    "ConicalGearAdvancedTimeSteppingAnalysisForModulation",
    "ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
    "ConnectionAdvancedTimeSteppingAnalysisForModulation",
    "ConnectorAdvancedTimeSteppingAnalysisForModulation",
    "CouplingAdvancedTimeSteppingAnalysisForModulation",
    "CouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
    "CouplingHalfAdvancedTimeSteppingAnalysisForModulation",
    "CVTAdvancedTimeSteppingAnalysisForModulation",
    "CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation",
    "CVTPulleyAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalDiscAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalGearAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation",
    "DatumAdvancedTimeSteppingAnalysisForModulation",
    "ExternalCADModelAdvancedTimeSteppingAnalysisForModulation",
    "FaceGearAdvancedTimeSteppingAnalysisForModulation",
    "FaceGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "FaceGearSetAdvancedTimeSteppingAnalysisForModulation",
    "FEPartAdvancedTimeSteppingAnalysisForModulation",
    "FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation",
    "GearAdvancedTimeSteppingAnalysisForModulation",
    "GearMeshAdvancedTimeSteppingAnalysisForModulation",
    "GearSetAdvancedTimeSteppingAnalysisForModulation",
    "GuideDxfModelAdvancedTimeSteppingAnalysisForModulation",
    "HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation",
    "HypoidGearAdvancedTimeSteppingAnalysisForModulation",
    "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "HypoidGearSetAdvancedTimeSteppingAnalysisForModulation",
    "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidConicalGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
    "MassDiscAdvancedTimeSteppingAnalysisForModulation",
    "MeasurementComponentAdvancedTimeSteppingAnalysisForModulation",
    "MountableComponentAdvancedTimeSteppingAnalysisForModulation",
    "OilSealAdvancedTimeSteppingAnalysisForModulation",
    "PartAdvancedTimeSteppingAnalysisForModulation",
    "PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation",
    "PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
    "PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation",
    "PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation",
    "PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation",
    "PlanetCarrierAdvancedTimeSteppingAnalysisForModulation",
    "PointLoadAdvancedTimeSteppingAnalysisForModulation",
    "PowerLoadAdvancedTimeSteppingAnalysisForModulation",
    "PulleyAdvancedTimeSteppingAnalysisForModulation",
    "RingPinsAdvancedTimeSteppingAnalysisForModulation",
    "RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation",
    "RollingRingAdvancedTimeSteppingAnalysisForModulation",
    "RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation",
    "RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation",
    "RootAssemblyAdvancedTimeSteppingAnalysisForModulation",
    "ShaftAdvancedTimeSteppingAnalysisForModulation",
    "ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation",
    "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
    "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
    "SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation",
    "SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
    "SpringDamperAdvancedTimeSteppingAnalysisForModulation",
    "SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation",
    "SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelGearAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserPartAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation",
    "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",
    "VirtualComponentAdvancedTimeSteppingAnalysisForModulation",
    "WormGearAdvancedTimeSteppingAnalysisForModulation",
    "WormGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "WormGearSetAdvancedTimeSteppingAnalysisForModulation",
    "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
    "ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
)
