"""PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5437
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2368
    from mastapy.system_model.analyses_and_results.static_loads import _6951
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5470, _5435
    from mastapy.system_model.analyses_and_results.analysis_cases import _7563, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis",)


Self = TypeVar(
    "Self", bound="PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis"
)


class PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis(
    _5437.CouplingConnectionMultibodyDynamicsAnalysis
):
    """PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis",
    )

    class _Cast_PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis:
        """Special nested class for casting PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis",
            parent: "PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_multibody_dynamics_analysis(
            self: "PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_5437.CouplingConnectionMultibodyDynamicsAnalysis":
            return self._parent._cast(_5437.CouplingConnectionMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_5470.InterMountableComponentConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5470

            return self._parent._cast(
                _5470.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_5435.ConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5435

            return self._parent._cast(_5435.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_7563.ConnectionTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7563

            return self._parent._cast(_7563.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_multibody_dynamics_analysis(
            self: "PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2368.PartToPartShearCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(
        self: Self,
    ) -> "_6951.PartToPartShearCouplingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis":
        return self._Cast_PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis(
            self
        )
