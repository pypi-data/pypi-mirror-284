"""BoltedJointCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6527
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "BoltedJointCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2463
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6318
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6429,
        _6508,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("BoltedJointCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="BoltedJointCompoundDynamicAnalysis")


class BoltedJointCompoundDynamicAnalysis(
    _6527.SpecialisedAssemblyCompoundDynamicAnalysis
):
    """BoltedJointCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _BOLTED_JOINT_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BoltedJointCompoundDynamicAnalysis")

    class _Cast_BoltedJointCompoundDynamicAnalysis:
        """Special nested class for casting BoltedJointCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "BoltedJointCompoundDynamicAnalysis._Cast_BoltedJointCompoundDynamicAnalysis",
            parent: "BoltedJointCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_dynamic_analysis(
            self: "BoltedJointCompoundDynamicAnalysis._Cast_BoltedJointCompoundDynamicAnalysis",
        ) -> "_6527.SpecialisedAssemblyCompoundDynamicAnalysis":
            return self._parent._cast(_6527.SpecialisedAssemblyCompoundDynamicAnalysis)

        @property
        def abstract_assembly_compound_dynamic_analysis(
            self: "BoltedJointCompoundDynamicAnalysis._Cast_BoltedJointCompoundDynamicAnalysis",
        ) -> "_6429.AbstractAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6429,
            )

            return self._parent._cast(_6429.AbstractAssemblyCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "BoltedJointCompoundDynamicAnalysis._Cast_BoltedJointCompoundDynamicAnalysis",
        ) -> "_6508.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6508,
            )

            return self._parent._cast(_6508.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "BoltedJointCompoundDynamicAnalysis._Cast_BoltedJointCompoundDynamicAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BoltedJointCompoundDynamicAnalysis._Cast_BoltedJointCompoundDynamicAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltedJointCompoundDynamicAnalysis._Cast_BoltedJointCompoundDynamicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bolted_joint_compound_dynamic_analysis(
            self: "BoltedJointCompoundDynamicAnalysis._Cast_BoltedJointCompoundDynamicAnalysis",
        ) -> "BoltedJointCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "BoltedJointCompoundDynamicAnalysis._Cast_BoltedJointCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "BoltedJointCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2463.BoltedJoint":
        """mastapy.system_model.part_model.BoltedJoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_6318.BoltedJointDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.BoltedJointDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(self: Self) -> "List[_6318.BoltedJointDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.BoltedJointDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BoltedJointCompoundDynamicAnalysis._Cast_BoltedJointCompoundDynamicAnalysis":
        return self._Cast_BoltedJointCompoundDynamicAnalysis(self)
