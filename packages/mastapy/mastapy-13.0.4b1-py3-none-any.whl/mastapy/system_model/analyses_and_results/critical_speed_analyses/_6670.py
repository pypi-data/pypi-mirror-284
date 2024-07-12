"""SpringDamperCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6602
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "SpringDamperCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2621
    from mastapy.system_model.analyses_and_results.static_loads import _6980
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6665,
        _6564,
        _6646,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="SpringDamperCriticalSpeedAnalysis")


class SpringDamperCriticalSpeedAnalysis(_6602.CouplingCriticalSpeedAnalysis):
    """SpringDamperCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpringDamperCriticalSpeedAnalysis")

    class _Cast_SpringDamperCriticalSpeedAnalysis:
        """Special nested class for casting SpringDamperCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "SpringDamperCriticalSpeedAnalysis._Cast_SpringDamperCriticalSpeedAnalysis",
            parent: "SpringDamperCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_critical_speed_analysis(
            self: "SpringDamperCriticalSpeedAnalysis._Cast_SpringDamperCriticalSpeedAnalysis",
        ) -> "_6602.CouplingCriticalSpeedAnalysis":
            return self._parent._cast(_6602.CouplingCriticalSpeedAnalysis)

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "SpringDamperCriticalSpeedAnalysis._Cast_SpringDamperCriticalSpeedAnalysis",
        ) -> "_6665.SpecialisedAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6665,
            )

            return self._parent._cast(_6665.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "SpringDamperCriticalSpeedAnalysis._Cast_SpringDamperCriticalSpeedAnalysis",
        ) -> "_6564.AbstractAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6564,
            )

            return self._parent._cast(_6564.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "SpringDamperCriticalSpeedAnalysis._Cast_SpringDamperCriticalSpeedAnalysis",
        ) -> "_6646.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6646,
            )

            return self._parent._cast(_6646.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SpringDamperCriticalSpeedAnalysis._Cast_SpringDamperCriticalSpeedAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpringDamperCriticalSpeedAnalysis._Cast_SpringDamperCriticalSpeedAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpringDamperCriticalSpeedAnalysis._Cast_SpringDamperCriticalSpeedAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperCriticalSpeedAnalysis._Cast_SpringDamperCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperCriticalSpeedAnalysis._Cast_SpringDamperCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def spring_damper_critical_speed_analysis(
            self: "SpringDamperCriticalSpeedAnalysis._Cast_SpringDamperCriticalSpeedAnalysis",
        ) -> "SpringDamperCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "SpringDamperCriticalSpeedAnalysis._Cast_SpringDamperCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "SpringDamperCriticalSpeedAnalysis.TYPE"
    ):
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
    def cast_to(
        self: Self,
    ) -> "SpringDamperCriticalSpeedAnalysis._Cast_SpringDamperCriticalSpeedAnalysis":
        return self._Cast_SpringDamperCriticalSpeedAnalysis(self)
