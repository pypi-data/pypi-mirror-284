"""LoadedNonLinearBearingResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.bearings.bearing_results import _1969
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_NON_LINEAR_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults", "LoadedNonLinearBearingResults"
)

if TYPE_CHECKING:
    from mastapy.materials.efficiency import _305, _306
    from mastapy.bearings.bearing_results import _1971, _1972, _1973, _1974
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
    from mastapy.bearings import _1895


__docformat__ = "restructuredtext en"
__all__ = ("LoadedNonLinearBearingResults",)


Self = TypeVar("Self", bound="LoadedNonLinearBearingResults")


class LoadedNonLinearBearingResults(_1969.LoadedBearingResults):
    """LoadedNonLinearBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_NON_LINEAR_BEARING_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedNonLinearBearingResults")

    class _Cast_LoadedNonLinearBearingResults:
        """Special nested class for casting LoadedNonLinearBearingResults to subclasses."""

        def __init__(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
            parent: "LoadedNonLinearBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_1969.LoadedBearingResults":
            return self._parent._cast(_1969.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_1895.BearingLoadCaseResultsLightweight":
            from mastapy.bearings import _1895

            return self._parent._cast(_1895.BearingLoadCaseResultsLightweight)

        @property
        def loaded_concept_axial_clearance_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_1971.LoadedConceptAxialClearanceBearingResults":
            from mastapy.bearings.bearing_results import _1971

            return self._parent._cast(_1971.LoadedConceptAxialClearanceBearingResults)

        @property
        def loaded_concept_clearance_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_1972.LoadedConceptClearanceBearingResults":
            from mastapy.bearings.bearing_results import _1972

            return self._parent._cast(_1972.LoadedConceptClearanceBearingResults)

        @property
        def loaded_concept_radial_clearance_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_1973.LoadedConceptRadialClearanceBearingResults":
            from mastapy.bearings.bearing_results import _1973

            return self._parent._cast(_1973.LoadedConceptRadialClearanceBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_1974.LoadedDetailedBearingResults":
            from mastapy.bearings.bearing_results import _1974

            return self._parent._cast(_1974.LoadedDetailedBearingResults)

        @property
        def loaded_angular_contact_ball_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2003.LoadedAngularContactBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2003

            return self._parent._cast(_2003.LoadedAngularContactBallBearingResults)

        @property
        def loaded_angular_contact_thrust_ball_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2006.LoadedAngularContactThrustBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2006

            return self._parent._cast(
                _2006.LoadedAngularContactThrustBallBearingResults
            )

        @property
        def loaded_asymmetric_spherical_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2009.LoadedAsymmetricSphericalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2009

            return self._parent._cast(
                _2009.LoadedAsymmetricSphericalRollerBearingResults
            )

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2014.LoadedAxialThrustCylindricalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2014

            return self._parent._cast(
                _2014.LoadedAxialThrustCylindricalRollerBearingResults
            )

        @property
        def loaded_axial_thrust_needle_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2017.LoadedAxialThrustNeedleRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2017

            return self._parent._cast(_2017.LoadedAxialThrustNeedleRollerBearingResults)

        @property
        def loaded_ball_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2022.LoadedBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2022

            return self._parent._cast(_2022.LoadedBallBearingResults)

        @property
        def loaded_crossed_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2025.LoadedCrossedRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2025

            return self._parent._cast(_2025.LoadedCrossedRollerBearingResults)

        @property
        def loaded_cylindrical_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2029.LoadedCylindricalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2029

            return self._parent._cast(_2029.LoadedCylindricalRollerBearingResults)

        @property
        def loaded_deep_groove_ball_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2032.LoadedDeepGrooveBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2032

            return self._parent._cast(_2032.LoadedDeepGrooveBallBearingResults)

        @property
        def loaded_four_point_contact_ball_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2037.LoadedFourPointContactBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2037

            return self._parent._cast(_2037.LoadedFourPointContactBallBearingResults)

        @property
        def loaded_needle_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2041.LoadedNeedleRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2041

            return self._parent._cast(_2041.LoadedNeedleRollerBearingResults)

        @property
        def loaded_non_barrel_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2044.LoadedNonBarrelRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2044

            return self._parent._cast(_2044.LoadedNonBarrelRollerBearingResults)

        @property
        def loaded_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2049.LoadedRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2049

            return self._parent._cast(_2049.LoadedRollerBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2053.LoadedRollingBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2053

            return self._parent._cast(_2053.LoadedRollingBearingResults)

        @property
        def loaded_self_aligning_ball_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2056.LoadedSelfAligningBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2056

            return self._parent._cast(_2056.LoadedSelfAligningBallBearingResults)

        @property
        def loaded_spherical_roller_radial_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2060.LoadedSphericalRollerRadialBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2060

            return self._parent._cast(_2060.LoadedSphericalRollerRadialBearingResults)

        @property
        def loaded_spherical_roller_thrust_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2063.LoadedSphericalRollerThrustBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2063

            return self._parent._cast(_2063.LoadedSphericalRollerThrustBearingResults)

        @property
        def loaded_taper_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2068.LoadedTaperRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2068

            return self._parent._cast(_2068.LoadedTaperRollerBearingResults)

        @property
        def loaded_three_point_contact_ball_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2071.LoadedThreePointContactBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2071

            return self._parent._cast(_2071.LoadedThreePointContactBallBearingResults)

        @property
        def loaded_thrust_ball_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2074.LoadedThrustBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2074

            return self._parent._cast(_2074.LoadedThrustBallBearingResults)

        @property
        def loaded_toroidal_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2077.LoadedToroidalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2077

            return self._parent._cast(_2077.LoadedToroidalRollerBearingResults)

        @property
        def loaded_fluid_film_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2139.LoadedFluidFilmBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2139

            return self._parent._cast(_2139.LoadedFluidFilmBearingResults)

        @property
        def loaded_grease_filled_journal_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2140.LoadedGreaseFilledJournalBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2140

            return self._parent._cast(_2140.LoadedGreaseFilledJournalBearingResults)

        @property
        def loaded_pad_fluid_film_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2141.LoadedPadFluidFilmBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2141

            return self._parent._cast(_2141.LoadedPadFluidFilmBearingResults)

        @property
        def loaded_plain_journal_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2142.LoadedPlainJournalBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2142

            return self._parent._cast(_2142.LoadedPlainJournalBearingResults)

        @property
        def loaded_plain_oil_fed_journal_bearing(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2144.LoadedPlainOilFedJournalBearing":
            from mastapy.bearings.bearing_results.fluid_film import _2144

            return self._parent._cast(_2144.LoadedPlainOilFedJournalBearing)

        @property
        def loaded_tilting_pad_journal_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2147.LoadedTiltingPadJournalBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2147

            return self._parent._cast(_2147.LoadedTiltingPadJournalBearingResults)

        @property
        def loaded_tilting_pad_thrust_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2148.LoadedTiltingPadThrustBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2148

            return self._parent._cast(_2148.LoadedTiltingPadThrustBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "LoadedNonLinearBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedNonLinearBearingResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def power_loss(self: Self) -> "_305.PowerLoss":
        """mastapy.materials.efficiency.PowerLoss

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLoss

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def resistive_torque(self: Self) -> "_306.ResistiveTorque":
        """mastapy.materials.efficiency.ResistiveTorque

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResistiveTorque

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults":
        return self._Cast_LoadedNonLinearBearingResults(self)
