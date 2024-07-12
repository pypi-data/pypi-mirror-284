"""LoadedRollingBearingDutyCycle"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.bearings import _1895
from mastapy.bearings.bearing_results import _1976
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ROLLING_BEARING_DUTY_CYCLE = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults", "LoadedRollingBearingDutyCycle"
)

if TYPE_CHECKING:
    from mastapy.utility.property import _1858, _1861, _1859, _1860
    from mastapy.nodal_analysis import _50
    from mastapy.bearings.bearing_results.rolling import (
        _2081,
        _2012,
        _2019,
        _2027,
        _2043,
        _2066,
    )
    from mastapy.bearings.bearing_results import _1968


__docformat__ = "restructuredtext en"
__all__ = ("LoadedRollingBearingDutyCycle",)


Self = TypeVar("Self", bound="LoadedRollingBearingDutyCycle")


class LoadedRollingBearingDutyCycle(_1976.LoadedNonLinearBearingDutyCycleResults):
    """LoadedRollingBearingDutyCycle

    This is a mastapy class.
    """

    TYPE = _LOADED_ROLLING_BEARING_DUTY_CYCLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedRollingBearingDutyCycle")

    class _Cast_LoadedRollingBearingDutyCycle:
        """Special nested class for casting LoadedRollingBearingDutyCycle to subclasses."""

        def __init__(
            self: "LoadedRollingBearingDutyCycle._Cast_LoadedRollingBearingDutyCycle",
            parent: "LoadedRollingBearingDutyCycle",
        ):
            self._parent = parent

        @property
        def loaded_non_linear_bearing_duty_cycle_results(
            self: "LoadedRollingBearingDutyCycle._Cast_LoadedRollingBearingDutyCycle",
        ) -> "_1976.LoadedNonLinearBearingDutyCycleResults":
            return self._parent._cast(_1976.LoadedNonLinearBearingDutyCycleResults)

        @property
        def loaded_bearing_duty_cycle(
            self: "LoadedRollingBearingDutyCycle._Cast_LoadedRollingBearingDutyCycle",
        ) -> "_1968.LoadedBearingDutyCycle":
            from mastapy.bearings.bearing_results import _1968

            return self._parent._cast(_1968.LoadedBearingDutyCycle)

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_duty_cycle(
            self: "LoadedRollingBearingDutyCycle._Cast_LoadedRollingBearingDutyCycle",
        ) -> "_2012.LoadedAxialThrustCylindricalRollerBearingDutyCycle":
            from mastapy.bearings.bearing_results.rolling import _2012

            return self._parent._cast(
                _2012.LoadedAxialThrustCylindricalRollerBearingDutyCycle
            )

        @property
        def loaded_ball_bearing_duty_cycle(
            self: "LoadedRollingBearingDutyCycle._Cast_LoadedRollingBearingDutyCycle",
        ) -> "_2019.LoadedBallBearingDutyCycle":
            from mastapy.bearings.bearing_results.rolling import _2019

            return self._parent._cast(_2019.LoadedBallBearingDutyCycle)

        @property
        def loaded_cylindrical_roller_bearing_duty_cycle(
            self: "LoadedRollingBearingDutyCycle._Cast_LoadedRollingBearingDutyCycle",
        ) -> "_2027.LoadedCylindricalRollerBearingDutyCycle":
            from mastapy.bearings.bearing_results.rolling import _2027

            return self._parent._cast(_2027.LoadedCylindricalRollerBearingDutyCycle)

        @property
        def loaded_non_barrel_roller_bearing_duty_cycle(
            self: "LoadedRollingBearingDutyCycle._Cast_LoadedRollingBearingDutyCycle",
        ) -> "_2043.LoadedNonBarrelRollerBearingDutyCycle":
            from mastapy.bearings.bearing_results.rolling import _2043

            return self._parent._cast(_2043.LoadedNonBarrelRollerBearingDutyCycle)

        @property
        def loaded_taper_roller_bearing_duty_cycle(
            self: "LoadedRollingBearingDutyCycle._Cast_LoadedRollingBearingDutyCycle",
        ) -> "_2066.LoadedTaperRollerBearingDutyCycle":
            from mastapy.bearings.bearing_results.rolling import _2066

            return self._parent._cast(_2066.LoadedTaperRollerBearingDutyCycle)

        @property
        def loaded_rolling_bearing_duty_cycle(
            self: "LoadedRollingBearingDutyCycle._Cast_LoadedRollingBearingDutyCycle",
        ) -> "LoadedRollingBearingDutyCycle":
            return self._parent

        def __getattr__(
            self: "LoadedRollingBearingDutyCycle._Cast_LoadedRollingBearingDutyCycle",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedRollingBearingDutyCycle.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def ansiabma_adjusted_rating_life_damage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ANSIABMAAdjustedRatingLifeDamage

        if temp is None:
            return 0.0

        return temp

    @property
    def ansiabma_adjusted_rating_life_reliability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ANSIABMAAdjustedRatingLifeReliability

        if temp is None:
            return 0.0

        return temp

    @property
    def ansiabma_adjusted_rating_life_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ANSIABMAAdjustedRatingLifeSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def ansiabma_adjusted_rating_life_time(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ANSIABMAAdjustedRatingLifeTime

        if temp is None:
            return 0.0

        return temp

    @property
    def ansiabma_adjusted_rating_life_unreliability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ANSIABMAAdjustedRatingLifeUnreliability

        if temp is None:
            return 0.0

        return temp

    @property
    def ansiabma_basic_rating_life_damage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ANSIABMABasicRatingLifeDamage

        if temp is None:
            return 0.0

        return temp

    @property
    def ansiabma_basic_rating_life_reliability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ANSIABMABasicRatingLifeReliability

        if temp is None:
            return 0.0

        return temp

    @property
    def ansiabma_basic_rating_life_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ANSIABMABasicRatingLifeSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def ansiabma_basic_rating_life_time(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ANSIABMABasicRatingLifeTime

        if temp is None:
            return 0.0

        return temp

    @property
    def ansiabma_basic_rating_life_unreliability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ANSIABMABasicRatingLifeUnreliability

        if temp is None:
            return 0.0

        return temp

    @property
    def ansiabma_dynamic_equivalent_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ANSIABMADynamicEquivalentLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def iso2812007_basic_rating_life_damage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO2812007BasicRatingLifeDamage

        if temp is None:
            return 0.0

        return temp

    @property
    def iso2812007_basic_rating_life_reliability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO2812007BasicRatingLifeReliability

        if temp is None:
            return 0.0

        return temp

    @property
    def iso2812007_basic_rating_life_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO2812007BasicRatingLifeSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def iso2812007_basic_rating_life_time(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO2812007BasicRatingLifeTime

        if temp is None:
            return 0.0

        return temp

    @property
    def iso2812007_basic_rating_life_unreliability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO2812007BasicRatingLifeUnreliability

        if temp is None:
            return 0.0

        return temp

    @property
    def iso2812007_dynamic_equivalent_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO2812007DynamicEquivalentLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def iso2812007_modified_rating_life_damage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO2812007ModifiedRatingLifeDamage

        if temp is None:
            return 0.0

        return temp

    @property
    def iso2812007_modified_rating_life_reliability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO2812007ModifiedRatingLifeReliability

        if temp is None:
            return 0.0

        return temp

    @property
    def iso2812007_modified_rating_life_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO2812007ModifiedRatingLifeSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def iso2812007_modified_rating_life_time(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO2812007ModifiedRatingLifeTime

        if temp is None:
            return 0.0

        return temp

    @property
    def iso2812007_modified_rating_life_unreliability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO2812007ModifiedRatingLifeUnreliability

        if temp is None:
            return 0.0

        return temp

    @property
    def iso762006_recommended_maximum_element_normal_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO762006RecommendedMaximumElementNormalStress

        if temp is None:
            return 0.0

        return temp

    @property
    def isots162812008_basic_reference_rating_life_damage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISOTS162812008BasicReferenceRatingLifeDamage

        if temp is None:
            return 0.0

        return temp

    @property
    def isots162812008_basic_reference_rating_life_reliability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISOTS162812008BasicReferenceRatingLifeReliability

        if temp is None:
            return 0.0

        return temp

    @property
    def isots162812008_basic_reference_rating_life_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISOTS162812008BasicReferenceRatingLifeSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def isots162812008_basic_reference_rating_life_time(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISOTS162812008BasicReferenceRatingLifeTime

        if temp is None:
            return 0.0

        return temp

    @property
    def isots162812008_basic_reference_rating_life_unreliability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISOTS162812008BasicReferenceRatingLifeUnreliability

        if temp is None:
            return 0.0

        return temp

    @property
    def isots162812008_dynamic_equivalent_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISOTS162812008DynamicEquivalentLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def isots162812008_modified_reference_rating_life_damage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISOTS162812008ModifiedReferenceRatingLifeDamage

        if temp is None:
            return 0.0

        return temp

    @property
    def isots162812008_modified_reference_rating_life_reliability(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISOTS162812008ModifiedReferenceRatingLifeReliability

        if temp is None:
            return 0.0

        return temp

    @property
    def isots162812008_modified_reference_rating_life_safety_factor(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISOTS162812008ModifiedReferenceRatingLifeSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def isots162812008_modified_reference_rating_life_time(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISOTS162812008ModifiedReferenceRatingLifeTime

        if temp is None:
            return 0.0

        return temp

    @property
    def isots162812008_modified_reference_rating_life_unreliability(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISOTS162812008ModifiedReferenceRatingLifeUnreliability

        if temp is None:
            return 0.0

        return temp

    @property
    def lambda_ratio_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LambdaRatioInner

        if temp is None:
            return 0.0

        return temp

    @property
    def lambda_ratio_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LambdaRatioOuter

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
    def minimum_lambda_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumLambdaRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_lubricating_film_thickness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumLubricatingFilmThickness

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
    def skf_bearing_rating_life_damage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SKFBearingRatingLifeDamage

        if temp is None:
            return 0.0

        return temp

    @property
    def skf_bearing_rating_life_reliability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SKFBearingRatingLifeReliability

        if temp is None:
            return 0.0

        return temp

    @property
    def skf_bearing_rating_life_time(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SKFBearingRatingLifeTime

        if temp is None:
            return 0.0

        return temp

    @property
    def skf_bearing_rating_life_unreliability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SKFBearingRatingLifeUnreliability

        if temp is None:
            return 0.0

        return temp

    @property
    def static_equivalent_load_capacity_ratio_limit(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StaticEquivalentLoadCapacityRatioLimit

        if temp is None:
            return 0.0

        return temp

    @property
    def worst_ansiabma_static_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorstANSIABMAStaticSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def worst_iso762006_safety_factor_static_equivalent_load_capacity_ratio(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorstISO762006SafetyFactorStaticEquivalentLoadCapacityRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def ansiabma_dynamic_equivalent_load_summary(
        self: Self,
    ) -> "_1858.DutyCyclePropertySummaryForce[_1895.BearingLoadCaseResultsLightweight]":
        """mastapy.utility.property.DutyCyclePropertySummaryForce[mastapy.bearings.BearingLoadCaseResultsLightweight]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ANSIABMADynamicEquivalentLoadSummary

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[
            _1895.BearingLoadCaseResultsLightweight
        ](temp)

    @property
    def analysis_settings(self: Self) -> "_50.AnalysisSettingsItem":
        """mastapy.nodal_analysis.AnalysisSettingsItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AnalysisSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def iso2812007_dynamic_equivalent_load_summary(
        self: Self,
    ) -> "_1858.DutyCyclePropertySummaryForce[_1895.BearingLoadCaseResultsLightweight]":
        """mastapy.utility.property.DutyCyclePropertySummaryForce[mastapy.bearings.BearingLoadCaseResultsLightweight]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO2812007DynamicEquivalentLoadSummary

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[
            _1895.BearingLoadCaseResultsLightweight
        ](temp)

    @property
    def isots162812008_dynamic_equivalent_load_summary(
        self: Self,
    ) -> "_1858.DutyCyclePropertySummaryForce[_1895.BearingLoadCaseResultsLightweight]":
        """mastapy.utility.property.DutyCyclePropertySummaryForce[mastapy.bearings.BearingLoadCaseResultsLightweight]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISOTS162812008DynamicEquivalentLoadSummary

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[
            _1895.BearingLoadCaseResultsLightweight
        ](temp)

    @property
    def maximum_element_normal_stress_inner_summary(
        self: Self,
    ) -> (
        "_1861.DutyCyclePropertySummaryStress[_1895.BearingLoadCaseResultsLightweight]"
    ):
        """mastapy.utility.property.DutyCyclePropertySummaryStress[mastapy.bearings.BearingLoadCaseResultsLightweight]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumElementNormalStressInnerSummary

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[
            _1895.BearingLoadCaseResultsLightweight
        ](temp)

    @property
    def maximum_element_normal_stress_outer_summary(
        self: Self,
    ) -> (
        "_1861.DutyCyclePropertySummaryStress[_1895.BearingLoadCaseResultsLightweight]"
    ):
        """mastapy.utility.property.DutyCyclePropertySummaryStress[mastapy.bearings.BearingLoadCaseResultsLightweight]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumElementNormalStressOuterSummary

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[
            _1895.BearingLoadCaseResultsLightweight
        ](temp)

    @property
    def maximum_element_normal_stress_summary(
        self: Self,
    ) -> (
        "_1861.DutyCyclePropertySummaryStress[_1895.BearingLoadCaseResultsLightweight]"
    ):
        """mastapy.utility.property.DutyCyclePropertySummaryStress[mastapy.bearings.BearingLoadCaseResultsLightweight]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumElementNormalStressSummary

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[
            _1895.BearingLoadCaseResultsLightweight
        ](temp)

    @property
    def maximum_static_contact_stress_duty_cycle(
        self: Self,
    ) -> "_2081.MaximumStaticContactStressDutyCycle":
        """mastapy.bearings.bearing_results.rolling.MaximumStaticContactStressDutyCycle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumStaticContactStressDutyCycle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def maximum_truncation_summary(
        self: Self,
    ) -> "_1859.DutyCyclePropertySummaryPercentage[_1895.BearingLoadCaseResultsLightweight]":
        """mastapy.utility.property.DutyCyclePropertySummaryPercentage[mastapy.bearings.BearingLoadCaseResultsLightweight]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumTruncationSummary

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[
            _1895.BearingLoadCaseResultsLightweight
        ](temp)

    @property
    def misalignment_summary(
        self: Self,
    ) -> "_1860.DutyCyclePropertySummarySmallAngle[_1895.BearingLoadCaseResultsLightweight]":
        """mastapy.utility.property.DutyCyclePropertySummarySmallAngle[mastapy.bearings.BearingLoadCaseResultsLightweight]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MisalignmentSummary

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[
            _1895.BearingLoadCaseResultsLightweight
        ](temp)

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedRollingBearingDutyCycle._Cast_LoadedRollingBearingDutyCycle":
        return self._Cast_LoadedRollingBearingDutyCycle(self)
