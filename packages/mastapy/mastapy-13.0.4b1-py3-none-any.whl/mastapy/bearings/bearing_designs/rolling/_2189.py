"""SphericalRollerBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_designs.rolling import _2162
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPHERICAL_ROLLER_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "SphericalRollerBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.rolling import _2182, _2185
    from mastapy.bearings.bearing_designs import _2151, _2154, _2150


__docformat__ = "restructuredtext en"
__all__ = ("SphericalRollerBearing",)


Self = TypeVar("Self", bound="SphericalRollerBearing")


class SphericalRollerBearing(_2162.BarrelRollerBearing):
    """SphericalRollerBearing

    This is a mastapy class.
    """

    TYPE = _SPHERICAL_ROLLER_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SphericalRollerBearing")

    class _Cast_SphericalRollerBearing:
        """Special nested class for casting SphericalRollerBearing to subclasses."""

        def __init__(
            self: "SphericalRollerBearing._Cast_SphericalRollerBearing",
            parent: "SphericalRollerBearing",
        ):
            self._parent = parent

        @property
        def barrel_roller_bearing(
            self: "SphericalRollerBearing._Cast_SphericalRollerBearing",
        ) -> "_2162.BarrelRollerBearing":
            return self._parent._cast(_2162.BarrelRollerBearing)

        @property
        def roller_bearing(
            self: "SphericalRollerBearing._Cast_SphericalRollerBearing",
        ) -> "_2182.RollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2182

            return self._parent._cast(_2182.RollerBearing)

        @property
        def rolling_bearing(
            self: "SphericalRollerBearing._Cast_SphericalRollerBearing",
        ) -> "_2185.RollingBearing":
            from mastapy.bearings.bearing_designs.rolling import _2185

            return self._parent._cast(_2185.RollingBearing)

        @property
        def detailed_bearing(
            self: "SphericalRollerBearing._Cast_SphericalRollerBearing",
        ) -> "_2151.DetailedBearing":
            from mastapy.bearings.bearing_designs import _2151

            return self._parent._cast(_2151.DetailedBearing)

        @property
        def non_linear_bearing(
            self: "SphericalRollerBearing._Cast_SphericalRollerBearing",
        ) -> "_2154.NonLinearBearing":
            from mastapy.bearings.bearing_designs import _2154

            return self._parent._cast(_2154.NonLinearBearing)

        @property
        def bearing_design(
            self: "SphericalRollerBearing._Cast_SphericalRollerBearing",
        ) -> "_2150.BearingDesign":
            from mastapy.bearings.bearing_designs import _2150

            return self._parent._cast(_2150.BearingDesign)

        @property
        def spherical_roller_bearing(
            self: "SphericalRollerBearing._Cast_SphericalRollerBearing",
        ) -> "SphericalRollerBearing":
            return self._parent

        def __getattr__(
            self: "SphericalRollerBearing._Cast_SphericalRollerBearing", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SphericalRollerBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "SphericalRollerBearing._Cast_SphericalRollerBearing":
        return self._Cast_SphericalRollerBearing(self)
