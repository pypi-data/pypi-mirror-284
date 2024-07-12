"""FourPointContactBallBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy.bearings.bearing_designs.rolling import _2179
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FOUR_POINT_CONTACT_BALL_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "FourPointContactBallBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.rolling import _2173, _2160, _2185
    from mastapy.bearings.bearing_designs import _2151, _2154, _2150


__docformat__ = "restructuredtext en"
__all__ = ("FourPointContactBallBearing",)


Self = TypeVar("Self", bound="FourPointContactBallBearing")


class FourPointContactBallBearing(_2179.MultiPointContactBallBearing):
    """FourPointContactBallBearing

    This is a mastapy class.
    """

    TYPE = _FOUR_POINT_CONTACT_BALL_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FourPointContactBallBearing")

    class _Cast_FourPointContactBallBearing:
        """Special nested class for casting FourPointContactBallBearing to subclasses."""

        def __init__(
            self: "FourPointContactBallBearing._Cast_FourPointContactBallBearing",
            parent: "FourPointContactBallBearing",
        ):
            self._parent = parent

        @property
        def multi_point_contact_ball_bearing(
            self: "FourPointContactBallBearing._Cast_FourPointContactBallBearing",
        ) -> "_2179.MultiPointContactBallBearing":
            return self._parent._cast(_2179.MultiPointContactBallBearing)

        @property
        def ball_bearing(
            self: "FourPointContactBallBearing._Cast_FourPointContactBallBearing",
        ) -> "_2160.BallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2160

            return self._parent._cast(_2160.BallBearing)

        @property
        def rolling_bearing(
            self: "FourPointContactBallBearing._Cast_FourPointContactBallBearing",
        ) -> "_2185.RollingBearing":
            from mastapy.bearings.bearing_designs.rolling import _2185

            return self._parent._cast(_2185.RollingBearing)

        @property
        def detailed_bearing(
            self: "FourPointContactBallBearing._Cast_FourPointContactBallBearing",
        ) -> "_2151.DetailedBearing":
            from mastapy.bearings.bearing_designs import _2151

            return self._parent._cast(_2151.DetailedBearing)

        @property
        def non_linear_bearing(
            self: "FourPointContactBallBearing._Cast_FourPointContactBallBearing",
        ) -> "_2154.NonLinearBearing":
            from mastapy.bearings.bearing_designs import _2154

            return self._parent._cast(_2154.NonLinearBearing)

        @property
        def bearing_design(
            self: "FourPointContactBallBearing._Cast_FourPointContactBallBearing",
        ) -> "_2150.BearingDesign":
            from mastapy.bearings.bearing_designs import _2150

            return self._parent._cast(_2150.BearingDesign)

        @property
        def four_point_contact_ball_bearing(
            self: "FourPointContactBallBearing._Cast_FourPointContactBallBearing",
        ) -> "FourPointContactBallBearing":
            return self._parent

        def __getattr__(
            self: "FourPointContactBallBearing._Cast_FourPointContactBallBearing",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FourPointContactBallBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_axial_internal_clearance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAxialInternalClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_angle_under_axial_load(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactAngleUnderAxialLoad

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def contact_angle_under_radial_load(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactAngleUnderRadialLoad

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def contact_angle_and_internal_clearance_definition(
        self: Self,
    ) -> "_2173.FourPointContactAngleDefinition":
        """mastapy.bearings.bearing_designs.rolling.FourPointContactAngleDefinition"""
        temp = self.wrapped.ContactAngleAndInternalClearanceDefinition

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Bearings.BearingDesigns.Rolling.FourPointContactAngleDefinition",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings.bearing_designs.rolling._2173",
            "FourPointContactAngleDefinition",
        )(value)

    @contact_angle_and_internal_clearance_definition.setter
    @enforce_parameter_types
    def contact_angle_and_internal_clearance_definition(
        self: Self, value: "_2173.FourPointContactAngleDefinition"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Bearings.BearingDesigns.Rolling.FourPointContactAngleDefinition",
        )
        self.wrapped.ContactAngleAndInternalClearanceDefinition = value

    @property
    def nominal_radial_internal_clearance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NominalRadialInternalClearance

        if temp is None:
            return 0.0

        return temp

    @nominal_radial_internal_clearance.setter
    @enforce_parameter_types
    def nominal_radial_internal_clearance(self: Self, value: "float"):
        self.wrapped.NominalRadialInternalClearance = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(
        self: Self,
    ) -> "FourPointContactBallBearing._Cast_FourPointContactBallBearing":
        return self._Cast_FourPointContactBallBearing(self)
