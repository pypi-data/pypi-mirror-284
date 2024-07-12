"""CylindricalSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets import _2316
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "CylindricalSocket"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import (
        _2286,
        _2287,
        _2294,
        _2299,
        _2300,
        _2302,
        _2303,
        _2304,
        _2305,
        _2306,
        _2308,
        _2309,
        _2310,
        _2313,
        _2314,
    )
    from mastapy.system_model.connections_and_sockets.gears import _2330
    from mastapy.system_model.connections_and_sockets.cycloidal import (
        _2353,
        _2354,
        _2356,
        _2357,
        _2359,
        _2360,
    )
    from mastapy.system_model.connections_and_sockets.couplings import (
        _2363,
        _2365,
        _2367,
        _2369,
        _2371,
        _2373,
        _2374,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalSocket",)


Self = TypeVar("Self", bound="CylindricalSocket")


class CylindricalSocket(_2316.Socket):
    """CylindricalSocket

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalSocket")

    class _Cast_CylindricalSocket:
        """Special nested class for casting CylindricalSocket to subclasses."""

        def __init__(
            self: "CylindricalSocket._Cast_CylindricalSocket",
            parent: "CylindricalSocket",
        ):
            self._parent = parent

        @property
        def socket(self: "CylindricalSocket._Cast_CylindricalSocket") -> "_2316.Socket":
            return self._parent._cast(_2316.Socket)

        @property
        def bearing_inner_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2286.BearingInnerSocket":
            from mastapy.system_model.connections_and_sockets import _2286

            return self._parent._cast(_2286.BearingInnerSocket)

        @property
        def bearing_outer_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2287.BearingOuterSocket":
            from mastapy.system_model.connections_and_sockets import _2287

            return self._parent._cast(_2287.BearingOuterSocket)

        @property
        def cvt_pulley_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2294.CVTPulleySocket":
            from mastapy.system_model.connections_and_sockets import _2294

            return self._parent._cast(_2294.CVTPulleySocket)

        @property
        def inner_shaft_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2299.InnerShaftSocket":
            from mastapy.system_model.connections_and_sockets import _2299

            return self._parent._cast(_2299.InnerShaftSocket)

        @property
        def inner_shaft_socket_base(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2300.InnerShaftSocketBase":
            from mastapy.system_model.connections_and_sockets import _2300

            return self._parent._cast(_2300.InnerShaftSocketBase)

        @property
        def mountable_component_inner_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2302.MountableComponentInnerSocket":
            from mastapy.system_model.connections_and_sockets import _2302

            return self._parent._cast(_2302.MountableComponentInnerSocket)

        @property
        def mountable_component_outer_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2303.MountableComponentOuterSocket":
            from mastapy.system_model.connections_and_sockets import _2303

            return self._parent._cast(_2303.MountableComponentOuterSocket)

        @property
        def mountable_component_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2304.MountableComponentSocket":
            from mastapy.system_model.connections_and_sockets import _2304

            return self._parent._cast(_2304.MountableComponentSocket)

        @property
        def outer_shaft_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2305.OuterShaftSocket":
            from mastapy.system_model.connections_and_sockets import _2305

            return self._parent._cast(_2305.OuterShaftSocket)

        @property
        def outer_shaft_socket_base(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2306.OuterShaftSocketBase":
            from mastapy.system_model.connections_and_sockets import _2306

            return self._parent._cast(_2306.OuterShaftSocketBase)

        @property
        def planetary_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2308.PlanetarySocket":
            from mastapy.system_model.connections_and_sockets import _2308

            return self._parent._cast(_2308.PlanetarySocket)

        @property
        def planetary_socket_base(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2309.PlanetarySocketBase":
            from mastapy.system_model.connections_and_sockets import _2309

            return self._parent._cast(_2309.PlanetarySocketBase)

        @property
        def pulley_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2310.PulleySocket":
            from mastapy.system_model.connections_and_sockets import _2310

            return self._parent._cast(_2310.PulleySocket)

        @property
        def rolling_ring_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2313.RollingRingSocket":
            from mastapy.system_model.connections_and_sockets import _2313

            return self._parent._cast(_2313.RollingRingSocket)

        @property
        def shaft_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2314.ShaftSocket":
            from mastapy.system_model.connections_and_sockets import _2314

            return self._parent._cast(_2314.ShaftSocket)

        @property
        def cylindrical_gear_teeth_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2330.CylindricalGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2330

            return self._parent._cast(_2330.CylindricalGearTeethSocket)

        @property
        def cycloidal_disc_axial_left_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2353.CycloidalDiscAxialLeftSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2353

            return self._parent._cast(_2353.CycloidalDiscAxialLeftSocket)

        @property
        def cycloidal_disc_axial_right_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2354.CycloidalDiscAxialRightSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2354

            return self._parent._cast(_2354.CycloidalDiscAxialRightSocket)

        @property
        def cycloidal_disc_inner_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2356.CycloidalDiscInnerSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2356

            return self._parent._cast(_2356.CycloidalDiscInnerSocket)

        @property
        def cycloidal_disc_outer_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2357.CycloidalDiscOuterSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2357

            return self._parent._cast(_2357.CycloidalDiscOuterSocket)

        @property
        def cycloidal_disc_planetary_bearing_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2359.CycloidalDiscPlanetaryBearingSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2359

            return self._parent._cast(_2359.CycloidalDiscPlanetaryBearingSocket)

        @property
        def ring_pins_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2360.RingPinsSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2360

            return self._parent._cast(_2360.RingPinsSocket)

        @property
        def clutch_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2363.ClutchSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2363

            return self._parent._cast(_2363.ClutchSocket)

        @property
        def concept_coupling_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2365.ConceptCouplingSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2365

            return self._parent._cast(_2365.ConceptCouplingSocket)

        @property
        def coupling_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2367.CouplingSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2367

            return self._parent._cast(_2367.CouplingSocket)

        @property
        def part_to_part_shear_coupling_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2369.PartToPartShearCouplingSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2369

            return self._parent._cast(_2369.PartToPartShearCouplingSocket)

        @property
        def spring_damper_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2371.SpringDamperSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2371

            return self._parent._cast(_2371.SpringDamperSocket)

        @property
        def torque_converter_pump_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2373.TorqueConverterPumpSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2373

            return self._parent._cast(_2373.TorqueConverterPumpSocket)

        @property
        def torque_converter_turbine_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "_2374.TorqueConverterTurbineSocket":
            from mastapy.system_model.connections_and_sockets.couplings import _2374

            return self._parent._cast(_2374.TorqueConverterTurbineSocket)

        @property
        def cylindrical_socket(
            self: "CylindricalSocket._Cast_CylindricalSocket",
        ) -> "CylindricalSocket":
            return self._parent

        def __getattr__(self: "CylindricalSocket._Cast_CylindricalSocket", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CylindricalSocket._Cast_CylindricalSocket":
        return self._Cast_CylindricalSocket(self)
