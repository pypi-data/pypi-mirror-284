"""DesignEntity"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from PIL.Image import Image

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DESIGN_ENTITY = python_net_import("SMT.MastaAPI.SystemModel", "DesignEntity")

if TYPE_CHECKING:
    from mastapy.system_model import _2220
    from mastapy.utility.model_validation import _1812, _1811
    from mastapy.utility.scripting import _1759
    from mastapy.system_model.connections_and_sockets import (
        _2285,
        _2288,
        _2289,
        _2292,
        _2293,
        _2301,
        _2307,
        _2312,
        _2315,
    )
    from mastapy.system_model.connections_and_sockets.gears import (
        _2319,
        _2321,
        _2323,
        _2325,
        _2327,
        _2329,
        _2331,
        _2333,
        _2335,
        _2338,
        _2339,
        _2340,
        _2343,
        _2345,
        _2347,
        _2349,
        _2351,
    )
    from mastapy.system_model.connections_and_sockets.cycloidal import (
        _2355,
        _2358,
        _2361,
    )
    from mastapy.system_model.connections_and_sockets.couplings import (
        _2362,
        _2364,
        _2366,
        _2368,
        _2370,
        _2372,
    )
    from mastapy.system_model.part_model import (
        _2453,
        _2454,
        _2455,
        _2456,
        _2459,
        _2462,
        _2463,
        _2464,
        _2467,
        _2468,
        _2472,
        _2473,
        _2474,
        _2475,
        _2482,
        _2483,
        _2484,
        _2486,
        _2488,
        _2489,
        _2491,
        _2492,
        _2494,
        _2496,
        _2497,
        _2499,
    )
    from mastapy.system_model.part_model.shaft_model import _2502
    from mastapy.system_model.part_model.gears import (
        _2533,
        _2534,
        _2535,
        _2536,
        _2537,
        _2538,
        _2539,
        _2540,
        _2541,
        _2542,
        _2543,
        _2544,
        _2545,
        _2546,
        _2547,
        _2548,
        _2549,
        _2550,
        _2552,
        _2554,
        _2555,
        _2556,
        _2557,
        _2558,
        _2559,
        _2560,
        _2561,
        _2562,
        _2563,
        _2564,
        _2565,
        _2566,
        _2567,
        _2568,
        _2569,
        _2570,
        _2571,
        _2572,
        _2573,
        _2574,
    )
    from mastapy.system_model.part_model.cycloidal import _2588, _2589, _2590
    from mastapy.system_model.part_model.couplings import (
        _2596,
        _2598,
        _2599,
        _2601,
        _2602,
        _2604,
        _2605,
        _2607,
        _2608,
        _2609,
        _2610,
        _2611,
        _2617,
        _2618,
        _2619,
        _2621,
        _2622,
        _2623,
        _2625,
        _2626,
        _2627,
        _2628,
        _2629,
        _2631,
    )


__docformat__ = "restructuredtext en"
__all__ = ("DesignEntity",)


Self = TypeVar("Self", bound="DesignEntity")


class DesignEntity(_0.APIBase):
    """DesignEntity

    This is a mastapy class.
    """

    TYPE = _DESIGN_ENTITY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DesignEntity")

    class _Cast_DesignEntity:
        """Special nested class for casting DesignEntity to subclasses."""

        def __init__(self: "DesignEntity._Cast_DesignEntity", parent: "DesignEntity"):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2285.AbstractShaftToMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2285

            return self._parent._cast(_2285.AbstractShaftToMountableComponentConnection)

        @property
        def belt_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2288.BeltConnection":
            from mastapy.system_model.connections_and_sockets import _2288

            return self._parent._cast(_2288.BeltConnection)

        @property
        def coaxial_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2289.CoaxialConnection":
            from mastapy.system_model.connections_and_sockets import _2289

            return self._parent._cast(_2289.CoaxialConnection)

        @property
        def connection(self: "DesignEntity._Cast_DesignEntity") -> "_2292.Connection":
            from mastapy.system_model.connections_and_sockets import _2292

            return self._parent._cast(_2292.Connection)

        @property
        def cvt_belt_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2293.CVTBeltConnection":
            from mastapy.system_model.connections_and_sockets import _2293

            return self._parent._cast(_2293.CVTBeltConnection)

        @property
        def inter_mountable_component_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2301.InterMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2301

            return self._parent._cast(_2301.InterMountableComponentConnection)

        @property
        def planetary_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2307.PlanetaryConnection":
            from mastapy.system_model.connections_and_sockets import _2307

            return self._parent._cast(_2307.PlanetaryConnection)

        @property
        def rolling_ring_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2312.RollingRingConnection":
            from mastapy.system_model.connections_and_sockets import _2312

            return self._parent._cast(_2312.RollingRingConnection)

        @property
        def shaft_to_mountable_component_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2315.ShaftToMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2315

            return self._parent._cast(_2315.ShaftToMountableComponentConnection)

        @property
        def agma_gleason_conical_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2319.AGMAGleasonConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2319

            return self._parent._cast(_2319.AGMAGleasonConicalGearMesh)

        @property
        def bevel_differential_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2321.BevelDifferentialGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2321

            return self._parent._cast(_2321.BevelDifferentialGearMesh)

        @property
        def bevel_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2323.BevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2323

            return self._parent._cast(_2323.BevelGearMesh)

        @property
        def concept_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2325.ConceptGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2325

            return self._parent._cast(_2325.ConceptGearMesh)

        @property
        def conical_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2327.ConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2327

            return self._parent._cast(_2327.ConicalGearMesh)

        @property
        def cylindrical_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2329.CylindricalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2329

            return self._parent._cast(_2329.CylindricalGearMesh)

        @property
        def face_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2331.FaceGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2331

            return self._parent._cast(_2331.FaceGearMesh)

        @property
        def gear_mesh(self: "DesignEntity._Cast_DesignEntity") -> "_2333.GearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2333

            return self._parent._cast(_2333.GearMesh)

        @property
        def hypoid_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2335.HypoidGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2335

            return self._parent._cast(_2335.HypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2338.KlingelnbergCycloPalloidConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2338

            return self._parent._cast(_2338.KlingelnbergCycloPalloidConicalGearMesh)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2339.KlingelnbergCycloPalloidHypoidGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2339

            return self._parent._cast(_2339.KlingelnbergCycloPalloidHypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2340.KlingelnbergCycloPalloidSpiralBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2340

            return self._parent._cast(_2340.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        @property
        def spiral_bevel_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2343.SpiralBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2343

            return self._parent._cast(_2343.SpiralBevelGearMesh)

        @property
        def straight_bevel_diff_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2345.StraightBevelDiffGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2345

            return self._parent._cast(_2345.StraightBevelDiffGearMesh)

        @property
        def straight_bevel_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2347.StraightBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2347

            return self._parent._cast(_2347.StraightBevelGearMesh)

        @property
        def worm_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2349.WormGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2349

            return self._parent._cast(_2349.WormGearMesh)

        @property
        def zerol_bevel_gear_mesh(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2351.ZerolBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2351

            return self._parent._cast(_2351.ZerolBevelGearMesh)

        @property
        def cycloidal_disc_central_bearing_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2355.CycloidalDiscCentralBearingConnection":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2355

            return self._parent._cast(_2355.CycloidalDiscCentralBearingConnection)

        @property
        def cycloidal_disc_planetary_bearing_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2358.CycloidalDiscPlanetaryBearingConnection":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2358

            return self._parent._cast(_2358.CycloidalDiscPlanetaryBearingConnection)

        @property
        def ring_pins_to_disc_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2361.RingPinsToDiscConnection":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2361

            return self._parent._cast(_2361.RingPinsToDiscConnection)

        @property
        def clutch_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2362.ClutchConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2362

            return self._parent._cast(_2362.ClutchConnection)

        @property
        def concept_coupling_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2364.ConceptCouplingConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2364

            return self._parent._cast(_2364.ConceptCouplingConnection)

        @property
        def coupling_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2366.CouplingConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2366

            return self._parent._cast(_2366.CouplingConnection)

        @property
        def part_to_part_shear_coupling_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2368.PartToPartShearCouplingConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2368

            return self._parent._cast(_2368.PartToPartShearCouplingConnection)

        @property
        def spring_damper_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2370.SpringDamperConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2370

            return self._parent._cast(_2370.SpringDamperConnection)

        @property
        def torque_converter_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2372.TorqueConverterConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2372

            return self._parent._cast(_2372.TorqueConverterConnection)

        @property
        def assembly(self: "DesignEntity._Cast_DesignEntity") -> "_2453.Assembly":
            from mastapy.system_model.part_model import _2453

            return self._parent._cast(_2453.Assembly)

        @property
        def abstract_assembly(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2454.AbstractAssembly":
            from mastapy.system_model.part_model import _2454

            return self._parent._cast(_2454.AbstractAssembly)

        @property
        def abstract_shaft(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2455.AbstractShaft":
            from mastapy.system_model.part_model import _2455

            return self._parent._cast(_2455.AbstractShaft)

        @property
        def abstract_shaft_or_housing(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2456.AbstractShaftOrHousing":
            from mastapy.system_model.part_model import _2456

            return self._parent._cast(_2456.AbstractShaftOrHousing)

        @property
        def bearing(self: "DesignEntity._Cast_DesignEntity") -> "_2459.Bearing":
            from mastapy.system_model.part_model import _2459

            return self._parent._cast(_2459.Bearing)

        @property
        def bolt(self: "DesignEntity._Cast_DesignEntity") -> "_2462.Bolt":
            from mastapy.system_model.part_model import _2462

            return self._parent._cast(_2462.Bolt)

        @property
        def bolted_joint(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2463.BoltedJoint":
            from mastapy.system_model.part_model import _2463

            return self._parent._cast(_2463.BoltedJoint)

        @property
        def component(self: "DesignEntity._Cast_DesignEntity") -> "_2464.Component":
            from mastapy.system_model.part_model import _2464

            return self._parent._cast(_2464.Component)

        @property
        def connector(self: "DesignEntity._Cast_DesignEntity") -> "_2467.Connector":
            from mastapy.system_model.part_model import _2467

            return self._parent._cast(_2467.Connector)

        @property
        def datum(self: "DesignEntity._Cast_DesignEntity") -> "_2468.Datum":
            from mastapy.system_model.part_model import _2468

            return self._parent._cast(_2468.Datum)

        @property
        def external_cad_model(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2472.ExternalCADModel":
            from mastapy.system_model.part_model import _2472

            return self._parent._cast(_2472.ExternalCADModel)

        @property
        def fe_part(self: "DesignEntity._Cast_DesignEntity") -> "_2473.FEPart":
            from mastapy.system_model.part_model import _2473

            return self._parent._cast(_2473.FEPart)

        @property
        def flexible_pin_assembly(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2474.FlexiblePinAssembly":
            from mastapy.system_model.part_model import _2474

            return self._parent._cast(_2474.FlexiblePinAssembly)

        @property
        def guide_dxf_model(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2475.GuideDxfModel":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.GuideDxfModel)

        @property
        def mass_disc(self: "DesignEntity._Cast_DesignEntity") -> "_2482.MassDisc":
            from mastapy.system_model.part_model import _2482

            return self._parent._cast(_2482.MassDisc)

        @property
        def measurement_component(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2483.MeasurementComponent":
            from mastapy.system_model.part_model import _2483

            return self._parent._cast(_2483.MeasurementComponent)

        @property
        def mountable_component(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2484.MountableComponent":
            from mastapy.system_model.part_model import _2484

            return self._parent._cast(_2484.MountableComponent)

        @property
        def oil_seal(self: "DesignEntity._Cast_DesignEntity") -> "_2486.OilSeal":
            from mastapy.system_model.part_model import _2486

            return self._parent._cast(_2486.OilSeal)

        @property
        def part(self: "DesignEntity._Cast_DesignEntity") -> "_2488.Part":
            from mastapy.system_model.part_model import _2488

            return self._parent._cast(_2488.Part)

        @property
        def planet_carrier(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2489.PlanetCarrier":
            from mastapy.system_model.part_model import _2489

            return self._parent._cast(_2489.PlanetCarrier)

        @property
        def point_load(self: "DesignEntity._Cast_DesignEntity") -> "_2491.PointLoad":
            from mastapy.system_model.part_model import _2491

            return self._parent._cast(_2491.PointLoad)

        @property
        def power_load(self: "DesignEntity._Cast_DesignEntity") -> "_2492.PowerLoad":
            from mastapy.system_model.part_model import _2492

            return self._parent._cast(_2492.PowerLoad)

        @property
        def root_assembly(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2494.RootAssembly":
            from mastapy.system_model.part_model import _2494

            return self._parent._cast(_2494.RootAssembly)

        @property
        def specialised_assembly(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2496.SpecialisedAssembly":
            from mastapy.system_model.part_model import _2496

            return self._parent._cast(_2496.SpecialisedAssembly)

        @property
        def unbalanced_mass(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2497.UnbalancedMass":
            from mastapy.system_model.part_model import _2497

            return self._parent._cast(_2497.UnbalancedMass)

        @property
        def virtual_component(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2499.VirtualComponent":
            from mastapy.system_model.part_model import _2499

            return self._parent._cast(_2499.VirtualComponent)

        @property
        def shaft(self: "DesignEntity._Cast_DesignEntity") -> "_2502.Shaft":
            from mastapy.system_model.part_model.shaft_model import _2502

            return self._parent._cast(_2502.Shaft)

        @property
        def agma_gleason_conical_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2533.AGMAGleasonConicalGear":
            from mastapy.system_model.part_model.gears import _2533

            return self._parent._cast(_2533.AGMAGleasonConicalGear)

        @property
        def agma_gleason_conical_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2534.AGMAGleasonConicalGearSet":
            from mastapy.system_model.part_model.gears import _2534

            return self._parent._cast(_2534.AGMAGleasonConicalGearSet)

        @property
        def bevel_differential_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2535.BevelDifferentialGear":
            from mastapy.system_model.part_model.gears import _2535

            return self._parent._cast(_2535.BevelDifferentialGear)

        @property
        def bevel_differential_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2536.BevelDifferentialGearSet":
            from mastapy.system_model.part_model.gears import _2536

            return self._parent._cast(_2536.BevelDifferentialGearSet)

        @property
        def bevel_differential_planet_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2537.BevelDifferentialPlanetGear":
            from mastapy.system_model.part_model.gears import _2537

            return self._parent._cast(_2537.BevelDifferentialPlanetGear)

        @property
        def bevel_differential_sun_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2538.BevelDifferentialSunGear":
            from mastapy.system_model.part_model.gears import _2538

            return self._parent._cast(_2538.BevelDifferentialSunGear)

        @property
        def bevel_gear(self: "DesignEntity._Cast_DesignEntity") -> "_2539.BevelGear":
            from mastapy.system_model.part_model.gears import _2539

            return self._parent._cast(_2539.BevelGear)

        @property
        def bevel_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2540.BevelGearSet":
            from mastapy.system_model.part_model.gears import _2540

            return self._parent._cast(_2540.BevelGearSet)

        @property
        def concept_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2541.ConceptGear":
            from mastapy.system_model.part_model.gears import _2541

            return self._parent._cast(_2541.ConceptGear)

        @property
        def concept_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2542.ConceptGearSet":
            from mastapy.system_model.part_model.gears import _2542

            return self._parent._cast(_2542.ConceptGearSet)

        @property
        def conical_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2543.ConicalGear":
            from mastapy.system_model.part_model.gears import _2543

            return self._parent._cast(_2543.ConicalGear)

        @property
        def conical_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2544.ConicalGearSet":
            from mastapy.system_model.part_model.gears import _2544

            return self._parent._cast(_2544.ConicalGearSet)

        @property
        def cylindrical_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2545.CylindricalGear":
            from mastapy.system_model.part_model.gears import _2545

            return self._parent._cast(_2545.CylindricalGear)

        @property
        def cylindrical_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2546.CylindricalGearSet":
            from mastapy.system_model.part_model.gears import _2546

            return self._parent._cast(_2546.CylindricalGearSet)

        @property
        def cylindrical_planet_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2547.CylindricalPlanetGear":
            from mastapy.system_model.part_model.gears import _2547

            return self._parent._cast(_2547.CylindricalPlanetGear)

        @property
        def face_gear(self: "DesignEntity._Cast_DesignEntity") -> "_2548.FaceGear":
            from mastapy.system_model.part_model.gears import _2548

            return self._parent._cast(_2548.FaceGear)

        @property
        def face_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2549.FaceGearSet":
            from mastapy.system_model.part_model.gears import _2549

            return self._parent._cast(_2549.FaceGearSet)

        @property
        def gear(self: "DesignEntity._Cast_DesignEntity") -> "_2550.Gear":
            from mastapy.system_model.part_model.gears import _2550

            return self._parent._cast(_2550.Gear)

        @property
        def gear_set(self: "DesignEntity._Cast_DesignEntity") -> "_2552.GearSet":
            from mastapy.system_model.part_model.gears import _2552

            return self._parent._cast(_2552.GearSet)

        @property
        def hypoid_gear(self: "DesignEntity._Cast_DesignEntity") -> "_2554.HypoidGear":
            from mastapy.system_model.part_model.gears import _2554

            return self._parent._cast(_2554.HypoidGear)

        @property
        def hypoid_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2555.HypoidGearSet":
            from mastapy.system_model.part_model.gears import _2555

            return self._parent._cast(_2555.HypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_conical_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2556.KlingelnbergCycloPalloidConicalGear":
            from mastapy.system_model.part_model.gears import _2556

            return self._parent._cast(_2556.KlingelnbergCycloPalloidConicalGear)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2557.KlingelnbergCycloPalloidConicalGearSet":
            from mastapy.system_model.part_model.gears import _2557

            return self._parent._cast(_2557.KlingelnbergCycloPalloidConicalGearSet)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2558.KlingelnbergCycloPalloidHypoidGear":
            from mastapy.system_model.part_model.gears import _2558

            return self._parent._cast(_2558.KlingelnbergCycloPalloidHypoidGear)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2559.KlingelnbergCycloPalloidHypoidGearSet":
            from mastapy.system_model.part_model.gears import _2559

            return self._parent._cast(_2559.KlingelnbergCycloPalloidHypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2560.KlingelnbergCycloPalloidSpiralBevelGear":
            from mastapy.system_model.part_model.gears import _2560

            return self._parent._cast(_2560.KlingelnbergCycloPalloidSpiralBevelGear)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2561.KlingelnbergCycloPalloidSpiralBevelGearSet":
            from mastapy.system_model.part_model.gears import _2561

            return self._parent._cast(_2561.KlingelnbergCycloPalloidSpiralBevelGearSet)

        @property
        def planetary_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2562.PlanetaryGearSet":
            from mastapy.system_model.part_model.gears import _2562

            return self._parent._cast(_2562.PlanetaryGearSet)

        @property
        def spiral_bevel_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2563.SpiralBevelGear":
            from mastapy.system_model.part_model.gears import _2563

            return self._parent._cast(_2563.SpiralBevelGear)

        @property
        def spiral_bevel_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2564.SpiralBevelGearSet":
            from mastapy.system_model.part_model.gears import _2564

            return self._parent._cast(_2564.SpiralBevelGearSet)

        @property
        def straight_bevel_diff_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2565.StraightBevelDiffGear":
            from mastapy.system_model.part_model.gears import _2565

            return self._parent._cast(_2565.StraightBevelDiffGear)

        @property
        def straight_bevel_diff_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2566.StraightBevelDiffGearSet":
            from mastapy.system_model.part_model.gears import _2566

            return self._parent._cast(_2566.StraightBevelDiffGearSet)

        @property
        def straight_bevel_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2567.StraightBevelGear":
            from mastapy.system_model.part_model.gears import _2567

            return self._parent._cast(_2567.StraightBevelGear)

        @property
        def straight_bevel_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2568.StraightBevelGearSet":
            from mastapy.system_model.part_model.gears import _2568

            return self._parent._cast(_2568.StraightBevelGearSet)

        @property
        def straight_bevel_planet_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2569.StraightBevelPlanetGear":
            from mastapy.system_model.part_model.gears import _2569

            return self._parent._cast(_2569.StraightBevelPlanetGear)

        @property
        def straight_bevel_sun_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2570.StraightBevelSunGear":
            from mastapy.system_model.part_model.gears import _2570

            return self._parent._cast(_2570.StraightBevelSunGear)

        @property
        def worm_gear(self: "DesignEntity._Cast_DesignEntity") -> "_2571.WormGear":
            from mastapy.system_model.part_model.gears import _2571

            return self._parent._cast(_2571.WormGear)

        @property
        def worm_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2572.WormGearSet":
            from mastapy.system_model.part_model.gears import _2572

            return self._parent._cast(_2572.WormGearSet)

        @property
        def zerol_bevel_gear(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2573.ZerolBevelGear":
            from mastapy.system_model.part_model.gears import _2573

            return self._parent._cast(_2573.ZerolBevelGear)

        @property
        def zerol_bevel_gear_set(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2574.ZerolBevelGearSet":
            from mastapy.system_model.part_model.gears import _2574

            return self._parent._cast(_2574.ZerolBevelGearSet)

        @property
        def cycloidal_assembly(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2588.CycloidalAssembly":
            from mastapy.system_model.part_model.cycloidal import _2588

            return self._parent._cast(_2588.CycloidalAssembly)

        @property
        def cycloidal_disc(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2589.CycloidalDisc":
            from mastapy.system_model.part_model.cycloidal import _2589

            return self._parent._cast(_2589.CycloidalDisc)

        @property
        def ring_pins(self: "DesignEntity._Cast_DesignEntity") -> "_2590.RingPins":
            from mastapy.system_model.part_model.cycloidal import _2590

            return self._parent._cast(_2590.RingPins)

        @property
        def belt_drive(self: "DesignEntity._Cast_DesignEntity") -> "_2596.BeltDrive":
            from mastapy.system_model.part_model.couplings import _2596

            return self._parent._cast(_2596.BeltDrive)

        @property
        def clutch(self: "DesignEntity._Cast_DesignEntity") -> "_2598.Clutch":
            from mastapy.system_model.part_model.couplings import _2598

            return self._parent._cast(_2598.Clutch)

        @property
        def clutch_half(self: "DesignEntity._Cast_DesignEntity") -> "_2599.ClutchHalf":
            from mastapy.system_model.part_model.couplings import _2599

            return self._parent._cast(_2599.ClutchHalf)

        @property
        def concept_coupling(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2601.ConceptCoupling":
            from mastapy.system_model.part_model.couplings import _2601

            return self._parent._cast(_2601.ConceptCoupling)

        @property
        def concept_coupling_half(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2602.ConceptCouplingHalf":
            from mastapy.system_model.part_model.couplings import _2602

            return self._parent._cast(_2602.ConceptCouplingHalf)

        @property
        def coupling(self: "DesignEntity._Cast_DesignEntity") -> "_2604.Coupling":
            from mastapy.system_model.part_model.couplings import _2604

            return self._parent._cast(_2604.Coupling)

        @property
        def coupling_half(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2605.CouplingHalf":
            from mastapy.system_model.part_model.couplings import _2605

            return self._parent._cast(_2605.CouplingHalf)

        @property
        def cvt(self: "DesignEntity._Cast_DesignEntity") -> "_2607.CVT":
            from mastapy.system_model.part_model.couplings import _2607

            return self._parent._cast(_2607.CVT)

        @property
        def cvt_pulley(self: "DesignEntity._Cast_DesignEntity") -> "_2608.CVTPulley":
            from mastapy.system_model.part_model.couplings import _2608

            return self._parent._cast(_2608.CVTPulley)

        @property
        def part_to_part_shear_coupling(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2609.PartToPartShearCoupling":
            from mastapy.system_model.part_model.couplings import _2609

            return self._parent._cast(_2609.PartToPartShearCoupling)

        @property
        def part_to_part_shear_coupling_half(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2610.PartToPartShearCouplingHalf":
            from mastapy.system_model.part_model.couplings import _2610

            return self._parent._cast(_2610.PartToPartShearCouplingHalf)

        @property
        def pulley(self: "DesignEntity._Cast_DesignEntity") -> "_2611.Pulley":
            from mastapy.system_model.part_model.couplings import _2611

            return self._parent._cast(_2611.Pulley)

        @property
        def rolling_ring(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2617.RollingRing":
            from mastapy.system_model.part_model.couplings import _2617

            return self._parent._cast(_2617.RollingRing)

        @property
        def rolling_ring_assembly(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2618.RollingRingAssembly":
            from mastapy.system_model.part_model.couplings import _2618

            return self._parent._cast(_2618.RollingRingAssembly)

        @property
        def shaft_hub_connection(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2619.ShaftHubConnection":
            from mastapy.system_model.part_model.couplings import _2619

            return self._parent._cast(_2619.ShaftHubConnection)

        @property
        def spring_damper(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2621.SpringDamper":
            from mastapy.system_model.part_model.couplings import _2621

            return self._parent._cast(_2621.SpringDamper)

        @property
        def spring_damper_half(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2622.SpringDamperHalf":
            from mastapy.system_model.part_model.couplings import _2622

            return self._parent._cast(_2622.SpringDamperHalf)

        @property
        def synchroniser(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2623.Synchroniser":
            from mastapy.system_model.part_model.couplings import _2623

            return self._parent._cast(_2623.Synchroniser)

        @property
        def synchroniser_half(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2625.SynchroniserHalf":
            from mastapy.system_model.part_model.couplings import _2625

            return self._parent._cast(_2625.SynchroniserHalf)

        @property
        def synchroniser_part(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2626.SynchroniserPart":
            from mastapy.system_model.part_model.couplings import _2626

            return self._parent._cast(_2626.SynchroniserPart)

        @property
        def synchroniser_sleeve(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2627.SynchroniserSleeve":
            from mastapy.system_model.part_model.couplings import _2627

            return self._parent._cast(_2627.SynchroniserSleeve)

        @property
        def torque_converter(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2628.TorqueConverter":
            from mastapy.system_model.part_model.couplings import _2628

            return self._parent._cast(_2628.TorqueConverter)

        @property
        def torque_converter_pump(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2629.TorqueConverterPump":
            from mastapy.system_model.part_model.couplings import _2629

            return self._parent._cast(_2629.TorqueConverterPump)

        @property
        def torque_converter_turbine(
            self: "DesignEntity._Cast_DesignEntity",
        ) -> "_2631.TorqueConverterTurbine":
            from mastapy.system_model.part_model.couplings import _2631

            return self._parent._cast(_2631.TorqueConverterTurbine)

        @property
        def design_entity(self: "DesignEntity._Cast_DesignEntity") -> "DesignEntity":
            return self._parent

        def __getattr__(self: "DesignEntity._Cast_DesignEntity", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DesignEntity.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def comment(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Comment

        if temp is None:
            return ""

        return temp

    @comment.setter
    @enforce_parameter_types
    def comment(self: Self, value: "str"):
        self.wrapped.Comment = str(value) if value is not None else ""

    @property
    def id(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ID

        if temp is None:
            return ""

        return temp

    @property
    def icon(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Icon

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def small_icon(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SmallIcon

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def unique_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UniqueName

        if temp is None:
            return ""

        return temp

    @property
    def design_properties(self: Self) -> "_2220.Design":
        """mastapy.system_model.Design

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DesignProperties

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def all_design_entities(self: Self) -> "List[DesignEntity]":
        """List[mastapy.system_model.DesignEntity]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllDesignEntities

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def all_status_errors(self: Self) -> "List[_1812.StatusItem]":
        """List[mastapy.utility.model_validation.StatusItem]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllStatusErrors

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def status(self: Self) -> "_1811.Status":
        """mastapy.utility.model_validation.Status

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Status

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def user_specified_data(self: Self) -> "_1759.UserSpecifiedData":
        """mastapy.utility.scripting.UserSpecifiedData

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UserSpecifiedData

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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

    def delete(self: Self):
        """Method does not return."""
        self.wrapped.Delete()

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
    def cast_to(self: Self) -> "DesignEntity._Cast_DesignEntity":
        return self._Cast_DesignEntity(self)
