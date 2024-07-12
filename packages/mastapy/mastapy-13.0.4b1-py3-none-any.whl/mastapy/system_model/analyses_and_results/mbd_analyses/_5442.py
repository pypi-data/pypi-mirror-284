"""CVTPulleyMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5497
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "CVTPulleyMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2608
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5438,
        _5485,
        _5425,
        _5488,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7570, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="CVTPulleyMultibodyDynamicsAnalysis")


class CVTPulleyMultibodyDynamicsAnalysis(_5497.PulleyMultibodyDynamicsAnalysis):
    """CVTPulleyMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTPulleyMultibodyDynamicsAnalysis")

    class _Cast_CVTPulleyMultibodyDynamicsAnalysis:
        """Special nested class for casting CVTPulleyMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CVTPulleyMultibodyDynamicsAnalysis._Cast_CVTPulleyMultibodyDynamicsAnalysis",
            parent: "CVTPulleyMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def pulley_multibody_dynamics_analysis(
            self: "CVTPulleyMultibodyDynamicsAnalysis._Cast_CVTPulleyMultibodyDynamicsAnalysis",
        ) -> "_5497.PulleyMultibodyDynamicsAnalysis":
            return self._parent._cast(_5497.PulleyMultibodyDynamicsAnalysis)

        @property
        def coupling_half_multibody_dynamics_analysis(
            self: "CVTPulleyMultibodyDynamicsAnalysis._Cast_CVTPulleyMultibodyDynamicsAnalysis",
        ) -> "_5438.CouplingHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5438

            return self._parent._cast(_5438.CouplingHalfMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "CVTPulleyMultibodyDynamicsAnalysis._Cast_CVTPulleyMultibodyDynamicsAnalysis",
        ) -> "_5485.MountableComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5485

            return self._parent._cast(_5485.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "CVTPulleyMultibodyDynamicsAnalysis._Cast_CVTPulleyMultibodyDynamicsAnalysis",
        ) -> "_5425.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5425

            return self._parent._cast(_5425.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "CVTPulleyMultibodyDynamicsAnalysis._Cast_CVTPulleyMultibodyDynamicsAnalysis",
        ) -> "_5488.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5488

            return self._parent._cast(_5488.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "CVTPulleyMultibodyDynamicsAnalysis._Cast_CVTPulleyMultibodyDynamicsAnalysis",
        ) -> "_7570.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7570

            return self._parent._cast(_7570.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTPulleyMultibodyDynamicsAnalysis._Cast_CVTPulleyMultibodyDynamicsAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTPulleyMultibodyDynamicsAnalysis._Cast_CVTPulleyMultibodyDynamicsAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTPulleyMultibodyDynamicsAnalysis._Cast_CVTPulleyMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyMultibodyDynamicsAnalysis._Cast_CVTPulleyMultibodyDynamicsAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def cvt_pulley_multibody_dynamics_analysis(
            self: "CVTPulleyMultibodyDynamicsAnalysis._Cast_CVTPulleyMultibodyDynamicsAnalysis",
        ) -> "CVTPulleyMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTPulleyMultibodyDynamicsAnalysis._Cast_CVTPulleyMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "CVTPulleyMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2608.CVTPulley":
        """mastapy.system_model.part_model.couplings.CVTPulley

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CVTPulleyMultibodyDynamicsAnalysis._Cast_CVTPulleyMultibodyDynamicsAnalysis":
        return self._Cast_CVTPulleyMultibodyDynamicsAnalysis(self)
