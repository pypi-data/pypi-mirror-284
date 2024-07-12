"""RootAssemblyCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4195
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "RootAssemblyCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.load_case_groups import _5681
    from mastapy.system_model.analyses_and_results.power_flows import _4152
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4188,
        _4267,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblyCompoundPowerFlow",)


Self = TypeVar("Self", bound="RootAssemblyCompoundPowerFlow")


class RootAssemblyCompoundPowerFlow(_4195.AssemblyCompoundPowerFlow):
    """RootAssemblyCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RootAssemblyCompoundPowerFlow")

    class _Cast_RootAssemblyCompoundPowerFlow:
        """Special nested class for casting RootAssemblyCompoundPowerFlow to subclasses."""

        def __init__(
            self: "RootAssemblyCompoundPowerFlow._Cast_RootAssemblyCompoundPowerFlow",
            parent: "RootAssemblyCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def assembly_compound_power_flow(
            self: "RootAssemblyCompoundPowerFlow._Cast_RootAssemblyCompoundPowerFlow",
        ) -> "_4195.AssemblyCompoundPowerFlow":
            return self._parent._cast(_4195.AssemblyCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(
            self: "RootAssemblyCompoundPowerFlow._Cast_RootAssemblyCompoundPowerFlow",
        ) -> "_4188.AbstractAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4188,
            )

            return self._parent._cast(_4188.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "RootAssemblyCompoundPowerFlow._Cast_RootAssemblyCompoundPowerFlow",
        ) -> "_4267.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4267,
            )

            return self._parent._cast(_4267.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "RootAssemblyCompoundPowerFlow._Cast_RootAssemblyCompoundPowerFlow",
        ) -> "_7567.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RootAssemblyCompoundPowerFlow._Cast_RootAssemblyCompoundPowerFlow",
        ) -> "_7564.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RootAssemblyCompoundPowerFlow._Cast_RootAssemblyCompoundPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def root_assembly_compound_power_flow(
            self: "RootAssemblyCompoundPowerFlow._Cast_RootAssemblyCompoundPowerFlow",
        ) -> "RootAssemblyCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "RootAssemblyCompoundPowerFlow._Cast_RootAssemblyCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RootAssemblyCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def compound_static_load(self: Self) -> "_5681.AbstractStaticLoadCaseGroup":
        """mastapy.system_model.analyses_and_results.load_case_groups.AbstractStaticLoadCaseGroup

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CompoundStaticLoad

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4152.RootAssemblyPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.RootAssemblyPowerFlow]

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
    def assembly_analysis_cases(self: Self) -> "List[_4152.RootAssemblyPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.RootAssemblyPowerFlow]

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

    def set_face_widths_for_specified_safety_factors(self: Self):
        """Method does not return."""
        self.wrapped.SetFaceWidthsForSpecifiedSafetyFactors()

    @property
    def cast_to(
        self: Self,
    ) -> "RootAssemblyCompoundPowerFlow._Cast_RootAssemblyCompoundPowerFlow":
        return self._Cast_RootAssemblyCompoundPowerFlow(self)
