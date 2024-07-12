"""BearingLoadCaseResultsLightweight"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_LOAD_CASE_RESULTS_LIGHTWEIGHT = python_net_import(
    "SMT.MastaAPI.Bearings", "BearingLoadCaseResultsLightweight"
)

if TYPE_CHECKING:
    from mastapy.bearings import _1894
    from mastapy.bearings.bearing_results import (
        _1969,
        _1971,
        _1972,
        _1973,
        _1974,
        _1975,
        _1977,
    )
    from mastapy.bearings.bearing_results.rolling import (
        _2003,
        _2006,
        _2009,
        _2014,
        _2017,
        _2022,
        _2025,
        _2029,
        _2032,
        _2037,
        _2041,
        _2044,
        _2049,
        _2053,
        _2056,
        _2060,
        _2063,
        _2068,
        _2071,
        _2074,
        _2077,
    )
    from mastapy.bearings.bearing_results.fluid_film import (
        _2139,
        _2140,
        _2141,
        _2142,
        _2144,
        _2147,
        _2148,
    )


__docformat__ = "restructuredtext en"
__all__ = ("BearingLoadCaseResultsLightweight",)


Self = TypeVar("Self", bound="BearingLoadCaseResultsLightweight")


class BearingLoadCaseResultsLightweight(_0.APIBase):
    """BearingLoadCaseResultsLightweight

    This is a mastapy class.
    """

    TYPE = _BEARING_LOAD_CASE_RESULTS_LIGHTWEIGHT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BearingLoadCaseResultsLightweight")

    class _Cast_BearingLoadCaseResultsLightweight:
        """Special nested class for casting BearingLoadCaseResultsLightweight to subclasses."""

        def __init__(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
            parent: "BearingLoadCaseResultsLightweight",
        ):
            self._parent = parent

        @property
        def bearing_load_case_results_for_pst(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_1894.BearingLoadCaseResultsForPST":
            from mastapy.bearings import _1894

            return self._parent._cast(_1894.BearingLoadCaseResultsForPST)

        @property
        def loaded_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_1969.LoadedBearingResults":
            from mastapy.bearings.bearing_results import _1969

            return self._parent._cast(_1969.LoadedBearingResults)

        @property
        def loaded_concept_axial_clearance_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_1971.LoadedConceptAxialClearanceBearingResults":
            from mastapy.bearings.bearing_results import _1971

            return self._parent._cast(_1971.LoadedConceptAxialClearanceBearingResults)

        @property
        def loaded_concept_clearance_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_1972.LoadedConceptClearanceBearingResults":
            from mastapy.bearings.bearing_results import _1972

            return self._parent._cast(_1972.LoadedConceptClearanceBearingResults)

        @property
        def loaded_concept_radial_clearance_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_1973.LoadedConceptRadialClearanceBearingResults":
            from mastapy.bearings.bearing_results import _1973

            return self._parent._cast(_1973.LoadedConceptRadialClearanceBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_1974.LoadedDetailedBearingResults":
            from mastapy.bearings.bearing_results import _1974

            return self._parent._cast(_1974.LoadedDetailedBearingResults)

        @property
        def loaded_linear_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_1975.LoadedLinearBearingResults":
            from mastapy.bearings.bearing_results import _1975

            return self._parent._cast(_1975.LoadedLinearBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_1977.LoadedNonLinearBearingResults":
            from mastapy.bearings.bearing_results import _1977

            return self._parent._cast(_1977.LoadedNonLinearBearingResults)

        @property
        def loaded_angular_contact_ball_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2003.LoadedAngularContactBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2003

            return self._parent._cast(_2003.LoadedAngularContactBallBearingResults)

        @property
        def loaded_angular_contact_thrust_ball_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2006.LoadedAngularContactThrustBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2006

            return self._parent._cast(
                _2006.LoadedAngularContactThrustBallBearingResults
            )

        @property
        def loaded_asymmetric_spherical_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2009.LoadedAsymmetricSphericalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2009

            return self._parent._cast(
                _2009.LoadedAsymmetricSphericalRollerBearingResults
            )

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2014.LoadedAxialThrustCylindricalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2014

            return self._parent._cast(
                _2014.LoadedAxialThrustCylindricalRollerBearingResults
            )

        @property
        def loaded_axial_thrust_needle_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2017.LoadedAxialThrustNeedleRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2017

            return self._parent._cast(_2017.LoadedAxialThrustNeedleRollerBearingResults)

        @property
        def loaded_ball_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2022.LoadedBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2022

            return self._parent._cast(_2022.LoadedBallBearingResults)

        @property
        def loaded_crossed_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2025.LoadedCrossedRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2025

            return self._parent._cast(_2025.LoadedCrossedRollerBearingResults)

        @property
        def loaded_cylindrical_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2029.LoadedCylindricalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2029

            return self._parent._cast(_2029.LoadedCylindricalRollerBearingResults)

        @property
        def loaded_deep_groove_ball_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2032.LoadedDeepGrooveBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2032

            return self._parent._cast(_2032.LoadedDeepGrooveBallBearingResults)

        @property
        def loaded_four_point_contact_ball_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2037.LoadedFourPointContactBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2037

            return self._parent._cast(_2037.LoadedFourPointContactBallBearingResults)

        @property
        def loaded_needle_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2041.LoadedNeedleRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2041

            return self._parent._cast(_2041.LoadedNeedleRollerBearingResults)

        @property
        def loaded_non_barrel_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2044.LoadedNonBarrelRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2044

            return self._parent._cast(_2044.LoadedNonBarrelRollerBearingResults)

        @property
        def loaded_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2049.LoadedRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2049

            return self._parent._cast(_2049.LoadedRollerBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2053.LoadedRollingBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2053

            return self._parent._cast(_2053.LoadedRollingBearingResults)

        @property
        def loaded_self_aligning_ball_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2056.LoadedSelfAligningBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2056

            return self._parent._cast(_2056.LoadedSelfAligningBallBearingResults)

        @property
        def loaded_spherical_roller_radial_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2060.LoadedSphericalRollerRadialBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2060

            return self._parent._cast(_2060.LoadedSphericalRollerRadialBearingResults)

        @property
        def loaded_spherical_roller_thrust_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2063.LoadedSphericalRollerThrustBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2063

            return self._parent._cast(_2063.LoadedSphericalRollerThrustBearingResults)

        @property
        def loaded_taper_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2068.LoadedTaperRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2068

            return self._parent._cast(_2068.LoadedTaperRollerBearingResults)

        @property
        def loaded_three_point_contact_ball_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2071.LoadedThreePointContactBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2071

            return self._parent._cast(_2071.LoadedThreePointContactBallBearingResults)

        @property
        def loaded_thrust_ball_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2074.LoadedThrustBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2074

            return self._parent._cast(_2074.LoadedThrustBallBearingResults)

        @property
        def loaded_toroidal_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2077.LoadedToroidalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2077

            return self._parent._cast(_2077.LoadedToroidalRollerBearingResults)

        @property
        def loaded_fluid_film_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2139.LoadedFluidFilmBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2139

            return self._parent._cast(_2139.LoadedFluidFilmBearingResults)

        @property
        def loaded_grease_filled_journal_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2140.LoadedGreaseFilledJournalBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2140

            return self._parent._cast(_2140.LoadedGreaseFilledJournalBearingResults)

        @property
        def loaded_pad_fluid_film_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2141.LoadedPadFluidFilmBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2141

            return self._parent._cast(_2141.LoadedPadFluidFilmBearingResults)

        @property
        def loaded_plain_journal_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2142.LoadedPlainJournalBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2142

            return self._parent._cast(_2142.LoadedPlainJournalBearingResults)

        @property
        def loaded_plain_oil_fed_journal_bearing(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2144.LoadedPlainOilFedJournalBearing":
            from mastapy.bearings.bearing_results.fluid_film import _2144

            return self._parent._cast(_2144.LoadedPlainOilFedJournalBearing)

        @property
        def loaded_tilting_pad_journal_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2147.LoadedTiltingPadJournalBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2147

            return self._parent._cast(_2147.LoadedTiltingPadJournalBearingResults)

        @property
        def loaded_tilting_pad_thrust_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2148.LoadedTiltingPadThrustBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2148

            return self._parent._cast(_2148.LoadedTiltingPadThrustBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "BearingLoadCaseResultsLightweight":
            return self._parent

        def __getattr__(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "BearingLoadCaseResultsLightweight.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def relative_misalignment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeMisalignment

        if temp is None:
            return 0.0

        return temp

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
    def cast_to(
        self: Self,
    ) -> "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight":
        return self._Cast_BearingLoadCaseResultsLightweight(self)
