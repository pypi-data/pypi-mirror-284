"""PlanetaryConnectionModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4702
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "PlanetaryConnectionModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2307
    from mastapy.system_model.analyses_and_results.static_loads import _6954
    from mastapy.system_model.analyses_and_results.system_deflections import _2810
    from mastapy.system_model.analyses_and_results.modal_analyses import _4596, _4628
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryConnectionModalAnalysis",)


Self = TypeVar("Self", bound="PlanetaryConnectionModalAnalysis")


class PlanetaryConnectionModalAnalysis(
    _4702.ShaftToMountableComponentConnectionModalAnalysis
):
    """PlanetaryConnectionModalAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetaryConnectionModalAnalysis")

    class _Cast_PlanetaryConnectionModalAnalysis:
        """Special nested class for casting PlanetaryConnectionModalAnalysis to subclasses."""

        def __init__(
            self: "PlanetaryConnectionModalAnalysis._Cast_PlanetaryConnectionModalAnalysis",
            parent: "PlanetaryConnectionModalAnalysis",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_modal_analysis(
            self: "PlanetaryConnectionModalAnalysis._Cast_PlanetaryConnectionModalAnalysis",
        ) -> "_4702.ShaftToMountableComponentConnectionModalAnalysis":
            return self._parent._cast(
                _4702.ShaftToMountableComponentConnectionModalAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis(
            self: "PlanetaryConnectionModalAnalysis._Cast_PlanetaryConnectionModalAnalysis",
        ) -> "_4596.AbstractShaftToMountableComponentConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4596

            return self._parent._cast(
                _4596.AbstractShaftToMountableComponentConnectionModalAnalysis
            )

        @property
        def connection_modal_analysis(
            self: "PlanetaryConnectionModalAnalysis._Cast_PlanetaryConnectionModalAnalysis",
        ) -> "_4628.ConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4628

            return self._parent._cast(_4628.ConnectionModalAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "PlanetaryConnectionModalAnalysis._Cast_PlanetaryConnectionModalAnalysis",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PlanetaryConnectionModalAnalysis._Cast_PlanetaryConnectionModalAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PlanetaryConnectionModalAnalysis._Cast_PlanetaryConnectionModalAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryConnectionModalAnalysis._Cast_PlanetaryConnectionModalAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryConnectionModalAnalysis._Cast_PlanetaryConnectionModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def planetary_connection_modal_analysis(
            self: "PlanetaryConnectionModalAnalysis._Cast_PlanetaryConnectionModalAnalysis",
        ) -> "PlanetaryConnectionModalAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetaryConnectionModalAnalysis._Cast_PlanetaryConnectionModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlanetaryConnectionModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2307.PlanetaryConnection":
        """mastapy.system_model.connections_and_sockets.PlanetaryConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6954.PlanetaryConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2810.PlanetaryConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.PlanetaryConnectionSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PlanetaryConnectionModalAnalysis._Cast_PlanetaryConnectionModalAnalysis":
        return self._Cast_PlanetaryConnectionModalAnalysis(self)
