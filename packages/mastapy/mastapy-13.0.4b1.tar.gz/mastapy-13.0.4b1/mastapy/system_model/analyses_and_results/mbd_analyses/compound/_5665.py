"""SynchroniserPartCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5589
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "SynchroniserPartCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5527
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5664,
        _5666,
        _5627,
        _5575,
        _5629,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="SynchroniserPartCompoundMultibodyDynamicsAnalysis")


class SynchroniserPartCompoundMultibodyDynamicsAnalysis(
    _5589.CouplingHalfCompoundMultibodyDynamicsAnalysis
):
    """SynchroniserPartCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserPartCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_SynchroniserPartCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting SynchroniserPartCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserPartCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserPartCompoundMultibodyDynamicsAnalysis",
            parent: "SynchroniserPartCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_multibody_dynamics_analysis(
            self: "SynchroniserPartCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserPartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5589.CouplingHalfCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5589.CouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "SynchroniserPartCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserPartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5627.MountableComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5627,
            )

            return self._parent._cast(
                _5627.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "SynchroniserPartCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserPartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5575.ComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5575,
            )

            return self._parent._cast(_5575.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "SynchroniserPartCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserPartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5629.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5629,
            )

            return self._parent._cast(_5629.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "SynchroniserPartCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserPartCompoundMultibodyDynamicsAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserPartCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserPartCompoundMultibodyDynamicsAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserPartCompoundMultibodyDynamicsAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def synchroniser_half_compound_multibody_dynamics_analysis(
            self: "SynchroniserPartCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserPartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5664.SynchroniserHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5664,
            )

            return self._parent._cast(
                _5664.SynchroniserHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_sleeve_compound_multibody_dynamics_analysis(
            self: "SynchroniserPartCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserPartCompoundMultibodyDynamicsAnalysis",
        ) -> "_5666.SynchroniserSleeveCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5666,
            )

            return self._parent._cast(
                _5666.SynchroniserSleeveCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_part_compound_multibody_dynamics_analysis(
            self: "SynchroniserPartCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserPartCompoundMultibodyDynamicsAnalysis",
        ) -> "SynchroniserPartCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserPartCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "SynchroniserPartCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5527.SynchroniserPartMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.SynchroniserPartMultibodyDynamicsAnalysis]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5527.SynchroniserPartMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.SynchroniserPartMultibodyDynamicsAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "SynchroniserPartCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserPartCompoundMultibodyDynamicsAnalysis":
        return self._Cast_SynchroniserPartCompoundMultibodyDynamicsAnalysis(self)
