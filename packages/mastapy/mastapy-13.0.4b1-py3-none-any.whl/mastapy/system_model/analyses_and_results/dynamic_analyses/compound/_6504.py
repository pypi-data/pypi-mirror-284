"""MassDiscCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6551
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASS_DISC_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "MassDiscCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2482
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6375
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6506,
        _6454,
        _6508,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("MassDiscCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="MassDiscCompoundDynamicAnalysis")


class MassDiscCompoundDynamicAnalysis(_6551.VirtualComponentCompoundDynamicAnalysis):
    """MassDiscCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _MASS_DISC_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MassDiscCompoundDynamicAnalysis")

    class _Cast_MassDiscCompoundDynamicAnalysis:
        """Special nested class for casting MassDiscCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "MassDiscCompoundDynamicAnalysis._Cast_MassDiscCompoundDynamicAnalysis",
            parent: "MassDiscCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_dynamic_analysis(
            self: "MassDiscCompoundDynamicAnalysis._Cast_MassDiscCompoundDynamicAnalysis",
        ) -> "_6551.VirtualComponentCompoundDynamicAnalysis":
            return self._parent._cast(_6551.VirtualComponentCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "MassDiscCompoundDynamicAnalysis._Cast_MassDiscCompoundDynamicAnalysis",
        ) -> "_6506.MountableComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6506,
            )

            return self._parent._cast(_6506.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "MassDiscCompoundDynamicAnalysis._Cast_MassDiscCompoundDynamicAnalysis",
        ) -> "_6454.ComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6454,
            )

            return self._parent._cast(_6454.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "MassDiscCompoundDynamicAnalysis._Cast_MassDiscCompoundDynamicAnalysis",
        ) -> "_6508.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6508,
            )

            return self._parent._cast(_6508.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "MassDiscCompoundDynamicAnalysis._Cast_MassDiscCompoundDynamicAnalysis",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MassDiscCompoundDynamicAnalysis._Cast_MassDiscCompoundDynamicAnalysis",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MassDiscCompoundDynamicAnalysis._Cast_MassDiscCompoundDynamicAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def mass_disc_compound_dynamic_analysis(
            self: "MassDiscCompoundDynamicAnalysis._Cast_MassDiscCompoundDynamicAnalysis",
        ) -> "MassDiscCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "MassDiscCompoundDynamicAnalysis._Cast_MassDiscCompoundDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MassDiscCompoundDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2482.MassDisc":
        """mastapy.system_model.part_model.MassDisc

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
    ) -> "List[_6375.MassDiscDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.MassDiscDynamicAnalysis]

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
    def planetaries(self: Self) -> "List[MassDiscCompoundDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.MassDiscCompoundDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(self: Self) -> "List[_6375.MassDiscDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.MassDiscDynamicAnalysis]

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
    ) -> "MassDiscCompoundDynamicAnalysis._Cast_MassDiscCompoundDynamicAnalysis":
        return self._Cast_MassDiscCompoundDynamicAnalysis(self)
