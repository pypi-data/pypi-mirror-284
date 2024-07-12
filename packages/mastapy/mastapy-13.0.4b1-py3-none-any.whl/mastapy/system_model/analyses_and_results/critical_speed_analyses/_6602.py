"""CouplingCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6665
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "CouplingCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2604
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6586,
        _6591,
        _6648,
        _6670,
        _6685,
        _6564,
        _6646,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CouplingCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="CouplingCriticalSpeedAnalysis")


class CouplingCriticalSpeedAnalysis(_6665.SpecialisedAssemblyCriticalSpeedAnalysis):
    """CouplingCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingCriticalSpeedAnalysis")

    class _Cast_CouplingCriticalSpeedAnalysis:
        """Special nested class for casting CouplingCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "CouplingCriticalSpeedAnalysis._Cast_CouplingCriticalSpeedAnalysis",
            parent: "CouplingCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "CouplingCriticalSpeedAnalysis._Cast_CouplingCriticalSpeedAnalysis",
        ) -> "_6665.SpecialisedAssemblyCriticalSpeedAnalysis":
            return self._parent._cast(_6665.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "CouplingCriticalSpeedAnalysis._Cast_CouplingCriticalSpeedAnalysis",
        ) -> "_6564.AbstractAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6564,
            )

            return self._parent._cast(_6564.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "CouplingCriticalSpeedAnalysis._Cast_CouplingCriticalSpeedAnalysis",
        ) -> "_6646.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6646,
            )

            return self._parent._cast(_6646.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CouplingCriticalSpeedAnalysis._Cast_CouplingCriticalSpeedAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingCriticalSpeedAnalysis._Cast_CouplingCriticalSpeedAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingCriticalSpeedAnalysis._Cast_CouplingCriticalSpeedAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingCriticalSpeedAnalysis._Cast_CouplingCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingCriticalSpeedAnalysis._Cast_CouplingCriticalSpeedAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_critical_speed_analysis(
            self: "CouplingCriticalSpeedAnalysis._Cast_CouplingCriticalSpeedAnalysis",
        ) -> "_6586.ClutchCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6586,
            )

            return self._parent._cast(_6586.ClutchCriticalSpeedAnalysis)

        @property
        def concept_coupling_critical_speed_analysis(
            self: "CouplingCriticalSpeedAnalysis._Cast_CouplingCriticalSpeedAnalysis",
        ) -> "_6591.ConceptCouplingCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6591,
            )

            return self._parent._cast(_6591.ConceptCouplingCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_critical_speed_analysis(
            self: "CouplingCriticalSpeedAnalysis._Cast_CouplingCriticalSpeedAnalysis",
        ) -> "_6648.PartToPartShearCouplingCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6648,
            )

            return self._parent._cast(
                _6648.PartToPartShearCouplingCriticalSpeedAnalysis
            )

        @property
        def spring_damper_critical_speed_analysis(
            self: "CouplingCriticalSpeedAnalysis._Cast_CouplingCriticalSpeedAnalysis",
        ) -> "_6670.SpringDamperCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6670,
            )

            return self._parent._cast(_6670.SpringDamperCriticalSpeedAnalysis)

        @property
        def torque_converter_critical_speed_analysis(
            self: "CouplingCriticalSpeedAnalysis._Cast_CouplingCriticalSpeedAnalysis",
        ) -> "_6685.TorqueConverterCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6685,
            )

            return self._parent._cast(_6685.TorqueConverterCriticalSpeedAnalysis)

        @property
        def coupling_critical_speed_analysis(
            self: "CouplingCriticalSpeedAnalysis._Cast_CouplingCriticalSpeedAnalysis",
        ) -> "CouplingCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingCriticalSpeedAnalysis._Cast_CouplingCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingCriticalSpeedAnalysis.TYPE"):
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
    def cast_to(
        self: Self,
    ) -> "CouplingCriticalSpeedAnalysis._Cast_CouplingCriticalSpeedAnalysis":
        return self._Cast_CouplingCriticalSpeedAnalysis(self)
