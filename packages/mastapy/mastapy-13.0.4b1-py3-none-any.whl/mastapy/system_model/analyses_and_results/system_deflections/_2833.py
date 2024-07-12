"""SpringDamperSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2752
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "SpringDamperSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2621
    from mastapy.system_model.analyses_and_results.static_loads import _6980
    from mastapy.system_model.analyses_and_results.power_flows import _4162
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2827,
        _2706,
        _2806,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7568,
        _7569,
        _7566,
    )
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperSystemDeflection",)


Self = TypeVar("Self", bound="SpringDamperSystemDeflection")


class SpringDamperSystemDeflection(_2752.CouplingSystemDeflection):
    """SpringDamperSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpringDamperSystemDeflection")

    class _Cast_SpringDamperSystemDeflection:
        """Special nested class for casting SpringDamperSystemDeflection to subclasses."""

        def __init__(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
            parent: "SpringDamperSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_system_deflection(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ) -> "_2752.CouplingSystemDeflection":
            return self._parent._cast(_2752.CouplingSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ) -> "_2827.SpecialisedAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2827,
            )

            return self._parent._cast(_2827.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ) -> "_2706.AbstractAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2706,
            )

            return self._parent._cast(_2706.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ) -> "_2806.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2806,
            )

            return self._parent._cast(_2806.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ) -> "_7568.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7568

            return self._parent._cast(_7568.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def spring_damper_system_deflection(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ) -> "SpringDamperSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpringDamperSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2621.SpringDamper":
        """mastapy.system_model.part_model.couplings.SpringDamper

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6980.SpringDamperLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4162.SpringDamperPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.SpringDamperPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection":
        return self._Cast_SpringDamperSystemDeflection(self)
