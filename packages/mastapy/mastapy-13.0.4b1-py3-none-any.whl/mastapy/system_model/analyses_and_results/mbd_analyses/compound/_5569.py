"""BoltCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5575
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLT_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "BoltCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2462
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5419
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5629
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("BoltCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="BoltCompoundMultibodyDynamicsAnalysis")


class BoltCompoundMultibodyDynamicsAnalysis(
    _5575.ComponentCompoundMultibodyDynamicsAnalysis
):
    """BoltCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _BOLT_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BoltCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_BoltCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting BoltCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "BoltCompoundMultibodyDynamicsAnalysis._Cast_BoltCompoundMultibodyDynamicsAnalysis",
            parent: "BoltCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "BoltCompoundMultibodyDynamicsAnalysis._Cast_BoltCompoundMultibodyDynamicsAnalysis",
        ) -> "_5575.ComponentCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(_5575.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "BoltCompoundMultibodyDynamicsAnalysis._Cast_BoltCompoundMultibodyDynamicsAnalysis",
        ) -> "_5629.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5629,
            )

            return self._parent._cast(_5629.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "BoltCompoundMultibodyDynamicsAnalysis._Cast_BoltCompoundMultibodyDynamicsAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BoltCompoundMultibodyDynamicsAnalysis._Cast_BoltCompoundMultibodyDynamicsAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltCompoundMultibodyDynamicsAnalysis._Cast_BoltCompoundMultibodyDynamicsAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bolt_compound_multibody_dynamics_analysis(
            self: "BoltCompoundMultibodyDynamicsAnalysis._Cast_BoltCompoundMultibodyDynamicsAnalysis",
        ) -> "BoltCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "BoltCompoundMultibodyDynamicsAnalysis._Cast_BoltCompoundMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "BoltCompoundMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2462.Bolt":
        """mastapy.system_model.part_model.Bolt

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5419.BoltMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.BoltMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5419.BoltMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.BoltMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BoltCompoundMultibodyDynamicsAnalysis._Cast_BoltCompoundMultibodyDynamicsAnalysis":
        return self._Cast_BoltCompoundMultibodyDynamicsAnalysis(self)
