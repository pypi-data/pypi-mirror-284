"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7162 import AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7163 import AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7164 import (
        AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7165 import (
        AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7166 import (
        AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7167 import (
        AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7168 import (
        AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7169 import AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7170 import BearingCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7171 import BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7172 import BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7173 import (
        BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7174 import (
        BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7175 import (
        BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7176 import (
        BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7177 import (
        BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7178 import BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7179 import BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7180 import BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7181 import BoltCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7182 import BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7183 import ClutchCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7184 import ClutchConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7185 import ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7186 import (
        CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7187 import ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7188 import ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7189 import (
        ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7190 import (
        ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7191 import ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7192 import ConceptGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7193 import ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7194 import ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7195 import ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7196 import ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7197 import ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7198 import ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7199 import CouplingCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7200 import (
        CouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7201 import CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7202 import (
        CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7203 import CVTCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7204 import CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7205 import (
        CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7206 import (
        CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7207 import CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7208 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7209 import CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7210 import (
        CylindricalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7211 import (
        CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7212 import (
        CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7213 import DatumCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7214 import ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7215 import FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7216 import FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7217 import FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7218 import FEPartCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7219 import (
        FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7220 import GearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7221 import GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7222 import GearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7223 import GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7224 import HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7225 import HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7226 import HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7227 import (
        InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7228 import (
        KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7229 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7230 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7231 import (
        KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7232 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7233 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7234 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7235 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7236 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7237 import MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7238 import (
        MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7239 import (
        MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7240 import OilSealCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7241 import PartCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7242 import (
        PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7243 import (
        PartToPartShearCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7244 import (
        PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7245 import (
        PlanetaryConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7246 import PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7247 import PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7248 import PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7249 import PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7250 import PulleyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7251 import RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7252 import (
        RingPinsToDiscConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7253 import (
        RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7254 import RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7255 import (
        RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7256 import RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7257 import ShaftCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7258 import (
        ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7259 import (
        ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7260 import (
        SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7261 import SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7262 import (
        SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7263 import (
        SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7264 import SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7265 import (
        SpringDamperConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7266 import SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7267 import (
        StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7268 import (
        StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7269 import (
        StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7270 import (
        StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7271 import (
        StraightBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7272 import (
        StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7273 import (
        StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7274 import (
        StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7275 import SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7276 import SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7277 import SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7278 import (
        SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7279 import TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7280 import (
        TorqueConverterConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7281 import (
        TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7282 import (
        TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7283 import UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7284 import VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7285 import WormGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7286 import WormGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7287 import WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7288 import ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7289 import (
        ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7290 import (
        ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
else:
    import_structure = {
        "_7162": ["AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7163": ["AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7164": [
            "AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7165": [
            "AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7166": [
            "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7167": [
            "AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7168": [
            "AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7169": ["AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7170": ["BearingCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7171": ["BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7172": ["BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7173": [
            "BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7174": [
            "BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7175": [
            "BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7176": [
            "BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7177": [
            "BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7178": ["BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7179": ["BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7180": ["BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7181": ["BoltCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7182": ["BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7183": ["ClutchCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7184": ["ClutchConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7185": ["ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7186": ["CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7187": ["ComponentCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7188": ["ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7189": [
            "ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7190": [
            "ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7191": ["ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7192": ["ConceptGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7193": ["ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7194": ["ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7195": ["ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7196": ["ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7197": ["ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7198": ["ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7199": ["CouplingCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7200": [
            "CouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7201": ["CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7202": ["CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7203": ["CVTCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7204": ["CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7205": ["CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7206": [
            "CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7207": ["CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7208": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7209": ["CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7210": [
            "CylindricalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7211": [
            "CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7212": [
            "CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7213": ["DatumCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7214": ["ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7215": ["FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7216": ["FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7217": ["FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7218": ["FEPartCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7219": [
            "FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7220": ["GearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7221": ["GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7222": ["GearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7223": ["GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7224": ["HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7225": ["HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7226": ["HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7227": [
            "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7228": [
            "KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7229": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7230": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7231": [
            "KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7232": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7233": [
            "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7234": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7235": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7236": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7237": ["MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7238": [
            "MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7239": [
            "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7240": ["OilSealCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7241": ["PartCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7242": [
            "PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7243": [
            "PartToPartShearCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7244": [
            "PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7245": [
            "PlanetaryConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7246": ["PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7247": ["PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7248": ["PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7249": ["PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7250": ["PulleyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7251": ["RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7252": [
            "RingPinsToDiscConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7253": [
            "RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7254": ["RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7255": [
            "RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7256": ["RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7257": ["ShaftCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7258": [
            "ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7259": [
            "ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7260": [
            "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7261": ["SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7262": [
            "SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7263": [
            "SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7264": ["SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7265": [
            "SpringDamperConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7266": ["SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7267": [
            "StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7268": [
            "StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7269": [
            "StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7270": ["StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7271": [
            "StraightBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7272": [
            "StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7273": [
            "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7274": [
            "StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7275": ["SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7276": ["SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7277": ["SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7278": [
            "SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7279": ["TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7280": [
            "TorqueConverterConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7281": [
            "TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7282": [
            "TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7283": ["UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7284": ["VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7285": ["WormGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7286": ["WormGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7287": ["WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7288": ["ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7289": [
            "ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7290": ["ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BearingCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BoltCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ClutchCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ClutchConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConceptGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CVTCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "DatumCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation",
    "FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "FEPartCompoundAdvancedTimeSteppingAnalysisForModulation",
    "FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "GearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "GearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation",
    "HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation",
    "MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
    "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
    "OilSealCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PartCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PartToPartShearCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PlanetaryConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PulleyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation",
    "RingPinsToDiscConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation",
    "RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ShaftCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpringDamperConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation",
    "UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation",
    "VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
    "WormGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "WormGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
)
