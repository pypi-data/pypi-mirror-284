"""CouplingConnectionModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4663
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "CouplingConnectionModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2366
    from mastapy.system_model.analyses_and_results.system_deflections import _2750
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4614,
        _4619,
        _4684,
        _4707,
        _4722,
        _4628,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7562, _7559
    from mastapy.system_model.analyses_and_results import _2670, _2674, _2672


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionModalAnalysis",)


Self = TypeVar("Self", bound="CouplingConnectionModalAnalysis")


class CouplingConnectionModalAnalysis(
    _4663.InterMountableComponentConnectionModalAnalysis
):
    """CouplingConnectionModalAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingConnectionModalAnalysis")

    class _Cast_CouplingConnectionModalAnalysis:
        """Special nested class for casting CouplingConnectionModalAnalysis to subclasses."""

        def __init__(
            self: "CouplingConnectionModalAnalysis._Cast_CouplingConnectionModalAnalysis",
            parent: "CouplingConnectionModalAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_modal_analysis(
            self: "CouplingConnectionModalAnalysis._Cast_CouplingConnectionModalAnalysis",
        ) -> "_4663.InterMountableComponentConnectionModalAnalysis":
            return self._parent._cast(
                _4663.InterMountableComponentConnectionModalAnalysis
            )

        @property
        def connection_modal_analysis(
            self: "CouplingConnectionModalAnalysis._Cast_CouplingConnectionModalAnalysis",
        ) -> "_4628.ConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4628

            return self._parent._cast(_4628.ConnectionModalAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CouplingConnectionModalAnalysis._Cast_CouplingConnectionModalAnalysis",
        ) -> "_7562.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7562

            return self._parent._cast(_7562.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CouplingConnectionModalAnalysis._Cast_CouplingConnectionModalAnalysis",
        ) -> "_7559.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7559

            return self._parent._cast(_7559.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CouplingConnectionModalAnalysis._Cast_CouplingConnectionModalAnalysis",
        ) -> "_2670.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2670

            return self._parent._cast(_2670.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingConnectionModalAnalysis._Cast_CouplingConnectionModalAnalysis",
        ) -> "_2674.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionModalAnalysis._Cast_CouplingConnectionModalAnalysis",
        ) -> "_2672.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.DesignEntityAnalysis)

        @property
        def clutch_connection_modal_analysis(
            self: "CouplingConnectionModalAnalysis._Cast_CouplingConnectionModalAnalysis",
        ) -> "_4614.ClutchConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4614

            return self._parent._cast(_4614.ClutchConnectionModalAnalysis)

        @property
        def concept_coupling_connection_modal_analysis(
            self: "CouplingConnectionModalAnalysis._Cast_CouplingConnectionModalAnalysis",
        ) -> "_4619.ConceptCouplingConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4619

            return self._parent._cast(_4619.ConceptCouplingConnectionModalAnalysis)

        @property
        def part_to_part_shear_coupling_connection_modal_analysis(
            self: "CouplingConnectionModalAnalysis._Cast_CouplingConnectionModalAnalysis",
        ) -> "_4684.PartToPartShearCouplingConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4684

            return self._parent._cast(
                _4684.PartToPartShearCouplingConnectionModalAnalysis
            )

        @property
        def spring_damper_connection_modal_analysis(
            self: "CouplingConnectionModalAnalysis._Cast_CouplingConnectionModalAnalysis",
        ) -> "_4707.SpringDamperConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4707

            return self._parent._cast(_4707.SpringDamperConnectionModalAnalysis)

        @property
        def torque_converter_connection_modal_analysis(
            self: "CouplingConnectionModalAnalysis._Cast_CouplingConnectionModalAnalysis",
        ) -> "_4722.TorqueConverterConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4722

            return self._parent._cast(_4722.TorqueConverterConnectionModalAnalysis)

        @property
        def coupling_connection_modal_analysis(
            self: "CouplingConnectionModalAnalysis._Cast_CouplingConnectionModalAnalysis",
        ) -> "CouplingConnectionModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionModalAnalysis._Cast_CouplingConnectionModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingConnectionModalAnalysis.TYPE"):
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
    def system_deflection_results(
        self: Self,
    ) -> "_2750.CouplingConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CouplingConnectionSystemDeflection

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
    ) -> "CouplingConnectionModalAnalysis._Cast_CouplingConnectionModalAnalysis":
        return self._Cast_CouplingConnectionModalAnalysis(self)
