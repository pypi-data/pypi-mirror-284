"""StraightBevelDiffGearSetCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6582
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "StraightBevelDiffGearSetCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2566
    from mastapy.system_model.analyses_and_results.static_loads import _6983
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6672,
        _6673,
        _6570,
        _6598,
        _6627,
        _6665,
        _6564,
        _6646,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSetCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="StraightBevelDiffGearSetCriticalSpeedAnalysis")


class StraightBevelDiffGearSetCriticalSpeedAnalysis(
    _6582.BevelGearSetCriticalSpeedAnalysis
):
    """StraightBevelDiffGearSetCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearSetCriticalSpeedAnalysis"
    )

    class _Cast_StraightBevelDiffGearSetCriticalSpeedAnalysis:
        """Special nested class for casting StraightBevelDiffGearSetCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearSetCriticalSpeedAnalysis._Cast_StraightBevelDiffGearSetCriticalSpeedAnalysis",
            parent: "StraightBevelDiffGearSetCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_critical_speed_analysis(
            self: "StraightBevelDiffGearSetCriticalSpeedAnalysis._Cast_StraightBevelDiffGearSetCriticalSpeedAnalysis",
        ) -> "_6582.BevelGearSetCriticalSpeedAnalysis":
            return self._parent._cast(_6582.BevelGearSetCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_set_critical_speed_analysis(
            self: "StraightBevelDiffGearSetCriticalSpeedAnalysis._Cast_StraightBevelDiffGearSetCriticalSpeedAnalysis",
        ) -> "_6570.AGMAGleasonConicalGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6570,
            )

            return self._parent._cast(
                _6570.AGMAGleasonConicalGearSetCriticalSpeedAnalysis
            )

        @property
        def conical_gear_set_critical_speed_analysis(
            self: "StraightBevelDiffGearSetCriticalSpeedAnalysis._Cast_StraightBevelDiffGearSetCriticalSpeedAnalysis",
        ) -> "_6598.ConicalGearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6598,
            )

            return self._parent._cast(_6598.ConicalGearSetCriticalSpeedAnalysis)

        @property
        def gear_set_critical_speed_analysis(
            self: "StraightBevelDiffGearSetCriticalSpeedAnalysis._Cast_StraightBevelDiffGearSetCriticalSpeedAnalysis",
        ) -> "_6627.GearSetCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6627,
            )

            return self._parent._cast(_6627.GearSetCriticalSpeedAnalysis)

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "StraightBevelDiffGearSetCriticalSpeedAnalysis._Cast_StraightBevelDiffGearSetCriticalSpeedAnalysis",
        ) -> "_6665.SpecialisedAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6665,
            )

            return self._parent._cast(_6665.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "StraightBevelDiffGearSetCriticalSpeedAnalysis._Cast_StraightBevelDiffGearSetCriticalSpeedAnalysis",
        ) -> "_6564.AbstractAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6564,
            )

            return self._parent._cast(_6564.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "StraightBevelDiffGearSetCriticalSpeedAnalysis._Cast_StraightBevelDiffGearSetCriticalSpeedAnalysis",
        ) -> "_6646.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6646,
            )

            return self._parent._cast(_6646.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelDiffGearSetCriticalSpeedAnalysis._Cast_StraightBevelDiffGearSetCriticalSpeedAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelDiffGearSetCriticalSpeedAnalysis._Cast_StraightBevelDiffGearSetCriticalSpeedAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelDiffGearSetCriticalSpeedAnalysis._Cast_StraightBevelDiffGearSetCriticalSpeedAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearSetCriticalSpeedAnalysis._Cast_StraightBevelDiffGearSetCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearSetCriticalSpeedAnalysis._Cast_StraightBevelDiffGearSetCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_set_critical_speed_analysis(
            self: "StraightBevelDiffGearSetCriticalSpeedAnalysis._Cast_StraightBevelDiffGearSetCriticalSpeedAnalysis",
        ) -> "StraightBevelDiffGearSetCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearSetCriticalSpeedAnalysis._Cast_StraightBevelDiffGearSetCriticalSpeedAnalysis",
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
        instance_to_wrap: "StraightBevelDiffGearSetCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2566.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6983.StraightBevelDiffGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def straight_bevel_diff_gears_critical_speed_analysis(
        self: Self,
    ) -> "List[_6672.StraightBevelDiffGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.StraightBevelDiffGearCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearsCriticalSpeedAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_meshes_critical_speed_analysis(
        self: Self,
    ) -> "List[_6673.StraightBevelDiffGearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.StraightBevelDiffGearMeshCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffMeshesCriticalSpeedAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearSetCriticalSpeedAnalysis._Cast_StraightBevelDiffGearSetCriticalSpeedAnalysis":
        return self._Cast_StraightBevelDiffGearSetCriticalSpeedAnalysis(self)
