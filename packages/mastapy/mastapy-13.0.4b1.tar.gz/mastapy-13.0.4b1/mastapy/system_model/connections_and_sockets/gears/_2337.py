"""KlingelnbergConicalGearTeethSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets.gears import _2328
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CONICAL_GEAR_TEETH_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears",
    "KlingelnbergConicalGearTeethSocket",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2341, _2342, _2334
    from mastapy.system_model.connections_and_sockets import _2316


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergConicalGearTeethSocket",)


Self = TypeVar("Self", bound="KlingelnbergConicalGearTeethSocket")


class KlingelnbergConicalGearTeethSocket(_2328.ConicalGearTeethSocket):
    """KlingelnbergConicalGearTeethSocket

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CONICAL_GEAR_TEETH_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_KlingelnbergConicalGearTeethSocket")

    class _Cast_KlingelnbergConicalGearTeethSocket:
        """Special nested class for casting KlingelnbergConicalGearTeethSocket to subclasses."""

        def __init__(
            self: "KlingelnbergConicalGearTeethSocket._Cast_KlingelnbergConicalGearTeethSocket",
            parent: "KlingelnbergConicalGearTeethSocket",
        ):
            self._parent = parent

        @property
        def conical_gear_teeth_socket(
            self: "KlingelnbergConicalGearTeethSocket._Cast_KlingelnbergConicalGearTeethSocket",
        ) -> "_2328.ConicalGearTeethSocket":
            return self._parent._cast(_2328.ConicalGearTeethSocket)

        @property
        def gear_teeth_socket(
            self: "KlingelnbergConicalGearTeethSocket._Cast_KlingelnbergConicalGearTeethSocket",
        ) -> "_2334.GearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2334

            return self._parent._cast(_2334.GearTeethSocket)

        @property
        def socket(
            self: "KlingelnbergConicalGearTeethSocket._Cast_KlingelnbergConicalGearTeethSocket",
        ) -> "_2316.Socket":
            from mastapy.system_model.connections_and_sockets import _2316

            return self._parent._cast(_2316.Socket)

        @property
        def klingelnberg_hypoid_gear_teeth_socket(
            self: "KlingelnbergConicalGearTeethSocket._Cast_KlingelnbergConicalGearTeethSocket",
        ) -> "_2341.KlingelnbergHypoidGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2341

            return self._parent._cast(_2341.KlingelnbergHypoidGearTeethSocket)

        @property
        def klingelnberg_spiral_bevel_gear_teeth_socket(
            self: "KlingelnbergConicalGearTeethSocket._Cast_KlingelnbergConicalGearTeethSocket",
        ) -> "_2342.KlingelnbergSpiralBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2342

            return self._parent._cast(_2342.KlingelnbergSpiralBevelGearTeethSocket)

        @property
        def klingelnberg_conical_gear_teeth_socket(
            self: "KlingelnbergConicalGearTeethSocket._Cast_KlingelnbergConicalGearTeethSocket",
        ) -> "KlingelnbergConicalGearTeethSocket":
            return self._parent

        def __getattr__(
            self: "KlingelnbergConicalGearTeethSocket._Cast_KlingelnbergConicalGearTeethSocket",
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
        self: Self, instance_to_wrap: "KlingelnbergConicalGearTeethSocket.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergConicalGearTeethSocket._Cast_KlingelnbergConicalGearTeethSocket":
        return self._Cast_KlingelnbergConicalGearTeethSocket(self)
