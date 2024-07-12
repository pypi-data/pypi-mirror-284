"""ZerolBevelGearSetStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3801
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "ZerolBevelGearSetStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2574
    from mastapy.system_model.analyses_and_results.static_loads import _7009
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3917,
        _3915,
        _3789,
        _3817,
        _3845,
        _3884,
        _3784,
        _3865,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearSetStabilityAnalysis",)


Self = TypeVar("Self", bound="ZerolBevelGearSetStabilityAnalysis")


class ZerolBevelGearSetStabilityAnalysis(_3801.BevelGearSetStabilityAnalysis):
    """ZerolBevelGearSetStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ZerolBevelGearSetStabilityAnalysis")

    class _Cast_ZerolBevelGearSetStabilityAnalysis:
        """Special nested class for casting ZerolBevelGearSetStabilityAnalysis to subclasses."""

        def __init__(
            self: "ZerolBevelGearSetStabilityAnalysis._Cast_ZerolBevelGearSetStabilityAnalysis",
            parent: "ZerolBevelGearSetStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_stability_analysis(
            self: "ZerolBevelGearSetStabilityAnalysis._Cast_ZerolBevelGearSetStabilityAnalysis",
        ) -> "_3801.BevelGearSetStabilityAnalysis":
            return self._parent._cast(_3801.BevelGearSetStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_set_stability_analysis(
            self: "ZerolBevelGearSetStabilityAnalysis._Cast_ZerolBevelGearSetStabilityAnalysis",
        ) -> "_3789.AGMAGleasonConicalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3789,
            )

            return self._parent._cast(_3789.AGMAGleasonConicalGearSetStabilityAnalysis)

        @property
        def conical_gear_set_stability_analysis(
            self: "ZerolBevelGearSetStabilityAnalysis._Cast_ZerolBevelGearSetStabilityAnalysis",
        ) -> "_3817.ConicalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3817,
            )

            return self._parent._cast(_3817.ConicalGearSetStabilityAnalysis)

        @property
        def gear_set_stability_analysis(
            self: "ZerolBevelGearSetStabilityAnalysis._Cast_ZerolBevelGearSetStabilityAnalysis",
        ) -> "_3845.GearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3845,
            )

            return self._parent._cast(_3845.GearSetStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "ZerolBevelGearSetStabilityAnalysis._Cast_ZerolBevelGearSetStabilityAnalysis",
        ) -> "_3884.SpecialisedAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3884,
            )

            return self._parent._cast(_3884.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "ZerolBevelGearSetStabilityAnalysis._Cast_ZerolBevelGearSetStabilityAnalysis",
        ) -> "_3784.AbstractAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3784,
            )

            return self._parent._cast(_3784.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "ZerolBevelGearSetStabilityAnalysis._Cast_ZerolBevelGearSetStabilityAnalysis",
        ) -> "_3865.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3865,
            )

            return self._parent._cast(_3865.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ZerolBevelGearSetStabilityAnalysis._Cast_ZerolBevelGearSetStabilityAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ZerolBevelGearSetStabilityAnalysis._Cast_ZerolBevelGearSetStabilityAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ZerolBevelGearSetStabilityAnalysis._Cast_ZerolBevelGearSetStabilityAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ZerolBevelGearSetStabilityAnalysis._Cast_ZerolBevelGearSetStabilityAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearSetStabilityAnalysis._Cast_ZerolBevelGearSetStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_set_stability_analysis(
            self: "ZerolBevelGearSetStabilityAnalysis._Cast_ZerolBevelGearSetStabilityAnalysis",
        ) -> "ZerolBevelGearSetStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearSetStabilityAnalysis._Cast_ZerolBevelGearSetStabilityAnalysis",
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
        self: Self, instance_to_wrap: "ZerolBevelGearSetStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2574.ZerolBevelGearSet":
        """mastapy.system_model.part_model.gears.ZerolBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_7009.ZerolBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def zerol_bevel_gears_stability_analysis(
        self: Self,
    ) -> "List[_3917.ZerolBevelGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ZerolBevelGearStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearsStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_meshes_stability_analysis(
        self: Self,
    ) -> "List[_3915.ZerolBevelGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ZerolBevelGearMeshStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelMeshesStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ZerolBevelGearSetStabilityAnalysis._Cast_ZerolBevelGearSetStabilityAnalysis":
        return self._Cast_ZerolBevelGearSetStabilityAnalysis(self)
