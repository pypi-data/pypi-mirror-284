"""CouplingConnectionStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3851
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "CouplingConnectionStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2366
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3805,
        _3810,
        _3866,
        _3888,
        _3906,
        _3819,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionStabilityAnalysis",)


Self = TypeVar("Self", bound="CouplingConnectionStabilityAnalysis")


class CouplingConnectionStabilityAnalysis(
    _3851.InterMountableComponentConnectionStabilityAnalysis
):
    """CouplingConnectionStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingConnectionStabilityAnalysis")

    class _Cast_CouplingConnectionStabilityAnalysis:
        """Special nested class for casting CouplingConnectionStabilityAnalysis to subclasses."""

        def __init__(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
            parent: "CouplingConnectionStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_stability_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_3851.InterMountableComponentConnectionStabilityAnalysis":
            return self._parent._cast(
                _3851.InterMountableComponentConnectionStabilityAnalysis
            )

        @property
        def connection_stability_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_3819.ConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3819,
            )

            return self._parent._cast(_3819.ConnectionStabilityAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_connection_stability_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_3805.ClutchConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3805,
            )

            return self._parent._cast(_3805.ClutchConnectionStabilityAnalysis)

        @property
        def concept_coupling_connection_stability_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_3810.ConceptCouplingConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3810,
            )

            return self._parent._cast(_3810.ConceptCouplingConnectionStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_stability_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_3866.PartToPartShearCouplingConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3866,
            )

            return self._parent._cast(
                _3866.PartToPartShearCouplingConnectionStabilityAnalysis
            )

        @property
        def spring_damper_connection_stability_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_3888.SpringDamperConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3888,
            )

            return self._parent._cast(_3888.SpringDamperConnectionStabilityAnalysis)

        @property
        def torque_converter_connection_stability_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_3906.TorqueConverterConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3906,
            )

            return self._parent._cast(_3906.TorqueConverterConnectionStabilityAnalysis)

        @property
        def coupling_connection_stability_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "CouplingConnectionStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
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
        self: Self, instance_to_wrap: "CouplingConnectionStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2366.CouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.CouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> (
        "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis"
    ):
        return self._Cast_CouplingConnectionStabilityAnalysis(self)
