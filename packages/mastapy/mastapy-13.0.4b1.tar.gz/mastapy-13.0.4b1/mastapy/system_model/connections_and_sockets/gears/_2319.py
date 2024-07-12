"""AGMAGleasonConicalGearMesh"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets.gears import _2327
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "AGMAGleasonConicalGearMesh"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import (
        _2321,
        _2323,
        _2335,
        _2343,
        _2345,
        _2347,
        _2351,
        _2333,
    )
    from mastapy.system_model.connections_and_sockets import _2301, _2292
    from mastapy.system_model import _2223


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMesh",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMesh")


class AGMAGleasonConicalGearMesh(_2327.ConicalGearMesh):
    """AGMAGleasonConicalGearMesh

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGearMesh")

    class _Cast_AGMAGleasonConicalGearMesh:
        """Special nested class for casting AGMAGleasonConicalGearMesh to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
            parent: "AGMAGleasonConicalGearMesh",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "_2327.ConicalGearMesh":
            return self._parent._cast(_2327.ConicalGearMesh)

        @property
        def gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "_2333.GearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2333

            return self._parent._cast(_2333.GearMesh)

        @property
        def inter_mountable_component_connection(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "_2301.InterMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2301

            return self._parent._cast(_2301.InterMountableComponentConnection)

        @property
        def connection(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "_2292.Connection":
            from mastapy.system_model.connections_and_sockets import _2292

            return self._parent._cast(_2292.Connection)

        @property
        def design_entity(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "_2223.DesignEntity":
            from mastapy.system_model import _2223

            return self._parent._cast(_2223.DesignEntity)

        @property
        def bevel_differential_gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "_2321.BevelDifferentialGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2321

            return self._parent._cast(_2321.BevelDifferentialGearMesh)

        @property
        def bevel_gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "_2323.BevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2323

            return self._parent._cast(_2323.BevelGearMesh)

        @property
        def hypoid_gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "_2335.HypoidGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2335

            return self._parent._cast(_2335.HypoidGearMesh)

        @property
        def spiral_bevel_gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "_2343.SpiralBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2343

            return self._parent._cast(_2343.SpiralBevelGearMesh)

        @property
        def straight_bevel_diff_gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "_2345.StraightBevelDiffGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2345

            return self._parent._cast(_2345.StraightBevelDiffGearMesh)

        @property
        def straight_bevel_gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "_2347.StraightBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2347

            return self._parent._cast(_2347.StraightBevelGearMesh)

        @property
        def zerol_bevel_gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "_2351.ZerolBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2351

            return self._parent._cast(_2351.ZerolBevelGearMesh)

        @property
        def agma_gleason_conical_gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "AGMAGleasonConicalGearMesh":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMAGleasonConicalGearMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh":
        return self._Cast_AGMAGleasonConicalGearMesh(self)
