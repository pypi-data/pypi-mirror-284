"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5138 import AbstractAssemblyModalAnalysisAtASpeed
    from ._5139 import AbstractShaftModalAnalysisAtASpeed
    from ._5140 import AbstractShaftOrHousingModalAnalysisAtASpeed
    from ._5141 import AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed
    from ._5142 import AGMAGleasonConicalGearMeshModalAnalysisAtASpeed
    from ._5143 import AGMAGleasonConicalGearModalAnalysisAtASpeed
    from ._5144 import AGMAGleasonConicalGearSetModalAnalysisAtASpeed
    from ._5145 import AssemblyModalAnalysisAtASpeed
    from ._5146 import BearingModalAnalysisAtASpeed
    from ._5147 import BeltConnectionModalAnalysisAtASpeed
    from ._5148 import BeltDriveModalAnalysisAtASpeed
    from ._5149 import BevelDifferentialGearMeshModalAnalysisAtASpeed
    from ._5150 import BevelDifferentialGearModalAnalysisAtASpeed
    from ._5151 import BevelDifferentialGearSetModalAnalysisAtASpeed
    from ._5152 import BevelDifferentialPlanetGearModalAnalysisAtASpeed
    from ._5153 import BevelDifferentialSunGearModalAnalysisAtASpeed
    from ._5154 import BevelGearMeshModalAnalysisAtASpeed
    from ._5155 import BevelGearModalAnalysisAtASpeed
    from ._5156 import BevelGearSetModalAnalysisAtASpeed
    from ._5157 import BoltedJointModalAnalysisAtASpeed
    from ._5158 import BoltModalAnalysisAtASpeed
    from ._5159 import ClutchConnectionModalAnalysisAtASpeed
    from ._5160 import ClutchHalfModalAnalysisAtASpeed
    from ._5161 import ClutchModalAnalysisAtASpeed
    from ._5162 import CoaxialConnectionModalAnalysisAtASpeed
    from ._5163 import ComponentModalAnalysisAtASpeed
    from ._5164 import ConceptCouplingConnectionModalAnalysisAtASpeed
    from ._5165 import ConceptCouplingHalfModalAnalysisAtASpeed
    from ._5166 import ConceptCouplingModalAnalysisAtASpeed
    from ._5167 import ConceptGearMeshModalAnalysisAtASpeed
    from ._5168 import ConceptGearModalAnalysisAtASpeed
    from ._5169 import ConceptGearSetModalAnalysisAtASpeed
    from ._5170 import ConicalGearMeshModalAnalysisAtASpeed
    from ._5171 import ConicalGearModalAnalysisAtASpeed
    from ._5172 import ConicalGearSetModalAnalysisAtASpeed
    from ._5173 import ConnectionModalAnalysisAtASpeed
    from ._5174 import ConnectorModalAnalysisAtASpeed
    from ._5175 import CouplingConnectionModalAnalysisAtASpeed
    from ._5176 import CouplingHalfModalAnalysisAtASpeed
    from ._5177 import CouplingModalAnalysisAtASpeed
    from ._5178 import CVTBeltConnectionModalAnalysisAtASpeed
    from ._5179 import CVTModalAnalysisAtASpeed
    from ._5180 import CVTPulleyModalAnalysisAtASpeed
    from ._5181 import CycloidalAssemblyModalAnalysisAtASpeed
    from ._5182 import CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed
    from ._5183 import CycloidalDiscModalAnalysisAtASpeed
    from ._5184 import CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed
    from ._5185 import CylindricalGearMeshModalAnalysisAtASpeed
    from ._5186 import CylindricalGearModalAnalysisAtASpeed
    from ._5187 import CylindricalGearSetModalAnalysisAtASpeed
    from ._5188 import CylindricalPlanetGearModalAnalysisAtASpeed
    from ._5189 import DatumModalAnalysisAtASpeed
    from ._5190 import ExternalCADModelModalAnalysisAtASpeed
    from ._5191 import FaceGearMeshModalAnalysisAtASpeed
    from ._5192 import FaceGearModalAnalysisAtASpeed
    from ._5193 import FaceGearSetModalAnalysisAtASpeed
    from ._5194 import FEPartModalAnalysisAtASpeed
    from ._5195 import FlexiblePinAssemblyModalAnalysisAtASpeed
    from ._5196 import GearMeshModalAnalysisAtASpeed
    from ._5197 import GearModalAnalysisAtASpeed
    from ._5198 import GearSetModalAnalysisAtASpeed
    from ._5199 import GuideDxfModelModalAnalysisAtASpeed
    from ._5200 import HypoidGearMeshModalAnalysisAtASpeed
    from ._5201 import HypoidGearModalAnalysisAtASpeed
    from ._5202 import HypoidGearSetModalAnalysisAtASpeed
    from ._5203 import InterMountableComponentConnectionModalAnalysisAtASpeed
    from ._5204 import KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed
    from ._5205 import KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed
    from ._5206 import KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed
    from ._5207 import KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed
    from ._5208 import KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed
    from ._5209 import KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed
    from ._5210 import KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed
    from ._5211 import KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed
    from ._5212 import KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed
    from ._5213 import MassDiscModalAnalysisAtASpeed
    from ._5214 import MeasurementComponentModalAnalysisAtASpeed
    from ._5215 import ModalAnalysisAtASpeed
    from ._5216 import MountableComponentModalAnalysisAtASpeed
    from ._5217 import OilSealModalAnalysisAtASpeed
    from ._5218 import PartModalAnalysisAtASpeed
    from ._5219 import PartToPartShearCouplingConnectionModalAnalysisAtASpeed
    from ._5220 import PartToPartShearCouplingHalfModalAnalysisAtASpeed
    from ._5221 import PartToPartShearCouplingModalAnalysisAtASpeed
    from ._5222 import PlanetaryConnectionModalAnalysisAtASpeed
    from ._5223 import PlanetaryGearSetModalAnalysisAtASpeed
    from ._5224 import PlanetCarrierModalAnalysisAtASpeed
    from ._5225 import PointLoadModalAnalysisAtASpeed
    from ._5226 import PowerLoadModalAnalysisAtASpeed
    from ._5227 import PulleyModalAnalysisAtASpeed
    from ._5228 import RingPinsModalAnalysisAtASpeed
    from ._5229 import RingPinsToDiscConnectionModalAnalysisAtASpeed
    from ._5230 import RollingRingAssemblyModalAnalysisAtASpeed
    from ._5231 import RollingRingConnectionModalAnalysisAtASpeed
    from ._5232 import RollingRingModalAnalysisAtASpeed
    from ._5233 import RootAssemblyModalAnalysisAtASpeed
    from ._5234 import ShaftHubConnectionModalAnalysisAtASpeed
    from ._5235 import ShaftModalAnalysisAtASpeed
    from ._5236 import ShaftToMountableComponentConnectionModalAnalysisAtASpeed
    from ._5237 import SpecialisedAssemblyModalAnalysisAtASpeed
    from ._5238 import SpiralBevelGearMeshModalAnalysisAtASpeed
    from ._5239 import SpiralBevelGearModalAnalysisAtASpeed
    from ._5240 import SpiralBevelGearSetModalAnalysisAtASpeed
    from ._5241 import SpringDamperConnectionModalAnalysisAtASpeed
    from ._5242 import SpringDamperHalfModalAnalysisAtASpeed
    from ._5243 import SpringDamperModalAnalysisAtASpeed
    from ._5244 import StraightBevelDiffGearMeshModalAnalysisAtASpeed
    from ._5245 import StraightBevelDiffGearModalAnalysisAtASpeed
    from ._5246 import StraightBevelDiffGearSetModalAnalysisAtASpeed
    from ._5247 import StraightBevelGearMeshModalAnalysisAtASpeed
    from ._5248 import StraightBevelGearModalAnalysisAtASpeed
    from ._5249 import StraightBevelGearSetModalAnalysisAtASpeed
    from ._5250 import StraightBevelPlanetGearModalAnalysisAtASpeed
    from ._5251 import StraightBevelSunGearModalAnalysisAtASpeed
    from ._5252 import SynchroniserHalfModalAnalysisAtASpeed
    from ._5253 import SynchroniserModalAnalysisAtASpeed
    from ._5254 import SynchroniserPartModalAnalysisAtASpeed
    from ._5255 import SynchroniserSleeveModalAnalysisAtASpeed
    from ._5256 import TorqueConverterConnectionModalAnalysisAtASpeed
    from ._5257 import TorqueConverterModalAnalysisAtASpeed
    from ._5258 import TorqueConverterPumpModalAnalysisAtASpeed
    from ._5259 import TorqueConverterTurbineModalAnalysisAtASpeed
    from ._5260 import UnbalancedMassModalAnalysisAtASpeed
    from ._5261 import VirtualComponentModalAnalysisAtASpeed
    from ._5262 import WormGearMeshModalAnalysisAtASpeed
    from ._5263 import WormGearModalAnalysisAtASpeed
    from ._5264 import WormGearSetModalAnalysisAtASpeed
    from ._5265 import ZerolBevelGearMeshModalAnalysisAtASpeed
    from ._5266 import ZerolBevelGearModalAnalysisAtASpeed
    from ._5267 import ZerolBevelGearSetModalAnalysisAtASpeed
