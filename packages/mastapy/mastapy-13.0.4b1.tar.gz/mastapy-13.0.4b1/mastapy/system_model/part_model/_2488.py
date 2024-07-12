"""Part"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from PIL.Image import Image

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model import _2223
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Part")

if TYPE_CHECKING:
    from mastapy.math_utility import _1536
    from mastapy.system_model.connections_and_sockets import _2292
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
        _2489,
        _2491,
        _2492,
        _2494,
        _2496,
        _2497,
        _2499,
    )
    from mastapy.system_model.import_export import _2262
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
__all__ = ("Part",)


Self = TypeVar("Self", bound="Part")


class Part(_2223.DesignEntity):
    """Part

    This is a mastapy class.
    """

    TYPE = _PART
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Part")

    class _Cast_Part:
        """Special nested class for casting Part to subclasses."""

        def __init__(self: "Part._Cast_Part", parent: "Part"):
            self._parent = parent

        @property
        def design_entity(self: "Part._Cast_Part") -> "_2223.DesignEntity":
            return self._parent._cast(_2223.DesignEntity)

        @property
        def assembly(self: "Part._Cast_Part") -> "_2453.Assembly":
            return self._parent._cast(_2453.Assembly)

        @property
        def abstract_assembly(self: "Part._Cast_Part") -> "_2454.AbstractAssembly":
            from mastapy.system_model.part_model import _2454

            return self._parent._cast(_2454.AbstractAssembly)

        @property
        def abstract_shaft(self: "Part._Cast_Part") -> "_2455.AbstractShaft":
            from mastapy.system_model.part_model import _2455

            return self._parent._cast(_2455.AbstractShaft)

        @property
        def abstract_shaft_or_housing(
            self: "Part._Cast_Part",
        ) -> "_2456.AbstractShaftOrHousing":
            from mastapy.system_model.part_model import _2456

            return self._parent._cast(_2456.AbstractShaftOrHousing)

        @property
        def bearing(self: "Part._Cast_Part") -> "_2459.Bearing":
            from mastapy.system_model.part_model import _2459

            return self._parent._cast(_2459.Bearing)

        @property
        def bolt(self: "Part._Cast_Part") -> "_2462.Bolt":
            from mastapy.system_model.part_model import _2462

            return self._parent._cast(_2462.Bolt)

        @property
        def bolted_joint(self: "Part._Cast_Part") -> "_2463.BoltedJoint":
            from mastapy.system_model.part_model import _2463

            return self._parent._cast(_2463.BoltedJoint)

        @property
        def component(self: "Part._Cast_Part") -> "_2464.Component":
            from mastapy.system_model.part_model import _2464

            return self._parent._cast(_2464.Component)

        @property
        def connector(self: "Part._Cast_Part") -> "_2467.Connector":
            from mastapy.system_model.part_model import _2467

            return self._parent._cast(_2467.Connector)

        @property
        def datum(self: "Part._Cast_Part") -> "_2468.Datum":
            from mastapy.system_model.part_model import _2468

            return self._parent._cast(_2468.Datum)

        @property
        def external_cad_model(self: "Part._Cast_Part") -> "_2472.ExternalCADModel":
            from mastapy.system_model.part_model import _2472

            return self._parent._cast(_2472.ExternalCADModel)

        @property
        def fe_part(self: "Part._Cast_Part") -> "_2473.FEPart":
            from mastapy.system_model.part_model import _2473

            return self._parent._cast(_2473.FEPart)

        @property
        def flexible_pin_assembly(
            self: "Part._Cast_Part",
        ) -> "_2474.FlexiblePinAssembly":
            from mastapy.system_model.part_model import _2474

            return self._parent._cast(_2474.FlexiblePinAssembly)

        @property
        def guide_dxf_model(self: "Part._Cast_Part") -> "_2475.GuideDxfModel":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.GuideDxfModel)

        @property
        def mass_disc(self: "Part._Cast_Part") -> "_2482.MassDisc":
            from mastapy.system_model.part_model import _2482

            return self._parent._cast(_2482.MassDisc)

        @property
        def measurement_component(
            self: "Part._Cast_Part",
        ) -> "_2483.MeasurementComponent":
            from mastapy.system_model.part_model import _2483

            return self._parent._cast(_2483.MeasurementComponent)

        @property
        def mountable_component(self: "Part._Cast_Part") -> "_2484.MountableComponent":
            from mastapy.system_model.part_model import _2484

            return self._parent._cast(_2484.MountableComponent)

        @property
        def oil_seal(self: "Part._Cast_Part") -> "_2486.OilSeal":
            from mastapy.system_model.part_model import _2486

            return self._parent._cast(_2486.OilSeal)

        @property
        def planet_carrier(self: "Part._Cast_Part") -> "_2489.PlanetCarrier":
            from mastapy.system_model.part_model import _2489

            return self._parent._cast(_2489.PlanetCarrier)

        @property
        def point_load(self: "Part._Cast_Part") -> "_2491.PointLoad":
            from mastapy.system_model.part_model import _2491

            return self._parent._cast(_2491.PointLoad)

        @property
        def power_load(self: "Part._Cast_Part") -> "_2492.PowerLoad":
            from mastapy.system_model.part_model import _2492

            return self._parent._cast(_2492.PowerLoad)

        @property
        def root_assembly(self: "Part._Cast_Part") -> "_2494.RootAssembly":
            from mastapy.system_model.part_model import _2494

            return self._parent._cast(_2494.RootAssembly)

        @property
        def specialised_assembly(
            self: "Part._Cast_Part",
        ) -> "_2496.SpecialisedAssembly":
            from mastapy.system_model.part_model import _2496

            return self._parent._cast(_2496.SpecialisedAssembly)

        @property
        def unbalanced_mass(self: "Part._Cast_Part") -> "_2497.UnbalancedMass":
            from mastapy.system_model.part_model import _2497

            return self._parent._cast(_2497.UnbalancedMass)

        @property
        def virtual_component(self: "Part._Cast_Part") -> "_2499.VirtualComponent":
            from mastapy.system_model.part_model import _2499

            return self._parent._cast(_2499.VirtualComponent)

        @property
        def shaft(self: "Part._Cast_Part") -> "_2502.Shaft":
            from mastapy.system_model.part_model.shaft_model import _2502

            return self._parent._cast(_2502.Shaft)

        @property
        def agma_gleason_conical_gear(
            self: "Part._Cast_Part",
        ) -> "_2533.AGMAGleasonConicalGear":
            from mastapy.system_model.part_model.gears import _2533

            return self._parent._cast(_2533.AGMAGleasonConicalGear)

        @property
        def agma_gleason_conical_gear_set(
            self: "Part._Cast_Part",
        ) -> "_2534.AGMAGleasonConicalGearSet":
            from mastapy.system_model.part_model.gears import _2534

            return self._parent._cast(_2534.AGMAGleasonConicalGearSet)

        @property
        def bevel_differential_gear(
            self: "Part._Cast_Part",
        ) -> "_2535.BevelDifferentialGear":
            from mastapy.system_model.part_model.gears import _2535

            return self._parent._cast(_2535.BevelDifferentialGear)

        @property
        def bevel_differential_gear_set(
            self: "Part._Cast_Part",
        ) -> "_2536.BevelDifferentialGearSet":
            from mastapy.system_model.part_model.gears import _2536

            return self._parent._cast(_2536.BevelDifferentialGearSet)

        @property
        def bevel_differential_planet_gear(
            self: "Part._Cast_Part",
        ) -> "_2537.BevelDifferentialPlanetGear":
            from mastapy.system_model.part_model.gears import _2537

            return self._parent._cast(_2537.BevelDifferentialPlanetGear)

        @property
        def bevel_differential_sun_gear(
            self: "Part._Cast_Part",
        ) -> "_2538.BevelDifferentialSunGear":
            from mastapy.system_model.part_model.gears import _2538

            return self._parent._cast(_2538.BevelDifferentialSunGear)

        @property
        def bevel_gear(self: "Part._Cast_Part") -> "_2539.BevelGear":
            from mastapy.system_model.part_model.gears import _2539

            return self._parent._cast(_2539.BevelGear)

        @property
        def bevel_gear_set(self: "Part._Cast_Part") -> "_2540.BevelGearSet":
            from mastapy.system_model.part_model.gears import _2540

            return self._parent._cast(_2540.BevelGearSet)

        @property
        def concept_gear(self: "Part._Cast_Part") -> "_2541.ConceptGear":
            from mastapy.system_model.part_model.gears import _2541

            return self._parent._cast(_2541.ConceptGear)

        @property
        def concept_gear_set(self: "Part._Cast_Part") -> "_2542.ConceptGearSet":
            from mastapy.system_model.part_model.gears import _2542

            return self._parent._cast(_2542.ConceptGearSet)

        @property
        def conical_gear(self: "Part._Cast_Part") -> "_2543.ConicalGear":
            from mastapy.system_model.part_model.gears import _2543

            return self._parent._cast(_2543.ConicalGear)

        @property
        def conical_gear_set(self: "Part._Cast_Part") -> "_2544.ConicalGearSet":
            from mastapy.system_model.part_model.gears import _2544

            return self._parent._cast(_2544.ConicalGearSet)

        @property
        def cylindrical_gear(self: "Part._Cast_Part") -> "_2545.CylindricalGear":
            from mastapy.system_model.part_model.gears import _2545

            return self._parent._cast(_2545.CylindricalGear)

        @property
        def cylindrical_gear_set(self: "Part._Cast_Part") -> "_2546.CylindricalGearSet":
            from mastapy.system_model.part_model.gears import _2546

            return self._parent._cast(_2546.CylindricalGearSet)

        @property
        def cylindrical_planet_gear(
            self: "Part._Cast_Part",
        ) -> "_2547.CylindricalPlanetGear":
            from mastapy.system_model.part_model.gears import _2547

            return self._parent._cast(_2547.CylindricalPlanetGear)

        @property
        def face_gear(self: "Part._Cast_Part") -> "_2548.FaceGear":
            from mastapy.system_model.part_model.gears import _2548

            return self._parent._cast(_2548.FaceGear)

        @property
        def face_gear_set(self: "Part._Cast_Part") -> "_2549.FaceGearSet":
            from mastapy.system_model.part_model.gears import _2549

            return self._parent._cast(_2549.FaceGearSet)

        @property
        def gear(self: "Part._Cast_Part") -> "_2550.Gear":
            from mastapy.system_model.part_model.gears import _2550

            return self._parent._cast(_2550.Gear)

        @property
        def gear_set(self: "Part._Cast_Part") -> "_2552.GearSet":
            from mastapy.system_model.part_model.gears import _2552

            return self._parent._cast(_2552.GearSet)

        @property
        def hypoid_gear(self: "Part._Cast_Part") -> "_2554.HypoidGear":
            from mastapy.system_model.part_model.gears import _2554

            return self._parent._cast(_2554.HypoidGear)

        @property
        def hypoid_gear_set(self: "Part._Cast_Part") -> "_2555.HypoidGearSet":
            from mastapy.system_model.part_model.gears import _2555

            return self._parent._cast(_2555.HypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_conical_gear(
            self: "Part._Cast_Part",
        ) -> "_2556.KlingelnbergCycloPalloidConicalGear":
            from mastapy.system_model.part_model.gears import _2556

            return self._parent._cast(_2556.KlingelnbergCycloPalloidConicalGear)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set(
            self: "Part._Cast_Part",
        ) -> "_2557.KlingelnbergCycloPalloidConicalGearSet":
            from mastapy.system_model.part_model.gears import _2557

            return self._parent._cast(_2557.KlingelnbergCycloPalloidConicalGearSet)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear(
            self: "Part._Cast_Part",
        ) -> "_2558.KlingelnbergCycloPalloidHypoidGear":
            from mastapy.system_model.part_model.gears import _2558

            return self._parent._cast(_2558.KlingelnbergCycloPalloidHypoidGear)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set(
            self: "Part._Cast_Part",
        ) -> "_2559.KlingelnbergCycloPalloidHypoidGearSet":
            from mastapy.system_model.part_model.gears import _2559

            return self._parent._cast(_2559.KlingelnbergCycloPalloidHypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear(
            self: "Part._Cast_Part",
        ) -> "_2560.KlingelnbergCycloPalloidSpiralBevelGear":
            from mastapy.system_model.part_model.gears import _2560

            return self._parent._cast(_2560.KlingelnbergCycloPalloidSpiralBevelGear)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set(
            self: "Part._Cast_Part",
        ) -> "_2561.KlingelnbergCycloPalloidSpiralBevelGearSet":
            from mastapy.system_model.part_model.gears import _2561

            return self._parent._cast(_2561.KlingelnbergCycloPalloidSpiralBevelGearSet)

        @property
        def planetary_gear_set(self: "Part._Cast_Part") -> "_2562.PlanetaryGearSet":
            from mastapy.system_model.part_model.gears import _2562

            return self._parent._cast(_2562.PlanetaryGearSet)

        @property
        def spiral_bevel_gear(self: "Part._Cast_Part") -> "_2563.SpiralBevelGear":
            from mastapy.system_model.part_model.gears import _2563

            return self._parent._cast(_2563.SpiralBevelGear)

        @property
        def spiral_bevel_gear_set(
            self: "Part._Cast_Part",
        ) -> "_2564.SpiralBevelGearSet":
            from mastapy.system_model.part_model.gears import _2564

            return self._parent._cast(_2564.SpiralBevelGearSet)

        @property
        def straight_bevel_diff_gear(
            self: "Part._Cast_Part",
        ) -> "_2565.StraightBevelDiffGear":
            from mastapy.system_model.part_model.gears import _2565

            return self._parent._cast(_2565.StraightBevelDiffGear)

        @property
        def straight_bevel_diff_gear_set(
            self: "Part._Cast_Part",
        ) -> "_2566.StraightBevelDiffGearSet":
            from mastapy.system_model.part_model.gears import _2566

            return self._parent._cast(_2566.StraightBevelDiffGearSet)

        @property
        def straight_bevel_gear(self: "Part._Cast_Part") -> "_2567.StraightBevelGear":
            from mastapy.system_model.part_model.gears import _2567

            return self._parent._cast(_2567.StraightBevelGear)

        @property
        def straight_bevel_gear_set(
            self: "Part._Cast_Part",
        ) -> "_2568.StraightBevelGearSet":
            from mastapy.system_model.part_model.gears import _2568

            return self._parent._cast(_2568.StraightBevelGearSet)

        @property
        def straight_bevel_planet_gear(
            self: "Part._Cast_Part",
        ) -> "_2569.StraightBevelPlanetGear":
            from mastapy.system_model.part_model.gears import _2569

            return self._parent._cast(_2569.StraightBevelPlanetGear)

        @property
        def straight_bevel_sun_gear(
            self: "Part._Cast_Part",
        ) -> "_2570.StraightBevelSunGear":
            from mastapy.system_model.part_model.gears import _2570

            return self._parent._cast(_2570.StraightBevelSunGear)

        @property
        def worm_gear(self: "Part._Cast_Part") -> "_2571.WormGear":
            from mastapy.system_model.part_model.gears import _2571

            return self._parent._cast(_2571.WormGear)

        @property
        def worm_gear_set(self: "Part._Cast_Part") -> "_2572.WormGearSet":
            from mastapy.system_model.part_model.gears import _2572

            return self._parent._cast(_2572.WormGearSet)

        @property
        def zerol_bevel_gear(self: "Part._Cast_Part") -> "_2573.ZerolBevelGear":
            from mastapy.system_model.part_model.gears import _2573

            return self._parent._cast(_2573.ZerolBevelGear)

        @property
        def zerol_bevel_gear_set(self: "Part._Cast_Part") -> "_2574.ZerolBevelGearSet":
            from mastapy.system_model.part_model.gears import _2574

            return self._parent._cast(_2574.ZerolBevelGearSet)

        @property
        def cycloidal_assembly(self: "Part._Cast_Part") -> "_2588.CycloidalAssembly":
            from mastapy.system_model.part_model.cycloidal import _2588

            return self._parent._cast(_2588.CycloidalAssembly)

        @property
        def cycloidal_disc(self: "Part._Cast_Part") -> "_2589.CycloidalDisc":
            from mastapy.system_model.part_model.cycloidal import _2589

            return self._parent._cast(_2589.CycloidalDisc)

        @property
        def ring_pins(self: "Part._Cast_Part") -> "_2590.RingPins":
            from mastapy.system_model.part_model.cycloidal import _2590

            return self._parent._cast(_2590.RingPins)

        @property
        def belt_drive(self: "Part._Cast_Part") -> "_2596.BeltDrive":
            from mastapy.system_model.part_model.couplings import _2596

            return self._parent._cast(_2596.BeltDrive)

        @property
        def clutch(self: "Part._Cast_Part") -> "_2598.Clutch":
            from mastapy.system_model.part_model.couplings import _2598

            return self._parent._cast(_2598.Clutch)

        @property
        def clutch_half(self: "Part._Cast_Part") -> "_2599.ClutchHalf":
            from mastapy.system_model.part_model.couplings import _2599

            return self._parent._cast(_2599.ClutchHalf)

        @property
        def concept_coupling(self: "Part._Cast_Part") -> "_2601.ConceptCoupling":
            from mastapy.system_model.part_model.couplings import _2601

            return self._parent._cast(_2601.ConceptCoupling)

        @property
        def concept_coupling_half(
            self: "Part._Cast_Part",
        ) -> "_2602.ConceptCouplingHalf":
            from mastapy.system_model.part_model.couplings import _2602

            return self._parent._cast(_2602.ConceptCouplingHalf)

        @property
        def coupling(self: "Part._Cast_Part") -> "_2604.Coupling":
            from mastapy.system_model.part_model.couplings import _2604

            return self._parent._cast(_2604.Coupling)

        @property
        def coupling_half(self: "Part._Cast_Part") -> "_2605.CouplingHalf":
            from mastapy.system_model.part_model.couplings import _2605

            return self._parent._cast(_2605.CouplingHalf)

        @property
        def cvt(self: "Part._Cast_Part") -> "_2607.CVT":
            from mastapy.system_model.part_model.couplings import _2607

            return self._parent._cast(_2607.CVT)

        @property
        def cvt_pulley(self: "Part._Cast_Part") -> "_2608.CVTPulley":
            from mastapy.system_model.part_model.couplings import _2608

            return self._parent._cast(_2608.CVTPulley)

        @property
        def part_to_part_shear_coupling(
            self: "Part._Cast_Part",
        ) -> "_2609.PartToPartShearCoupling":
            from mastapy.system_model.part_model.couplings import _2609

            return self._parent._cast(_2609.PartToPartShearCoupling)

        @property
        def part_to_part_shear_coupling_half(
            self: "Part._Cast_Part",
        ) -> "_2610.PartToPartShearCouplingHalf":
            from mastapy.system_model.part_model.couplings import _2610

            return self._parent._cast(_2610.PartToPartShearCouplingHalf)

        @property
        def pulley(self: "Part._Cast_Part") -> "_2611.Pulley":
            from mastapy.system_model.part_model.couplings import _2611

            return self._parent._cast(_2611.Pulley)

        @property
        def rolling_ring(self: "Part._Cast_Part") -> "_2617.RollingRing":
            from mastapy.system_model.part_model.couplings import _2617

            return self._parent._cast(_2617.RollingRing)

        @property
        def rolling_ring_assembly(
            self: "Part._Cast_Part",
        ) -> "_2618.RollingRingAssembly":
            from mastapy.system_model.part_model.couplings import _2618

            return self._parent._cast(_2618.RollingRingAssembly)

        @property
        def shaft_hub_connection(self: "Part._Cast_Part") -> "_2619.ShaftHubConnection":
            from mastapy.system_model.part_model.couplings import _2619

            return self._parent._cast(_2619.ShaftHubConnection)

        @property
        def spring_damper(self: "Part._Cast_Part") -> "_2621.SpringDamper":
            from mastapy.system_model.part_model.couplings import _2621

            return self._parent._cast(_2621.SpringDamper)

        @property
        def spring_damper_half(self: "Part._Cast_Part") -> "_2622.SpringDamperHalf":
            from mastapy.system_model.part_model.couplings import _2622

            return self._parent._cast(_2622.SpringDamperHalf)

        @property
        def synchroniser(self: "Part._Cast_Part") -> "_2623.Synchroniser":
            from mastapy.system_model.part_model.couplings import _2623

            return self._parent._cast(_2623.Synchroniser)

        @property
        def synchroniser_half(self: "Part._Cast_Part") -> "_2625.SynchroniserHalf":
            from mastapy.system_model.part_model.couplings import _2625

            return self._parent._cast(_2625.SynchroniserHalf)

        @property
        def synchroniser_part(self: "Part._Cast_Part") -> "_2626.SynchroniserPart":
            from mastapy.system_model.part_model.couplings import _2626

            return self._parent._cast(_2626.SynchroniserPart)

        @property
        def synchroniser_sleeve(self: "Part._Cast_Part") -> "_2627.SynchroniserSleeve":
            from mastapy.system_model.part_model.couplings import _2627

            return self._parent._cast(_2627.SynchroniserSleeve)

        @property
        def torque_converter(self: "Part._Cast_Part") -> "_2628.TorqueConverter":
            from mastapy.system_model.part_model.couplings import _2628

            return self._parent._cast(_2628.TorqueConverter)

        @property
        def torque_converter_pump(
            self: "Part._Cast_Part",
        ) -> "_2629.TorqueConverterPump":
            from mastapy.system_model.part_model.couplings import _2629

            return self._parent._cast(_2629.TorqueConverterPump)

        @property
        def torque_converter_turbine(
            self: "Part._Cast_Part",
        ) -> "_2631.TorqueConverterTurbine":
            from mastapy.system_model.part_model.couplings import _2631

            return self._parent._cast(_2631.TorqueConverterTurbine)

        @property
        def part(self: "Part._Cast_Part") -> "Part":
            return self._parent

        def __getattr__(self: "Part._Cast_Part", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Part.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def two_d_drawing(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TwoDDrawing

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def two_d_drawing_full_model(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TwoDDrawingFullModel

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_isometric_view(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDIsometricView

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDView

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view_orientated_in_xy_plane_with_z_axis_pointing_into_the_screen(
        self: Self,
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDViewOrientatedInXyPlaneWithZAxisPointingIntoTheScreen

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view_orientated_in_xy_plane_with_z_axis_pointing_out_of_the_screen(
        self: Self,
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDViewOrientatedInXyPlaneWithZAxisPointingOutOfTheScreen

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view_orientated_in_xz_plane_with_y_axis_pointing_into_the_screen(
        self: Self,
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDViewOrientatedInXzPlaneWithYAxisPointingIntoTheScreen

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view_orientated_in_xz_plane_with_y_axis_pointing_out_of_the_screen(
        self: Self,
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDViewOrientatedInXzPlaneWithYAxisPointingOutOfTheScreen

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view_orientated_in_yz_plane_with_x_axis_pointing_into_the_screen(
        self: Self,
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDViewOrientatedInYzPlaneWithXAxisPointingIntoTheScreen

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view_orientated_in_yz_plane_with_x_axis_pointing_out_of_the_screen(
        self: Self,
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDViewOrientatedInYzPlaneWithXAxisPointingOutOfTheScreen

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def drawing_number(self: Self) -> "str":
        """str"""
        temp = self.wrapped.DrawingNumber

        if temp is None:
            return ""

        return temp

    @drawing_number.setter
    @enforce_parameter_types
    def drawing_number(self: Self, value: "str"):
        self.wrapped.DrawingNumber = str(value) if value is not None else ""

    @property
    def editable_name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.EditableName

        if temp is None:
            return ""

        return temp

    @editable_name.setter
    @enforce_parameter_types
    def editable_name(self: Self, value: "str"):
        self.wrapped.EditableName = str(value) if value is not None else ""

    @property
    def mass(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Mass

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @mass.setter
    @enforce_parameter_types
    def mass(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Mass = value

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
    def mass_properties_from_design(self: Self) -> "_1536.MassProperties":
        """mastapy.math_utility.MassProperties

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassPropertiesFromDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mass_properties_from_design_including_planetary_duplicates(
        self: Self,
    ) -> "_1536.MassProperties":
        """mastapy.math_utility.MassProperties

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassPropertiesFromDesignIncludingPlanetaryDuplicates

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connections(self: Self) -> "List[_2292.Connection]":
        """List[mastapy.system_model.connections_and_sockets.Connection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Connections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def local_connections(self: Self) -> "List[_2292.Connection]":
        """List[mastapy.system_model.connections_and_sockets.Connection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LocalConnections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def connections_to(self: Self, part: "Part") -> "List[_2292.Connection]":
        """List[mastapy.system_model.connections_and_sockets.Connection]

        Args:
            part (mastapy.system_model.part_model.Part)
        """
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.ConnectionsTo(part.wrapped if part else None)
        )

    @enforce_parameter_types
    def copy_to(self: Self, container: "_2453.Assembly") -> "Part":
        """mastapy.system_model.part_model.Part

        Args:
            container (mastapy.system_model.part_model.Assembly)
        """
        method_result = self.wrapped.CopyTo(container.wrapped if container else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def create_geometry_export_options(self: Self) -> "_2262.GeometryExportOptions":
        """mastapy.system_model.import_export.GeometryExportOptions"""
        method_result = self.wrapped.CreateGeometryExportOptions()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def delete_connections(self: Self):
        """Method does not return."""
        self.wrapped.DeleteConnections()

    @property
    def cast_to(self: Self) -> "Part._Cast_Part":
        return self._Cast_Part(self)
