"""MountableComponent"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.system_model.part_model import _2464
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "MountableComponent"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import (
        _2455,
        _2465,
        _2459,
        _2467,
        _2482,
        _2483,
        _2486,
        _2489,
        _2491,
        _2492,
        _2497,
        _2499,
        _2488,
    )
    from mastapy.system_model.connections_and_sockets import _2292, _2296, _2289
    from mastapy.system_model.part_model.gears import (
        _2533,
        _2535,
        _2537,
        _2538,
        _2539,
        _2541,
        _2543,
        _2545,
        _2547,
        _2548,
        _2550,
        _2554,
        _2556,
        _2558,
        _2560,
        _2563,
        _2565,
        _2567,
        _2569,
        _2570,
        _2571,
        _2573,
    )
    from mastapy.system_model.part_model.cycloidal import _2590
    from mastapy.system_model.part_model.couplings import (
        _2599,
        _2602,
        _2605,
        _2608,
        _2610,
        _2611,
        _2617,
        _2619,
        _2622,
        _2625,
        _2626,
        _2627,
        _2629,
        _2631,
    )
    from mastapy.system_model import _2223


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponent",)


Self = TypeVar("Self", bound="MountableComponent")


class MountableComponent(_2464.Component):
    """MountableComponent

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MountableComponent")

    class _Cast_MountableComponent:
        """Special nested class for casting MountableComponent to subclasses."""

        def __init__(
            self: "MountableComponent._Cast_MountableComponent",
            parent: "MountableComponent",
        ):
            self._parent = parent

        @property
        def component(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2464.Component":
            return self._parent._cast(_2464.Component)

        @property
        def part(self: "MountableComponent._Cast_MountableComponent") -> "_2488.Part":
            from mastapy.system_model.part_model import _2488

            return self._parent._cast(_2488.Part)

        @property
        def design_entity(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2223.DesignEntity":
            from mastapy.system_model import _2223

            return self._parent._cast(_2223.DesignEntity)

        @property
        def bearing(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2459.Bearing":
            from mastapy.system_model.part_model import _2459

            return self._parent._cast(_2459.Bearing)

        @property
        def connector(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2467.Connector":
            from mastapy.system_model.part_model import _2467

            return self._parent._cast(_2467.Connector)

        @property
        def mass_disc(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2482.MassDisc":
            from mastapy.system_model.part_model import _2482

            return self._parent._cast(_2482.MassDisc)

        @property
        def measurement_component(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2483.MeasurementComponent":
            from mastapy.system_model.part_model import _2483

            return self._parent._cast(_2483.MeasurementComponent)

        @property
        def oil_seal(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2486.OilSeal":
            from mastapy.system_model.part_model import _2486

            return self._parent._cast(_2486.OilSeal)

        @property
        def planet_carrier(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2489.PlanetCarrier":
            from mastapy.system_model.part_model import _2489

            return self._parent._cast(_2489.PlanetCarrier)

        @property
        def point_load(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2491.PointLoad":
            from mastapy.system_model.part_model import _2491

            return self._parent._cast(_2491.PointLoad)

        @property
        def power_load(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2492.PowerLoad":
            from mastapy.system_model.part_model import _2492

            return self._parent._cast(_2492.PowerLoad)

        @property
        def unbalanced_mass(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2497.UnbalancedMass":
            from mastapy.system_model.part_model import _2497

            return self._parent._cast(_2497.UnbalancedMass)

        @property
        def virtual_component(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2499.VirtualComponent":
            from mastapy.system_model.part_model import _2499

            return self._parent._cast(_2499.VirtualComponent)

        @property
        def agma_gleason_conical_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2533.AGMAGleasonConicalGear":
            from mastapy.system_model.part_model.gears import _2533

            return self._parent._cast(_2533.AGMAGleasonConicalGear)

        @property
        def bevel_differential_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2535.BevelDifferentialGear":
            from mastapy.system_model.part_model.gears import _2535

            return self._parent._cast(_2535.BevelDifferentialGear)

        @property
        def bevel_differential_planet_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2537.BevelDifferentialPlanetGear":
            from mastapy.system_model.part_model.gears import _2537

            return self._parent._cast(_2537.BevelDifferentialPlanetGear)

        @property
        def bevel_differential_sun_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2538.BevelDifferentialSunGear":
            from mastapy.system_model.part_model.gears import _2538

            return self._parent._cast(_2538.BevelDifferentialSunGear)

        @property
        def bevel_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2539.BevelGear":
            from mastapy.system_model.part_model.gears import _2539

            return self._parent._cast(_2539.BevelGear)

        @property
        def concept_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2541.ConceptGear":
            from mastapy.system_model.part_model.gears import _2541

            return self._parent._cast(_2541.ConceptGear)

        @property
        def conical_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2543.ConicalGear":
            from mastapy.system_model.part_model.gears import _2543

            return self._parent._cast(_2543.ConicalGear)

        @property
        def cylindrical_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2545.CylindricalGear":
            from mastapy.system_model.part_model.gears import _2545

            return self._parent._cast(_2545.CylindricalGear)

        @property
        def cylindrical_planet_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2547.CylindricalPlanetGear":
            from mastapy.system_model.part_model.gears import _2547

            return self._parent._cast(_2547.CylindricalPlanetGear)

        @property
        def face_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2548.FaceGear":
            from mastapy.system_model.part_model.gears import _2548

            return self._parent._cast(_2548.FaceGear)

        @property
        def gear(self: "MountableComponent._Cast_MountableComponent") -> "_2550.Gear":
            from mastapy.system_model.part_model.gears import _2550

            return self._parent._cast(_2550.Gear)

        @property
        def hypoid_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2554.HypoidGear":
            from mastapy.system_model.part_model.gears import _2554

            return self._parent._cast(_2554.HypoidGear)

        @property
        def klingelnberg_cyclo_palloid_conical_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2556.KlingelnbergCycloPalloidConicalGear":
            from mastapy.system_model.part_model.gears import _2556

            return self._parent._cast(_2556.KlingelnbergCycloPalloidConicalGear)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2558.KlingelnbergCycloPalloidHypoidGear":
            from mastapy.system_model.part_model.gears import _2558

            return self._parent._cast(_2558.KlingelnbergCycloPalloidHypoidGear)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2560.KlingelnbergCycloPalloidSpiralBevelGear":
            from mastapy.system_model.part_model.gears import _2560

            return self._parent._cast(_2560.KlingelnbergCycloPalloidSpiralBevelGear)

        @property
        def spiral_bevel_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2563.SpiralBevelGear":
            from mastapy.system_model.part_model.gears import _2563

            return self._parent._cast(_2563.SpiralBevelGear)

        @property
        def straight_bevel_diff_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2565.StraightBevelDiffGear":
            from mastapy.system_model.part_model.gears import _2565

            return self._parent._cast(_2565.StraightBevelDiffGear)

        @property
        def straight_bevel_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2567.StraightBevelGear":
            from mastapy.system_model.part_model.gears import _2567

            return self._parent._cast(_2567.StraightBevelGear)

        @property
        def straight_bevel_planet_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2569.StraightBevelPlanetGear":
            from mastapy.system_model.part_model.gears import _2569

            return self._parent._cast(_2569.StraightBevelPlanetGear)

        @property
        def straight_bevel_sun_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2570.StraightBevelSunGear":
            from mastapy.system_model.part_model.gears import _2570

            return self._parent._cast(_2570.StraightBevelSunGear)

        @property
        def worm_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2571.WormGear":
            from mastapy.system_model.part_model.gears import _2571

            return self._parent._cast(_2571.WormGear)

        @property
        def zerol_bevel_gear(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2573.ZerolBevelGear":
            from mastapy.system_model.part_model.gears import _2573

            return self._parent._cast(_2573.ZerolBevelGear)

        @property
        def ring_pins(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2590.RingPins":
            from mastapy.system_model.part_model.cycloidal import _2590

            return self._parent._cast(_2590.RingPins)

        @property
        def clutch_half(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2599.ClutchHalf":
            from mastapy.system_model.part_model.couplings import _2599

            return self._parent._cast(_2599.ClutchHalf)

        @property
        def concept_coupling_half(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2602.ConceptCouplingHalf":
            from mastapy.system_model.part_model.couplings import _2602

            return self._parent._cast(_2602.ConceptCouplingHalf)

        @property
        def coupling_half(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2605.CouplingHalf":
            from mastapy.system_model.part_model.couplings import _2605

            return self._parent._cast(_2605.CouplingHalf)

        @property
        def cvt_pulley(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2608.CVTPulley":
            from mastapy.system_model.part_model.couplings import _2608

            return self._parent._cast(_2608.CVTPulley)

        @property
        def part_to_part_shear_coupling_half(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2610.PartToPartShearCouplingHalf":
            from mastapy.system_model.part_model.couplings import _2610

            return self._parent._cast(_2610.PartToPartShearCouplingHalf)

        @property
        def pulley(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2611.Pulley":
            from mastapy.system_model.part_model.couplings import _2611

            return self._parent._cast(_2611.Pulley)

        @property
        def rolling_ring(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2617.RollingRing":
            from mastapy.system_model.part_model.couplings import _2617

            return self._parent._cast(_2617.RollingRing)

        @property
        def shaft_hub_connection(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2619.ShaftHubConnection":
            from mastapy.system_model.part_model.couplings import _2619

            return self._parent._cast(_2619.ShaftHubConnection)

        @property
        def spring_damper_half(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2622.SpringDamperHalf":
            from mastapy.system_model.part_model.couplings import _2622

            return self._parent._cast(_2622.SpringDamperHalf)

        @property
        def synchroniser_half(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2625.SynchroniserHalf":
            from mastapy.system_model.part_model.couplings import _2625

            return self._parent._cast(_2625.SynchroniserHalf)

        @property
        def synchroniser_part(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2626.SynchroniserPart":
            from mastapy.system_model.part_model.couplings import _2626

            return self._parent._cast(_2626.SynchroniserPart)

        @property
        def synchroniser_sleeve(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2627.SynchroniserSleeve":
            from mastapy.system_model.part_model.couplings import _2627

            return self._parent._cast(_2627.SynchroniserSleeve)

        @property
        def torque_converter_pump(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2629.TorqueConverterPump":
            from mastapy.system_model.part_model.couplings import _2629

            return self._parent._cast(_2629.TorqueConverterPump)

        @property
        def torque_converter_turbine(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "_2631.TorqueConverterTurbine":
            from mastapy.system_model.part_model.couplings import _2631

            return self._parent._cast(_2631.TorqueConverterTurbine)

        @property
        def mountable_component(
            self: "MountableComponent._Cast_MountableComponent",
        ) -> "MountableComponent":
            return self._parent

        def __getattr__(self: "MountableComponent._Cast_MountableComponent", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MountableComponent.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rotation_about_axis(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RotationAboutAxis

        if temp is None:
            return 0.0

        return temp

    @rotation_about_axis.setter
    @enforce_parameter_types
    def rotation_about_axis(self: Self, value: "float"):
        self.wrapped.RotationAboutAxis = float(value) if value is not None else 0.0

    @property
    def inner_component(self: Self) -> "_2455.AbstractShaft":
        """mastapy.system_model.part_model.AbstractShaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerComponent

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_connection(self: Self) -> "_2292.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerConnection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_socket(self: Self) -> "_2296.CylindricalSocket":
        """mastapy.system_model.connections_and_sockets.CylindricalSocket

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerSocket

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def is_mounted(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsMounted

        if temp is None:
            return False

        return temp

    @enforce_parameter_types
    def mount_on(
        self: Self, shaft: "_2455.AbstractShaft", offset: "float" = float("nan")
    ) -> "_2289.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Args:
            shaft (mastapy.system_model.part_model.AbstractShaft)
            offset (float, optional)
        """
        offset = float(offset)
        method_result = self.wrapped.MountOn(
            shaft.wrapped if shaft else None, offset if offset else 0.0
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def try_mount_on(
        self: Self, shaft: "_2455.AbstractShaft", offset: "float" = float("nan")
    ) -> "_2465.ComponentsConnectedResult":
        """mastapy.system_model.part_model.ComponentsConnectedResult

        Args:
            shaft (mastapy.system_model.part_model.AbstractShaft)
            offset (float, optional)
        """
        offset = float(offset)
        method_result = self.wrapped.TryMountOn(
            shaft.wrapped if shaft else None, offset if offset else 0.0
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "MountableComponent._Cast_MountableComponent":
        return self._Cast_MountableComponent(self)
