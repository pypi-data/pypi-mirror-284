"""ShaftSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets import _2296
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "ShaftSocket"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import (
        _2299,
        _2300,
        _2305,
        _2306,
        _2316,
    )
    from mastapy.system_model.connections_and_sockets.cycloidal import (
        _2353,
        _2354,
        _2356,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ShaftSocket",)


Self = TypeVar("Self", bound="ShaftSocket")


class ShaftSocket(_2296.CylindricalSocket):
    """ShaftSocket

    This is a mastapy class.
    """

    TYPE = _SHAFT_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftSocket")

    class _Cast_ShaftSocket:
        """Special nested class for casting ShaftSocket to subclasses."""

        def __init__(self: "ShaftSocket._Cast_ShaftSocket", parent: "ShaftSocket"):
            self._parent = parent

        @property
        def cylindrical_socket(
            self: "ShaftSocket._Cast_ShaftSocket",
        ) -> "_2296.CylindricalSocket":
            return self._parent._cast(_2296.CylindricalSocket)

        @property
        def socket(self: "ShaftSocket._Cast_ShaftSocket") -> "_2316.Socket":
            from mastapy.system_model.connections_and_sockets import _2316

            return self._parent._cast(_2316.Socket)

        @property
        def inner_shaft_socket(
            self: "ShaftSocket._Cast_ShaftSocket",
        ) -> "_2299.InnerShaftSocket":
            from mastapy.system_model.connections_and_sockets import _2299

            return self._parent._cast(_2299.InnerShaftSocket)

        @property
        def inner_shaft_socket_base(
            self: "ShaftSocket._Cast_ShaftSocket",
        ) -> "_2300.InnerShaftSocketBase":
            from mastapy.system_model.connections_and_sockets import _2300

            return self._parent._cast(_2300.InnerShaftSocketBase)

        @property
        def outer_shaft_socket(
            self: "ShaftSocket._Cast_ShaftSocket",
        ) -> "_2305.OuterShaftSocket":
            from mastapy.system_model.connections_and_sockets import _2305

            return self._parent._cast(_2305.OuterShaftSocket)

        @property
        def outer_shaft_socket_base(
            self: "ShaftSocket._Cast_ShaftSocket",
        ) -> "_2306.OuterShaftSocketBase":
            from mastapy.system_model.connections_and_sockets import _2306

            return self._parent._cast(_2306.OuterShaftSocketBase)

        @property
        def cycloidal_disc_axial_left_socket(
            self: "ShaftSocket._Cast_ShaftSocket",
        ) -> "_2353.CycloidalDiscAxialLeftSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2353

            return self._parent._cast(_2353.CycloidalDiscAxialLeftSocket)

        @property
        def cycloidal_disc_axial_right_socket(
            self: "ShaftSocket._Cast_ShaftSocket",
        ) -> "_2354.CycloidalDiscAxialRightSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2354

            return self._parent._cast(_2354.CycloidalDiscAxialRightSocket)

        @property
        def cycloidal_disc_inner_socket(
            self: "ShaftSocket._Cast_ShaftSocket",
        ) -> "_2356.CycloidalDiscInnerSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2356

            return self._parent._cast(_2356.CycloidalDiscInnerSocket)

        @property
        def shaft_socket(self: "ShaftSocket._Cast_ShaftSocket") -> "ShaftSocket":
            return self._parent

        def __getattr__(self: "ShaftSocket._Cast_ShaftSocket", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ShaftSocket._Cast_ShaftSocket":
        return self._Cast_ShaftSocket(self)
