"""LoadedBearingResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.bearings import _1895
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults", "LoadedBearingResults"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results import (
        _1980,
        _1971,
        _1972,
        _1973,
        _1974,
        _1975,
        _1977,
    )
    from mastapy.bearings.bearing_designs import _2150
    from mastapy.math_utility.measured_vectors import _1582
    from mastapy.bearings.bearing_results.rolling import (
        _2088,
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
__all__ = ("LoadedBearingResults",)


Self = TypeVar("Self", bound="LoadedBearingResults")


class LoadedBearingResults(_1895.BearingLoadCaseResultsLightweight):
    """LoadedBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_BEARING_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedBearingResults")

    class _Cast_LoadedBearingResults:
        """Special nested class for casting LoadedBearingResults to subclasses."""

        def __init__(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
            parent: "LoadedBearingResults",
        ):
            self._parent = parent

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_1895.BearingLoadCaseResultsLightweight":
            return self._parent._cast(_1895.BearingLoadCaseResultsLightweight)

        @property
        def loaded_concept_axial_clearance_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_1971.LoadedConceptAxialClearanceBearingResults":
            from mastapy.bearings.bearing_results import _1971

            return self._parent._cast(_1971.LoadedConceptAxialClearanceBearingResults)

        @property
        def loaded_concept_clearance_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_1972.LoadedConceptClearanceBearingResults":
            from mastapy.bearings.bearing_results import _1972

            return self._parent._cast(_1972.LoadedConceptClearanceBearingResults)

        @property
        def loaded_concept_radial_clearance_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_1973.LoadedConceptRadialClearanceBearingResults":
            from mastapy.bearings.bearing_results import _1973

            return self._parent._cast(_1973.LoadedConceptRadialClearanceBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_1974.LoadedDetailedBearingResults":
            from mastapy.bearings.bearing_results import _1974

            return self._parent._cast(_1974.LoadedDetailedBearingResults)

        @property
        def loaded_linear_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_1975.LoadedLinearBearingResults":
            from mastapy.bearings.bearing_results import _1975

            return self._parent._cast(_1975.LoadedLinearBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_1977.LoadedNonLinearBearingResults":
            from mastapy.bearings.bearing_results import _1977

            return self._parent._cast(_1977.LoadedNonLinearBearingResults)

        @property
        def loaded_angular_contact_ball_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2003.LoadedAngularContactBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2003

            return self._parent._cast(_2003.LoadedAngularContactBallBearingResults)

        @property
        def loaded_angular_contact_thrust_ball_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2006.LoadedAngularContactThrustBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2006

            return self._parent._cast(
                _2006.LoadedAngularContactThrustBallBearingResults
            )

        @property
        def loaded_asymmetric_spherical_roller_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2009.LoadedAsymmetricSphericalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2009

            return self._parent._cast(
                _2009.LoadedAsymmetricSphericalRollerBearingResults
            )

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2014.LoadedAxialThrustCylindricalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2014

            return self._parent._cast(
                _2014.LoadedAxialThrustCylindricalRollerBearingResults
            )

        @property
        def loaded_axial_thrust_needle_roller_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2017.LoadedAxialThrustNeedleRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2017

            return self._parent._cast(_2017.LoadedAxialThrustNeedleRollerBearingResults)

        @property
        def loaded_ball_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2022.LoadedBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2022

            return self._parent._cast(_2022.LoadedBallBearingResults)

        @property
        def loaded_crossed_roller_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2025.LoadedCrossedRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2025

            return self._parent._cast(_2025.LoadedCrossedRollerBearingResults)

        @property
        def loaded_cylindrical_roller_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2029.LoadedCylindricalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2029

            return self._parent._cast(_2029.LoadedCylindricalRollerBearingResults)

        @property
        def loaded_deep_groove_ball_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2032.LoadedDeepGrooveBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2032

            return self._parent._cast(_2032.LoadedDeepGrooveBallBearingResults)

        @property
        def loaded_four_point_contact_ball_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2037.LoadedFourPointContactBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2037

            return self._parent._cast(_2037.LoadedFourPointContactBallBearingResults)

        @property
        def loaded_needle_roller_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2041.LoadedNeedleRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2041

            return self._parent._cast(_2041.LoadedNeedleRollerBearingResults)

        @property
        def loaded_non_barrel_roller_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2044.LoadedNonBarrelRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2044

            return self._parent._cast(_2044.LoadedNonBarrelRollerBearingResults)

        @property
        def loaded_roller_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2049.LoadedRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2049

            return self._parent._cast(_2049.LoadedRollerBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2053.LoadedRollingBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2053

            return self._parent._cast(_2053.LoadedRollingBearingResults)

        @property
        def loaded_self_aligning_ball_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2056.LoadedSelfAligningBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2056

            return self._parent._cast(_2056.LoadedSelfAligningBallBearingResults)

        @property
        def loaded_spherical_roller_radial_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2060.LoadedSphericalRollerRadialBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2060

            return self._parent._cast(_2060.LoadedSphericalRollerRadialBearingResults)

        @property
        def loaded_spherical_roller_thrust_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2063.LoadedSphericalRollerThrustBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2063

            return self._parent._cast(_2063.LoadedSphericalRollerThrustBearingResults)

        @property
        def loaded_taper_roller_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2068.LoadedTaperRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2068

            return self._parent._cast(_2068.LoadedTaperRollerBearingResults)

        @property
        def loaded_three_point_contact_ball_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2071.LoadedThreePointContactBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2071

            return self._parent._cast(_2071.LoadedThreePointContactBallBearingResults)

        @property
        def loaded_thrust_ball_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2074.LoadedThrustBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2074

            return self._parent._cast(_2074.LoadedThrustBallBearingResults)

        @property
        def loaded_toroidal_roller_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2077.LoadedToroidalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2077

            return self._parent._cast(_2077.LoadedToroidalRollerBearingResults)

        @property
        def loaded_fluid_film_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2139.LoadedFluidFilmBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2139

            return self._parent._cast(_2139.LoadedFluidFilmBearingResults)

        @property
        def loaded_grease_filled_journal_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2140.LoadedGreaseFilledJournalBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2140

            return self._parent._cast(_2140.LoadedGreaseFilledJournalBearingResults)

        @property
        def loaded_pad_fluid_film_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2141.LoadedPadFluidFilmBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2141

            return self._parent._cast(_2141.LoadedPadFluidFilmBearingResults)

        @property
        def loaded_plain_journal_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2142.LoadedPlainJournalBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2142

            return self._parent._cast(_2142.LoadedPlainJournalBearingResults)

        @property
        def loaded_plain_oil_fed_journal_bearing(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2144.LoadedPlainOilFedJournalBearing":
            from mastapy.bearings.bearing_results.fluid_film import _2144

            return self._parent._cast(_2144.LoadedPlainOilFedJournalBearing)

        @property
        def loaded_tilting_pad_journal_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2147.LoadedTiltingPadJournalBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2147

            return self._parent._cast(_2147.LoadedTiltingPadJournalBearingResults)

        @property
        def loaded_tilting_pad_thrust_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "_2148.LoadedTiltingPadThrustBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2148

            return self._parent._cast(_2148.LoadedTiltingPadThrustBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedBearingResults._Cast_LoadedBearingResults",
        ) -> "LoadedBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedBearingResults._Cast_LoadedBearingResults", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedBearingResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle_of_gravity_from_z_axis(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngleOfGravityFromZAxis

        if temp is None:
            return 0.0

        return temp

    @property
    def axial_displacement_preload(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AxialDisplacementPreload

        if temp is None:
            return 0.0

        return temp

    @axial_displacement_preload.setter
    @enforce_parameter_types
    def axial_displacement_preload(self: Self, value: "float"):
        self.wrapped.AxialDisplacementPreload = (
            float(value) if value is not None else 0.0
        )

    @property
    def duration(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Duration

        if temp is None:
            return 0.0

        return temp

    @duration.setter
    @enforce_parameter_types
    def duration(self: Self, value: "float"):
        self.wrapped.Duration = float(value) if value is not None else 0.0

    @property
    def force_results_are_overridden(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceResultsAreOverridden

        if temp is None:
            return False

        return temp

    @property
    def inner_ring_angular_velocity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.InnerRingAngularVelocity

        if temp is None:
            return 0.0

        return temp

    @inner_ring_angular_velocity.setter
    @enforce_parameter_types
    def inner_ring_angular_velocity(self: Self, value: "float"):
        self.wrapped.InnerRingAngularVelocity = (
            float(value) if value is not None else 0.0
        )

    @property
    def orientation(self: Self) -> "_1980.Orientations":
        """mastapy.bearings.bearing_results.Orientations"""
        temp = self.wrapped.Orientation

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Bearings.BearingResults.Orientations"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings.bearing_results._1980", "Orientations"
        )(value)

    @orientation.setter
    @enforce_parameter_types
    def orientation(self: Self, value: "_1980.Orientations"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Bearings.BearingResults.Orientations"
        )
        self.wrapped.Orientation = value

    @property
    def outer_ring_angular_velocity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OuterRingAngularVelocity

        if temp is None:
            return 0.0

        return temp

    @outer_ring_angular_velocity.setter
    @enforce_parameter_types
    def outer_ring_angular_velocity(self: Self, value: "float"):
        self.wrapped.OuterRingAngularVelocity = (
            float(value) if value is not None else 0.0
        )

    @property
    def relative_angular_velocity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeAngularVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_axial_displacement(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeAxialDisplacement

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_radial_displacement(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeRadialDisplacement

        if temp is None:
            return 0.0

        return temp

    @property
    def signed_relative_angular_velocity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SignedRelativeAngularVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def specified_axial_internal_clearance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SpecifiedAxialInternalClearance

        if temp is None:
            return 0.0

        return temp

    @specified_axial_internal_clearance.setter
    @enforce_parameter_types
    def specified_axial_internal_clearance(self: Self, value: "float"):
        self.wrapped.SpecifiedAxialInternalClearance = (
            float(value) if value is not None else 0.0
        )

    @property
    def specified_radial_internal_clearance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SpecifiedRadialInternalClearance

        if temp is None:
            return 0.0

        return temp

    @specified_radial_internal_clearance.setter
    @enforce_parameter_types
    def specified_radial_internal_clearance(self: Self, value: "float"):
        self.wrapped.SpecifiedRadialInternalClearance = (
            float(value) if value is not None else 0.0
        )

    @property
    def bearing(self: Self) -> "_2150.BearingDesign":
        """mastapy.bearings.bearing_designs.BearingDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Bearing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def force_on_inner_race(self: Self) -> "_1582.VectorWithLinearAndAngularComponents":
        """mastapy.math_utility.measured_vectors.VectorWithLinearAndAngularComponents

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceOnInnerRace

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def ring_results(self: Self) -> "List[_2088.RingForceAndDisplacement]":
        """List[mastapy.bearings.bearing_results.rolling.RingForceAndDisplacement]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RingResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "LoadedBearingResults._Cast_LoadedBearingResults":
        return self._Cast_LoadedBearingResults(self)
