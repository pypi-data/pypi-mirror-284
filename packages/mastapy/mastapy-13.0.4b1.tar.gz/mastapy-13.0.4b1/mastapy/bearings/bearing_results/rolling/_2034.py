"""LoadedElement"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ELEMENT = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedElement"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results import _1964
    from mastapy.bearings.bearing_results.rolling import (
        _1993,
        _2093,
        _2002,
        _2005,
        _2008,
        _2013,
        _2016,
        _2020,
        _2024,
        _2028,
        _2031,
        _2035,
        _2039,
        _2040,
        _2047,
        _2048,
        _2055,
        _2058,
        _2059,
        _2065,
        _2067,
        _2070,
        _2073,
        _2076,
    )


__docformat__ = "restructuredtext en"
__all__ = ("LoadedElement",)


Self = TypeVar("Self", bound="LoadedElement")


class LoadedElement(_0.APIBase):
    """LoadedElement

    This is a mastapy class.
    """

    TYPE = _LOADED_ELEMENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedElement")

    class _Cast_LoadedElement:
        """Special nested class for casting LoadedElement to subclasses."""

        def __init__(
            self: "LoadedElement._Cast_LoadedElement", parent: "LoadedElement"
        ):
            self._parent = parent

        @property
        def loaded_angular_contact_ball_bearing_element(
            self: "LoadedElement._Cast_LoadedElement",
        ) -> "_2002.LoadedAngularContactBallBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2002

            return self._parent._cast(_2002.LoadedAngularContactBallBearingElement)

        @property
        def loaded_angular_contact_thrust_ball_bearing_element(
            self: "LoadedElement._Cast_LoadedElement",
        ) -> "_2005.LoadedAngularContactThrustBallBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2005

            return self._parent._cast(
                _2005.LoadedAngularContactThrustBallBearingElement
            )

        @property
        def loaded_asymmetric_spherical_roller_bearing_element(
            self: "LoadedElement._Cast_LoadedElement",
        ) -> "_2008.LoadedAsymmetricSphericalRollerBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2008

            return self._parent._cast(
                _2008.LoadedAsymmetricSphericalRollerBearingElement
            )

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_element(
            self: "LoadedElement._Cast_LoadedElement",
        ) -> "_2013.LoadedAxialThrustCylindricalRollerBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2013

            return self._parent._cast(
                _2013.LoadedAxialThrustCylindricalRollerBearingElement
            )

        @property
        def loaded_axial_thrust_needle_roller_bearing_element(
            self: "LoadedElement._Cast_LoadedElement",
        ) -> "_2016.LoadedAxialThrustNeedleRollerBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2016

            return self._parent._cast(_2016.LoadedAxialThrustNeedleRollerBearingElement)

        @property
        def loaded_ball_bearing_element(
            self: "LoadedElement._Cast_LoadedElement",
        ) -> "_2020.LoadedBallBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2020

            return self._parent._cast(_2020.LoadedBallBearingElement)

        @property
        def loaded_crossed_roller_bearing_element(
            self: "LoadedElement._Cast_LoadedElement",
        ) -> "_2024.LoadedCrossedRollerBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2024

            return self._parent._cast(_2024.LoadedCrossedRollerBearingElement)

        @property
        def loaded_cylindrical_roller_bearing_element(
            self: "LoadedElement._Cast_LoadedElement",
        ) -> "_2028.LoadedCylindricalRollerBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2028

            return self._parent._cast(_2028.LoadedCylindricalRollerBearingElement)

        @property
        def loaded_deep_groove_ball_bearing_element(
            self: "LoadedElement._Cast_LoadedElement",
        ) -> "_2031.LoadedDeepGrooveBallBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2031

            return self._parent._cast(_2031.LoadedDeepGrooveBallBearingElement)

        @property
        def loaded_four_point_contact_ball_bearing_element(
            self: "LoadedElement._Cast_LoadedElement",
        ) -> "_2035.LoadedFourPointContactBallBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2035

            return self._parent._cast(_2035.LoadedFourPointContactBallBearingElement)

        @property
        def loaded_multi_point_contact_ball_bearing_element(
            self: "LoadedElement._Cast_LoadedElement",
        ) -> "_2039.LoadedMultiPointContactBallBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2039

            return self._parent._cast(_2039.LoadedMultiPointContactBallBearingElement)

        @property
        def loaded_needle_roller_bearing_element(
            self: "LoadedElement._Cast_LoadedElement",
        ) -> "_2040.LoadedNeedleRollerBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2040

            return self._parent._cast(_2040.LoadedNeedleRollerBearingElement)

        @property
        def loaded_non_barrel_roller_element(
            self: "LoadedElement._Cast_LoadedElement",
        ) -> "_2047.LoadedNonBarrelRollerElement":
            from mastapy.bearings.bearing_results.rolling import _2047

            return self._parent._cast(_2047.LoadedNonBarrelRollerElement)

        @property
        def loaded_roller_bearing_element(
            self: "LoadedElement._Cast_LoadedElement",
        ) -> "_2048.LoadedRollerBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2048

            return self._parent._cast(_2048.LoadedRollerBearingElement)

        @property
        def loaded_self_aligning_ball_bearing_element(
            self: "LoadedElement._Cast_LoadedElement",
        ) -> "_2055.LoadedSelfAligningBallBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2055

            return self._parent._cast(_2055.LoadedSelfAligningBallBearingElement)

        @property
        def loaded_spherical_radial_roller_bearing_element(
            self: "LoadedElement._Cast_LoadedElement",
        ) -> "_2058.LoadedSphericalRadialRollerBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2058

            return self._parent._cast(_2058.LoadedSphericalRadialRollerBearingElement)

        @property
        def loaded_spherical_roller_bearing_element(
            self: "LoadedElement._Cast_LoadedElement",
        ) -> "_2059.LoadedSphericalRollerBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2059

            return self._parent._cast(_2059.LoadedSphericalRollerBearingElement)

        @property
        def loaded_spherical_thrust_roller_bearing_element(
            self: "LoadedElement._Cast_LoadedElement",
        ) -> "_2065.LoadedSphericalThrustRollerBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2065

            return self._parent._cast(_2065.LoadedSphericalThrustRollerBearingElement)

        @property
        def loaded_taper_roller_bearing_element(
            self: "LoadedElement._Cast_LoadedElement",
        ) -> "_2067.LoadedTaperRollerBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2067

            return self._parent._cast(_2067.LoadedTaperRollerBearingElement)

        @property
        def loaded_three_point_contact_ball_bearing_element(
            self: "LoadedElement._Cast_LoadedElement",
        ) -> "_2070.LoadedThreePointContactBallBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2070

            return self._parent._cast(_2070.LoadedThreePointContactBallBearingElement)

        @property
        def loaded_thrust_ball_bearing_element(
            self: "LoadedElement._Cast_LoadedElement",
        ) -> "_2073.LoadedThrustBallBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2073

            return self._parent._cast(_2073.LoadedThrustBallBearingElement)

        @property
        def loaded_toroidal_roller_bearing_element(
            self: "LoadedElement._Cast_LoadedElement",
        ) -> "_2076.LoadedToroidalRollerBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2076

            return self._parent._cast(_2076.LoadedToroidalRollerBearingElement)

        @property
        def loaded_element(
            self: "LoadedElement._Cast_LoadedElement",
        ) -> "LoadedElement":
            return self._parent

        def __getattr__(self: "LoadedElement._Cast_LoadedElement", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedElement.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Angle

        if temp is None:
            return 0.0

        return temp

    @property
    def axial_loading(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialLoading

        if temp is None:
            return 0.0

        return temp

    @property
    def element_id(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementId

        if temp is None:
            return ""

        return temp

    @property
    def element_raceway_contact_area_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementRacewayContactAreaInner

        if temp is None:
            return 0.0

        return temp

    @property
    def element_raceway_contact_area_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementRacewayContactAreaLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def element_raceway_contact_area_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementRacewayContactAreaOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def element_raceway_contact_area_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementRacewayContactAreaRight

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalStress

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_lubricating_film_thickness_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumLubricatingFilmThicknessInner

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_lubricating_film_thickness_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumLubricatingFilmThicknessOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_load_inner(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NormalLoadInner

        if temp is None:
            return 0.0

        return temp

    @normal_load_inner.setter
    @enforce_parameter_types
    def normal_load_inner(self: Self, value: "float"):
        self.wrapped.NormalLoadInner = float(value) if value is not None else 0.0

    @property
    def normal_load_outer(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NormalLoadOuter

        if temp is None:
            return 0.0

        return temp

    @normal_load_outer.setter
    @enforce_parameter_types
    def normal_load_outer(self: Self, value: "float"):
        self.wrapped.NormalLoadOuter = float(value) if value is not None else 0.0

    @property
    def race_deflection_inner(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RaceDeflectionInner

        if temp is None:
            return 0.0

        return temp

    @race_deflection_inner.setter
    @enforce_parameter_types
    def race_deflection_inner(self: Self, value: "float"):
        self.wrapped.RaceDeflectionInner = float(value) if value is not None else 0.0

    @property
    def race_deflection_outer(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RaceDeflectionOuter

        if temp is None:
            return 0.0

        return temp

    @race_deflection_outer.setter
    @enforce_parameter_types
    def race_deflection_outer(self: Self, value: "float"):
        self.wrapped.RaceDeflectionOuter = float(value) if value is not None else 0.0

    @property
    def race_deflection_total(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RaceDeflectionTotal

        if temp is None:
            return 0.0

        return temp

    @race_deflection_total.setter
    @enforce_parameter_types
    def race_deflection_total(self: Self, value: "float"):
        self.wrapped.RaceDeflectionTotal = float(value) if value is not None else 0.0

    @property
    def race_separation_at_element_axial(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RaceSeparationAtElementAxial

        if temp is None:
            return 0.0

        return temp

    @property
    def race_separation_at_element_radial(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RaceSeparationAtElementRadial

        if temp is None:
            return 0.0

        return temp

    @property
    def force_from_inner_race(self: Self) -> "_1964.ElementForce":
        """mastapy.bearings.bearing_results.ElementForce

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceFromInnerRace

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def operating_internal_clearance(self: Self) -> "_1993.InternalClearance":
        """mastapy.bearings.bearing_results.rolling.InternalClearance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OperatingInternalClearance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def subsurface_shear_stress_distribution_inner(
        self: Self,
    ) -> "List[_2093.StressAtPosition]":
        """List[mastapy.bearings.bearing_results.rolling.StressAtPosition]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SubsurfaceShearStressDistributionInner

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def subsurface_shear_stress_distribution_outer(
        self: Self,
    ) -> "List[_2093.StressAtPosition]":
        """List[mastapy.bearings.bearing_results.rolling.StressAtPosition]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SubsurfaceShearStressDistributionOuter

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
    def cast_to(self: Self) -> "LoadedElement._Cast_LoadedElement":
        return self._Cast_LoadedElement(self)
