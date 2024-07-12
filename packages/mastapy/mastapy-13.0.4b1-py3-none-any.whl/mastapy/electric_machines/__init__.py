"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1261 import AbstractStator
    from ._1262 import AbstractToothAndSlot
    from ._1263 import CADConductor
    from ._1264 import CADElectricMachineDetail
    from ._1265 import CADMagnetDetails
    from ._1266 import CADMagnetsForLayer
    from ._1267 import CADRotor
    from ._1268 import CADStator
    from ._1269 import CADToothAndSlot
    from ._1270 import Coil
    from ._1271 import CoilPositionInSlot
    from ._1272 import CoolingDuctLayerSpecification
    from ._1273 import CoolingDuctShape
    from ._1274 import CoreLossBuildFactorSpecificationMethod
    from ._1275 import CoreLossCoefficients
    from ._1276 import DoubleLayerWindingSlotPositions
    from ._1277 import DQAxisConvention
    from ._1278 import Eccentricity
    from ._1279 import ElectricMachineDetail
    from ._1280 import ElectricMachineDetailInitialInformation
    from ._1281 import ElectricMachineMechanicalAnalysisMeshingOptions
    from ._1282 import ElectricMachineMeshingOptions
    from ._1283 import ElectricMachineMeshingOptionsBase
    from ._1284 import ElectricMachineSetup
    from ._1285 import ElectricMachineType
    from ._1286 import FillFactorSpecificationMethod
    from ._1287 import FluxBarrierOrWeb
    from ._1288 import FluxBarrierStyle
    from ._1289 import HairpinConductor
    from ._1290 import HarmonicLoadDataControlExcitationOptionForElectricMachineMode
    from ._1291 import IndividualConductorSpecificationSource
    from ._1292 import InteriorPermanentMagnetAndSynchronousReluctanceRotor
    from ._1293 import InteriorPermanentMagnetMachine
    from ._1294 import IronLossCoefficientSpecificationMethod
    from ._1295 import MagnetClearance
    from ._1296 import MagnetConfiguration
    from ._1297 import MagnetData
    from ._1298 import MagnetDesign
    from ._1299 import MagnetForLayer
    from ._1300 import MagnetisationDirection
    from ._1301 import MagnetMaterial
    from ._1302 import MagnetMaterialDatabase
    from ._1303 import MotorRotorSideFaceDetail
    from ._1304 import NonCADElectricMachineDetail
    from ._1305 import NotchShape
    from ._1306 import NotchSpecification
    from ._1307 import PermanentMagnetAssistedSynchronousReluctanceMachine
    from ._1308 import PermanentMagnetRotor
    from ._1309 import Phase
    from ._1310 import RegionID
    from ._1311 import Rotor
    from ._1312 import RotorInternalLayerSpecification
    from ._1313 import RotorSkewSlice
    from ._1314 import RotorType
    from ._1315 import SingleOrDoubleLayerWindings
    from ._1316 import SlotSectionDetail
    from ._1317 import Stator
    from ._1318 import StatorCutoutSpecification
    from ._1319 import StatorRotorMaterial
    from ._1320 import StatorRotorMaterialDatabase
    from ._1321 import SurfacePermanentMagnetMachine
    from ._1322 import SurfacePermanentMagnetRotor
    from ._1323 import SynchronousReluctanceMachine
    from ._1324 import ToothAndSlot
    from ._1325 import ToothSlotStyle
    from ._1326 import ToothTaperSpecification
    from ._1327 import TwoDimensionalFEModelForAnalysis
    from ._1328 import UShapedLayerSpecification
    from ._1329 import VShapedMagnetLayerSpecification
    from ._1330 import WindingConductor
    from ._1331 import WindingConnection
    from ._1332 import WindingMaterial
    from ._1333 import WindingMaterialDatabase
    from ._1334 import Windings
    from ._1335 import WindingsViewer
    from ._1336 import WindingType
    from ._1337 import WireSizeSpecificationMethod
    from ._1338 import WoundFieldSynchronousMachine
