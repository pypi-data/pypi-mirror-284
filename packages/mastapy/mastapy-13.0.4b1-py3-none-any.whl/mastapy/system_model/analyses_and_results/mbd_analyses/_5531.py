"""TorqueConverterMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5439
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "TorqueConverterMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2628
    from mastapy.system_model.analyses_and_results.static_loads import _6995
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5510,
        _5397,
        _5488,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7570, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="TorqueConverterMultibodyDynamicsAnalysis")


class TorqueConverterMultibodyDynamicsAnalysis(_5439.CouplingMultibodyDynamicsAnalysis):
    """TorqueConverterMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterMultibodyDynamicsAnalysis"
    )

    class _Cast_TorqueConverterMultibodyDynamicsAnalysis:
        """Special nested class for casting TorqueConverterMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "TorqueConverterMultibodyDynamicsAnalysis._Cast_TorqueConverterMultibodyDynamicsAnalysis",
            parent: "TorqueConverterMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_multibody_dynamics_analysis(
            self: "TorqueConverterMultibodyDynamicsAnalysis._Cast_TorqueConverterMultibodyDynamicsAnalysis",
        ) -> "_5439.CouplingMultibodyDynamicsAnalysis":
            return self._parent._cast(_5439.CouplingMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "TorqueConverterMultibodyDynamicsAnalysis._Cast_TorqueConverterMultibodyDynamicsAnalysis",
        ) -> "_5510.SpecialisedAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5510

            return self._parent._cast(
                _5510.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "TorqueConverterMultibodyDynamicsAnalysis._Cast_TorqueConverterMultibodyDynamicsAnalysis",
        ) -> "_5397.AbstractAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5397

            return self._parent._cast(_5397.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "TorqueConverterMultibodyDynamicsAnalysis._Cast_TorqueConverterMultibodyDynamicsAnalysis",
        ) -> "_5488.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5488

            return self._parent._cast(_5488.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "TorqueConverterMultibodyDynamicsAnalysis._Cast_TorqueConverterMultibodyDynamicsAnalysis",
        ) -> "_7570.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7570

            return self._parent._cast(_7570.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterMultibodyDynamicsAnalysis._Cast_TorqueConverterMultibodyDynamicsAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterMultibodyDynamicsAnalysis._Cast_TorqueConverterMultibodyDynamicsAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterMultibodyDynamicsAnalysis._Cast_TorqueConverterMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterMultibodyDynamicsAnalysis._Cast_TorqueConverterMultibodyDynamicsAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def torque_converter_multibody_dynamics_analysis(
            self: "TorqueConverterMultibodyDynamicsAnalysis._Cast_TorqueConverterMultibodyDynamicsAnalysis",
        ) -> "TorqueConverterMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "TorqueConverterMultibodyDynamicsAnalysis._Cast_TorqueConverterMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "TorqueConverterMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2628.TorqueConverter":
        """mastapy.system_model.part_model.couplings.TorqueConverter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6995.TorqueConverterLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterLoadCase

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
    ) -> "TorqueConverterMultibodyDynamicsAnalysis._Cast_TorqueConverterMultibodyDynamicsAnalysis":
        return self._Cast_TorqueConverterMultibodyDynamicsAnalysis(self)
