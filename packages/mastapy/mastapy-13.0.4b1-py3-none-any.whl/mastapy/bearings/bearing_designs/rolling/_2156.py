"""AngularContactThrustBallBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.bearings.bearing_designs.rolling import _2155
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANGULAR_CONTACT_THRUST_BALL_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "AngularContactThrustBallBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.rolling import _2160, _2185
    from mastapy.bearings.bearing_designs import _2151, _2154, _2150


__docformat__ = "restructuredtext en"
__all__ = ("AngularContactThrustBallBearing",)


Self = TypeVar("Self", bound="AngularContactThrustBallBearing")


class AngularContactThrustBallBearing(_2155.AngularContactBallBearing):
    """AngularContactThrustBallBearing

    This is a mastapy class.
    """

    TYPE = _ANGULAR_CONTACT_THRUST_BALL_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AngularContactThrustBallBearing")

    class _Cast_AngularContactThrustBallBearing:
        """Special nested class for casting AngularContactThrustBallBearing to subclasses."""

        def __init__(
            self: "AngularContactThrustBallBearing._Cast_AngularContactThrustBallBearing",
            parent: "AngularContactThrustBallBearing",
        ):
            self._parent = parent

        @property
        def angular_contact_ball_bearing(
            self: "AngularContactThrustBallBearing._Cast_AngularContactThrustBallBearing",
        ) -> "_2155.AngularContactBallBearing":
            return self._parent._cast(_2155.AngularContactBallBearing)

        @property
        def ball_bearing(
            self: "AngularContactThrustBallBearing._Cast_AngularContactThrustBallBearing",
        ) -> "_2160.BallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2160

            return self._parent._cast(_2160.BallBearing)

        @property
        def rolling_bearing(
            self: "AngularContactThrustBallBearing._Cast_AngularContactThrustBallBearing",
        ) -> "_2185.RollingBearing":
            from mastapy.bearings.bearing_designs.rolling import _2185

            return self._parent._cast(_2185.RollingBearing)

        @property
        def detailed_bearing(
            self: "AngularContactThrustBallBearing._Cast_AngularContactThrustBallBearing",
        ) -> "_2151.DetailedBearing":
            from mastapy.bearings.bearing_designs import _2151

            return self._parent._cast(_2151.DetailedBearing)

        @property
        def non_linear_bearing(
            self: "AngularContactThrustBallBearing._Cast_AngularContactThrustBallBearing",
        ) -> "_2154.NonLinearBearing":
            from mastapy.bearings.bearing_designs import _2154

            return self._parent._cast(_2154.NonLinearBearing)

        @property
        def bearing_design(
            self: "AngularContactThrustBallBearing._Cast_AngularContactThrustBallBearing",
        ) -> "_2150.BearingDesign":
            from mastapy.bearings.bearing_designs import _2150

            return self._parent._cast(_2150.BearingDesign)

        @property
        def angular_contact_thrust_ball_bearing(
            self: "AngularContactThrustBallBearing._Cast_AngularContactThrustBallBearing",
        ) -> "AngularContactThrustBallBearing":
            return self._parent

        def __getattr__(
            self: "AngularContactThrustBallBearing._Cast_AngularContactThrustBallBearing",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AngularContactThrustBallBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Width

        if temp is None:
            return 0.0

        return temp

    @width.setter
    @enforce_parameter_types
    def width(self: Self, value: "float"):
        self.wrapped.Width = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "AngularContactThrustBallBearing._Cast_AngularContactThrustBallBearing":
        return self._Cast_AngularContactThrustBallBearing(self)
