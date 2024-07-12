"""SynchroniserPartCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6468
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "SynchroniserPartCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6415
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6543,
        _6545,
        _6506,
        _6454,
        _6508,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="SynchroniserPartCompoundDynamicAnalysis")


class SynchroniserPartCompoundDynamicAnalysis(
    _6468.CouplingHalfCompoundDynamicAnalysis
):
    """SynchroniserPartCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserPartCompoundDynamicAnalysis"
    )

    class _Cast_SynchroniserPartCompoundDynamicAnalysis:
        """Special nested class for casting SynchroniserPartCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserPartCompoundDynamicAnalysis._Cast_SynchroniserPartCompoundDynamicAnalysis",
            parent: "SynchroniserPartCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_dynamic_analysis(
            self: "SynchroniserPartCompoundDynamicAnalysis._Cast_SynchroniserPartCompoundDynamicAnalysis",
        ) -> "_6468.CouplingHalfCompoundDynamicAnalysis":
            return self._parent._cast(_6468.CouplingHalfCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "SynchroniserPartCompoundDynamicAnalysis._Cast_SynchroniserPartCompoundDynamicAnalysis",
        ) -> "_6506.MountableComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6506,
            )

            return self._parent._cast(_6506.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "SynchroniserPartCompoundDynamicAnalysis._Cast_SynchroniserPartCompoundDynamicAnalysis",
        ) -> "_6454.ComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6454,
            )

            return self._parent._cast(_6454.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "SynchroniserPartCompoundDynamicAnalysis._Cast_SynchroniserPartCompoundDynamicAnalysis",
        ) -> "_6508.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6508,
            )

            return self._parent._cast(_6508.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "SynchroniserPartCompoundDynamicAnalysis._Cast_SynchroniserPartCompoundDynamicAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserPartCompoundDynamicAnalysis._Cast_SynchroniserPartCompoundDynamicAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartCompoundDynamicAnalysis._Cast_SynchroniserPartCompoundDynamicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def synchroniser_half_compound_dynamic_analysis(
            self: "SynchroniserPartCompoundDynamicAnalysis._Cast_SynchroniserPartCompoundDynamicAnalysis",
        ) -> "_6543.SynchroniserHalfCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6543,
            )

            return self._parent._cast(_6543.SynchroniserHalfCompoundDynamicAnalysis)

        @property
        def synchroniser_sleeve_compound_dynamic_analysis(
            self: "SynchroniserPartCompoundDynamicAnalysis._Cast_SynchroniserPartCompoundDynamicAnalysis",
        ) -> "_6545.SynchroniserSleeveCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6545,
            )

            return self._parent._cast(_6545.SynchroniserSleeveCompoundDynamicAnalysis)

        @property
        def synchroniser_part_compound_dynamic_analysis(
            self: "SynchroniserPartCompoundDynamicAnalysis._Cast_SynchroniserPartCompoundDynamicAnalysis",
        ) -> "SynchroniserPartCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartCompoundDynamicAnalysis._Cast_SynchroniserPartCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "SynchroniserPartCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6415.SynchroniserPartDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.SynchroniserPartDynamicAnalysis]

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
    ) -> "List[_6415.SynchroniserPartDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.SynchroniserPartDynamicAnalysis]

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
    ) -> "SynchroniserPartCompoundDynamicAnalysis._Cast_SynchroniserPartCompoundDynamicAnalysis":
        return self._Cast_SynchroniserPartCompoundDynamicAnalysis(self)
