"""BoltedJointCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5998
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "BoltedJointCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2463
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5719
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5900,
        _5979,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("BoltedJointCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="BoltedJointCompoundHarmonicAnalysis")


class BoltedJointCompoundHarmonicAnalysis(
    _5998.SpecialisedAssemblyCompoundHarmonicAnalysis
):
    """BoltedJointCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _BOLTED_JOINT_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BoltedJointCompoundHarmonicAnalysis")

    class _Cast_BoltedJointCompoundHarmonicAnalysis:
        """Special nested class for casting BoltedJointCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "BoltedJointCompoundHarmonicAnalysis._Cast_BoltedJointCompoundHarmonicAnalysis",
            parent: "BoltedJointCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_harmonic_analysis(
            self: "BoltedJointCompoundHarmonicAnalysis._Cast_BoltedJointCompoundHarmonicAnalysis",
        ) -> "_5998.SpecialisedAssemblyCompoundHarmonicAnalysis":
            return self._parent._cast(_5998.SpecialisedAssemblyCompoundHarmonicAnalysis)

        @property
        def abstract_assembly_compound_harmonic_analysis(
            self: "BoltedJointCompoundHarmonicAnalysis._Cast_BoltedJointCompoundHarmonicAnalysis",
        ) -> "_5900.AbstractAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5900,
            )

            return self._parent._cast(_5900.AbstractAssemblyCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "BoltedJointCompoundHarmonicAnalysis._Cast_BoltedJointCompoundHarmonicAnalysis",
        ) -> "_5979.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5979,
            )

            return self._parent._cast(_5979.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "BoltedJointCompoundHarmonicAnalysis._Cast_BoltedJointCompoundHarmonicAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BoltedJointCompoundHarmonicAnalysis._Cast_BoltedJointCompoundHarmonicAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltedJointCompoundHarmonicAnalysis._Cast_BoltedJointCompoundHarmonicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bolted_joint_compound_harmonic_analysis(
            self: "BoltedJointCompoundHarmonicAnalysis._Cast_BoltedJointCompoundHarmonicAnalysis",
        ) -> "BoltedJointCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "BoltedJointCompoundHarmonicAnalysis._Cast_BoltedJointCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "BoltedJointCompoundHarmonicAnalysis.TYPE"
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
    ) -> "List[_5719.BoltedJointHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.BoltedJointHarmonicAnalysis]

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
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5719.BoltedJointHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.BoltedJointHarmonicAnalysis]

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
    ) -> (
        "BoltedJointCompoundHarmonicAnalysis._Cast_BoltedJointCompoundHarmonicAnalysis"
    ):
        return self._Cast_BoltedJointCompoundHarmonicAnalysis(self)
