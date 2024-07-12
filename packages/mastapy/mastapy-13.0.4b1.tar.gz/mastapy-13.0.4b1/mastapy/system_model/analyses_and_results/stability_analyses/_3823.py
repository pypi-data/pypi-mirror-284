"""CouplingStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3884
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "CouplingStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2604
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3807,
        _3812,
        _3868,
        _3890,
        _3908,
        _3784,
        _3865,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CouplingStabilityAnalysis",)


Self = TypeVar("Self", bound="CouplingStabilityAnalysis")


class CouplingStabilityAnalysis(_3884.SpecialisedAssemblyStabilityAnalysis):
    """CouplingStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingStabilityAnalysis")

    class _Cast_CouplingStabilityAnalysis:
        """Special nested class for casting CouplingStabilityAnalysis to subclasses."""

        def __init__(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
            parent: "CouplingStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_stability_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ) -> "_3884.SpecialisedAssemblyStabilityAnalysis":
            return self._parent._cast(_3884.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ) -> "_3784.AbstractAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3784,
            )

            return self._parent._cast(_3784.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ) -> "_3865.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3865,
            )

            return self._parent._cast(_3865.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ) -> "_7569.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_stability_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ) -> "_3807.ClutchStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3807,
            )

            return self._parent._cast(_3807.ClutchStabilityAnalysis)

        @property
        def concept_coupling_stability_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ) -> "_3812.ConceptCouplingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3812,
            )

            return self._parent._cast(_3812.ConceptCouplingStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_stability_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ) -> "_3868.PartToPartShearCouplingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3868,
            )

            return self._parent._cast(_3868.PartToPartShearCouplingStabilityAnalysis)

        @property
        def spring_damper_stability_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ) -> "_3890.SpringDamperStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3890,
            )

            return self._parent._cast(_3890.SpringDamperStabilityAnalysis)

        @property
        def torque_converter_stability_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ) -> "_3908.TorqueConverterStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3908,
            )

            return self._parent._cast(_3908.TorqueConverterStabilityAnalysis)

        @property
        def coupling_stability_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ) -> "CouplingStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingStabilityAnalysis.TYPE"):
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
    ) -> "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis":
        return self._Cast_CouplingStabilityAnalysis(self)
