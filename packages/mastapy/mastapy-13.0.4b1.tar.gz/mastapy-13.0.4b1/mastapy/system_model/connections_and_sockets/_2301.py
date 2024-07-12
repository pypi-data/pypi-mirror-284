"""InterMountableComponentConnection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.system_model.connections_and_sockets import _2292
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets",
    "InterMountableComponentConnection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2288, _2293, _2312
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
    from mastapy.system_model.connections_and_sockets.cycloidal import _2361
    from mastapy.system_model.connections_and_sockets.couplings import (
        _2362,
        _2364,
        _2366,
        _2368,
        _2370,
        _2372,
    )
    from mastapy.system_model import _2223


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnection",)


Self = TypeVar("Self", bound="InterMountableComponentConnection")


class InterMountableComponentConnection(_2292.Connection):
    """InterMountableComponentConnection

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_InterMountableComponentConnection")

    class _Cast_InterMountableComponentConnection:
        """Special nested class for casting InterMountableComponentConnection to subclasses."""

        def __init__(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
            parent: "InterMountableComponentConnection",
        ):
            self._parent = parent

        @property
        def connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2292.Connection":
            return self._parent._cast(_2292.Connection)

        @property
        def design_entity(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2223.DesignEntity":
            from mastapy.system_model import _2223

            return self._parent._cast(_2223.DesignEntity)

        @property
        def belt_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2288.BeltConnection":
            from mastapy.system_model.connections_and_sockets import _2288

            return self._parent._cast(_2288.BeltConnection)

        @property
        def cvt_belt_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2293.CVTBeltConnection":
            from mastapy.system_model.connections_and_sockets import _2293

            return self._parent._cast(_2293.CVTBeltConnection)

        @property
        def rolling_ring_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2312.RollingRingConnection":
            from mastapy.system_model.connections_and_sockets import _2312

            return self._parent._cast(_2312.RollingRingConnection)

        @property
        def agma_gleason_conical_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2319.AGMAGleasonConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2319

            return self._parent._cast(_2319.AGMAGleasonConicalGearMesh)

        @property
        def bevel_differential_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2321.BevelDifferentialGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2321

            return self._parent._cast(_2321.BevelDifferentialGearMesh)

        @property
        def bevel_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2323.BevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2323

            return self._parent._cast(_2323.BevelGearMesh)

        @property
        def concept_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2325.ConceptGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2325

            return self._parent._cast(_2325.ConceptGearMesh)

        @property
        def conical_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2327.ConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2327

            return self._parent._cast(_2327.ConicalGearMesh)

        @property
        def cylindrical_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2329.CylindricalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2329

            return self._parent._cast(_2329.CylindricalGearMesh)

        @property
        def face_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2331.FaceGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2331

            return self._parent._cast(_2331.FaceGearMesh)

        @property
        def gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2333.GearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2333

            return self._parent._cast(_2333.GearMesh)

        @property
        def hypoid_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2335.HypoidGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2335

            return self._parent._cast(_2335.HypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2338.KlingelnbergCycloPalloidConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2338

            return self._parent._cast(_2338.KlingelnbergCycloPalloidConicalGearMesh)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2339.KlingelnbergCycloPalloidHypoidGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2339

            return self._parent._cast(_2339.KlingelnbergCycloPalloidHypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2340.KlingelnbergCycloPalloidSpiralBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2340

            return self._parent._cast(_2340.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        @property
        def spiral_bevel_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2343.SpiralBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2343

            return self._parent._cast(_2343.SpiralBevelGearMesh)

        @property
        def straight_bevel_diff_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2345.StraightBevelDiffGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2345

            return self._parent._cast(_2345.StraightBevelDiffGearMesh)

        @property
        def straight_bevel_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2347.StraightBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2347

            return self._parent._cast(_2347.StraightBevelGearMesh)

        @property
        def worm_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2349.WormGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2349

            return self._parent._cast(_2349.WormGearMesh)

        @property
        def zerol_bevel_gear_mesh(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2351.ZerolBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2351

            return self._parent._cast(_2351.ZerolBevelGearMesh)

        @property
        def ring_pins_to_disc_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2361.RingPinsToDiscConnection":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2361

            return self._parent._cast(_2361.RingPinsToDiscConnection)

        @property
        def clutch_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2362.ClutchConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2362

            return self._parent._cast(_2362.ClutchConnection)

        @property
        def concept_coupling_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2364.ConceptCouplingConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2364

            return self._parent._cast(_2364.ConceptCouplingConnection)

        @property
        def coupling_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2366.CouplingConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2366

            return self._parent._cast(_2366.CouplingConnection)

        @property
        def part_to_part_shear_coupling_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2368.PartToPartShearCouplingConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2368

            return self._parent._cast(_2368.PartToPartShearCouplingConnection)

        @property
        def spring_damper_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2370.SpringDamperConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2370

            return self._parent._cast(_2370.SpringDamperConnection)

        @property
        def torque_converter_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "_2372.TorqueConverterConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2372

            return self._parent._cast(_2372.TorqueConverterConnection)

        @property
        def inter_mountable_component_connection(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
        ) -> "InterMountableComponentConnection":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnection._Cast_InterMountableComponentConnection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "InterMountableComponentConnection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def additional_modal_damping_ratio(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AdditionalModalDampingRatio

        if temp is None:
            return 0.0

        return temp

    @additional_modal_damping_ratio.setter
    @enforce_parameter_types
    def additional_modal_damping_ratio(self: Self, value: "float"):
        self.wrapped.AdditionalModalDampingRatio = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(
        self: Self,
    ) -> "InterMountableComponentConnection._Cast_InterMountableComponentConnection":
        return self._Cast_InterMountableComponentConnection(self)
