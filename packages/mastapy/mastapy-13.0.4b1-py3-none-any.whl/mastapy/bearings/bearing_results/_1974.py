"""LoadedDetailedBearingResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.bearings.bearing_results import _1977
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_DETAILED_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults", "LoadedDetailedBearingResults"
)

if TYPE_CHECKING:
    from mastapy.materials import _270
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
    from mastapy.bearings.bearing_results import _1969
    from mastapy.bearings import _1895


__docformat__ = "restructuredtext en"
__all__ = ("LoadedDetailedBearingResults",)


Self = TypeVar("Self", bound="LoadedDetailedBearingResults")


class LoadedDetailedBearingResults(_1977.LoadedNonLinearBearingResults):
    """LoadedDetailedBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_DETAILED_BEARING_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedDetailedBearingResults")

    class _Cast_LoadedDetailedBearingResults:
        """Special nested class for casting LoadedDetailedBearingResults to subclasses."""

        def __init__(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
            parent: "LoadedDetailedBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_1977.LoadedNonLinearBearingResults":
            return self._parent._cast(_1977.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_1969.LoadedBearingResults":
            from mastapy.bearings.bearing_results import _1969

            return self._parent._cast(_1969.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_1895.BearingLoadCaseResultsLightweight":
            from mastapy.bearings import _1895

            return self._parent._cast(_1895.BearingLoadCaseResultsLightweight)

        @property
        def loaded_angular_contact_ball_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2003.LoadedAngularContactBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2003

            return self._parent._cast(_2003.LoadedAngularContactBallBearingResults)

        @property
        def loaded_angular_contact_thrust_ball_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2006.LoadedAngularContactThrustBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2006

            return self._parent._cast(
                _2006.LoadedAngularContactThrustBallBearingResults
            )

        @property
        def loaded_asymmetric_spherical_roller_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2009.LoadedAsymmetricSphericalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2009

            return self._parent._cast(
                _2009.LoadedAsymmetricSphericalRollerBearingResults
            )

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2014.LoadedAxialThrustCylindricalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2014

            return self._parent._cast(
                _2014.LoadedAxialThrustCylindricalRollerBearingResults
            )

        @property
        def loaded_axial_thrust_needle_roller_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2017.LoadedAxialThrustNeedleRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2017

            return self._parent._cast(_2017.LoadedAxialThrustNeedleRollerBearingResults)

        @property
        def loaded_ball_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2022.LoadedBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2022

            return self._parent._cast(_2022.LoadedBallBearingResults)

        @property
        def loaded_crossed_roller_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2025.LoadedCrossedRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2025

            return self._parent._cast(_2025.LoadedCrossedRollerBearingResults)

        @property
        def loaded_cylindrical_roller_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2029.LoadedCylindricalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2029

            return self._parent._cast(_2029.LoadedCylindricalRollerBearingResults)

        @property
        def loaded_deep_groove_ball_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2032.LoadedDeepGrooveBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2032

            return self._parent._cast(_2032.LoadedDeepGrooveBallBearingResults)

        @property
        def loaded_four_point_contact_ball_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2037.LoadedFourPointContactBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2037

            return self._parent._cast(_2037.LoadedFourPointContactBallBearingResults)

        @property
        def loaded_needle_roller_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2041.LoadedNeedleRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2041

            return self._parent._cast(_2041.LoadedNeedleRollerBearingResults)

        @property
        def loaded_non_barrel_roller_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2044.LoadedNonBarrelRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2044

            return self._parent._cast(_2044.LoadedNonBarrelRollerBearingResults)

        @property
        def loaded_roller_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2049.LoadedRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2049

            return self._parent._cast(_2049.LoadedRollerBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2053.LoadedRollingBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2053

            return self._parent._cast(_2053.LoadedRollingBearingResults)

        @property
        def loaded_self_aligning_ball_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2056.LoadedSelfAligningBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2056

            return self._parent._cast(_2056.LoadedSelfAligningBallBearingResults)

        @property
        def loaded_spherical_roller_radial_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2060.LoadedSphericalRollerRadialBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2060

            return self._parent._cast(_2060.LoadedSphericalRollerRadialBearingResults)

        @property
        def loaded_spherical_roller_thrust_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2063.LoadedSphericalRollerThrustBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2063

            return self._parent._cast(_2063.LoadedSphericalRollerThrustBearingResults)

        @property
        def loaded_taper_roller_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2068.LoadedTaperRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2068

            return self._parent._cast(_2068.LoadedTaperRollerBearingResults)

        @property
        def loaded_three_point_contact_ball_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2071.LoadedThreePointContactBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2071

            return self._parent._cast(_2071.LoadedThreePointContactBallBearingResults)

        @property
        def loaded_thrust_ball_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2074.LoadedThrustBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2074

            return self._parent._cast(_2074.LoadedThrustBallBearingResults)

        @property
        def loaded_toroidal_roller_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2077.LoadedToroidalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2077

            return self._parent._cast(_2077.LoadedToroidalRollerBearingResults)

        @property
        def loaded_fluid_film_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2139.LoadedFluidFilmBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2139

            return self._parent._cast(_2139.LoadedFluidFilmBearingResults)

        @property
        def loaded_grease_filled_journal_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2140.LoadedGreaseFilledJournalBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2140

            return self._parent._cast(_2140.LoadedGreaseFilledJournalBearingResults)

        @property
        def loaded_pad_fluid_film_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2141.LoadedPadFluidFilmBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2141

            return self._parent._cast(_2141.LoadedPadFluidFilmBearingResults)

        @property
        def loaded_plain_journal_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2142.LoadedPlainJournalBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2142

            return self._parent._cast(_2142.LoadedPlainJournalBearingResults)

        @property
        def loaded_plain_oil_fed_journal_bearing(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2144.LoadedPlainOilFedJournalBearing":
            from mastapy.bearings.bearing_results.fluid_film import _2144

            return self._parent._cast(_2144.LoadedPlainOilFedJournalBearing)

        @property
        def loaded_tilting_pad_journal_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2147.LoadedTiltingPadJournalBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2147

            return self._parent._cast(_2147.LoadedTiltingPadJournalBearingResults)

        @property
        def loaded_tilting_pad_thrust_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "_2148.LoadedTiltingPadThrustBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2148

            return self._parent._cast(_2148.LoadedTiltingPadThrustBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
        ) -> "LoadedDetailedBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedDetailedBearingResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def lubricant_flow_rate(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LubricantFlowRate

        if temp is None:
            return 0.0

        return temp

    @lubricant_flow_rate.setter
    @enforce_parameter_types
    def lubricant_flow_rate(self: Self, value: "float"):
        self.wrapped.LubricantFlowRate = float(value) if value is not None else 0.0

    @property
    def oil_sump_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OilSumpTemperature

        if temp is None:
            return 0.0

        return temp

    @oil_sump_temperature.setter
    @enforce_parameter_types
    def oil_sump_temperature(self: Self, value: "float"):
        self.wrapped.OilSumpTemperature = float(value) if value is not None else 0.0

    @property
    def operating_air_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OperatingAirTemperature

        if temp is None:
            return 0.0

        return temp

    @operating_air_temperature.setter
    @enforce_parameter_types
    def operating_air_temperature(self: Self, value: "float"):
        self.wrapped.OperatingAirTemperature = (
            float(value) if value is not None else 0.0
        )

    @property
    def temperature_when_assembled(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TemperatureWhenAssembled

        if temp is None:
            return 0.0

        return temp

    @temperature_when_assembled.setter
    @enforce_parameter_types
    def temperature_when_assembled(self: Self, value: "float"):
        self.wrapped.TemperatureWhenAssembled = (
            float(value) if value is not None else 0.0
        )

    @property
    def lubrication(self: Self) -> "_270.LubricationDetail":
        """mastapy.materials.LubricationDetail

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Lubrication

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults":
        return self._Cast_LoadedDetailedBearingResults(self)
