"""CylindricalGearMicroGeometryBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy.gears.analysis import _1239
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MICRO_GEOMETRY_BASE = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "CylindricalGearMicroGeometryBase",
)

if TYPE_CHECKING:
    from mastapy.utility.report import _1804
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import (
        _1106,
        _1121,
        _1112,
        _1116,
    )
    from mastapy.gears.gear_designs.cylindrical import _1022, _1035
    from mastapy.gears.analysis import _1236, _1233


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMicroGeometryBase",)


Self = TypeVar("Self", bound="CylindricalGearMicroGeometryBase")


class CylindricalGearMicroGeometryBase(_1239.GearImplementationDetail):
    """CylindricalGearMicroGeometryBase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MICRO_GEOMETRY_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearMicroGeometryBase")

    class _Cast_CylindricalGearMicroGeometryBase:
        """Special nested class for casting CylindricalGearMicroGeometryBase to subclasses."""

        def __init__(
            self: "CylindricalGearMicroGeometryBase._Cast_CylindricalGearMicroGeometryBase",
            parent: "CylindricalGearMicroGeometryBase",
        ):
            self._parent = parent

        @property
        def gear_implementation_detail(
            self: "CylindricalGearMicroGeometryBase._Cast_CylindricalGearMicroGeometryBase",
        ) -> "_1239.GearImplementationDetail":
            return self._parent._cast(_1239.GearImplementationDetail)

        @property
        def gear_design_analysis(
            self: "CylindricalGearMicroGeometryBase._Cast_CylindricalGearMicroGeometryBase",
        ) -> "_1236.GearDesignAnalysis":
            from mastapy.gears.analysis import _1236

            return self._parent._cast(_1236.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "CylindricalGearMicroGeometryBase._Cast_CylindricalGearMicroGeometryBase",
        ) -> "_1233.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1233

            return self._parent._cast(_1233.AbstractGearAnalysis)

        @property
        def cylindrical_gear_micro_geometry(
            self: "CylindricalGearMicroGeometryBase._Cast_CylindricalGearMicroGeometryBase",
        ) -> "_1112.CylindricalGearMicroGeometry":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1112

            return self._parent._cast(_1112.CylindricalGearMicroGeometry)

        @property
        def cylindrical_gear_micro_geometry_per_tooth(
            self: "CylindricalGearMicroGeometryBase._Cast_CylindricalGearMicroGeometryBase",
        ) -> "_1116.CylindricalGearMicroGeometryPerTooth":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1116

            return self._parent._cast(_1116.CylindricalGearMicroGeometryPerTooth)

        @property
        def cylindrical_gear_micro_geometry_base(
            self: "CylindricalGearMicroGeometryBase._Cast_CylindricalGearMicroGeometryBase",
        ) -> "CylindricalGearMicroGeometryBase":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMicroGeometryBase._Cast_CylindricalGearMicroGeometryBase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearMicroGeometryBase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def adjust_micro_geometry_for_analysis_when_including_pitch_errors(
        self: Self,
    ) -> "overridable.Overridable_bool":
        """Overridable[bool]"""
        temp = self.wrapped.AdjustMicroGeometryForAnalysisWhenIncludingPitchErrors

        if temp is None:
            return False

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_bool"
        )(temp)

    @adjust_micro_geometry_for_analysis_when_including_pitch_errors.setter
    @enforce_parameter_types
    def adjust_micro_geometry_for_analysis_when_including_pitch_errors(
        self: Self, value: "Union[bool, Tuple[bool, bool]]"
    ):
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else False, is_overridden
        )
        self.wrapped.AdjustMicroGeometryForAnalysisWhenIncludingPitchErrors = value

    @property
    def comment(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Comment

        if temp is None:
            return ""

        return temp

    @comment.setter
    @enforce_parameter_types
    def comment(self: Self, value: "str"):
        self.wrapped.Comment = str(value) if value is not None else ""

    @property
    def lead_form_chart(self: Self) -> "_1804.SimpleChartDefinition":
        """mastapy.utility.report.SimpleChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeadFormChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def lead_slope_chart(self: Self) -> "_1804.SimpleChartDefinition":
        """mastapy.utility.report.SimpleChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeadSlopeChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def lead_total_nominal_chart(self: Self) -> "_1804.SimpleChartDefinition":
        """mastapy.utility.report.SimpleChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeadTotalNominalChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def lead_total_chart(self: Self) -> "_1804.SimpleChartDefinition":
        """mastapy.utility.report.SimpleChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeadTotalChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def profile_control_point_is_user_specified(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ProfileControlPointIsUserSpecified

        if temp is None:
            return False

        return temp

    @profile_control_point_is_user_specified.setter
    @enforce_parameter_types
    def profile_control_point_is_user_specified(self: Self, value: "bool"):
        self.wrapped.ProfileControlPointIsUserSpecified = (
            bool(value) if value is not None else False
        )

    @property
    def profile_form_10_percent_chart(self: Self) -> "_1804.SimpleChartDefinition":
        """mastapy.utility.report.SimpleChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileForm10PercentChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def profile_form_50_percent_chart(self: Self) -> "_1804.SimpleChartDefinition":
        """mastapy.utility.report.SimpleChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileForm50PercentChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def profile_form_90_percent_chart(self: Self) -> "_1804.SimpleChartDefinition":
        """mastapy.utility.report.SimpleChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileForm90PercentChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def profile_form_chart(self: Self) -> "_1804.SimpleChartDefinition":
        """mastapy.utility.report.SimpleChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileFormChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def profile_total_nominal_chart(self: Self) -> "_1804.SimpleChartDefinition":
        """mastapy.utility.report.SimpleChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileTotalNominalChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def profile_total_chart(self: Self) -> "_1804.SimpleChartDefinition":
        """mastapy.utility.report.SimpleChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileTotalChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def use_same_micro_geometry_on_both_flanks(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseSameMicroGeometryOnBothFlanks

        if temp is None:
            return False

        return temp

    @use_same_micro_geometry_on_both_flanks.setter
    @enforce_parameter_types
    def use_same_micro_geometry_on_both_flanks(self: Self, value: "bool"):
        self.wrapped.UseSameMicroGeometryOnBothFlanks = (
            bool(value) if value is not None else False
        )

    @property
    def common_micro_geometry_of_left_flank(
        self: Self,
    ) -> "_1106.CylindricalGearCommonFlankMicroGeometry":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearCommonFlankMicroGeometry

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CommonMicroGeometryOfLeftFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def common_micro_geometry_of_right_flank(
        self: Self,
    ) -> "_1106.CylindricalGearCommonFlankMicroGeometry":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearCommonFlankMicroGeometry

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CommonMicroGeometryOfRightFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear(self: Self) -> "_1022.CylindricalGearDesign":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def profile_control_point(self: Self) -> "_1035.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileControlPoint

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def common_micro_geometries_of_flanks(
        self: Self,
    ) -> "List[_1106.CylindricalGearCommonFlankMicroGeometry]":
        """List[mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearCommonFlankMicroGeometry]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CommonMicroGeometriesOfFlanks

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def tooth_micro_geometries(
        self: Self,
    ) -> "List[_1121.CylindricalGearToothMicroGeometry]":
        """List[mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearToothMicroGeometry]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothMicroGeometries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearMicroGeometryBase._Cast_CylindricalGearMicroGeometryBase":
        return self._Cast_CylindricalGearMicroGeometryBase(self)
