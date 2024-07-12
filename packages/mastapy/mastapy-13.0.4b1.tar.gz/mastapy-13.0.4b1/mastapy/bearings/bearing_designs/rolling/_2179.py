"""MultiPointContactBallBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_designs.rolling import _2160
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MULTI_POINT_CONTACT_BALL_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "MultiPointContactBallBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.rolling import _2174, _2192, _2185
    from mastapy.bearings.bearing_designs import _2151, _2154, _2150


__docformat__ = "restructuredtext en"
__all__ = ("MultiPointContactBallBearing",)


Self = TypeVar("Self", bound="MultiPointContactBallBearing")


class MultiPointContactBallBearing(_2160.BallBearing):
    """MultiPointContactBallBearing

    This is a mastapy class.
    """

    TYPE = _MULTI_POINT_CONTACT_BALL_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MultiPointContactBallBearing")

    class _Cast_MultiPointContactBallBearing:
        """Special nested class for casting MultiPointContactBallBearing to subclasses."""

        def __init__(
            self: "MultiPointContactBallBearing._Cast_MultiPointContactBallBearing",
            parent: "MultiPointContactBallBearing",
        ):
            self._parent = parent

        @property
        def ball_bearing(
            self: "MultiPointContactBallBearing._Cast_MultiPointContactBallBearing",
        ) -> "_2160.BallBearing":
            return self._parent._cast(_2160.BallBearing)

        @property
        def rolling_bearing(
            self: "MultiPointContactBallBearing._Cast_MultiPointContactBallBearing",
        ) -> "_2185.RollingBearing":
            from mastapy.bearings.bearing_designs.rolling import _2185

            return self._parent._cast(_2185.RollingBearing)

        @property
        def detailed_bearing(
            self: "MultiPointContactBallBearing._Cast_MultiPointContactBallBearing",
        ) -> "_2151.DetailedBearing":
            from mastapy.bearings.bearing_designs import _2151

            return self._parent._cast(_2151.DetailedBearing)

        @property
        def non_linear_bearing(
            self: "MultiPointContactBallBearing._Cast_MultiPointContactBallBearing",
        ) -> "_2154.NonLinearBearing":
            from mastapy.bearings.bearing_designs import _2154

            return self._parent._cast(_2154.NonLinearBearing)

        @property
        def bearing_design(
            self: "MultiPointContactBallBearing._Cast_MultiPointContactBallBearing",
        ) -> "_2150.BearingDesign":
            from mastapy.bearings.bearing_designs import _2150

            return self._parent._cast(_2150.BearingDesign)

        @property
        def four_point_contact_ball_bearing(
            self: "MultiPointContactBallBearing._Cast_MultiPointContactBallBearing",
        ) -> "_2174.FourPointContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2174

            return self._parent._cast(_2174.FourPointContactBallBearing)

        @property
        def three_point_contact_ball_bearing(
            self: "MultiPointContactBallBearing._Cast_MultiPointContactBallBearing",
        ) -> "_2192.ThreePointContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2192

            return self._parent._cast(_2192.ThreePointContactBallBearing)

        @property
        def multi_point_contact_ball_bearing(
            self: "MultiPointContactBallBearing._Cast_MultiPointContactBallBearing",
        ) -> "MultiPointContactBallBearing":
            return self._parent

        def __getattr__(
            self: "MultiPointContactBallBearing._Cast_MultiPointContactBallBearing",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MultiPointContactBallBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "MultiPointContactBallBearing._Cast_MultiPointContactBallBearing":
        return self._Cast_MultiPointContactBallBearing(self)
