"""ConnectorMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5485
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "ConnectorMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2467
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5406,
        _5487,
        _5506,
        _5425,
        _5488,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7570, _7566
    from mastapy.system_model.analyses_and_results import _2678, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="ConnectorMultibodyDynamicsAnalysis")


class ConnectorMultibodyDynamicsAnalysis(
    _5485.MountableComponentMultibodyDynamicsAnalysis
):
    """ConnectorMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorMultibodyDynamicsAnalysis")

    class _Cast_ConnectorMultibodyDynamicsAnalysis:
        """Special nested class for casting ConnectorMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ConnectorMultibodyDynamicsAnalysis._Cast_ConnectorMultibodyDynamicsAnalysis",
            parent: "ConnectorMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "ConnectorMultibodyDynamicsAnalysis._Cast_ConnectorMultibodyDynamicsAnalysis",
        ) -> "_5485.MountableComponentMultibodyDynamicsAnalysis":
            return self._parent._cast(_5485.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "ConnectorMultibodyDynamicsAnalysis._Cast_ConnectorMultibodyDynamicsAnalysis",
        ) -> "_5425.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5425

            return self._parent._cast(_5425.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "ConnectorMultibodyDynamicsAnalysis._Cast_ConnectorMultibodyDynamicsAnalysis",
        ) -> "_5488.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5488

            return self._parent._cast(_5488.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "ConnectorMultibodyDynamicsAnalysis._Cast_ConnectorMultibodyDynamicsAnalysis",
        ) -> "_7570.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7570

            return self._parent._cast(_7570.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConnectorMultibodyDynamicsAnalysis._Cast_ConnectorMultibodyDynamicsAnalysis",
        ) -> "_7566.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConnectorMultibodyDynamicsAnalysis._Cast_ConnectorMultibodyDynamicsAnalysis",
        ) -> "_2678.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2678

            return self._parent._cast(_2678.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectorMultibodyDynamicsAnalysis._Cast_ConnectorMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorMultibodyDynamicsAnalysis._Cast_ConnectorMultibodyDynamicsAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def bearing_multibody_dynamics_analysis(
            self: "ConnectorMultibodyDynamicsAnalysis._Cast_ConnectorMultibodyDynamicsAnalysis",
        ) -> "_5406.BearingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5406

            return self._parent._cast(_5406.BearingMultibodyDynamicsAnalysis)

        @property
        def oil_seal_multibody_dynamics_analysis(
            self: "ConnectorMultibodyDynamicsAnalysis._Cast_ConnectorMultibodyDynamicsAnalysis",
        ) -> "_5487.OilSealMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5487

            return self._parent._cast(_5487.OilSealMultibodyDynamicsAnalysis)

        @property
        def shaft_hub_connection_multibody_dynamics_analysis(
            self: "ConnectorMultibodyDynamicsAnalysis._Cast_ConnectorMultibodyDynamicsAnalysis",
        ) -> "_5506.ShaftHubConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5506

            return self._parent._cast(_5506.ShaftHubConnectionMultibodyDynamicsAnalysis)

        @property
        def connector_multibody_dynamics_analysis(
            self: "ConnectorMultibodyDynamicsAnalysis._Cast_ConnectorMultibodyDynamicsAnalysis",
        ) -> "ConnectorMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectorMultibodyDynamicsAnalysis._Cast_ConnectorMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "ConnectorMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2467.Connector":
        """mastapy.system_model.part_model.Connector

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
    ) -> "ConnectorMultibodyDynamicsAnalysis._Cast_ConnectorMultibodyDynamicsAnalysis":
        return self._Cast_ConnectorMultibodyDynamicsAnalysis(self)
