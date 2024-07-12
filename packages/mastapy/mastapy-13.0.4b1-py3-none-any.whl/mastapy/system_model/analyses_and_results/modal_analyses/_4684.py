"""PartToPartShearCouplingConnectionModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4631
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_CONNECTION_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "PartToPartShearCouplingConnectionModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2368
    from mastapy.system_model.analyses_and_results.static_loads import _6951
    from mastapy.system_model.analyses_and_results.system_deflections import _2807
    from mastapy.system_model.analyses_and_results.modal_analyses import _4663, _4628
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingConnectionModalAnalysis",)


Self = TypeVar("Self", bound="PartToPartShearCouplingConnectionModalAnalysis")


class PartToPartShearCouplingConnectionModalAnalysis(
    _4631.CouplingConnectionModalAnalysis
):
    """PartToPartShearCouplingConnectionModalAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_CONNECTION_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingConnectionModalAnalysis"
    )

    class _Cast_PartToPartShearCouplingConnectionModalAnalysis:
        """Special nested class for casting PartToPartShearCouplingConnectionModalAnalysis to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingConnectionModalAnalysis._Cast_PartToPartShearCouplingConnectionModalAnalysis",
            parent: "PartToPartShearCouplingConnectionModalAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_modal_analysis(
            self: "PartToPartShearCouplingConnectionModalAnalysis._Cast_PartToPartShearCouplingConnectionModalAnalysis",
        ) -> "_4631.CouplingConnectionModalAnalysis":
            return self._parent._cast(_4631.CouplingConnectionModalAnalysis)

        @property
        def inter_mountable_component_connection_modal_analysis(
            self: "PartToPartShearCouplingConnectionModalAnalysis._Cast_PartToPartShearCouplingConnectionModalAnalysis",
        ) -> "_4663.InterMountableComponentConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4663

            return self._parent._cast(
                _4663.InterMountableComponentConnectionModalAnalysis
            )

        @property
        def connection_modal_analysis(
            self: "PartToPartShearCouplingConnectionModalAnalysis._Cast_PartToPartShearCouplingConnectionModalAnalysis",
        ) -> "_4628.ConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4628

            return self._parent._cast(_4628.ConnectionModalAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "PartToPartShearCouplingConnectionModalAnalysis._Cast_PartToPartShearCouplingConnectionModalAnalysis",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PartToPartShearCouplingConnectionModalAnalysis._Cast_PartToPartShearCouplingConnectionModalAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PartToPartShearCouplingConnectionModalAnalysis._Cast_PartToPartShearCouplingConnectionModalAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingConnectionModalAnalysis._Cast_PartToPartShearCouplingConnectionModalAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingConnectionModalAnalysis._Cast_PartToPartShearCouplingConnectionModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_modal_analysis(
            self: "PartToPartShearCouplingConnectionModalAnalysis._Cast_PartToPartShearCouplingConnectionModalAnalysis",
        ) -> "PartToPartShearCouplingConnectionModalAnalysis":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingConnectionModalAnalysis._Cast_PartToPartShearCouplingConnectionModalAnalysis",
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
        instance_to_wrap: "PartToPartShearCouplingConnectionModalAnalysis.TYPE",
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
    def system_deflection_results(
        self: Self,
    ) -> "_2807.PartToPartShearCouplingConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.PartToPartShearCouplingConnectionSystemDeflection

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
    ) -> "PartToPartShearCouplingConnectionModalAnalysis._Cast_PartToPartShearCouplingConnectionModalAnalysis":
        return self._Cast_PartToPartShearCouplingConnectionModalAnalysis(self)
