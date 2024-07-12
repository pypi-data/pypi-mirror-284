"""HypoidGearSetStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3789
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "HypoidGearSetStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2555
    from mastapy.system_model.analyses_and_results.static_loads import _6929
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3850,
        _3848,
        _3817,
        _3845,
        _3884,
        _3784,
        _3865,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearSetStabilityAnalysis",)


Self = TypeVar("Self", bound="HypoidGearSetStabilityAnalysis")


class HypoidGearSetStabilityAnalysis(_3789.AGMAGleasonConicalGearSetStabilityAnalysis):
    """HypoidGearSetStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearSetStabilityAnalysis")

    class _Cast_HypoidGearSetStabilityAnalysis:
        """Special nested class for casting HypoidGearSetStabilityAnalysis to subclasses."""

        def __init__(
            self: "HypoidGearSetStabilityAnalysis._Cast_HypoidGearSetStabilityAnalysis",
            parent: "HypoidGearSetStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_stability_analysis(
            self: "HypoidGearSetStabilityAnalysis._Cast_HypoidGearSetStabilityAnalysis",
        ) -> "_3789.AGMAGleasonConicalGearSetStabilityAnalysis":
            return self._parent._cast(_3789.AGMAGleasonConicalGearSetStabilityAnalysis)

        @property
        def conical_gear_set_stability_analysis(
            self: "HypoidGearSetStabilityAnalysis._Cast_HypoidGearSetStabilityAnalysis",
        ) -> "_3817.ConicalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3817,
            )

            return self._parent._cast(_3817.ConicalGearSetStabilityAnalysis)

        @property
        def gear_set_stability_analysis(
            self: "HypoidGearSetStabilityAnalysis._Cast_HypoidGearSetStabilityAnalysis",
        ) -> "_3845.GearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3845,
            )

            return self._parent._cast(_3845.GearSetStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "HypoidGearSetStabilityAnalysis._Cast_HypoidGearSetStabilityAnalysis",
        ) -> "_3884.SpecialisedAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3884,
            )

            return self._parent._cast(_3884.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "HypoidGearSetStabilityAnalysis._Cast_HypoidGearSetStabilityAnalysis",
        ) -> "_3784.AbstractAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3784,
            )

            return self._parent._cast(_3784.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "HypoidGearSetStabilityAnalysis._Cast_HypoidGearSetStabilityAnalysis",
        ) -> "_3865.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3865,
            )

            return self._parent._cast(_3865.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "HypoidGearSetStabilityAnalysis._Cast_HypoidGearSetStabilityAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "HypoidGearSetStabilityAnalysis._Cast_HypoidGearSetStabilityAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "HypoidGearSetStabilityAnalysis._Cast_HypoidGearSetStabilityAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearSetStabilityAnalysis._Cast_HypoidGearSetStabilityAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearSetStabilityAnalysis._Cast_HypoidGearSetStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def hypoid_gear_set_stability_analysis(
            self: "HypoidGearSetStabilityAnalysis._Cast_HypoidGearSetStabilityAnalysis",
        ) -> "HypoidGearSetStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "HypoidGearSetStabilityAnalysis._Cast_HypoidGearSetStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearSetStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2555.HypoidGearSet":
        """mastapy.system_model.part_model.gears.HypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6929.HypoidGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def hypoid_gears_stability_analysis(
        self: Self,
    ) -> "List[_3850.HypoidGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.HypoidGearStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearsStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_meshes_stability_analysis(
        self: Self,
    ) -> "List[_3848.HypoidGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.HypoidGearMeshStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidMeshesStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "HypoidGearSetStabilityAnalysis._Cast_HypoidGearSetStabilityAnalysis":
        return self._Cast_HypoidGearSetStabilityAnalysis(self)
