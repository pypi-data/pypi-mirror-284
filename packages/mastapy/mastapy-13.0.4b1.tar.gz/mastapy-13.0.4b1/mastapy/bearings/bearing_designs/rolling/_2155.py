"""AngularContactBallBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_designs.rolling import _2160
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANGULAR_CONTACT_BALL_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "AngularContactBallBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.rolling import _2156, _2185
    from mastapy.bearings.bearing_designs import _2151, _2154, _2150


__docformat__ = "restructuredtext en"
__all__ = ("AngularContactBallBearing",)


Self = TypeVar("Self", bound="AngularContactBallBearing")


class AngularContactBallBearing(_2160.BallBearing):
    """AngularContactBallBearing

    This is a mastapy class.
    """

    TYPE = _ANGULAR_CONTACT_BALL_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AngularContactBallBearing")

    class _Cast_AngularContactBallBearing:
        """Special nested class for casting AngularContactBallBearing to subclasses."""

        def __init__(
            self: "AngularContactBallBearing._Cast_AngularContactBallBearing",
            parent: "AngularContactBallBearing",
        ):
            self._parent = parent

        @property
        def ball_bearing(
            self: "AngularContactBallBearing._Cast_AngularContactBallBearing",
        ) -> "_2160.BallBearing":
            return self._parent._cast(_2160.BallBearing)

        @property
        def rolling_bearing(
            self: "AngularContactBallBearing._Cast_AngularContactBallBearing",
        ) -> "_2185.RollingBearing":
            from mastapy.bearings.bearing_designs.rolling import _2185

            return self._parent._cast(_2185.RollingBearing)

        @property
        def detailed_bearing(
            self: "AngularContactBallBearing._Cast_AngularContactBallBearing",
        ) -> "_2151.DetailedBearing":
            from mastapy.bearings.bearing_designs import _2151

            return self._parent._cast(_2151.DetailedBearing)

        @property
        def non_linear_bearing(
            self: "AngularContactBallBearing._Cast_AngularContactBallBearing",
        ) -> "_2154.NonLinearBearing":
            from mastapy.bearings.bearing_designs import _2154

            return self._parent._cast(_2154.NonLinearBearing)

        @property
        def bearing_design(
            self: "AngularContactBallBearing._Cast_AngularContactBallBearing",
        ) -> "_2150.BearingDesign":
            from mastapy.bearings.bearing_designs import _2150

            return self._parent._cast(_2150.BearingDesign)

        @property
        def angular_contact_thrust_ball_bearing(
            self: "AngularContactBallBearing._Cast_AngularContactBallBearing",
        ) -> "_2156.AngularContactThrustBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2156

            return self._parent._cast(_2156.AngularContactThrustBallBearing)

        @property
        def angular_contact_ball_bearing(
            self: "AngularContactBallBearing._Cast_AngularContactBallBearing",
        ) -> "AngularContactBallBearing":
            return self._parent

        def __getattr__(
            self: "AngularContactBallBearing._Cast_AngularContactBallBearing", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AngularContactBallBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "AngularContactBallBearing._Cast_AngularContactBallBearing":
        return self._Cast_AngularContactBallBearing(self)
