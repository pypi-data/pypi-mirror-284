"""LoadedRollingBearingRow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from PIL.Image import Image

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ROLLING_BEARING_ROW = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedRollingBearingRow"
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1887
    from mastapy.bearings.bearing_results.rolling import (
        _2053,
        _1993,
        _2034,
        _2052,
        _2088,
        _2093,
        _2004,
        _2007,
        _2010,
        _2015,
        _2018,
        _2023,
        _2026,
        _2030,
        _2033,
        _2038,
        _2042,
        _2045,
        _2050,
        _2057,
        _2061,
        _2064,
        _2069,
        _2072,
        _2075,
        _2078,
    )


__docformat__ = "restructuredtext en"
__all__ = ("LoadedRollingBearingRow",)


Self = TypeVar("Self", bound="LoadedRollingBearingRow")


class LoadedRollingBearingRow(_0.APIBase):
    """LoadedRollingBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_ROLLING_BEARING_ROW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedRollingBearingRow")

    class _Cast_LoadedRollingBearingRow:
        """Special nested class for casting LoadedRollingBearingRow to subclasses."""

        def __init__(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
            parent: "LoadedRollingBearingRow",
        ):
            self._parent = parent

        @property
        def loaded_angular_contact_ball_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_2004.LoadedAngularContactBallBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2004

            return self._parent._cast(_2004.LoadedAngularContactBallBearingRow)

        @property
        def loaded_angular_contact_thrust_ball_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_2007.LoadedAngularContactThrustBallBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2007

            return self._parent._cast(_2007.LoadedAngularContactThrustBallBearingRow)

        @property
        def loaded_asymmetric_spherical_roller_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_2010.LoadedAsymmetricSphericalRollerBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2010

            return self._parent._cast(_2010.LoadedAsymmetricSphericalRollerBearingRow)

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_2015.LoadedAxialThrustCylindricalRollerBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2015

            return self._parent._cast(
                _2015.LoadedAxialThrustCylindricalRollerBearingRow
            )

        @property
        def loaded_axial_thrust_needle_roller_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_2018.LoadedAxialThrustNeedleRollerBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2018

            return self._parent._cast(_2018.LoadedAxialThrustNeedleRollerBearingRow)

        @property
        def loaded_ball_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_2023.LoadedBallBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2023

            return self._parent._cast(_2023.LoadedBallBearingRow)

        @property
        def loaded_crossed_roller_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_2026.LoadedCrossedRollerBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2026

            return self._parent._cast(_2026.LoadedCrossedRollerBearingRow)

        @property
        def loaded_cylindrical_roller_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_2030.LoadedCylindricalRollerBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2030

            return self._parent._cast(_2030.LoadedCylindricalRollerBearingRow)

        @property
        def loaded_deep_groove_ball_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_2033.LoadedDeepGrooveBallBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2033

            return self._parent._cast(_2033.LoadedDeepGrooveBallBearingRow)

        @property
        def loaded_four_point_contact_ball_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_2038.LoadedFourPointContactBallBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2038

            return self._parent._cast(_2038.LoadedFourPointContactBallBearingRow)

        @property
        def loaded_needle_roller_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_2042.LoadedNeedleRollerBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2042

            return self._parent._cast(_2042.LoadedNeedleRollerBearingRow)

        @property
        def loaded_non_barrel_roller_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_2045.LoadedNonBarrelRollerBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2045

            return self._parent._cast(_2045.LoadedNonBarrelRollerBearingRow)

        @property
        def loaded_roller_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_2050.LoadedRollerBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2050

            return self._parent._cast(_2050.LoadedRollerBearingRow)

        @property
        def loaded_self_aligning_ball_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_2057.LoadedSelfAligningBallBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2057

            return self._parent._cast(_2057.LoadedSelfAligningBallBearingRow)

        @property
        def loaded_spherical_roller_radial_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_2061.LoadedSphericalRollerRadialBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2061

            return self._parent._cast(_2061.LoadedSphericalRollerRadialBearingRow)

        @property
        def loaded_spherical_roller_thrust_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_2064.LoadedSphericalRollerThrustBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2064

            return self._parent._cast(_2064.LoadedSphericalRollerThrustBearingRow)

        @property
        def loaded_taper_roller_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_2069.LoadedTaperRollerBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2069

            return self._parent._cast(_2069.LoadedTaperRollerBearingRow)

        @property
        def loaded_three_point_contact_ball_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_2072.LoadedThreePointContactBallBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2072

            return self._parent._cast(_2072.LoadedThreePointContactBallBearingRow)

        @property
        def loaded_thrust_ball_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_2075.LoadedThrustBallBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2075

            return self._parent._cast(_2075.LoadedThrustBallBearingRow)

        @property
        def loaded_toroidal_roller_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_2078.LoadedToroidalRollerBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2078

            return self._parent._cast(_2078.LoadedToroidalRollerBearingRow)

        @property
        def loaded_rolling_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "LoadedRollingBearingRow":
            return self._parent

        def __getattr__(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedRollingBearingRow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def dynamic_equivalent_reference_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicEquivalentReferenceLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def life_modification_factor_for_systems_approach(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LifeModificationFactorForSystemsApproach

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_element_normal_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumElementNormalStress

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_element_normal_stress_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumElementNormalStressInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_element_normal_stress_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumElementNormalStressOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_load_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalLoadInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_load_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalLoadOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_contact_stress_chart_inner(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalContactStressChartInner

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def normal_contact_stress_chart_left(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalContactStressChartLeft

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def normal_contact_stress_chart_outer(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalContactStressChartOuter

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def normal_contact_stress_chart_right(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalContactStressChartRight

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def row_id(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RowID

        if temp is None:
            return ""

        return temp

    @property
    def subsurface_shear_stress_chart_inner(self: Self) -> "_1887.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SubsurfaceShearStressChartInner

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def subsurface_shear_stress_chart_outer(self: Self) -> "_1887.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SubsurfaceShearStressChartOuter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def loaded_bearing(self: Self) -> "_2053.LoadedRollingBearingResults":
        """mastapy.bearings.bearing_results.rolling.LoadedRollingBearingResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadedBearing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def maximum_operating_internal_clearance(self: Self) -> "_1993.InternalClearance":
        """mastapy.bearings.bearing_results.rolling.InternalClearance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumOperatingInternalClearance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def minimum_operating_internal_clearance(self: Self) -> "_1993.InternalClearance":
        """mastapy.bearings.bearing_results.rolling.InternalClearance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumOperatingInternalClearance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def elements(self: Self) -> "List[_2034.LoadedElement]":
        """List[mastapy.bearings.bearing_results.rolling.LoadedElement]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Elements

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def race_results(self: Self) -> "List[_2052.LoadedRollingBearingRaceResults]":
        """List[mastapy.bearings.bearing_results.rolling.LoadedRollingBearingRaceResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RaceResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def ring_force_and_displacement_results(
        self: Self,
    ) -> "List[_2088.RingForceAndDisplacement]":
        """List[mastapy.bearings.bearing_results.rolling.RingForceAndDisplacement]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RingForceAndDisplacementResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def subsurface_shear_stress_for_most_heavily_loaded_element_inner(
        self: Self,
    ) -> "List[_2093.StressAtPosition]":
        """List[mastapy.bearings.bearing_results.rolling.StressAtPosition]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SubsurfaceShearStressForMostHeavilyLoadedElementInner

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def subsurface_shear_stress_for_most_heavily_loaded_element_outer(
        self: Self,
    ) -> "List[_2093.StressAtPosition]":
        """List[mastapy.bearings.bearing_results.rolling.StressAtPosition]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SubsurfaceShearStressForMostHeavilyLoadedElementOuter

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(self: Self) -> "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow":
        return self._Cast_LoadedRollingBearingRow(self)
