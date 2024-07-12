"""BoltedJointStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3884
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "BoltedJointStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2463
    from mastapy.system_model.analyses_and_results.static_loads import _6852
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3784,
        _3865,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("BoltedJointStabilityAnalysis",)


Self = TypeVar("Self", bound="BoltedJointStabilityAnalysis")


class BoltedJointStabilityAnalysis(_3884.SpecialisedAssemblyStabilityAnalysis):
    """BoltedJointStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _BOLTED_JOINT_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BoltedJointStabilityAnalysis")

    class _Cast_BoltedJointStabilityAnalysis:
        """Special nested class for casting BoltedJointStabilityAnalysis to subclasses."""

        def __init__(
            self: "BoltedJointStabilityAnalysis._Cast_BoltedJointStabilityAnalysis",
            parent: "BoltedJointStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_stability_analysis(
            self: "BoltedJointStabilityAnalysis._Cast_BoltedJointStabilityAnalysis",
        ) -> "_3884.SpecialisedAssemblyStabilityAnalysis":
            return self._parent._cast(_3884.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "BoltedJointStabilityAnalysis._Cast_BoltedJointStabilityAnalysis",
        ) -> "_3784.AbstractAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3784,
            )

            return self._parent._cast(_3784.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "BoltedJointStabilityAnalysis._Cast_BoltedJointStabilityAnalysis",
        ) -> "_3865.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3865,
            )

            return self._parent._cast(_3865.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BoltedJointStabilityAnalysis._Cast_BoltedJointStabilityAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BoltedJointStabilityAnalysis._Cast_BoltedJointStabilityAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BoltedJointStabilityAnalysis._Cast_BoltedJointStabilityAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BoltedJointStabilityAnalysis._Cast_BoltedJointStabilityAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltedJointStabilityAnalysis._Cast_BoltedJointStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bolted_joint_stability_analysis(
            self: "BoltedJointStabilityAnalysis._Cast_BoltedJointStabilityAnalysis",
        ) -> "BoltedJointStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "BoltedJointStabilityAnalysis._Cast_BoltedJointStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BoltedJointStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2463.BoltedJoint":
        """mastapy.system_model.part_model.BoltedJoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6852.BoltedJointLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BoltedJointLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BoltedJointStabilityAnalysis._Cast_BoltedJointStabilityAnalysis":
        return self._Cast_BoltedJointStabilityAnalysis(self)