else:
    import_structure = {
        "_5138": ["AbstractAssemblyModalAnalysisAtASpeed"],
        "_5139": ["AbstractShaftModalAnalysisAtASpeed"],
        "_5140": ["AbstractShaftOrHousingModalAnalysisAtASpeed"],
        "_5141": ["AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed"],
        "_5142": ["AGMAGleasonConicalGearMeshModalAnalysisAtASpeed"],
        "_5143": ["AGMAGleasonConicalGearModalAnalysisAtASpeed"],
        "_5144": ["AGMAGleasonConicalGearSetModalAnalysisAtASpeed"],
        "_5145": ["AssemblyModalAnalysisAtASpeed"],
        "_5146": ["BearingModalAnalysisAtASpeed"],
        "_5147": ["BeltConnectionModalAnalysisAtASpeed"],
        "_5148": ["BeltDriveModalAnalysisAtASpeed"],
        "_5149": ["BevelDifferentialGearMeshModalAnalysisAtASpeed"],
        "_5150": ["BevelDifferentialGearModalAnalysisAtASpeed"],
        "_5151": ["BevelDifferentialGearSetModalAnalysisAtASpeed"],
        "_5152": ["BevelDifferentialPlanetGearModalAnalysisAtASpeed"],
        "_5153": ["BevelDifferentialSunGearModalAnalysisAtASpeed"],
        "_5154": ["BevelGearMeshModalAnalysisAtASpeed"],
        "_5155": ["BevelGearModalAnalysisAtASpeed"],
        "_5156": ["BevelGearSetModalAnalysisAtASpeed"],
        "_5157": ["BoltedJointModalAnalysisAtASpeed"],
        "_5158": ["BoltModalAnalysisAtASpeed"],
        "_5159": ["ClutchConnectionModalAnalysisAtASpeed"],
        "_5160": ["ClutchHalfModalAnalysisAtASpeed"],
        "_5161": ["ClutchModalAnalysisAtASpeed"],
        "_5162": ["CoaxialConnectionModalAnalysisAtASpeed"],
        "_5163": ["ComponentModalAnalysisAtASpeed"],
        "_5164": ["ConceptCouplingConnectionModalAnalysisAtASpeed"],
        "_5165": ["ConceptCouplingHalfModalAnalysisAtASpeed"],
        "_5166": ["ConceptCouplingModalAnalysisAtASpeed"],
        "_5167": ["ConceptGearMeshModalAnalysisAtASpeed"],
        "_5168": ["ConceptGearModalAnalysisAtASpeed"],
        "_5169": ["ConceptGearSetModalAnalysisAtASpeed"],
        "_5170": ["ConicalGearMeshModalAnalysisAtASpeed"],
        "_5171": ["ConicalGearModalAnalysisAtASpeed"],
        "_5172": ["ConicalGearSetModalAnalysisAtASpeed"],
        "_5173": ["ConnectionModalAnalysisAtASpeed"],
        "_5174": ["ConnectorModalAnalysisAtASpeed"],
        "_5175": ["CouplingConnectionModalAnalysisAtASpeed"],
        "_5176": ["CouplingHalfModalAnalysisAtASpeed"],
        "_5177": ["CouplingModalAnalysisAtASpeed"],
        "_5178": ["CVTBeltConnectionModalAnalysisAtASpeed"],
        "_5179": ["CVTModalAnalysisAtASpeed"],
        "_5180": ["CVTPulleyModalAnalysisAtASpeed"],
        "_5181": ["CycloidalAssemblyModalAnalysisAtASpeed"],
        "_5182": ["CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed"],
        "_5183": ["CycloidalDiscModalAnalysisAtASpeed"],
        "_5184": ["CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed"],
        "_5185": ["CylindricalGearMeshModalAnalysisAtASpeed"],
        "_5186": ["CylindricalGearModalAnalysisAtASpeed"],
        "_5187": ["CylindricalGearSetModalAnalysisAtASpeed"],
        "_5188": ["CylindricalPlanetGearModalAnalysisAtASpeed"],
        "_5189": ["DatumModalAnalysisAtASpeed"],
        "_5190": ["ExternalCADModelModalAnalysisAtASpeed"],
        "_5191": ["FaceGearMeshModalAnalysisAtASpeed"],
        "_5192": ["FaceGearModalAnalysisAtASpeed"],
        "_5193": ["FaceGearSetModalAnalysisAtASpeed"],
        "_5194": ["FEPartModalAnalysisAtASpeed"],
        "_5195": ["FlexiblePinAssemblyModalAnalysisAtASpeed"],
        "_5196": ["GearMeshModalAnalysisAtASpeed"],
        "_5197": ["GearModalAnalysisAtASpeed"],
        "_5198": ["GearSetModalAnalysisAtASpeed"],
        "_5199": ["GuideDxfModelModalAnalysisAtASpeed"],
        "_5200": ["HypoidGearMeshModalAnalysisAtASpeed"],
        "_5201": ["HypoidGearModalAnalysisAtASpeed"],
        "_5202": ["HypoidGearSetModalAnalysisAtASpeed"],
        "_5203": ["InterMountableComponentConnectionModalAnalysisAtASpeed"],
        "_5204": ["KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed"],
        "_5205": ["KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed"],
        "_5206": ["KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed"],
        "_5207": ["KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed"],
        "_5208": ["KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed"],
        "_5209": ["KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed"],
        "_5210": ["KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed"],
        "_5211": ["KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed"],
        "_5212": ["KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed"],
        "_5213": ["MassDiscModalAnalysisAtASpeed"],
        "_5214": ["MeasurementComponentModalAnalysisAtASpeed"],
        "_5215": ["ModalAnalysisAtASpeed"],
        "_5216": ["MountableComponentModalAnalysisAtASpeed"],
        "_5217": ["OilSealModalAnalysisAtASpeed"],
        "_5218": ["PartModalAnalysisAtASpeed"],
        "_5219": ["PartToPartShearCouplingConnectionModalAnalysisAtASpeed"],
        "_5220": ["PartToPartShearCouplingHalfModalAnalysisAtASpeed"],
        "_5221": ["PartToPartShearCouplingModalAnalysisAtASpeed"],
        "_5222": ["PlanetaryConnectionModalAnalysisAtASpeed"],
        "_5223": ["PlanetaryGearSetModalAnalysisAtASpeed"],
        "_5224": ["PlanetCarrierModalAnalysisAtASpeed"],
        "_5225": ["PointLoadModalAnalysisAtASpeed"],
        "_5226": ["PowerLoadModalAnalysisAtASpeed"],
        "_5227": ["PulleyModalAnalysisAtASpeed"],
        "_5228": ["RingPinsModalAnalysisAtASpeed"],
        "_5229": ["RingPinsToDiscConnectionModalAnalysisAtASpeed"],
        "_5230": ["RollingRingAssemblyModalAnalysisAtASpeed"],
        "_5231": ["RollingRingConnectionModalAnalysisAtASpeed"],
        "_5232": ["RollingRingModalAnalysisAtASpeed"],
        "_5233": ["RootAssemblyModalAnalysisAtASpeed"],
        "_5234": ["ShaftHubConnectionModalAnalysisAtASpeed"],
        "_5235": ["ShaftModalAnalysisAtASpeed"],
        "_5236": ["ShaftToMountableComponentConnectionModalAnalysisAtASpeed"],
        "_5237": ["SpecialisedAssemblyModalAnalysisAtASpeed"],
        "_5238": ["SpiralBevelGearMeshModalAnalysisAtASpeed"],
        "_5239": ["SpiralBevelGearModalAnalysisAtASpeed"],
        "_5240": ["SpiralBevelGearSetModalAnalysisAtASpeed"],
        "_5241": ["SpringDamperConnectionModalAnalysisAtASpeed"],
        "_5242": ["SpringDamperHalfModalAnalysisAtASpeed"],
        "_5243": ["SpringDamperModalAnalysisAtASpeed"],
        "_5244": ["StraightBevelDiffGearMeshModalAnalysisAtASpeed"],
        "_5245": ["StraightBevelDiffGearModalAnalysisAtASpeed"],
        "_5246": ["StraightBevelDiffGearSetModalAnalysisAtASpeed"],
        "_5247": ["StraightBevelGearMeshModalAnalysisAtASpeed"],
        "_5248": ["StraightBevelGearModalAnalysisAtASpeed"],
        "_5249": ["StraightBevelGearSetModalAnalysisAtASpeed"],
        "_5250": ["StraightBevelPlanetGearModalAnalysisAtASpeed"],
        "_5251": ["StraightBevelSunGearModalAnalysisAtASpeed"],
        "_5252": ["SynchroniserHalfModalAnalysisAtASpeed"],
        "_5253": ["SynchroniserModalAnalysisAtASpeed"],
        "_5254": ["SynchroniserPartModalAnalysisAtASpeed"],
        "_5255": ["SynchroniserSleeveModalAnalysisAtASpeed"],
        "_5256": ["TorqueConverterConnectionModalAnalysisAtASpeed"],
        "_5257": ["TorqueConverterModalAnalysisAtASpeed"],
        "_5258": ["TorqueConverterPumpModalAnalysisAtASpeed"],
        "_5259": ["TorqueConverterTurbineModalAnalysisAtASpeed"],
        "_5260": ["UnbalancedMassModalAnalysisAtASpeed"],
        "_5261": ["VirtualComponentModalAnalysisAtASpeed"],
        "_5262": ["WormGearMeshModalAnalysisAtASpeed"],
        "_5263": ["WormGearModalAnalysisAtASpeed"],
        "_5264": ["WormGearSetModalAnalysisAtASpeed"],
        "_5265": ["ZerolBevelGearMeshModalAnalysisAtASpeed"],
        "_5266": ["ZerolBevelGearModalAnalysisAtASpeed"],
        "_5267": ["ZerolBevelGearSetModalAnalysisAtASpeed"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyModalAnalysisAtASpeed",
    "AbstractShaftModalAnalysisAtASpeed",
    "AbstractShaftOrHousingModalAnalysisAtASpeed",
    "AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed",
    "AGMAGleasonConicalGearMeshModalAnalysisAtASpeed",
    "AGMAGleasonConicalGearModalAnalysisAtASpeed",
    "AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
    "AssemblyModalAnalysisAtASpeed",
    "BearingModalAnalysisAtASpeed",
    "BeltConnectionModalAnalysisAtASpeed",
    "BeltDriveModalAnalysisAtASpeed",
    "BevelDifferentialGearMeshModalAnalysisAtASpeed",
    "BevelDifferentialGearModalAnalysisAtASpeed",
    "BevelDifferentialGearSetModalAnalysisAtASpeed",
    "BevelDifferentialPlanetGearModalAnalysisAtASpeed",
    "BevelDifferentialSunGearModalAnalysisAtASpeed",
    "BevelGearMeshModalAnalysisAtASpeed",
    "BevelGearModalAnalysisAtASpeed",
    "BevelGearSetModalAnalysisAtASpeed",
    "BoltedJointModalAnalysisAtASpeed",
    "BoltModalAnalysisAtASpeed",
    "ClutchConnectionModalAnalysisAtASpeed",
    "ClutchHalfModalAnalysisAtASpeed",
    "ClutchModalAnalysisAtASpeed",
    "CoaxialConnectionModalAnalysisAtASpeed",
    "ComponentModalAnalysisAtASpeed",
    "ConceptCouplingConnectionModalAnalysisAtASpeed",
    "ConceptCouplingHalfModalAnalysisAtASpeed",
    "ConceptCouplingModalAnalysisAtASpeed",
    "ConceptGearMeshModalAnalysisAtASpeed",
    "ConceptGearModalAnalysisAtASpeed",
    "ConceptGearSetModalAnalysisAtASpeed",
    "ConicalGearMeshModalAnalysisAtASpeed",
    "ConicalGearModalAnalysisAtASpeed",
    "ConicalGearSetModalAnalysisAtASpeed",
    "ConnectionModalAnalysisAtASpeed",
    "ConnectorModalAnalysisAtASpeed",
    "CouplingConnectionModalAnalysisAtASpeed",
    "CouplingHalfModalAnalysisAtASpeed",
    "CouplingModalAnalysisAtASpeed",
    "CVTBeltConnectionModalAnalysisAtASpeed",
    "CVTModalAnalysisAtASpeed",
    "CVTPulleyModalAnalysisAtASpeed",
    "CycloidalAssemblyModalAnalysisAtASpeed",
    "CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed",
    "CycloidalDiscModalAnalysisAtASpeed",
    "CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed",
    "CylindricalGearMeshModalAnalysisAtASpeed",
    "CylindricalGearModalAnalysisAtASpeed",
    "CylindricalGearSetModalAnalysisAtASpeed",
    "CylindricalPlanetGearModalAnalysisAtASpeed",
    "DatumModalAnalysisAtASpeed",
    "ExternalCADModelModalAnalysisAtASpeed",
    "FaceGearMeshModalAnalysisAtASpeed",
    "FaceGearModalAnalysisAtASpeed",
    "FaceGearSetModalAnalysisAtASpeed",
    "FEPartModalAnalysisAtASpeed",
    "FlexiblePinAssemblyModalAnalysisAtASpeed",
    "GearMeshModalAnalysisAtASpeed",
    "GearModalAnalysisAtASpeed",
    "GearSetModalAnalysisAtASpeed",
    "GuideDxfModelModalAnalysisAtASpeed",
    "HypoidGearMeshModalAnalysisAtASpeed",
    "HypoidGearModalAnalysisAtASpeed",
    "HypoidGearSetModalAnalysisAtASpeed",
    "InterMountableComponentConnectionModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed",
    "MassDiscModalAnalysisAtASpeed",
    "MeasurementComponentModalAnalysisAtASpeed",
    "ModalAnalysisAtASpeed",
    "MountableComponentModalAnalysisAtASpeed",
    "OilSealModalAnalysisAtASpeed",
    "PartModalAnalysisAtASpeed",
    "PartToPartShearCouplingConnectionModalAnalysisAtASpeed",
    "PartToPartShearCouplingHalfModalAnalysisAtASpeed",
    "PartToPartShearCouplingModalAnalysisAtASpeed",
    "PlanetaryConnectionModalAnalysisAtASpeed",
    "PlanetaryGearSetModalAnalysisAtASpeed",
    "PlanetCarrierModalAnalysisAtASpeed",
    "PointLoadModalAnalysisAtASpeed",
    "PowerLoadModalAnalysisAtASpeed",
    "PulleyModalAnalysisAtASpeed",
    "RingPinsModalAnalysisAtASpeed",
    "RingPinsToDiscConnectionModalAnalysisAtASpeed",
    "RollingRingAssemblyModalAnalysisAtASpeed",
    "RollingRingConnectionModalAnalysisAtASpeed",
    "RollingRingModalAnalysisAtASpeed",
    "RootAssemblyModalAnalysisAtASpeed",
    "ShaftHubConnectionModalAnalysisAtASpeed",
    "ShaftModalAnalysisAtASpeed",
    "ShaftToMountableComponentConnectionModalAnalysisAtASpeed",
    "SpecialisedAssemblyModalAnalysisAtASpeed",
    "SpiralBevelGearMeshModalAnalysisAtASpeed",
    "SpiralBevelGearModalAnalysisAtASpeed",
    "SpiralBevelGearSetModalAnalysisAtASpeed",
    "SpringDamperConnectionModalAnalysisAtASpeed",
    "SpringDamperHalfModalAnalysisAtASpeed",
    "SpringDamperModalAnalysisAtASpeed",
    "StraightBevelDiffGearMeshModalAnalysisAtASpeed",
    "StraightBevelDiffGearModalAnalysisAtASpeed",
    "StraightBevelDiffGearSetModalAnalysisAtASpeed",
    "StraightBevelGearMeshModalAnalysisAtASpeed",
    "StraightBevelGearModalAnalysisAtASpeed",
    "StraightBevelGearSetModalAnalysisAtASpeed",
    "StraightBevelPlanetGearModalAnalysisAtASpeed",
    "StraightBevelSunGearModalAnalysisAtASpeed",
    "SynchroniserHalfModalAnalysisAtASpeed",
    "SynchroniserModalAnalysisAtASpeed",
    "SynchroniserPartModalAnalysisAtASpeed",
    "SynchroniserSleeveModalAnalysisAtASpeed",
    "TorqueConverterConnectionModalAnalysisAtASpeed",
    "TorqueConverterModalAnalysisAtASpeed",
    "TorqueConverterPumpModalAnalysisAtASpeed",
    "TorqueConverterTurbineModalAnalysisAtASpeed",
    "UnbalancedMassModalAnalysisAtASpeed",
    "VirtualComponentModalAnalysisAtASpeed",
    "WormGearMeshModalAnalysisAtASpeed",
    "WormGearModalAnalysisAtASpeed",
    "WormGearSetModalAnalysisAtASpeed",
    "ZerolBevelGearMeshModalAnalysisAtASpeed",
    "ZerolBevelGearModalAnalysisAtASpeed",
    "ZerolBevelGearSetModalAnalysisAtASpeed",
)
