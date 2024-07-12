"""SpiralBevelGearMesh"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.gears import _2323
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "SpiralBevelGearMesh"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.spiral_bevel import _974
    from mastapy.system_model.connections_and_sockets.gears import _2319, _2327, _2333
    from mastapy.system_model.connections_and_sockets import _2301, _2292
    from mastapy.system_model import _2223


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMesh",)


Self = TypeVar("Self", bound="SpiralBevelGearMesh")


class SpiralBevelGearMesh(_2323.BevelGearMesh):
    """SpiralBevelGearMesh

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelGearMesh")

    class _Cast_SpiralBevelGearMesh:
        """Special nested class for casting SpiralBevelGearMesh to subclasses."""

        def __init__(
            self: "SpiralBevelGearMesh._Cast_SpiralBevelGearMesh",
            parent: "SpiralBevelGearMesh",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh(
            self: "SpiralBevelGearMesh._Cast_SpiralBevelGearMesh",
        ) -> "_2323.BevelGearMesh":
            return self._parent._cast(_2323.BevelGearMesh)

        @property
        def agma_gleason_conical_gear_mesh(
            self: "SpiralBevelGearMesh._Cast_SpiralBevelGearMesh",
        ) -> "_2319.AGMAGleasonConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2319

            return self._parent._cast(_2319.AGMAGleasonConicalGearMesh)

        @property
        def conical_gear_mesh(
            self: "SpiralBevelGearMesh._Cast_SpiralBevelGearMesh",
        ) -> "_2327.ConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2327

            return self._parent._cast(_2327.ConicalGearMesh)

        @property
        def gear_mesh(
            self: "SpiralBevelGearMesh._Cast_SpiralBevelGearMesh",
        ) -> "_2333.GearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2333

            return self._parent._cast(_2333.GearMesh)

        @property
        def inter_mountable_component_connection(
            self: "SpiralBevelGearMesh._Cast_SpiralBevelGearMesh",
        ) -> "_2301.InterMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2301

            return self._parent._cast(_2301.InterMountableComponentConnection)

        @property
        def connection(
            self: "SpiralBevelGearMesh._Cast_SpiralBevelGearMesh",
        ) -> "_2292.Connection":
            from mastapy.system_model.connections_and_sockets import _2292

            return self._parent._cast(_2292.Connection)

        @property
        def design_entity(
            self: "SpiralBevelGearMesh._Cast_SpiralBevelGearMesh",
        ) -> "_2223.DesignEntity":
            from mastapy.system_model import _2223

            return self._parent._cast(_2223.DesignEntity)

        @property
        def spiral_bevel_gear_mesh(
            self: "SpiralBevelGearMesh._Cast_SpiralBevelGearMesh",
        ) -> "SpiralBevelGearMesh":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearMesh._Cast_SpiralBevelGearMesh", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpiralBevelGearMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bevel_gear_mesh_design(self: Self) -> "_974.SpiralBevelGearMeshDesign":
        """mastapy.gears.gear_designs.spiral_bevel.SpiralBevelGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def spiral_bevel_gear_mesh_design(self: Self) -> "_974.SpiralBevelGearMeshDesign":
        """mastapy.gears.gear_designs.spiral_bevel.SpiralBevelGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "SpiralBevelGearMesh._Cast_SpiralBevelGearMesh":
        return self._Cast_SpiralBevelGearMesh(self)
