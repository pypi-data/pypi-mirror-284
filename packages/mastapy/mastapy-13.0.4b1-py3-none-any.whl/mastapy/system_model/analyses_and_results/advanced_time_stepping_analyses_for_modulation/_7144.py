"""StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7138,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2569
    from mastapy.system_model.analyses_and_results.system_deflections import _2840
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7048,
        _7035,
        _7064,
        _7090,
        _7110,
        _7057,
        _7112,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation"
)


class StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation(
    _7138.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation
):
    """StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
            parent: "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7138.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7138.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7048.BevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7048,
            )

            return self._parent._cast(
                _7048.BevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7035.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7035,
            )

            return self._parent._cast(
                _7035.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7064.ConicalGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7064,
            )

            return self._parent._cast(
                _7064.ConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7090.GearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7090,
            )

            return self._parent._cast(
                _7090.GearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7110.MountableComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7110,
            )

            return self._parent._cast(
                _7110.MountableComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7057.ComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7057,
            )

            return self._parent._cast(
                _7057.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7112.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7112,
            )

            return self._parent._cast(
                _7112.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
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
        self: Self,
        instance_to_wrap: "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2569.StraightBevelPlanetGear":
        """mastapy.system_model.part_model.gears.StraightBevelPlanetGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2840.StraightBevelPlanetGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.StraightBevelPlanetGearSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation":
        return (
            self._Cast_StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation(
                self
            )
        )
