"""StraightBevelDiffGearMesh"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.gears import _2323
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "StraightBevelDiffGearMesh"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.straight_bevel_diff import _970
    from mastapy.system_model.connections_and_sockets.gears import _2319, _2327, _2333
    from mastapy.system_model.connections_and_sockets import _2301, _2292
    from mastapy.system_model import _2223


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearMesh",)


Self = TypeVar("Self", bound="StraightBevelDiffGearMesh")


class StraightBevelDiffGearMesh(_2323.BevelGearMesh):
    """StraightBevelDiffGearMesh

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelDiffGearMesh")

    class _Cast_StraightBevelDiffGearMesh:
        """Special nested class for casting StraightBevelDiffGearMesh to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearMesh._Cast_StraightBevelDiffGearMesh",
            parent: "StraightBevelDiffGearMesh",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh(
            self: "StraightBevelDiffGearMesh._Cast_StraightBevelDiffGearMesh",
        ) -> "_2323.BevelGearMesh":
            return self._parent._cast(_2323.BevelGearMesh)

        @property
        def agma_gleason_conical_gear_mesh(
            self: "StraightBevelDiffGearMesh._Cast_StraightBevelDiffGearMesh",
        ) -> "_2319.AGMAGleasonConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2319

            return self._parent._cast(_2319.AGMAGleasonConicalGearMesh)

        @property
        def conical_gear_mesh(
            self: "StraightBevelDiffGearMesh._Cast_StraightBevelDiffGearMesh",
        ) -> "_2327.ConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2327

            return self._parent._cast(_2327.ConicalGearMesh)

        @property
        def gear_mesh(
            self: "StraightBevelDiffGearMesh._Cast_StraightBevelDiffGearMesh",
        ) -> "_2333.GearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2333

            return self._parent._cast(_2333.GearMesh)

        @property
        def inter_mountable_component_connection(
            self: "StraightBevelDiffGearMesh._Cast_StraightBevelDiffGearMesh",
        ) -> "_2301.InterMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2301

            return self._parent._cast(_2301.InterMountableComponentConnection)

        @property
        def connection(
            self: "StraightBevelDiffGearMesh._Cast_StraightBevelDiffGearMesh",
        ) -> "_2292.Connection":
            from mastapy.system_model.connections_and_sockets import _2292

            return self._parent._cast(_2292.Connection)

        @property
        def design_entity(
            self: "StraightBevelDiffGearMesh._Cast_StraightBevelDiffGearMesh",
        ) -> "_2223.DesignEntity":
            from mastapy.system_model import _2223

            return self._parent._cast(_2223.DesignEntity)

        @property
        def straight_bevel_diff_gear_mesh(
            self: "StraightBevelDiffGearMesh._Cast_StraightBevelDiffGearMesh",
        ) -> "StraightBevelDiffGearMesh":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearMesh._Cast_StraightBevelDiffGearMesh", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelDiffGearMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bevel_gear_mesh_design(self: Self) -> "_970.StraightBevelDiffGearMeshDesign":
        """mastapy.gears.gear_designs.straight_bevel_diff.StraightBevelDiffGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def straight_bevel_diff_gear_mesh_design(
        self: Self,
    ) -> "_970.StraightBevelDiffGearMeshDesign":
        """mastapy.gears.gear_designs.straight_bevel_diff.StraightBevelDiffGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearMesh._Cast_StraightBevelDiffGearMesh":
        return self._Cast_StraightBevelDiffGearMesh(self)
