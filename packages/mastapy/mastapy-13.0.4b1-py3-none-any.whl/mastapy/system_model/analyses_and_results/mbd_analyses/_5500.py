"""RollingRingAssemblyMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5510
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "RollingRingAssemblyMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2618
    from mastapy.system_model.analyses_and_results.static_loads import _6967
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5397, _5488
    from mastapy.system_model.analyses_and_results.analysis_cases import _7570, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingAssemblyMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="RollingRingAssemblyMultibodyDynamicsAnalysis")


class RollingRingAssemblyMultibodyDynamicsAnalysis(
    _5510.SpecialisedAssemblyMultibodyDynamicsAnalysis
):
    """RollingRingAssemblyMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_ASSEMBLY_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RollingRingAssemblyMultibodyDynamicsAnalysis"
    )

    class _Cast_RollingRingAssemblyMultibodyDynamicsAnalysis:
        """Special nested class for casting RollingRingAssemblyMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "RollingRingAssemblyMultibodyDynamicsAnalysis._Cast_RollingRingAssemblyMultibodyDynamicsAnalysis",
            parent: "RollingRingAssemblyMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "RollingRingAssemblyMultibodyDynamicsAnalysis._Cast_RollingRingAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5510.SpecialisedAssemblyMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5510.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "RollingRingAssemblyMultibodyDynamicsAnalysis._Cast_RollingRingAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5397.AbstractAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5397

            return self._parent._cast(_5397.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "RollingRingAssemblyMultibodyDynamicsAnalysis._Cast_RollingRingAssemblyMultibodyDynamicsAnalysis",
        ) -> "_5488.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5488

            return self._parent._cast(_5488.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "RollingRingAssemblyMultibodyDynamicsAnalysis._Cast_RollingRingAssemblyMultibodyDynamicsAnalysis",
        ) -> "_7570.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7570

            return self._parent._cast(_7570.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RollingRingAssemblyMultibodyDynamicsAnalysis._Cast_RollingRingAssemblyMultibodyDynamicsAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RollingRingAssemblyMultibodyDynamicsAnalysis._Cast_RollingRingAssemblyMultibodyDynamicsAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingAssemblyMultibodyDynamicsAnalysis._Cast_RollingRingAssemblyMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingAssemblyMultibodyDynamicsAnalysis._Cast_RollingRingAssemblyMultibodyDynamicsAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def rolling_ring_assembly_multibody_dynamics_analysis(
            self: "RollingRingAssemblyMultibodyDynamicsAnalysis._Cast_RollingRingAssemblyMultibodyDynamicsAnalysis",
        ) -> "RollingRingAssemblyMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "RollingRingAssemblyMultibodyDynamicsAnalysis._Cast_RollingRingAssemblyMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "RollingRingAssemblyMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2618.RollingRingAssembly":
        """mastapy.system_model.part_model.couplings.RollingRingAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6967.RollingRingAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase

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
    ) -> "RollingRingAssemblyMultibodyDynamicsAnalysis._Cast_RollingRingAssemblyMultibodyDynamicsAnalysis":
        return self._Cast_RollingRingAssemblyMultibodyDynamicsAnalysis(self)
