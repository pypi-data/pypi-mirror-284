"""AbstractShaftToMountableComponentConnection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets import _2292
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets",
    "AbstractShaftToMountableComponentConnection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2484, _2455
    from mastapy.system_model.connections_and_sockets import _2289, _2307, _2315
    from mastapy.system_model.connections_and_sockets.cycloidal import _2355, _2358
    from mastapy.system_model import _2223


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftToMountableComponentConnection",)


Self = TypeVar("Self", bound="AbstractShaftToMountableComponentConnection")


class AbstractShaftToMountableComponentConnection(_2292.Connection):
    """AbstractShaftToMountableComponentConnection

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftToMountableComponentConnection"
    )

    class _Cast_AbstractShaftToMountableComponentConnection:
        """Special nested class for casting AbstractShaftToMountableComponentConnection to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnection._Cast_AbstractShaftToMountableComponentConnection",
            parent: "AbstractShaftToMountableComponentConnection",
        ):
            self._parent = parent

        @property
        def connection(
            self: "AbstractShaftToMountableComponentConnection._Cast_AbstractShaftToMountableComponentConnection",
        ) -> "_2292.Connection":
            return self._parent._cast(_2292.Connection)

        @property
        def design_entity(
            self: "AbstractShaftToMountableComponentConnection._Cast_AbstractShaftToMountableComponentConnection",
        ) -> "_2223.DesignEntity":
            from mastapy.system_model import _2223

            return self._parent._cast(_2223.DesignEntity)

        @property
        def coaxial_connection(
            self: "AbstractShaftToMountableComponentConnection._Cast_AbstractShaftToMountableComponentConnection",
        ) -> "_2289.CoaxialConnection":
            from mastapy.system_model.connections_and_sockets import _2289

            return self._parent._cast(_2289.CoaxialConnection)

        @property
        def planetary_connection(
            self: "AbstractShaftToMountableComponentConnection._Cast_AbstractShaftToMountableComponentConnection",
        ) -> "_2307.PlanetaryConnection":
            from mastapy.system_model.connections_and_sockets import _2307

            return self._parent._cast(_2307.PlanetaryConnection)

        @property
        def shaft_to_mountable_component_connection(
            self: "AbstractShaftToMountableComponentConnection._Cast_AbstractShaftToMountableComponentConnection",
        ) -> "_2315.ShaftToMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2315

            return self._parent._cast(_2315.ShaftToMountableComponentConnection)

        @property
        def cycloidal_disc_central_bearing_connection(
            self: "AbstractShaftToMountableComponentConnection._Cast_AbstractShaftToMountableComponentConnection",
        ) -> "_2355.CycloidalDiscCentralBearingConnection":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2355

            return self._parent._cast(_2355.CycloidalDiscCentralBearingConnection)

        @property
        def cycloidal_disc_planetary_bearing_connection(
            self: "AbstractShaftToMountableComponentConnection._Cast_AbstractShaftToMountableComponentConnection",
        ) -> "_2358.CycloidalDiscPlanetaryBearingConnection":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2358

            return self._parent._cast(_2358.CycloidalDiscPlanetaryBearingConnection)

        @property
        def abstract_shaft_to_mountable_component_connection(
            self: "AbstractShaftToMountableComponentConnection._Cast_AbstractShaftToMountableComponentConnection",
        ) -> "AbstractShaftToMountableComponentConnection":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnection._Cast_AbstractShaftToMountableComponentConnection",
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
        self: Self, instance_to_wrap: "AbstractShaftToMountableComponentConnection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mountable_component(self: Self) -> "_2484.MountableComponent":
        """mastapy.system_model.part_model.MountableComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MountableComponent

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def shaft(self: Self) -> "_2455.AbstractShaft":
        """mastapy.system_model.part_model.AbstractShaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Shaft

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractShaftToMountableComponentConnection._Cast_AbstractShaftToMountableComponentConnection":
        return self._Cast_AbstractShaftToMountableComponentConnection(self)
