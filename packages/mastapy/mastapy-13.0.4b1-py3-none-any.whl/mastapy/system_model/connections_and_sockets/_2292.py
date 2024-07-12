"""Connection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.python_net import python_net_import
from mastapy.system_model import _2223
from mastapy._internal.cast_exception import CastException

_COMPONENT = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Component")
_SOCKET = python_net_import("SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "Socket")
_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "Connection"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2464
    from mastapy.system_model.connections_and_sockets import (
        _2316,
        _2285,
        _2288,
        _2289,
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


__docformat__ = "restructuredtext en"
__all__ = ("Connection",)


Self = TypeVar("Self", bound="Connection")


class Connection(_2223.DesignEntity):
    """Connection

    This is a mastapy class.
    """

    TYPE = _CONNECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Connection")

    class _Cast_Connection:
        """Special nested class for casting Connection to subclasses."""

        def __init__(self: "Connection._Cast_Connection", parent: "Connection"):
            self._parent = parent

        @property
        def design_entity(self: "Connection._Cast_Connection") -> "_2223.DesignEntity":
            return self._parent._cast(_2223.DesignEntity)

        @property
        def abstract_shaft_to_mountable_component_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2285.AbstractShaftToMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2285

            return self._parent._cast(_2285.AbstractShaftToMountableComponentConnection)

        @property
        def belt_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2288.BeltConnection":
            from mastapy.system_model.connections_and_sockets import _2288

            return self._parent._cast(_2288.BeltConnection)

        @property
        def coaxial_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2289.CoaxialConnection":
            from mastapy.system_model.connections_and_sockets import _2289

            return self._parent._cast(_2289.CoaxialConnection)

        @property
        def cvt_belt_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2293.CVTBeltConnection":
            from mastapy.system_model.connections_and_sockets import _2293

            return self._parent._cast(_2293.CVTBeltConnection)

        @property
        def inter_mountable_component_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2301.InterMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2301

            return self._parent._cast(_2301.InterMountableComponentConnection)

        @property
        def planetary_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2307.PlanetaryConnection":
            from mastapy.system_model.connections_and_sockets import _2307

            return self._parent._cast(_2307.PlanetaryConnection)

        @property
        def rolling_ring_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2312.RollingRingConnection":
            from mastapy.system_model.connections_and_sockets import _2312

            return self._parent._cast(_2312.RollingRingConnection)

        @property
        def shaft_to_mountable_component_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2315.ShaftToMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2315

            return self._parent._cast(_2315.ShaftToMountableComponentConnection)

        @property
        def agma_gleason_conical_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2319.AGMAGleasonConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2319

            return self._parent._cast(_2319.AGMAGleasonConicalGearMesh)

        @property
        def bevel_differential_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2321.BevelDifferentialGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2321

            return self._parent._cast(_2321.BevelDifferentialGearMesh)

        @property
        def bevel_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2323.BevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2323

            return self._parent._cast(_2323.BevelGearMesh)

        @property
        def concept_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2325.ConceptGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2325

            return self._parent._cast(_2325.ConceptGearMesh)

        @property
        def conical_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2327.ConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2327

            return self._parent._cast(_2327.ConicalGearMesh)

        @property
        def cylindrical_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2329.CylindricalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2329

            return self._parent._cast(_2329.CylindricalGearMesh)

        @property
        def face_gear_mesh(self: "Connection._Cast_Connection") -> "_2331.FaceGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2331

            return self._parent._cast(_2331.FaceGearMesh)

        @property
        def gear_mesh(self: "Connection._Cast_Connection") -> "_2333.GearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2333

            return self._parent._cast(_2333.GearMesh)

        @property
        def hypoid_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2335.HypoidGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2335

            return self._parent._cast(_2335.HypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2338.KlingelnbergCycloPalloidConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2338

            return self._parent._cast(_2338.KlingelnbergCycloPalloidConicalGearMesh)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2339.KlingelnbergCycloPalloidHypoidGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2339

            return self._parent._cast(_2339.KlingelnbergCycloPalloidHypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2340.KlingelnbergCycloPalloidSpiralBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2340

            return self._parent._cast(_2340.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        @property
        def spiral_bevel_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2343.SpiralBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2343

            return self._parent._cast(_2343.SpiralBevelGearMesh)

        @property
        def straight_bevel_diff_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2345.StraightBevelDiffGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2345

            return self._parent._cast(_2345.StraightBevelDiffGearMesh)

        @property
        def straight_bevel_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2347.StraightBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2347

            return self._parent._cast(_2347.StraightBevelGearMesh)

        @property
        def worm_gear_mesh(self: "Connection._Cast_Connection") -> "_2349.WormGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2349

            return self._parent._cast(_2349.WormGearMesh)

        @property
        def zerol_bevel_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2351.ZerolBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2351

            return self._parent._cast(_2351.ZerolBevelGearMesh)

        @property
        def cycloidal_disc_central_bearing_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2355.CycloidalDiscCentralBearingConnection":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2355

            return self._parent._cast(_2355.CycloidalDiscCentralBearingConnection)

        @property
        def cycloidal_disc_planetary_bearing_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2358.CycloidalDiscPlanetaryBearingConnection":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2358

            return self._parent._cast(_2358.CycloidalDiscPlanetaryBearingConnection)

        @property
        def ring_pins_to_disc_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2361.RingPinsToDiscConnection":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2361

            return self._parent._cast(_2361.RingPinsToDiscConnection)

        @property
        def clutch_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2362.ClutchConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2362

            return self._parent._cast(_2362.ClutchConnection)

        @property
        def concept_coupling_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2364.ConceptCouplingConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2364

            return self._parent._cast(_2364.ConceptCouplingConnection)

        @property
        def coupling_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2366.CouplingConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2366

            return self._parent._cast(_2366.CouplingConnection)

        @property
        def part_to_part_shear_coupling_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2368.PartToPartShearCouplingConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2368

            return self._parent._cast(_2368.PartToPartShearCouplingConnection)

        @property
        def spring_damper_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2370.SpringDamperConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2370

            return self._parent._cast(_2370.SpringDamperConnection)

        @property
        def torque_converter_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2372.TorqueConverterConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2372

            return self._parent._cast(_2372.TorqueConverterConnection)

        @property
        def connection(self: "Connection._Cast_Connection") -> "Connection":
            return self._parent

        def __getattr__(self: "Connection._Cast_Connection", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Connection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_id(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionID

        if temp is None:
            return ""

        return temp

    @property
    def drawing_position(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.DrawingPosition

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @drawing_position.setter
    @enforce_parameter_types
    def drawing_position(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.DrawingPosition = value

    @property
    def speed_ratio_from_a_to_b(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpeedRatioFromAToB

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_ratio_from_a_to_b(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueRatioFromAToB

        if temp is None:
            return 0.0

        return temp

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
    def owner_a(self: Self) -> "_2464.Component":
        """mastapy.system_model.part_model.Component

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OwnerA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def owner_b(self: Self) -> "_2464.Component":
        """mastapy.system_model.part_model.Component

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OwnerB

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def socket_a(self: Self) -> "_2316.Socket":
        """mastapy.system_model.connections_and_sockets.Socket

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SocketA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def socket_b(self: Self) -> "_2316.Socket":
        """mastapy.system_model.connections_and_sockets.Socket

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SocketB

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @enforce_parameter_types
    def other_owner(self: Self, component: "_2464.Component") -> "_2464.Component":
        """mastapy.system_model.part_model.Component

        Args:
            component (mastapy.system_model.part_model.Component)
        """
        method_result = self.wrapped.OtherOwner(
            component.wrapped if component else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def other_socket_for_component(
        self: Self, component: "_2464.Component"
    ) -> "_2316.Socket":
        """mastapy.system_model.connections_and_sockets.Socket

        Args:
            component (mastapy.system_model.part_model.Component)
        """
        method_result = self.wrapped.OtherSocket.Overloads[_COMPONENT](
            component.wrapped if component else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def other_socket(self: Self, socket: "_2316.Socket") -> "_2316.Socket":
        """mastapy.system_model.connections_and_sockets.Socket

        Args:
            socket (mastapy.system_model.connections_and_sockets.Socket)
        """
        method_result = self.wrapped.OtherSocket.Overloads[_SOCKET](
            socket.wrapped if socket else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def socket_for(self: Self, component: "_2464.Component") -> "_2316.Socket":
        """mastapy.system_model.connections_and_sockets.Socket

        Args:
            component (mastapy.system_model.part_model.Component)
        """
        method_result = self.wrapped.SocketFor(component.wrapped if component else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "Connection._Cast_Connection":
        return self._Cast_Connection(self)
