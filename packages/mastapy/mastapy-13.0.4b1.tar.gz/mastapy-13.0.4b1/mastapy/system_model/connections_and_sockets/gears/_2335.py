"""HypoidGearMesh"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.gears import _2319
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "HypoidGearMesh"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.hypoid import _990
    from mastapy.system_model.connections_and_sockets.gears import _2327, _2333
    from mastapy.system_model.connections_and_sockets import _2301, _2292
    from mastapy.system_model import _2223


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearMesh",)


Self = TypeVar("Self", bound="HypoidGearMesh")


class HypoidGearMesh(_2319.AGMAGleasonConicalGearMesh):
    """HypoidGearMesh

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearMesh")

    class _Cast_HypoidGearMesh:
        """Special nested class for casting HypoidGearMesh to subclasses."""

        def __init__(
            self: "HypoidGearMesh._Cast_HypoidGearMesh", parent: "HypoidGearMesh"
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh(
            self: "HypoidGearMesh._Cast_HypoidGearMesh",
        ) -> "_2319.AGMAGleasonConicalGearMesh":
            return self._parent._cast(_2319.AGMAGleasonConicalGearMesh)

        @property
        def conical_gear_mesh(
            self: "HypoidGearMesh._Cast_HypoidGearMesh",
        ) -> "_2327.ConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2327

            return self._parent._cast(_2327.ConicalGearMesh)

        @property
        def gear_mesh(self: "HypoidGearMesh._Cast_HypoidGearMesh") -> "_2333.GearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2333

            return self._parent._cast(_2333.GearMesh)

        @property
        def inter_mountable_component_connection(
            self: "HypoidGearMesh._Cast_HypoidGearMesh",
        ) -> "_2301.InterMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2301

            return self._parent._cast(_2301.InterMountableComponentConnection)

        @property
        def connection(
            self: "HypoidGearMesh._Cast_HypoidGearMesh",
        ) -> "_2292.Connection":
            from mastapy.system_model.connections_and_sockets import _2292

            return self._parent._cast(_2292.Connection)

        @property
        def design_entity(
            self: "HypoidGearMesh._Cast_HypoidGearMesh",
        ) -> "_2223.DesignEntity":
            from mastapy.system_model import _2223

            return self._parent._cast(_2223.DesignEntity)

        @property
        def hypoid_gear_mesh(
            self: "HypoidGearMesh._Cast_HypoidGearMesh",
        ) -> "HypoidGearMesh":
            return self._parent

        def __getattr__(self: "HypoidGearMesh._Cast_HypoidGearMesh", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_gear_mesh_design(self: Self) -> "_990.HypoidGearMeshDesign":
        """mastapy.gears.gear_designs.hypoid.HypoidGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def hypoid_gear_mesh_design(self: Self) -> "_990.HypoidGearMeshDesign":
        """mastapy.gears.gear_designs.hypoid.HypoidGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "HypoidGearMesh._Cast_HypoidGearMesh":
        return self._Cast_HypoidGearMesh(self)
