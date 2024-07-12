"""BevelGearTeethSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets.gears import _2320
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_TEETH_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "BevelGearTeethSocket"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import (
        _2322,
        _2344,
        _2346,
        _2348,
        _2352,
        _2328,
        _2334,
    )
    from mastapy.system_model.connections_and_sockets import _2316


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearTeethSocket",)


Self = TypeVar("Self", bound="BevelGearTeethSocket")


class BevelGearTeethSocket(_2320.AGMAGleasonConicalGearTeethSocket):
    """BevelGearTeethSocket

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_TEETH_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearTeethSocket")

    class _Cast_BevelGearTeethSocket:
        """Special nested class for casting BevelGearTeethSocket to subclasses."""

        def __init__(
            self: "BevelGearTeethSocket._Cast_BevelGearTeethSocket",
            parent: "BevelGearTeethSocket",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_teeth_socket(
            self: "BevelGearTeethSocket._Cast_BevelGearTeethSocket",
        ) -> "_2320.AGMAGleasonConicalGearTeethSocket":
            return self._parent._cast(_2320.AGMAGleasonConicalGearTeethSocket)

        @property
        def conical_gear_teeth_socket(
            self: "BevelGearTeethSocket._Cast_BevelGearTeethSocket",
        ) -> "_2328.ConicalGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2328

            return self._parent._cast(_2328.ConicalGearTeethSocket)

        @property
        def gear_teeth_socket(
            self: "BevelGearTeethSocket._Cast_BevelGearTeethSocket",
        ) -> "_2334.GearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2334

            return self._parent._cast(_2334.GearTeethSocket)

        @property
        def socket(
            self: "BevelGearTeethSocket._Cast_BevelGearTeethSocket",
        ) -> "_2316.Socket":
            from mastapy.system_model.connections_and_sockets import _2316

            return self._parent._cast(_2316.Socket)

        @property
        def bevel_differential_gear_teeth_socket(
            self: "BevelGearTeethSocket._Cast_BevelGearTeethSocket",
        ) -> "_2322.BevelDifferentialGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2322

            return self._parent._cast(_2322.BevelDifferentialGearTeethSocket)

        @property
        def spiral_bevel_gear_teeth_socket(
            self: "BevelGearTeethSocket._Cast_BevelGearTeethSocket",
        ) -> "_2344.SpiralBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2344

            return self._parent._cast(_2344.SpiralBevelGearTeethSocket)

        @property
        def straight_bevel_diff_gear_teeth_socket(
            self: "BevelGearTeethSocket._Cast_BevelGearTeethSocket",
        ) -> "_2346.StraightBevelDiffGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2346

            return self._parent._cast(_2346.StraightBevelDiffGearTeethSocket)

        @property
        def straight_bevel_gear_teeth_socket(
            self: "BevelGearTeethSocket._Cast_BevelGearTeethSocket",
        ) -> "_2348.StraightBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2348

            return self._parent._cast(_2348.StraightBevelGearTeethSocket)

        @property
        def zerol_bevel_gear_teeth_socket(
            self: "BevelGearTeethSocket._Cast_BevelGearTeethSocket",
        ) -> "_2352.ZerolBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2352

            return self._parent._cast(_2352.ZerolBevelGearTeethSocket)

        @property
        def bevel_gear_teeth_socket(
            self: "BevelGearTeethSocket._Cast_BevelGearTeethSocket",
        ) -> "BevelGearTeethSocket":
            return self._parent

        def __getattr__(
            self: "BevelGearTeethSocket._Cast_BevelGearTeethSocket", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearTeethSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "BevelGearTeethSocket._Cast_BevelGearTeethSocket":
        return self._Cast_BevelGearTeethSocket(self)
