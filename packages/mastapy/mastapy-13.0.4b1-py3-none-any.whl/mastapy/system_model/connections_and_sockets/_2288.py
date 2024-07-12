"""BeltConnection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets import _2301
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "BeltConnection"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2293, _2292
    from mastapy.system_model import _2223


__docformat__ = "restructuredtext en"
__all__ = ("BeltConnection",)


Self = TypeVar("Self", bound="BeltConnection")


class BeltConnection(_2301.InterMountableComponentConnection):
    """BeltConnection

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BeltConnection")

    class _Cast_BeltConnection:
        """Special nested class for casting BeltConnection to subclasses."""

        def __init__(
            self: "BeltConnection._Cast_BeltConnection", parent: "BeltConnection"
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection(
            self: "BeltConnection._Cast_BeltConnection",
        ) -> "_2301.InterMountableComponentConnection":
            return self._parent._cast(_2301.InterMountableComponentConnection)

        @property
        def connection(
            self: "BeltConnection._Cast_BeltConnection",
        ) -> "_2292.Connection":
            from mastapy.system_model.connections_and_sockets import _2292

            return self._parent._cast(_2292.Connection)

        @property
        def design_entity(
            self: "BeltConnection._Cast_BeltConnection",
        ) -> "_2223.DesignEntity":
            from mastapy.system_model import _2223

            return self._parent._cast(_2223.DesignEntity)

        @property
        def cvt_belt_connection(
            self: "BeltConnection._Cast_BeltConnection",
        ) -> "_2293.CVTBeltConnection":
            from mastapy.system_model.connections_and_sockets import _2293

            return self._parent._cast(_2293.CVTBeltConnection)

        @property
        def belt_connection(
            self: "BeltConnection._Cast_BeltConnection",
        ) -> "BeltConnection":
            return self._parent

        def __getattr__(self: "BeltConnection._Cast_BeltConnection", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BeltConnection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def stiffness_of_strand(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessOfStrand

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "BeltConnection._Cast_BeltConnection":
        return self._Cast_BeltConnection(self)
