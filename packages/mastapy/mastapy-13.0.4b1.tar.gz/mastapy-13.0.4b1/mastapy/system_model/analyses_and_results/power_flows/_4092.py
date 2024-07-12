"""CouplingPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4156
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "CouplingPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2604
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4076,
        _4081,
        _4138,
        _4162,
        _4177,
        _4053,
        _4135,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CouplingPowerFlow",)


Self = TypeVar("Self", bound="CouplingPowerFlow")


class CouplingPowerFlow(_4156.SpecialisedAssemblyPowerFlow):
    """CouplingPowerFlow

    This is a mastapy class.
    """

    TYPE = _COUPLING_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingPowerFlow")

    class _Cast_CouplingPowerFlow:
        """Special nested class for casting CouplingPowerFlow to subclasses."""

        def __init__(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
            parent: "CouplingPowerFlow",
        ):
            self._parent = parent

        @property
        def specialised_assembly_power_flow(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
        ) -> "_4156.SpecialisedAssemblyPowerFlow":
            return self._parent._cast(_4156.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
        ) -> "_4053.AbstractAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4053

            return self._parent._cast(_4053.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
        ) -> "_4135.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4135

            return self._parent._cast(_4135.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_power_flow(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
        ) -> "_4076.ClutchPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4076

            return self._parent._cast(_4076.ClutchPowerFlow)

        @property
        def concept_coupling_power_flow(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
        ) -> "_4081.ConceptCouplingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4081

            return self._parent._cast(_4081.ConceptCouplingPowerFlow)

        @property
        def part_to_part_shear_coupling_power_flow(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
        ) -> "_4138.PartToPartShearCouplingPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4138

            return self._parent._cast(_4138.PartToPartShearCouplingPowerFlow)

        @property
        def spring_damper_power_flow(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
        ) -> "_4162.SpringDamperPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4162

            return self._parent._cast(_4162.SpringDamperPowerFlow)

        @property
        def torque_converter_power_flow(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
        ) -> "_4177.TorqueConverterPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4177

            return self._parent._cast(_4177.TorqueConverterPowerFlow)

        @property
        def coupling_power_flow(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
        ) -> "CouplingPowerFlow":
            return self._parent

        def __getattr__(self: "CouplingPowerFlow._Cast_CouplingPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2604.Coupling":
        """mastapy.system_model.part_model.couplings.Coupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CouplingPowerFlow._Cast_CouplingPowerFlow":
        return self._Cast_CouplingPowerFlow(self)
