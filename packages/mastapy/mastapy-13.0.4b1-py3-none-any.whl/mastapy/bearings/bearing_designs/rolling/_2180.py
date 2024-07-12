"""NeedleRollerBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_designs.rolling import _2169
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NEEDLE_ROLLER_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "NeedleRollerBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.rolling import _2181, _2182, _2185
    from mastapy.bearings.bearing_designs import _2151, _2154, _2150


__docformat__ = "restructuredtext en"
__all__ = ("NeedleRollerBearing",)


Self = TypeVar("Self", bound="NeedleRollerBearing")


class NeedleRollerBearing(_2169.CylindricalRollerBearing):
    """NeedleRollerBearing

    This is a mastapy class.
    """

    TYPE = _NEEDLE_ROLLER_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NeedleRollerBearing")

    class _Cast_NeedleRollerBearing:
        """Special nested class for casting NeedleRollerBearing to subclasses."""

        def __init__(
            self: "NeedleRollerBearing._Cast_NeedleRollerBearing",
            parent: "NeedleRollerBearing",
        ):
            self._parent = parent

        @property
        def cylindrical_roller_bearing(
            self: "NeedleRollerBearing._Cast_NeedleRollerBearing",
        ) -> "_2169.CylindricalRollerBearing":
            return self._parent._cast(_2169.CylindricalRollerBearing)

        @property
        def non_barrel_roller_bearing(
            self: "NeedleRollerBearing._Cast_NeedleRollerBearing",
        ) -> "_2181.NonBarrelRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2181

            return self._parent._cast(_2181.NonBarrelRollerBearing)

        @property
        def roller_bearing(
            self: "NeedleRollerBearing._Cast_NeedleRollerBearing",
        ) -> "_2182.RollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2182

            return self._parent._cast(_2182.RollerBearing)

        @property
        def rolling_bearing(
            self: "NeedleRollerBearing._Cast_NeedleRollerBearing",
        ) -> "_2185.RollingBearing":
            from mastapy.bearings.bearing_designs.rolling import _2185

            return self._parent._cast(_2185.RollingBearing)

        @property
        def detailed_bearing(
            self: "NeedleRollerBearing._Cast_NeedleRollerBearing",
        ) -> "_2151.DetailedBearing":
            from mastapy.bearings.bearing_designs import _2151

            return self._parent._cast(_2151.DetailedBearing)

        @property
        def non_linear_bearing(
            self: "NeedleRollerBearing._Cast_NeedleRollerBearing",
        ) -> "_2154.NonLinearBearing":
            from mastapy.bearings.bearing_designs import _2154

            return self._parent._cast(_2154.NonLinearBearing)

        @property
        def bearing_design(
            self: "NeedleRollerBearing._Cast_NeedleRollerBearing",
        ) -> "_2150.BearingDesign":
            from mastapy.bearings.bearing_designs import _2150

            return self._parent._cast(_2150.BearingDesign)

        @property
        def needle_roller_bearing(
            self: "NeedleRollerBearing._Cast_NeedleRollerBearing",
        ) -> "NeedleRollerBearing":
            return self._parent

        def __getattr__(
            self: "NeedleRollerBearing._Cast_NeedleRollerBearing", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NeedleRollerBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "NeedleRollerBearing._Cast_NeedleRollerBearing":
        return self._Cast_NeedleRollerBearing(self)