else:
    import_structure = {
        "_1261": ["AbstractStator"],
        "_1262": ["AbstractToothAndSlot"],
        "_1263": ["CADConductor"],
        "_1264": ["CADElectricMachineDetail"],
        "_1265": ["CADMagnetDetails"],
        "_1266": ["CADMagnetsForLayer"],
        "_1267": ["CADRotor"],
        "_1268": ["CADStator"],
        "_1269": ["CADToothAndSlot"],
        "_1270": ["Coil"],
        "_1271": ["CoilPositionInSlot"],
        "_1272": ["CoolingDuctLayerSpecification"],
        "_1273": ["CoolingDuctShape"],
        "_1274": ["CoreLossBuildFactorSpecificationMethod"],
        "_1275": ["CoreLossCoefficients"],
        "_1276": ["DoubleLayerWindingSlotPositions"],
        "_1277": ["DQAxisConvention"],
        "_1278": ["Eccentricity"],
        "_1279": ["ElectricMachineDetail"],
        "_1280": ["ElectricMachineDetailInitialInformation"],
        "_1281": ["ElectricMachineMechanicalAnalysisMeshingOptions"],
        "_1282": ["ElectricMachineMeshingOptions"],
        "_1283": ["ElectricMachineMeshingOptionsBase"],
        "_1284": ["ElectricMachineSetup"],
        "_1285": ["ElectricMachineType"],
        "_1286": ["FillFactorSpecificationMethod"],
        "_1287": ["FluxBarrierOrWeb"],
        "_1288": ["FluxBarrierStyle"],
        "_1289": ["HairpinConductor"],
        "_1290": ["HarmonicLoadDataControlExcitationOptionForElectricMachineMode"],
        "_1291": ["IndividualConductorSpecificationSource"],
        "_1292": ["InteriorPermanentMagnetAndSynchronousReluctanceRotor"],
        "_1293": ["InteriorPermanentMagnetMachine"],
        "_1294": ["IronLossCoefficientSpecificationMethod"],
        "_1295": ["MagnetClearance"],
        "_1296": ["MagnetConfiguration"],
        "_1297": ["MagnetData"],
        "_1298": ["MagnetDesign"],
        "_1299": ["MagnetForLayer"],
        "_1300": ["MagnetisationDirection"],
        "_1301": ["MagnetMaterial"],
        "_1302": ["MagnetMaterialDatabase"],
        "_1303": ["MotorRotorSideFaceDetail"],
        "_1304": ["NonCADElectricMachineDetail"],
        "_1305": ["NotchShape"],
        "_1306": ["NotchSpecification"],
        "_1307": ["PermanentMagnetAssistedSynchronousReluctanceMachine"],
        "_1308": ["PermanentMagnetRotor"],
        "_1309": ["Phase"],
        "_1310": ["RegionID"],
        "_1311": ["Rotor"],
        "_1312": ["RotorInternalLayerSpecification"],
        "_1313": ["RotorSkewSlice"],
        "_1314": ["RotorType"],
        "_1315": ["SingleOrDoubleLayerWindings"],
        "_1316": ["SlotSectionDetail"],
        "_1317": ["Stator"],
        "_1318": ["StatorCutoutSpecification"],
        "_1319": ["StatorRotorMaterial"],
        "_1320": ["StatorRotorMaterialDatabase"],
        "_1321": ["SurfacePermanentMagnetMachine"],
        "_1322": ["SurfacePermanentMagnetRotor"],
        "_1323": ["SynchronousReluctanceMachine"],
        "_1324": ["ToothAndSlot"],
        "_1325": ["ToothSlotStyle"],
        "_1326": ["ToothTaperSpecification"],
        "_1327": ["TwoDimensionalFEModelForAnalysis"],
        "_1328": ["UShapedLayerSpecification"],
        "_1329": ["VShapedMagnetLayerSpecification"],
        "_1330": ["WindingConductor"],
        "_1331": ["WindingConnection"],
        "_1332": ["WindingMaterial"],
        "_1333": ["WindingMaterialDatabase"],
        "_1334": ["Windings"],
        "_1335": ["WindingsViewer"],
        "_1336": ["WindingType"],
        "_1337": ["WireSizeSpecificationMethod"],
        "_1338": ["WoundFieldSynchronousMachine"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractStator",
    "AbstractToothAndSlot",
    "CADConductor",
    "CADElectricMachineDetail",
    "CADMagnetDetails",
    "CADMagnetsForLayer",
    "CADRotor",
    "CADStator",
    "CADToothAndSlot",
    "Coil",
    "CoilPositionInSlot",
    "CoolingDuctLayerSpecification",
    "CoolingDuctShape",
    "CoreLossBuildFactorSpecificationMethod",
    "CoreLossCoefficients",
    "DoubleLayerWindingSlotPositions",
    "DQAxisConvention",
    "Eccentricity",
    "ElectricMachineDetail",
    "ElectricMachineDetailInitialInformation",
    "ElectricMachineMechanicalAnalysisMeshingOptions",
    "ElectricMachineMeshingOptions",
    "ElectricMachineMeshingOptionsBase",
    "ElectricMachineSetup",
    "ElectricMachineType",
    "FillFactorSpecificationMethod",
    "FluxBarrierOrWeb",
    "FluxBarrierStyle",
    "HairpinConductor",
    "HarmonicLoadDataControlExcitationOptionForElectricMachineMode",
    "IndividualConductorSpecificationSource",
    "InteriorPermanentMagnetAndSynchronousReluctanceRotor",
    "InteriorPermanentMagnetMachine",
    "IronLossCoefficientSpecificationMethod",
    "MagnetClearance",
    "MagnetConfiguration",
    "MagnetData",
    "MagnetDesign",
    "MagnetForLayer",
    "MagnetisationDirection",
    "MagnetMaterial",
    "MagnetMaterialDatabase",
    "MotorRotorSideFaceDetail",
    "NonCADElectricMachineDetail",
    "NotchShape",
    "NotchSpecification",
    "PermanentMagnetAssistedSynchronousReluctanceMachine",
    "PermanentMagnetRotor",
    "Phase",
    "RegionID",
    "Rotor",
    "RotorInternalLayerSpecification",
    "RotorSkewSlice",
    "RotorType",
    "SingleOrDoubleLayerWindings",
    "SlotSectionDetail",
    "Stator",
    "StatorCutoutSpecification",
    "StatorRotorMaterial",
    "StatorRotorMaterialDatabase",
    "SurfacePermanentMagnetMachine",
    "SurfacePermanentMagnetRotor",
    "SynchronousReluctanceMachine",
    "ToothAndSlot",
    "ToothSlotStyle",
    "ToothTaperSpecification",
    "TwoDimensionalFEModelForAnalysis",
    "UShapedLayerSpecification",
    "VShapedMagnetLayerSpecification",
    "WindingConductor",
    "WindingConnection",
    "WindingMaterial",
    "WindingMaterialDatabase",
    "Windings",
    "WindingsViewer",
    "WindingType",
    "WireSizeSpecificationMethod",
    "WoundFieldSynchronousMachine",
)
