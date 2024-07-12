"""StraightBevelDiffGearTeethSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets.gears import _2324
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_TEETH_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears",
    "StraightBevelDiffGearTeethSocket",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2320, _2328, _2334
    from mastapy.system_model.connections_and_sockets import _2316


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearTeethSocket",)


Self = TypeVar("Self", bound="StraightBevelDiffGearTeethSocket")


class StraightBevelDiffGearTeethSocket(_2324.BevelGearTeethSocket):
    """StraightBevelDiffGearTeethSocket

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_TEETH_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelDiffGearTeethSocket")

    class _Cast_StraightBevelDiffGearTeethSocket:
        """Special nested class for casting StraightBevelDiffGearTeethSocket to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearTeethSocket._Cast_StraightBevelDiffGearTeethSocket",
            parent: "StraightBevelDiffGearTeethSocket",
        ):
            self._parent = parent

        @property
        def bevel_gear_teeth_socket(
            self: "StraightBevelDiffGearTeethSocket._Cast_StraightBevelDiffGearTeethSocket",
        ) -> "_2324.BevelGearTeethSocket":
            return self._parent._cast(_2324.BevelGearTeethSocket)

        @property
        def agma_gleason_conical_gear_teeth_socket(
            self: "StraightBevelDiffGearTeethSocket._Cast_StraightBevelDiffGearTeethSocket",
        ) -> "_2320.AGMAGleasonConicalGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2320

            return self._parent._cast(_2320.AGMAGleasonConicalGearTeethSocket)

        @property
        def conical_gear_teeth_socket(
            self: "StraightBevelDiffGearTeethSocket._Cast_StraightBevelDiffGearTeethSocket",
        ) -> "_2328.ConicalGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2328

            return self._parent._cast(_2328.ConicalGearTeethSocket)

        @property
        def gear_teeth_socket(
            self: "StraightBevelDiffGearTeethSocket._Cast_StraightBevelDiffGearTeethSocket",
        ) -> "_2334.GearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2334

            return self._parent._cast(_2334.GearTeethSocket)

        @property
        def socket(
            self: "StraightBevelDiffGearTeethSocket._Cast_StraightBevelDiffGearTeethSocket",
        ) -> "_2316.Socket":
            from mastapy.system_model.connections_and_sockets import _2316

            return self._parent._cast(_2316.Socket)

        @property
        def straight_bevel_diff_gear_teeth_socket(
            self: "StraightBevelDiffGearTeethSocket._Cast_StraightBevelDiffGearTeethSocket",
        ) -> "StraightBevelDiffGearTeethSocket":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearTeethSocket._Cast_StraightBevelDiffGearTeethSocket",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelDiffGearTeethSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearTeethSocket._Cast_StraightBevelDiffGearTeethSocket":
        return self._Cast_StraightBevelDiffGearTeethSocket(self)
